#include <stdio.h>
void LCD(char *s)
{
 const long lcd[5] = {772,1010519,16391,488807,16644};
 const char str[][7] = {"***** ","    * ","*     ","*   * "};
 int i,j;
 for(i = 0; i<5; i++)
 {
   for (j = 0; s[j]; j++)
    {
     printf(str[lcd[i]>>((s[j]-'0')<<1)&3]);
    }
      printf("\n");
 }

}
int main()
{
 LCD("2005");
 
}
 
