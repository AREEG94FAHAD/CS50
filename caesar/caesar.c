#include <cs50.h>
#include <stdio.h>
#include<string.h>
int main(int argc, string argv[])
{

    
    if (argv[1] == NULL)
    {
        return 1;
    }
    else
    {
    
//     argc= get_int("");
        int key = atoi(argv[1]);
    
        while (key > 26)
        {
            key = key % 26;
        }
//     int key = get_int("");
//     
//     
        string massege = get_string("plaintext:  ");
        int lenght_of_massege = strlen(massege);
        printf("ciphertext: ");
        for (int i = 0 ; i < lenght_of_massege ; i++)
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
                else if (c < 122)
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
                else if (c < 90)
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
// \n
// \n
// \n
// \n
        }
        printf("\n");
    }

}
        
     




//         else if(c<97)
//         {
//              asscii=asscii+key;
//              printf("%c",asscii); 
//         }
        
//         else if(c>97)
//         {
//              asscii=122-(26-key);
            
//              printf("%c",asscii);
//         }
        
        
        
        
        
//         if(asscii>90)
        
//             asscii=asscii-(25-key);
            
//              printf("%i",asscii);
//         }
//         
//         //             asscii=asscii+key;
//              printf("%c",asscii);
//              
//  
    

