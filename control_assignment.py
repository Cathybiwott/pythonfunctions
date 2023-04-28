# Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50. 
def print_even_numbers():
    num = 0
    while num <= 50:
        if num % 2 != 0:
            num += 1
            continue
        print(num)
        num += 1

print_even_numbers()

# Write a function that takes an integer argument and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def is_prime(num):
    if num < 2:
        print(f"{num} is not prime")
    elif num == 2:
        print(f"{num} is prime")
    elif num % 2 == 0:
        print(f"{num} is not prime")
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                print(f"{num} is not prime")
                break
        else:
            print(f"{num} is prime")

is_prime(7)  
is_prime(20) 


 # Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.
def sum_even_numbers(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    print("sum of even numbers is:", total)

my_list = [3, 8, 2, 9, 12, 7, 6]
sum_even_numbers(my_list)



# # Write a function that takes any two integers as input, and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def sum_divisible_by_three(a, b):
    total = 0
    for i in range(a, b+1):
        if i % 3 == 0:
            total += i
    print(total)

sum_divisible_by_three(20, 30)

    