#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int sum=0;
    //for second number
    int mod=0;
    //for second value
    int div;
    //for first number and so on 
    int mod2=0;
    //for the third
    int c=0;
    //for the for
    int dii=0;
    //for the five
    int ok=0;
    //for the last 
   long long int n=get_long("Number:");
   //for all AMEXcard
    if(((349999999999999/n)>=1&&(n/340000000000000)>=1)||((379999999999999/n)>=1&&(n/370000000000000)>=1)){
        while(n!=0)
             
        {
            mod+=n%10;
            n=n/10;
            c=n%10;
            if(c>4)
            {
//                 printf("%iln",c);
               c=c*2;
//                  printf("%iln",c);
               dii=c%10;
//                  printf("%iln",dii);
                c=c/10;
                mod2+=dii+c;
//                  printf("%iln",mod2);
                n=n/10;
                
            }
            else{
            
            mod2+=(n%10)*2;
            n=n/10;
            
//             mod2*=2;
            }
        }
   int   modtotal=mod+(mod2);
        if((modtotal%10==0))
        {
          printf("AMEX\n");  
        }
        else
        {
          printf("INVALID\n");
        }
    }
    //for mastercard
       else if(((5599999999999999/n)>=1&&(n/5100000000000000)>=1)){
          while(n!=0)
             
        {
            mod+=n%10;
            n=n/10;
            c=n%10;
            if(c>4)
            {
//                 printf("%iln",c);
               c=c*2;
//                  printf("%iln",c);
               dii=c%10;
//                  printf("%iln",dii);
                c=c/10;
                mod2+=dii+c;
//                  printf("%iln",mod2);
                n=n/10;
                
            }
            else{
            
            mod2+=(n%10)*2;
            n=n/10;
            
//             mod2*=2;
            }
        }
               
       
     int modtotal=mod+(mod2);
        //ceck if the sum equal 0
        if((modtotal%10==0))
        {
          printf("MASTERCARD\n");  
        }
           else
           {
               printf("INVALID\n");
           }
    }
    
    else if(((4999999999999999/n)>=1&&(n/4000000000000000)>=1)||((4999999999999/n)>=1&&(n/4000000000000)>=1)){
        while(n!=0)
        {
             {
            
            
            mod+=n%10;
            n=n/10;
            
            c=n%10;
            if(c>4)
            {
//                 printf("%iln",c);
               c=c*2;
//                  printf("%iln",c);
               dii=c%10;
//                  printf("%iln",dii);
                c=c/10;
                mod2+=dii+c;
//                  printf("%iln",mod2);
                n=n/10;
                
            }
            else
            {
            mod2+=(n%10)*2;
            n=n/10;
            }
            

             }
            
            
            mod+=n%10;
            n=n/10;
            
            c=n%10;
            if(c>4)
            {
//                 printf("%iln",c);
               c=c*2;
//                  printf("%iln",c);
               dii=c%10;
//                  printf("%iln",dii);
                c=c/10;
                mod2+=dii+c;
//                  printf("%iln",mod2);
                n=n/10;
                
            }
            else
            {
            
            mod2+=(n%10)*2;
            n=n/10;
            }
        }
            
//             mod2*=2;
            
        
   int   modtotal=mod+(mod2)+ok;
        if((modtotal%10==0))
        {
          printf("VISA\n");  
        }
        else
        {
               printf("INVALID\n");
        }
    }
    
    else 
    {
        printf("INVALID\n");
    }
    
    
}
