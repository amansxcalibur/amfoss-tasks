package main
import "fmt"

func main() {
    var num int
    fmt.Println("Enter the number")
    fmt.Scanln(&num)
    for i:=1;i<=num;i++{
        var count int=0
        for j:=1;j<=i;j++{
            if i % j == 0 {
                count += 1;
            }
        }

        if count == 2 {
            fmt.Println(i);
        }
    }
}