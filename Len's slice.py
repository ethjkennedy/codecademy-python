#This script is used to practice working with lists in Python.

# List of inventory
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

#Pricing
prices = [2, 6, 1, 3, 2, 7, 2]

#Number of slices wich are 2 dollars
print(prices.count(2))

#Number of pizza options
num_pizzas = len(toppings)
print(num_pizzas)

# Statment
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# 2-D list of pizza slices
pizza_and_prices = []
for i in range(len(toppings)):
    pizza_and_prices.append([toppings[i], prices[i]])

#Sorting by prices
pizza_and_prices.sort(key=lambda x: x[1])
print(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

#Removing the last option as it is now sold out
pizza_and_prices.pop(-1)
print(pizza_and_prices)

# Adding a new pizza option
pizza_and_prices.insert(4, ['peppers', 2.5])
print(pizza_and_prices)

#Fidning the 3 cheapest options
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)