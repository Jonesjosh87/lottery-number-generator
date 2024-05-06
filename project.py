import random

def generate_lottery_number():
    # Create an empty list to store the lottery numbers
    lottery_number = []
    
    # Generate seven random numbers in the range of 0 through 9
    for _ in range(7):
        # Generate a random number from 0 to 9
        random_number = random.randint(0, 9)
        # Append the number to the list
        lottery_number.append(random_number)
    
    # Display the contents of the list
    print("Lottery number: ", end='')
    for number in lottery_number:
        print(number, end='')
    print()  # Print a newline at the end

# Call the function to generate and display the lottery number
generate_lottery_number()