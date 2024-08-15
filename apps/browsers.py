import os
import webbrowser

def clearscreen():
    os.system('cls') #clears the screen

def browserselect():
    clearscreen()

    print('Select browser\n')

    # Lists available browsers
    print('[1] Google Chrome')
    print('[2] Firefox')
    print('')

    answer = input('Select: ')

    if answer == '1': # Chrome selected
        clearscreen()

        print('[1] Download Google Chrome')
        print('[2] Back\n')

        answer = input('Select: ')

        if answer == '1':
            webbrowser.open_new("https://www.google.com/chrome/index.html") #Opens the web browser
            clearscreen()
            browserselect()

        if answer == '2':
            clearscreen()
            browserselect()

    if answer == '2': # Firefox selected
        clearscreen()

        print('[1] Download Firefox')
        print('[2] Back\n')

        answer = input('Select: ')

        if answer == '1':
            webbrowser.open_new("https://www.mozilla.org/en-US/firefox/all/#product-desktop-release") #Opens the web browser
            clearscreen()
            browserselect()

        if answer == '2':
            clearscreen()
            browserselect
