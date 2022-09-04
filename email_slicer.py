
# Function slicing will slice the given email into
# the username, domain, and extension.
# After completing this it will give you an option so either
# slice another email or not.
def slicing():
    print("Welcome to my email slicer!!!")
    emailslice = str(input("What email would you like to slice? "))

    (username, domain) = emailslice.split("@")
    (domain, extension) = domain.split(".")

    print("The email username is: " + username)
    print("The email domain is: " + domain)
    print("The email extension is: " + extension)

    again = str(input("Would you like to slice another email?(Yes or No) "))

    if again.lower() == "yes":
        slicing()
    
    if again.lower() == "no":
        print("Goodbye See You Next Time")

slicing()