# python-challenge-1
Python Challenge 1 AI Bootcamp due 12/10/2024

## Overview
1. Create a food truck ordering system where customer can order different kinds of food and/or drinks
2. If the data entry is not in the right format (ie. not as an integer) then the program will prompt an error message asking for the right input
3. Customer can continue ordering as much as they want
4. The quantity of ordering is default to 1 if no number is entered
5. Behind the scene, the customer order if being stored until they complete ordering things
6. Once they finish with the order they will see the total cost per each menu category PLUS the total order cost of everything
7. In this exercise we want to make sure calculations are done correctly and each warning makes sense

## How I did my work
1. Downloaded the homework starter file
2. Created pseudo code by outlining what needs to be done
3. Received help from ChatGPT and Claude.AI, modified things that needed to be done to comply with instructions
4. Debug and test multiple times
5. Connected with a tutor to get some guidance on process of thought
6. Total hours spent to finalize the code to ensure accuracy and meeting the goal is approx 20 hours

## Output Examples, copy paste from the terminal after the program was run

```
Welcome to the variety food truck.

Here's our full menu:

Snacks:
  - Cookie: $0.99
  - Banana: $0.69
  - Apple: $0.49
  - Granola bar: $1.99

Meals:
  - Burrito: $4.49
  - Teriyaki Chicken: $9.99
  - Sushi: $7.49
  - Pad Thai: $6.99
  Pizza:
    - Cheese: $8.99
    - Pepperoni: $10.99
    - Vegetarian: $9.99
  Burger:
    - Chicken: $7.49
    - Beef: $8.49

Drinks:
  Soda:
    - Small: $1.99
    - Medium: $2.49
    - Large: $2.99
  Tea:
    - Green: $2.49
    - Thai iced: $3.99
    - Irish breakfast: $2.49
  Coffee:
    - Espresso: $2.99
    - Flat white: $2.99
    - Iced: $3.49

Dessert:
  - Chocolate lava cake: $10.99
  Cheesecake:
    - New York: $4.99
    - Strawberry: $6.49
  - Australian Pavlova: $9.99
  - Rice pudding: $4.99
  - Fried banana: $4.49

From which menu would you like to order?
1: Snacks
2: Meals
3: Drinks
4: Dessert

Type menu number: e
Please enter a valid number.

Would you like to keep ordering? (Y)es or (N)o: y

From which menu would you like to order?
1: Snacks
2: Meals
3: Drinks
4: Dessert

Type menu number: 2

You selected Meals

What Meals item would you like to order?

Item # | Item name                | Price
-------|--------------------------|-------
1      | Burrito                  | $4.49
2      | Teriyaki Chicken         | $9.99
3      | Sushi                    | $7.49
4      | Pad Thai                 | $6.99
5      | Pizza - Cheese           | $8.99
6      | Pizza - Pepperoni        | $10.99
7      | Pizza - Vegetarian       | $9.99
8      | Burger - Chicken         | $7.49
9      | Burger - Beef            | $8.49

Enter item number: 3t
Please enter a valid number.

Would you like to keep ordering? (Y)es or (N)o: y

From which menu would you like to order?
1: Snacks
2: Meals
3: Drinks
4: Dessert

Type menu number: 2

You selected Meals

What Meals item would you like to order?

Item # | Item name                | Price
-------|--------------------------|-------
1      | Burrito                  | $4.49
2      | Teriyaki Chicken         | $9.99
3      | Sushi                    | $7.49
4      | Pad Thai                 | $6.99
5      | Pizza - Cheese           | $8.99
6      | Pizza - Pepperoni        | $10.99
7      | Pizza - Vegetarian       | $9.99
8      | Burger - Chicken         | $7.49
9      | Burger - Beef            | $8.49

Enter item number: 4
Enter quantity (default is 1): 

Added 1 x Pad Thai to your order.

Would you like to keep ordering? (Y)es or (N)o: y

From which menu would you like to order?
1: Snacks
2: Meals
3: Drinks
4: Dessert

Type menu number: 5
5 was not a menu option.

Would you like to keep ordering? (Y)es or (N)o: y

From which menu would you like to order?
1: Snacks
2: Meals
3: Drinks
4: Dessert

Type menu number: 1

You selected Snacks

What Snacks item would you like to order?

Item # | Item name                | Price
-------|--------------------------|-------
1      | Cookie                   | $0.99
2      | Banana                   | $0.69
3      | Apple                    | $0.49
4      | Granola bar              | $1.99

Enter item number: 2
Enter quantity (default is 1): 9

Added 9 x Banana to your order.

Would you like to keep ordering? (Y)es or (N)o: y

From which menu would you like to order?
1: Snacks
2: Meals
3: Drinks
4: Dessert

Type menu number: 4

You selected Dessert

What Dessert item would you like to order?

Item # | Item name                | Price
-------|--------------------------|-------
1      | Chocolate lava cake      | $10.99
2      | Cheesecake - New York    | $4.99
3      | Cheesecake - Strawberry  | $6.49
4      | Australian Pavlova       | $9.99
5      | Rice pudding             | $4.99
6      | Fried banana             | $4.49

Enter item number: 1
Enter quantity (default is 1): 5f
Please enter a valid positive number.
Enter quantity (default is 1): 5

Added 5 x Chocolate lava cake to your order.

Would you like to keep ordering? (Y)es or (N)o: y

From which menu would you like to order?
1: Snacks
2: Meals
3: Drinks
4: Dessert

Type menu number: 3

You selected Drinks

What Drinks item would you like to order?

Item # | Item name                | Price
-------|--------------------------|-------
1      | Soda - Small             | $1.99
2      | Soda - Medium            | $2.49
3      | Soda - Large             | $2.99
4      | Tea - Green              | $2.49
5      | Tea - Thai iced          | $3.99
6      | Tea - Irish breakfast    | $2.49
7      | Coffee - Espresso        | $2.99
8      | Coffee - Flat white      | $2.99
9      | Coffee - Iced            | $3.49

Enter item number: 2
Enter quantity (default is 1): 

Added 1 x Soda - Medium to your order.

Would you like to keep ordering? (Y)es or (N)o: n

Thank you for stopping by!

This is what we are preparing for you.

Item name                 | Price    | Quantity | Total
--------------------------|----------|----------|-------
Pad Thai                  | $6.99    | 1        | $6.99
Banana                    | $0.69    | 9        | $6.21
Chocolate lava cake       | $10.99   | 5        | $54.95
Soda - Medium             | $2.49    | 1        | $2.49
--------------------------------------------------------
Total order cost: $70.64

Thank you for your payment!
```
