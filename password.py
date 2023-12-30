def main():
    
    # Get the key
    while True:
        key = input("Enter 10 digit key: ")
        if len(key) == 10 and len(set(key)) == 10 and key.isdigit():
            break
    
    # Get platform name
    platform = input("Enter platform name: ")
    
    # Ask for Conditions
    while True:
        try:
            length = int(input("Length of password: "))
            break
        except ValueError:
            pass
    upper = input("Include uppercase? (y/n): ").lower() == "y"
    lower = input("Include lowercase? (y/n): ") == "y"
    number = input("Include numbers? (y/n): ").lower() == "y"
    symbol = input("Include symbols? (y/n): ").lower() == "y"
    
    # Print password
    password = get_password(key, platform, length, upper, lower, number, symbol)
    print(f"\nYour password is: {password}")

    
        
#  Get the same password for same key, platform and constraints
def get_password(key, platform, length, upper, lower, number, symbol):
    ...              
    
main()