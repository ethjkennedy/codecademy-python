#Not summing to ten

num1 = 5
num2 = 6

def sum_to_ten(num1, num2):
    if num1 + num2 == 10:
        return True
    else:
        return False

#Checking if expenses go over a budget
budget = 2000

food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

total = food_bill + electricity_bill + internet_bill + rent
if total > budget:
    over_budget = True
else:
    over_budget = False

# In range

def in_range(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False  
    
print(in_range(4,1,10))

# Same name

def same_name(name1, name2):
    if (name1 == name2):
        return True
    else:
        return False
    
# Always false

def always_false(num):
    if num > 10 and num < 0:
        return True
    else:
        return False
    
print(always_false(5))