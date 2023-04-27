# 02-15-2023
# Using 100 as an estimate, Pi is approximated to be 3.1415926535897936

# Defines the function to approximate Pi
def abr_pi(n):
    pi_approx = 0 # Initializes Pi
    for i in range(0,n+1):
        pi_approx += ((2*(-1)**i)*(3**((1/2)-i)))/(2*i+1) # Abraham Series
    return pi_approx

# Defines the function to get user input and plug it into the abr_pi function
def main():

    n = int(input("Enter the number of terms: ")) # Gets user input

    pi = abr_pi(n) # Sets Pi equal to the approximation when using n

    print("Using", n, "as an estimate, Pi is approximated to be", pi) # Prints result

if __name__ == '__main__': # Initializes main
    main()