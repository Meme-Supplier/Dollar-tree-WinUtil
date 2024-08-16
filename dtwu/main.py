# main.py

import sys

try:
    import os
    import platform

except:

    print('You need the OS module installed to continue.')
    input("Press 'Enter' to exit.")

ostype = platform.system()

def clearscreen():
    os.system('cls') #clears the screen

def close():
    print('Exiting...')

def main():
    clearscreen()

    print("Dollar tree WinUtil V0.5")
    print("OS:" , ostype , platform.release())
    print('\n')
    print('Choose a tool\n')

    print('[0] Download the real WinUtil\n')

    # Menu selection
    print('[1] Apps')
    print('[2] Windows utilities')
    print('')
    print('[3] Close')
    print('')

    answer = input('Select: ')

    if answer == '0':
        os.startfile("C:\\Users\\omdeb\\Desktop\\Dtwu\\psscripts\\WinUtilInstaller.cmd")
        main()
        
    if answer == '1':
        clearscreen()
        # Add the subfolder to the system path
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'apps')))

        # Now you can import the module
        import appselection

        # Use the imported function
        print(appselection.apptypeselection())

    if answer == '2':
        clearscreen()
        # Add the subfolder to the system path
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'WindowsUtilities')))

        # Now you can import the module
        import windowsutilities

        # Use the imported function
        print(windowsutilities.clearscreen())

    if answer == '3':
        print('Closing...')


if ostype == 'Windows':
    main()

else:

    print("This project only works on Windows, and I don't even know if it's supported on macOS. I haven't tested out macOS because I don't own one. Let me know if it does support it.")
    print('Press enter to close\n')
    input('')
