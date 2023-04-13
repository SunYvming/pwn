#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void function()
{
    char buff[256];
    gets(buff);
}

int main()
{
    int no = 1;
    int* ptr = &no;
    function();
}