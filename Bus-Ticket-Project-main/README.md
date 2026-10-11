# Bus-Ticket-Project
This project allows a customer to login as either an admin or user, after logging in as a user, the customer is given a range of different ticket categories to select, the user selects a category, then selects a top-up type for their chosen category. 

When logging in as an admin, different choices are presented instead of the usual ticket options.

If the user enters an invalid choice when logging in, the program tells them this and they must enter a valid choice to proceed.

After the user has finished making their choices on tickets, the price of their ticket is displayed, they can then either checkout, this quits the program, or they can change their ticket for a different one.

This program has two classes, Category and TopupTypes, the Category class handles the reading of the categories and their respective codes from the CSV file.

The TopupTypes class is responsible for reading the choices of TopupTypes and their respective codes from the CSV file, it is also responsible for reading the prices for each option.

The data for the categories, topup-types and prices are all read from the CSV file also in this repository, in order for this code to function the CSV file must be put in the same folder as the Python code.

Before attempting to use this code ensure Python is installed (version 3.11 works with this code),
And ensure the CSV file has been downloaded and placed in the same folder as the Python Code.
No other plugins are needed.
