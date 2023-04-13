#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char *shell = "/bin/sh";
char buf2[100];

void secure(void)
{
    int secretcode, input;
    srand(time(NULL));

    secretcode = rand();
    scanf("%d", &input);
    if(input == secretcode)
        system("shell!?");
}

void function(){
    char buf1[100];
    gets(buf1);
}

int main(void)
{
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);

    printf("RET2LIBC\n");
    function();

    return 0;
}