/* Algorithm:-  Fizz and Buzz refer to any number that's a multiple of 3 and 5 respectively. 
                In other words, if a number is divisible by 3, it is substituted with fizz; 
                if a number is divisible by 5, it is substituted with buzz. 
                If a number is simultaneously a multiple of 3 AND 5, the number is replaced with "fizz buzz." 
*/
 let number = [1,2,3,4,5]
// here 3 is fizz and 5 is buzz

for num in number { 
    if num % 3 == 0 {
        print("\(num) fizz")
    } 
    else if num % 5 == 0 { 
        print("\(num) buzz")
    } 
    else { 
        print(num)
    } 
}
