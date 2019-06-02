#!/usr/bin/python3
import hashlib
import pyfiglet


print(pyfiglet.figlet_format('HASHMATE'))

while 1:

    print('Which hashing function you want to compute?')
    print('1. md5')
    print('2. sha1')
    print('3. sha256')
    print('4. sha512')

    try:
        choice = int(input('Enter your choice: '))
    except ValueError:
        print('\nPlease enter a number, not a alphabet or word!')    
    else:
        if 1 <= choice <= 4:
            str = input('Now enter the string to be hashed: ')

            if choice == 1:
                print(hashlib.md5(str.encode('utf-8')).hexdigest())

            elif choice == 2:
                print(hashlib.sha1(str.encode('utf-8')).hexdigest())

            elif choice == 3:
                print(hashlib.sha256(str.encode('utf-8')).hexdigest())

            elif choice == 4:
                print(hashlib.sha512(str.encode('utf-8')).hexdigest())

        else:
            print('Invalid choice!\nPlease Choose a no. b/w 1 and 4')

    ch = input('\nDo you want to continue(y/n): ')
    if ch != 'y' and ch != 'Y':
        break        