# Warmup-1 > sleep_in
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

# my answer:

def sleep_in(weekday, vacation):
    if weekday == False and vacation == False:
        return True
    if weekday == True and vacation == False:
        return False
    if weekday == False and vacation == True:
        return True
    if weekday == True and vacation == True:
        return True
        
sleep_in(True, False)

# coding bat's answer:

# def sleep_in(weekday, vacation):
#   if not weekday or vacation:
#     return True
#   else:
#     return False

# sleep_in(True, False)

# Warmup-1 > monkey_trouble
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

# my answer:
def monkey_trouble(a_smile, b_smile):
    if a_smile == True and b_smile == True:
        return True
    if a_smile == False and b_smile == False:
        return True
    if a_smile == True and b_smile == False:
        return False
    if a_smile == False and b_smile == True:
        return False

monkey_trouble(True, True)

# my answer2:
# def monkey_trouble(a_smile, b_smile):
#     if not a_smile and not b_smile:
#         return True
#     if not a_smile and b_smile:
#         return False
#     if a_smile and not b_smile:
#         return False 
#     if a_smile and b_smile:
#         return True

# monkey_trouble(True, False)

# coding bat's answer:
# def monkey_trouble(a_smile, b_smile):
#   if a_smile and b_smile:
#     return True
#   if not a_smile and not b_smile:
#     return True
#   return False

# monkey_trouble(True, False)

# Warmup-1 > sum_double
# Given two int values, return their sum. Unless the two values are the same, then return double their sum.

# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8
    
# my answer:
def sum_double(a, b):
    if a == b:
        return (a + b) *2
    else:
        return a + b

print(sum_double(1, 2))

# coding bat's answer:
# def sum_double(a, b):
#   # Store the sum in a local variable
#   sum = a + b
  
#   # Double it if a and b are the same
#   if a == b:
#     sum = sum * 2
#   return sum

#Warmup-1 > diff21
#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
def diff21(n):
    if n > 21:  #n greater than 21
        return (n - 21) *2
    if n < 21:  #n less than 21
        return 21 - n
    else:   #n is equal to itself
        return n - 21

print(diff21(21))

# coding bat's answer:
# def diff21(n):
#   if n <= 21:
#     return 21 - n
#   else:
#     return (n - 21) * 2

# Warmup-1 > parrot_trouble
# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

# coding bat's answer:
# def parrot_trouble(talking, hour):
#   return (talking and (hour < 7 or hour > 20))