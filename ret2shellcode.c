#include <stdio.h>
#include <string.h>

char buf2[100];

int main(void)
{

    char buf[100];

    printf("No system for you this time !!!\n");
    gets(buf);
    strncpy(buf2, buf, 100);
    printf("bye bye ~\n");

    return 0;
}