#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>




int main(int argc, string argv[])
{
    if (argv[1] == NULL)
    {
        return 1;
    }
    else
    {
        int key = 0;
        string cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        string sma = "abcdefghijklmnopqrstuvwxyz";
        string keey = argv[1];
        string massege = get_string("plaintext:  ");
        int lenght_of_massege = strlen(massege);

        while (strlen(keey) < strlen(massege))
        {
            for (int i = 0; i < strlen(keey); i++)
        {
            //   strcat(keey, &keey[i]);

            strncat(keey, &keey[i], 1);
//             strcat( "a", str1 );
//             keey+=keey[i];
//             printf("%c",j);
                if (strlen(keey) == strlen(massege))
                {
                    break;
                }
            }
            //printf("%s",keey);
        }
        int i = 0;
        printf("ciphertext: ");
        while (i < strlen(keey))
        {
            {
                for (int j = 0; j < strlen(sma); j++)
                {
                    if (massege[i] > 'z' && massege[i] < 'A')


                    {
                        keey[i] = keey[i - 1];
                    }




                    if (keey[i] == sma[j] || keey[i] == cap[j])
                    {

                        key = j;
//             while (key > 20)
//         {
//             key = key % 20;
//         }
                        // for (int ik = i ; ik < lenght_of_massege ; ik++)
                        {
                            int asscii = (int) massege[i];

//         printf("%i",asscii);
                            int c = asscii + key;



                            if (massege[i] >= 'a' && massege[i] <= 'z')
                            {

                                if (c > 122)
                                {
                                    asscii = asscii - (26 - key);

                                    printf("%c", asscii);
                                }
                                else if (c <= 122)
                                {
                                    asscii = asscii + key;
                                    printf("%c", asscii);
                                }
                            }
                            else if (massege[i] >= 'A' && massege[i] <= 'Z')
                            {
                                if (c > 90)
                                {

                                    asscii = asscii - (26 - key);

                                    printf("%c", asscii);
                                }
                                else if (c <= 90)
                                {
                                    asscii = asscii + key;
                                    printf("%c", asscii);
                                }
                            }
// \n
                            else
                            {
                                printf("%c", asscii);

                            }

                        }


                    }



                }
















































//     for(int j=0;j<strlen(cap);j++)
//     {
//         if(keey[i]==cap[j]){
//              key=j;







//           ////////////////////////////////////////////////////////////  printf("%i\n",j);
//         }
//     }

            }
            i++;
        }



    }
    printf("\n");

}
