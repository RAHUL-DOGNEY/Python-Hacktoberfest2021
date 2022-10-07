# A year is considered a leap year if that year is exactly divisible by 4, except for years that end with 00(century year). 
# A century year is a leap year if that is exactly divisible by 400. However, a year which not divisible by 400 and divisible by 100 is not a leap year.
# Example:

# 2004 is a leap year.
# 2020 is a leap year.
# 1900 is not a leap year.
# 2013 is not a leap year.

# Two ways of making program

# Using Conditional Statement
input_year = int(input("Enter the Year to be checked: "))
if (( input_year%400 == 0)or (( input_year%4 == 0 ) and ( input_year%100 != 0))):
    print("%d is Leap Year" %input_year)
else:
    print("%d is Not the Leap Year" %input_year)
    
    
    
# Using Nested If
input_year = int(input("Enter the Year to be checked: "))
if(input_year%4 == 0):
    if(input_year%100 == 0):
        if(input_year%400 == 0):
            print("%d is Leap Year" %input_year)
        else:
            print("%d is Not the Leap Year" %input_year)
    else:
        print("%d is Leap Year" %input_year)
else:
    print("%d is Not the Leap Year" %input_year)

