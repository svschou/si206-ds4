import unittest
# function to return the factorial of a number
# Add comments
def factorial(num):
    ans = 1 # computing factorials will begin with 1
    if num < 0: # will not compute negative number factorials
        return None 
    elif num < 2:
        return ans # 0 or 1 factorial will always be 1
    else:
        for i in range(1, num + 1): # loop through num times
            ans = ans * i # multiply by the next number for each loop through
        return ans # return computed value


# function to check if the input year is a leap year or not
def check_leap_year(year):
    isLeap = False # default is NOT a leap year
    if (year % 4) == 0: # if the year is divisible by 4
        if (year % 100) == 0: # if the year is divisible by 100 AND
            if (year % 400) == 0: # if the year is divisible by 400
                isLeap = True # is a leap year
        else: # if the year is divisible by 4 but not 100 or 400
            isLeap = True # is a leap year
    return isLeap

print("factorial(0): {}".format(factorial(0)))
print("factorial(1): {}".format(factorial(1)))
print("factorial(5): {}".format(factorial(5)))
print("factorial(-3): {}".format(factorial(-3)))

print("check_leap_year(2000): {}".format(check_leap_year(2000)))
print("check_leap_year(1990): {}".format(check_leap_year(1990)))
print("check_leap_year(2012): {}".format(check_leap_year(2012)))
print("check_leap_year(2100): {}".format(check_leap_year(2100)))

class TestFactorial(unittest.TestCase):
    def test_factorial_0(self):
        self.assertEqual(factorial(0), 1)
    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)
    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)
    def test_factorial_neg_3(self):
        self.assertEqual(factorial(-3), None)

unittest.main(verbosity=2) 
