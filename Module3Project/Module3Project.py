# Ice Cream Shop Application
# Author: Ifa Namee
# Date: 1/29/2025
# Capstone class

# import statement to get time we this program runs.
import time

# Store our ice cream shop's menu items
# Add three ice cream flavors
cones = ["cake cone", "waffle cone", "dipped cone", "waffle bowl"]
flavors = ["vanilla", "caramel", "mint", "strawberry", "mango", "banana"]
toppings = ["sprinkles", "nuts", "cherry"]
prices = {"scoop": 4.50, "topping": 1.50}

# Function for menu 
def display_menu():
    # Shows available flavors and toppings to the customer
    print("\n=== Welcome to the Ice Cream Shop! ===")

    # For loop to through cones and display
    print("\nChoose a cone:")
    for index, cone in enumerate(cones, start=1):  # Using enumerate() to add index
        print(f" {index} = {cone}")  # Displays index starting from 1

    # Loop through the flavor list and show each flavor, then 
    # For loop through the toppings list and display them
    print("\nAvailable flavors:")
    for flavor in flavors:
        print(f" - {flavor}")

    # Printing toppings using for loop to through all topping
    print("\nAvailable Toppings:")
    for topping in toppings:
        print(f"- {topping}")

    # Display the prices
    print("\nPrices")
    print(f"Scoops: ${prices['scoop']:.2f} each")
    print(f"Toppings: ${prices['topping']:.2f} each")


def pick_cone():
    # Gets ice cream cone choice from the customer
    while True:
        try:
            # Prompt the user to choose a cone by name or number
            user_input = input("\nChoose a cone (name or number 1-4): ").strip().lower()

            # Check if input is a number
            if user_input.isdigit():
                choice = int(user_input)
                if 1 <= choice <= len(cones):  # Ensure it's within range
                    return cones[choice - 1]
                else:
                    print("\nInvalid number. Please choose between 1 and 4.")
            else:
                # Check if the user entered a valid cone name
                if user_input in [cone.lower() for cone in cones]:
                    return user_input.title()
                else:
                    print("\nInvalid input. Please enter a valid cone name or number.")

        except ValueError:
            print("Invalid input. Please enter a valid number or cone name.")


def get_flavors():
    # Gets ice cream flavor choices from the customer
    chosen_flavors = []  # Empty list to collect flavors.

    # Use a while loop to keep taking orders until the customer is done
    while True:
        try:
            # Prompt the user to choose their scoops of ice cream
            # Add three ice cream flavors so gonna be 1 to 6 range
            num_scoops = int(input("\nHow many scoops would you like? (1-6): "))
            # Validate the input 
            if 1 <= num_scoops <= 6:
                break
            print("Please choose between 1 and 6 scoops.")
        except ValueError:
            print("Please enter a number.")

    # Prompt the user to enter the ice cream flavor
    print("\nFor each scoop, enter the flavor you'd like:")
    for i in range(num_scoops): #For loop prompts for each scoop of ice cream
        # Nested while loop handles the user's input and validation
        while True:
            flavor = input(f"Scoop {i+1}: ").lower() # lower means change into lower cases.
            # Check to see if the flavor is one that's in the shop's list
            if flavor in flavors:
                chosen_flavors.append(flavor) # append is add into chosen_flovors list
                break
            print("Sorry, that flavor isn't available.")
    
    # Return to the calling function, the number of scoops the user wants
    # and the flavors they picked
    return num_scoops, chosen_flavors

def get_toppings():
    chosen_toppings = []  # Empty list to collect toppings.

    # Use a while loop to prompt the user for the toppings until they
    #  are done adding toppings
    while True:
        topping = input("\nEnter a topping (or 'done' if finished): ").lower()
        #Test if the user is done ordering toppings
        if topping == 'done':
            break
        # Test if the topping is in the list of toppings for our shop
        if topping in toppings:
            chosen_toppings.append(topping)  # append is add into chosen_toppings list
            print(f"Added {topping}!")
        else:
            print("Sorry, that topping isn't available.")

    # Return the list of toppings that the user chose
    return chosen_toppings

def calculate_total(num_scoops, num_toppings):
    # Calculates the total cost of the order
    scoop_cost = num_scoops * prices["scoop"] # math calculation to get total amount of flavors
    topping_cost = num_toppings * prices["topping"] # math calculation to get total amount of flavors
    return scoop_cost + topping_cost  # add total amount of order.

def print_receipt(chosen_cone, num_scoops, chosen_flavors, chosen_toppings, formatted_time, formatted_date):
    # Prints a nice receipt for the customer
    print()
    print("=====================================")
    print("\n=== Your Ice Cream Order ===")

    print(f"\nYou selection: {chosen_cone}")

    for i in range(num_scoops):
        print(f"Scoop {i+1}: {chosen_flavors[i].title()}") # title is to captalize first letter.

    if chosen_toppings:
        print("\nToppings:")
        # Loop through the list of toppings
        for topping in chosen_toppings:
            print(f" - {topping.title()}")

    # Print the total
    # or total = calculate_total(scoop_cost + topping_cost)
    total = calculate_total(num_scoops, len(chosen_toppings))
    print(f"\nTotal: ${total:.2f}")

    print("\nCurrent time ",formatted_time,"," ,formatted_date)
    print("=====================================")
    print()

    # Save order to file 
    with open("daily_orders.txt", "a") as file:
        file.write(f"\n{num_scoops} scoops - ${total:.2f}, Ordered at {formatted_time}, {formatted_date}")

# Main function - updated test fucnction
def main():
    display_menu()

    # call the pick function which return the of user cone choose
    chosen_cone = pick_cone()  # Added missing function call
    
    # Call get flavors function, which returns the number of scoops
    # and the list of flavors
    num_scoops, chosen_flavors = get_flavors()

    # Call the get toppings functions which returns the list of toppings
    chosen_toppings = get_toppings()

    # Get current time and format it
    current_time = time.localtime()
    formatted_time = time.strftime("%I:%M %p", current_time)  # Format time (12-hour format with AM/PM)
    formatted_date = time.strftime("%m-%d-%Y", current_time)  # Format date (MM-DD-YYYY)

    # Display the receipts and time of order made.
    print_receipt(chosen_cone, num_scoops, chosen_flavors, chosen_toppings, formatted_time, formatted_date)

# Automatically execute the main function when the application runs
if __name__ == "__main__":
    main()