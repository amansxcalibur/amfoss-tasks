use std::io;

    fn main() {
    println!("Enter a name:");
    let mut guess = String::new();
    io::stdin().read_line(&mut guess).expect("failed to readline");
    let num2=guess.trim();
    let num: i32 = num2.parse().unwrap();
    for i in 1..num {
        let mut count = 0;

        for j in 1..i+1 {
            if i % j == 0 {
                count += 1;
            }
        }

        if count == 2 {
            print!("{} ", i);
        }
    }
}
