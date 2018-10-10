#! /usr/bin/env python3
"""
Example: Publish Roomba OI library via XMLRPC
"""

from xmlrpc.server import SimpleXMLRPCServer
from pycreate2 import Create2

from settings import Settings

# Instantiate iRobot OI
cr2 = Create2(Settings.ROOMBA_SERIAL)
cr2.open()

# Create server
with SimpleXMLRPCServer(('', Settings.XMLRPC_PORT), allow_none=True) as server:
    server.register_introspection_functions()
    server.register_multicall_functions()

    server.register_instance(cr2)
    server.serve_forever()


