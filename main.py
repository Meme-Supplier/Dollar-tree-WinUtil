import webbrowser

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

    print("Dollar tree WinUtil V0.3.1")
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
        import app

    if answer == '2':
        clearscreen()
        import windowsutilities

    if answer == '3':
        print('Closing...')


# OS detection

if ostype == 'Windows': # Detect if the OS is Windows
    main()

elif ostype == 'darwin': # Detects if the OS is macOS
    clearscreen()

    print('Seems like you are using macOS. macOS may not be supported. Continue anyway?\n')

    def answerselect():

        answer = input('Y or N')

        if answer == 'y' or 'Y':
            main()

        elif answer == 'n' or 'N':
            close()

    answerselect()

elif ostype == 'Linux': # Detects if the OS is Linux
    print('Seems like you are using Linux. Linux may not be supported. Continue anyway?\n')

    def answerselect():

        answer = input('Y or N')

        if answer == 'y' or 'Y':

            try:

                import os
                import platform
                main()

            except:
                clearscreen()
                print("Doesn't seem like you have one of the modules required.")
                print("Press 'Enter' to exit")
                input('')

        elif answer ==  'n' or 'N':
            clearscreen()
            close()

    answerselect()

else:
    print("This project only works on Windows, and I don't even know if it's supported on macOS. I haven't tested out macOS because I don't own one. Let me know if it does support it.")
    print('Press enter to close')
    input('')
