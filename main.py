import webbrowser

try:
    import os

except:

    print('You need the OS module installed to continue.')
    input("Press 'Enter' to exit.")

def clearscreen():
    os.system('cls') #clears the screen

def main():
    clearscreen()

    print("Dollar tree WinUtil V0.2.1")
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
main()
