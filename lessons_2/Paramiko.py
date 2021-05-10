import paramiko

nbytes = 4096
hostname = '192.168.1.31'
port = 22
username = 'idan'
password = 'rootroot'
command = 'mkdir paramiko_ssh'

client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)

stdout_data = []
stderr_data = []
session = client.open_channel(kind='session')
session.exec_command(command)

session.close()
client.close()
