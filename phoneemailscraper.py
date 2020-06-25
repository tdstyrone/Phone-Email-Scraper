import re  # import regular expressions
import pyperclip  # import pyperperclip module to get text from clipboard


def scrape_phone_number(text):

    phone_regex = re.compile(r'''
    (
    ((\d\d\d) | (\(\d\d\d\)))?      # area code (optional)
    (\s|-)                          # first seperator
    \d\d\d                          # first 3 digits
    -                               # second seperator
    \d\d\d\d                        # last 4 digits
    (((ext(\.)?\s)|x) (\d{2, 5}))?  # extension (optional)
    )
    ''', re.VERBOSE)

    extracted_numbers = phone_regex.findall(text)

    phone_numbers = []
    for numbers in extracted_numbers:
        phone_numbers.append(numbers[0])

    print("\nList of phone numbers extracted: ")
    print('\n'.join(phone_numbers))
pass

def scrape_emails(text):

    email_regex = re.compile(r'''
     [a-z0-9_+.]+  # username part
     @             # @ symbol
     [a-z0-9_+.]+  # domain name part
    ''', re.VERBOSE | re.IGNORECASE)

    extracted_emails = email_regex.findall(text)
    print("\nList of Email Addresses extracted:")
    print('\n'.join(extracted_emails))
pass

def main():
    print("----------------- PHONE NUMBER & EMAIL ADDRESS SCRAPER--------------------------")
    print('''Hi, Welcome to Tyrone's Phone Number and Email Address scraper!
    
    In order to use:
    * You must copy the text you wish to scrape to your clipboard.
    * Then you must choose an option from below:
    
    1. Extract Phone Numbers
    2. Extract Email Addresses
    0. To Exit
    ''')
    user_choice = int(input("Your Choice: "))
    while user_choice != 0:
        if user_choice == 1:
            text = pyperclip.paste()  # Get text from clipboard
            scrape_phone_number(text)
            user_choice = int(input("\nYour Choice: "))
        elif user_choice == 2:
            text = pyperclip.paste()
            scrape_emails(text)
            user_choice = int(input("\nYour Choice: "))
        else:
            print("Please enter a valid choice.")
    print("\n!!!THANKS FOR USING!!!")
pass

if __name__ == "__main__":
    main()
