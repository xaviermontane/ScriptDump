import random
import string

length = int(input('Enter the length of the password: '))

print ('Choose the type of password you want to generate:\n 1. Numbers\n2. Letters\n3. Alphanumeric\n4. Special Characters')
choice = int(input('Enter your choice: '))

while True:
    if choice == 1:
        print(''.join(random.choice(string.digits) for x in range(length)))
        break
    elif choice == 2:
        print(''.join(random.choice(string.ascii_letters) for x in range(length)))
        break
    elif choice == 3:
        print(''.join(random.choice(string.ascii_letters + string.digits) for x in range(length)))
        break
    elif choice == 4:
        print(''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(length)))
        break
    else:
        print('Invalid choice')