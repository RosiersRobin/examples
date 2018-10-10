import sys

if sys.hexversion < 0x3060000:
    from xmlrpc.server import SimpleXMLRPCServer as OldXMLRPCServer


    class SimpleXMLRPCServer(OldXMLRPCServer):
        def __enter__(self):
            return self

        def __exit__(self, *args):
            self.server_close()
else:
    from xmlrpc.server import SimpleXMLRPCServer

