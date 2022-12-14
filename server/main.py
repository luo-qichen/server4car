import threading

# import server4car.server4car.server.http_server as http_server
# import server4car.server4car.server.msg_server as msg_server

import http_server
import msg_server

try:
    http_server.port = 8000
    http_server_thread = threading.Thread(
        target=http_server.run_http_server, name="http_server")

    msg_server_thread = threading.Thread(
        target=msg_server.run_msg_server, name="msg_server")

    http_server_thread.start()
    msg_server_thread.start()
    msg_server_thread

except Exception as e:
    print(e)

while 1:
    pass
