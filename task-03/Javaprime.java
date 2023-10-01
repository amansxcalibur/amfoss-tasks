import java.util.*;
public class Prime {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number limit");
        int num=sc.nextInt();
        int count=0;
        for(int j=2;j<=num;j++){
         count=0;
         for(int i=1;i<=j;i++){
            if(j%i==0){
               count++;
            }
         }
         if(count==2)
         System.out.print(j+" ");
      }
        
    }
}
