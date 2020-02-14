#include <cs50.h>
#include <stdio.h>
int main(void)
{

int nhash= get_int("Height: ");
    while(nhash>8||nhash<1){

    nhash= get_int("Height: ");

    }


        for(int i=0;i<nhash;i++)
        { 

            for(int j=nhash-1;j>i;j--)
            {  
               printf(" ");  

            }
            for(int o=i;o>=0;o--){
                 printf("#");  

            }
            printf("\n");
        }






//    
//     {

//         for(int j=0;j<n;j++){
//            printf(" #");
//         }
//         printf("\n");
//     }



}
