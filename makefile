CC ?= gcc
CXX ?= g++

CFLAGS=-fno-stack-protector -no-pie -g -O0 -m32
CFLAGS_EXTRA=-z execstack -z norelro

all: ret2text ret2shellcode ret2ret ret2libc

ret2text:
	$(CC) $(CFLAGS) -o ret2text.out ret2text.c

ret2shellcode:
	$(CC) $(CFLAGS) $(CFLAGS_EXTRA) -o ret2shellcode.out ret2shellcode.c

ret2ret:
	$(CC) $(CFLAGS) $(CFLAGS_EXTRA) -o ret2ret.out ret2ret.c

ret2libc:
	$(CC) $(CFLAGS) $(CFLAGS_EXTRA) -o ret2libc.out ret2libc.c

clean:
	rm *.out