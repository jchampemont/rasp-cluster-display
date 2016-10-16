import httplib

pool = {}

def get_conn(node):
    if node in pool:
        return pool[node]
    else:
        c = httplib.HTTPConnection(node, 5000)
        pool[node] = c
        return c

def get_hostname(node):
    conn = get_conn(node)
    conn.request("GET", "/hostname")
    r = conn.getresponse()
    return r.read()

def get_ip_address(node, interface):
    conn = get_conn(node)
    conn.request("GET", "/ip/" + interface)
    r = conn.getresponse()
    return r.read()

def get_load_averages(node):
    conn = get_conn(node)
    conn.request("GET", "/load_averages")
    r = conn.getresponse()
    return r.read()

def uptime(node):
    conn = get_conn(node)
    conn.request("GET", "/uptime")
    r = conn.getresponse()
    return r.read()
