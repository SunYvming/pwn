#include <stdio.h>
#include <string.h>

void vuln(char *input) {
        char buffer[100];
        strcpy(buffer, input);
}


int main(int argc, char **argv) {
        vuln(argv[1]);
        return 0;
}