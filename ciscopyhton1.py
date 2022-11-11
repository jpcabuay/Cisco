#hello world
import getpass  
import telnetlib 

host = "192.168.233.136"
user = input("Ano ang Cisco Username?:")
password = getpass.getpass()

tn = telnetlib.Telnet(host)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') +b"\n")
if password: 
     tn.read_until(b"Password: ")
     tn.write(password.encode('ascii') +b"\n")

tn.write(b"config t\n")
tn.write(b"hostname PythonMADE\n")
tn.write(b"int lo1\n")
tn.write(b"ip add 1.1.1.1 255.255.255.255\n")
tn.write(b"int lo2\n")
tn.write(b"ip add 2.2.2.2 255.255.255.255\n")
tn.write(b"int lo3\n")
tn.write(b"ip add 3.3.3.3 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

