import itertools
import string
import time
from alive_progress import alive_bar

def brute_force(target_password, max_length):
    start_time = time.time()  # Record the start time

    # Define the character set for the password guess attempts
    characters = string.ascii_letters + string.digits 

    # Get the total number of password combinations to calculate progress
    total_combinations = sum(len(characters) ** length for length in range(1, max_length + 1))

    with alive_bar(total_combinations, bar='classic', spinner='dots_waves') as bar:
        # Iterate through different password lengths
        for length in range(1, max_length + 1):
            # Iterate through all possible combinations of characters for the current password length
            for attempt in itertools.product(characters, repeat=length):
                attempt = ''.join(attempt)
                if attempt == target_password:
                    end_time = time.time()  # Record the end time
                    duration = end_time - start_time  # Calculate the duration
                    return attempt, duration
                bar()  # Increment the progress bar

    return None, None

def main():
    print("Brute-force password guesser for educational purposes only.")
    print("Enter the target password and the maximum length to guess (up to 6 for reasonable runtimes).")

    # Get the target password from the user
    target_password = input("Enter the target password: ")
    # Get the maximum length from the user 
    max_length = int(input("Enter the maximum length: ")) 

    guessed_password, duration = brute_force(target_password, max_length)

    if guessed_password:
        print(f"Password found: {guessed_password}")
        print(f"Time taken: {duration:.2f} seconds")
    else:
        print("Password not found")

if __name__ == "__main__":
    main()
