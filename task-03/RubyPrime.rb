require 'prime'
puts "Enter the number"
num=gets.chomp.to_i
puts num
i=1
while i<=num do
  if Prime.prime?(i)==true
    puts i
end
  i=i+1
end
