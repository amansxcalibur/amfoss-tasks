#include <iostream>
using namespace std;

int main() {
    int num;
    cout<<"Enter the number: ";
    cin>>num;
    for(int j=2;j<=num;j++){
         int count=0;
         for(int i=1;i<=j;i++){
            if(j%i==0){
               count++;
            }
         }
         if(count==2){
            cout<<j<<" ";}
    }
    return 0;
}