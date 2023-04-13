#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void function()
{
    char buff[512];
    gets(buff);
}

int main()
{
    int no = 1;
    int* ptr = &no;
    function();
}