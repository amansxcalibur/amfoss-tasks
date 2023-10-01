#include <stdio.h>

int main() {
    int num;
    printf("Enter an integer: ");  
    scanf("%d", &num);
    for(int j=2;j<=num;j++){
         int count=0;
         for(int i=1;i<=j;i++){
            if(j%i==0){
               count++;
            }
         }
         if(count==2)
         printf("%d ",j);
    }
    return 0;
}