#define _XOPEN_SOURCE
#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <crypt.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./crack hash\n");
        return 1;
    }
    string hashcode = argv[1];
    //char salt[3];
    string characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
    char salt[2];
    memcpy(salt, hashcode, 2);
    //salt[2]='\0';
    //string massege=NULL;
    char massege[5] = "\0\0\0\0\0";
    int len=53;
    for(int i0=0;i0<len;i0++)
    {
        for(int i1=0;i1<len;i1++)
        {
            for(int i2=0;i2<len;i2++)
            {
                for(int i3=0;i3<len;i3++)
                {
                    for(int i4=0;i4<len;i4++)
                    {
                        massege[0] = characters[i4];  // 1)
                        massege[1] = characters[i3]; // 2)
                        massege[2] = characters[i2];  // 3)
                        massege[3] = characters[i1]; // 4)
                        massege[4] = characters[i0];  // 5)
                        
                        if (strcmp(crypt(massege, salt), hashcode) == 0)
                        {
                            printf("%s\n", massege);
                            return 0;
                        }
                    }
                }
            }
        }    
    }
    printf("sorry");
}
   
