from __future__ import print_function

import os
import errno
import sys
import socket
import time
try:
    from xmlrpc.client import ServerProxy
except ImportError:
    from xmlrpclib import ServerProxy

try: #py3k
    import urllib.parse as urlparse
except ImportError:
    import urlparse

from optparse import OptionParser
import rosgraph
import rosgraph.names
import rostopic

NAME='rosnode'
ID = '/rosnode'

class ROSNodeException(Exception):
    """
    rosnode base exception type
    """
    pass
class ROSNodeIOException(ROSNodeException):
    """
    Exceptions for communication-related (i/o) errors, generally due to Master or Node network communication issues.
    """
    pass

# need for calling node APIs
def _succeed(args):
    code, msg, val = args
    if code != 1:
        raise ROSNodeException("remote call failed: %s"%msg)
    return val

_caller_apis = {}
def get_api_uri(master, caller_id, skip_cache=False):
    """
    @param master: XMLRPC handle to ROS Master
    @type  master: rosgraph.Master
    @param caller_id: node name
    @type  caller_id: str
    @param skip_cache: flag to skip cached data and force to lookup node from master
    @type  skip_cache: bool
    @return: xmlrpc URI of caller_id
    @rtype: str
    @raise ROSNodeIOException: if unable to communicate with master
    """
    caller_api = _caller_apis.get(caller_id, None)
    if not caller_api or skip_cache:
        try:
            caller_api = master.lookupNode(caller_id)
            _caller_apis[caller_id] = caller_api
        except rosgraph.MasterError:
            return None
        except socket.error:
            raise ROSNodeIOException("Unable to communicate with master!")
    return caller_api

def lookup_uri(master, system_state, topic, uri):
    for l in system_state[0:2]:
        for entry in l:
            if entry[0] == topic:
                for n in entry[1]:
                    if rostopic.get_api(master, n) == uri:
                        return '%s (%s)' % (n, uri)
    return uri

def get_node_names(namespace=None):
    """
    @param namespace: optional namespace to scope return values by. Namespace must already be resolved.
    @type  namespace: str
    @return: list of node caller IDs
    @rtype: [str]
    @raise ROSNodeIOException: if unable to communicate with master
    """
    master = rosgraph.Master(ID)
    try:
        state = master.getSystemState()
    except socket.error:
        raise ROSNodeIOException("Unable to communicate with master!")
    nodes = []
    if namespace:
        # canonicalize namespace with leading/trailing slash
        g_ns = rosgraph.names.make_global_ns(namespace)
        for s in state:
            for t, l in s:
                nodes.extend([n for n in l if n.startswith(g_ns) or n == namespace])
    else:
        for s in state:
            for t, l in s:
                nodes.extend(l)
    return list(set(nodes))

def rosnode_ping(node_name, max_count=None, verbose=False):
    """
    Test connectivity to node by calling its XMLRPC API
    @param node_name: name of node to ping
    @type  node_name: str
    @param max_count: number of ping requests to make
    @type  max_count: int
    @param verbose: print ping information to screen
    @type  verbose: bool
    @return: True if node pinged
    @rtype: bool
    @raise ROSNodeIOException: if unable to communicate with master
    """
    result_str = ""
    master = rosgraph.Master(ID)
    node_api = get_api_uri(master,node_name)
    if not node_api:
        result_str = result_str + ("cannot ping [%s]: unknown node"%node_name)
        # print(result_str)
        # return False
        return result_str

    timeout = 3.

    # if verbose:
    #     print("pinging %s with a timeout of %ss"%(node_name, timeout))
    socket.setdefaulttimeout(timeout)
    node = ServerProxy(node_api)
    lastcall = 0.
    count = 0
    acc = 0.
    try:
        while True:
            try:
                start = time.time()
                pid = _succeed(node.getPid(ID))
                end = time.time()

                dur = (end-start)*1000.
                acc += dur
                count += 1

                if verbose:
                    result_str=result_str+("[%s] node is running fine"%node_name)
                    return(result_str)
                    # print(result_str)
                # 1s between pings
            except socket.error as e:
                # 3786: catch ValueError on unpack as socket.error is not always a tuple
                try:
                    # #3659
                    errnum, msg = e
                    if errnum == -2: #name/service unknown
                        p = urlparse.urlparse(node_api)
                        result_str = result_str + ("ERROR: Unknown host [%s] for node [%s]"%(p.hostname, node_name))
                        return(result_str)
                        # print(result_str)
                    elif errnum == errno.ECONNREFUSED:
                        # check if node url has changed
                        new_node_api = get_api_uri(master,node_name, skip_cache=True)
                        if not new_node_api:
                            result_str = result_str + ("cannot ping [%s]: unknown node"%node_name)
                            # print(result_str)
                            # return False
                            return result_str
                        if new_node_api != node_api:
                            if verbose:
                                result_str = result_str + ("node url has changed from [%s] to [%s], retrying to ping"%(node_api, new_node_api))
                                # print(result_str)

                            node_api = new_node_api
                            node = ServerProxy(node_api)
                            continue
                        result_str = result_str + ("[%s] has CRASHED. Could be a memory-leak, segmentation fault or division by zero "%(node_name))
                        # print(result_str)
                    else:
                        result_str = result_str + ("connection to [%s] timed out"%node_name)
                        # print("connection to [%s] timed out"%node_name, file=sys.stderr)
                    # return False
                    return result_str
                except ValueError:
                    x=1
                    # print("unknown network error contacting node: %s"%(str(e)))
            if max_count and count >= max_count:
                break
            time.sleep(1.0)
            return(result_str)

    except KeyboardInterrupt:
        pass

    # if verbose and count > 1:
    #     print("ping average: %fms"%(acc/count))
    # return True

def rosnode_ping_all(verbose=False):
    """
    Ping all running nodes
    @return [str], [str]: pinged nodes, un-pingable nodes
    @raise ROSNodeIOException: if unable to communicate with master
    """
    data=[]
    master = rosgraph.Master(ID)
    try:
        state = master.getSystemState()
    except socket.error:
        raise ROSNodeIOException("Unable to communicate with master!")

    nodes = []
    for s in state:
        for t, l in s:
            nodes.extend(l)
    nodes = list(set(nodes)) #uniq
    # if verbose:
    #     print("Will ping the following nodes: \n"+''.join([" * %s\n"%n for n in nodes]))
    # pinged = []
    # unpinged = []
    for node in nodes:
        data.append(rosnode_ping(node, max_count=1, verbose=verbose))
    return data

if(__name__=="__main__"):
    a= rosnode_ping_all(True)
