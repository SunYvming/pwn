CC ?= gcc
CXX ?= g++

CFLAGS=-fno-stack-protector -no-pie -g -O0

all: ret2text

ret2text:
	$(CC) $(CFLAGS) -o ret2text.out ret2text.c