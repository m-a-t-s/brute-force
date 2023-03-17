<h2>Installation</h2>
Before running the script, you need to install the alive-progress library. You can do this by running the following command in your terminal:

`
pip install alive-progress
Once the library is installed, download the script and run it in your preferred Python environment.
`

<h2>Usage</h2>
To use the password guesser, run the script and follow the instructions provided in the command line interface. You will be prompted to enter the target password and the maximum length to guess (up to 6 for reasonable runtimes).

`$ python password_guesser.py
Brute-force password guesser for educational purposes only.
Enter the target password and the maximum length to guess (up to 6 for reasonable runtimes).
Enter the target password: <target_password>
Enter the maximum length: <max_length>
`
A progress bar will be displayed in the terminal to indicate the progress of the password guess attempts. The progress bar updates for each iteration of the loop, showing the percentage completion and the estimated time remaining.

Once the password is found or all combinations have been tried, the script will display the result and the time taken to guess the password.

<h2>Disclaimer</h2>
This script is for educational purposes only and should not be used to gain unauthorized access to any system or account. The use of brute-force attacks to obtain passwords is illegal and unethical.