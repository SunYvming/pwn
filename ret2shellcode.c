#include <stdio.h>
#include <string.h>
#include <sys/mman.h>

char buf2[100] = "hello world\0";

void func(){
    char buf[100];
    gets(buf);
    gets(buf2);
}

int main(void)
{
    mprotect(0x0804b000, 4096, PROT_READ | PROT_WRITE | PROT_EXEC);

    printf("No system for you this time !!!\n");
    func();
    printf("bye bye ~\n");

    return 0;
}