import time
import xmlrpc.client

from settings import Settings

cr2rpc = xmlrpc.client.ServerProxy("http://{}:{}".format(Settings.XMLRPC_HOST, Settings.XMLRPC_PORT))
print(cr2rpc.system.listMethods())
time.sleep(1)

print(cr2rpc.get_sensors())
time.sleep(1)
