CC ?= gcc
CXX ?= g++

CFLAGS=-fno-stack-protector -no-pie -g -O0 -m32 
CFLAGS_EXTRA=-z execstack -z norelro

all: ret2text ret2shellcode ret2libc ret2syscall ret2reg

ret2text:
	$(CC) $(CFLAGS) -o ret2text.out ret2text.c

ret2shellcode:
	$(CC) $(CFLAGS) $(CFLAGS_EXTRA) -o ret2shellcode.out ret2shellcode.c

ret2syscall:
	@echo "ret2syscall使用已有的elf"
	# $(CC) -static $(CFLAGS) -o ret2syscall.out ret2syscall.c

ret2libc:
	$(CC) $(CFLAGS) $(CFLAGS_EXTRA) -o ret2libc.out ret2libc.c

ret2reg:
	$(CC) $(CFLAGS) $(CFLAGS_EXTRA) -o ret2reg.out ret2reg.c

clean:
	rm ret2text.out ret2shellcode.out ret2libc.out ret2reg.out
	rm *.txt