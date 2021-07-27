"""

This Module Contains Advanced Functions like Average, Percentage, LCM, HCF and More

Author: Programmer Ayush
Discord: Programmer Ayush#8357
YouTube: Ayush's Magical World Of Science

"""

def average(nums: list):
    numbers = 0
    count = 0
    average = 0
    
    for num in nums:
        numbers += 1
        count += num

    average = count/numbers

    return average


def percent(percent, amount):
    percent = amount/100*percent

    return percent

def factors(num):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    factors = []
    
    for number in numbers:
        if num % number == 0:
            factor = num/number
            factors.append(int(factor))
            factors.append(number)
            
        else:
            pass

    return factors

def cube(num):
    return num*num*num

def hfc(num1, num2):
    factors1 = set(factors(num1))
    factors2 = set(factors(num2))
    
    common = list(factors1 & factors2)
    
    if (factors1 & factors2):
        hfc = max(common)
        return hfc

    else:
        return "No Common Factors"

def lcm(num1, num2):
    factors1 = set(factors(num1))
    factors2 = set(factors(num2))
    
    common = list(factors1 & factors2)
    common.remove(1)
    
    if not common:
        return num1*num2
    
    if (factors1 & factors2):
        lcm = min(common)
        return lcm

    else:
        return "No Common Multiples"

