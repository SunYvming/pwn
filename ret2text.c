#include <stdio.h>
#include <string.h>

char *gets (char *str);

void success() { puts("Hijack success!"); }

void vulnerable() {
  char s[12];
//   scanf("%s", s);
    gets(s);
  puts(s);
  return;
}

int main(int argc, char **argv) {
  vulnerable();
  return 0;
}