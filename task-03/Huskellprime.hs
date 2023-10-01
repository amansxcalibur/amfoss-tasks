factors :: Int->[Int]
factors n = [x | x<-[1..n], (mod n x)==0]

isPrime :: Int->Bool
isPrime n = (factors n) == [1,n]

generatePrime :: Int->[Int]
generatePrime n = [x | x<-[1..n], isPrime x]

main :: IO ()
main = do
   putStrLn "Enter an integer: "
   input <- getLine
   let n = read input :: Int
   print (generatePrime n)