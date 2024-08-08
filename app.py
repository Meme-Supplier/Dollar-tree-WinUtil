import os
import webbrowser

def clearscreen():
    os.system('cls') #clears the screen

def appselection():

    clearscreen()

    # Tool select
    print('[0] Back to select screen (Not working)')
    print('')
    print('[1] Download Winaero Tweaker')
    print('[2] HiBit Uninstaller')
    print('[3] 7-Zip File Manager')
    print('[4] Rufus')
    print('[5] Notepad++')
    print('[6] GIMP')
    print('')

    answer = input("Select: ")

    if answer == "0":
        import main

    if answer == "1": #Winaero Tweaker selected
        clearscreen()

        print('[1] Download Winaero Tweaker')
        print('[2] Go back')
        print('')

        answer = input("Select: ")

        if answer == "1": # Download Winaero Tweaker

            clearscreen()

            webbrowser.open_new("https://winaerotweaker.com/") #Opens the web browser
            clearscreen()
            appselection()

        if answer == "2": #Returns

            clearscreen()
            appselection()

    if answer == "2": #Hibit Uninstaller selected
        clearscreen()

        print('[1] Download Hibit Uninstaller')
        print('[2] Go back')
        print('')

        answer = input('Select:')

        if answer == "1": # Download Hibit Uninstaller

            clearscreen()

            webbrowser.open_new("https://www.majorgeeks.com/mg/get/hibit_uninstaller,1.html") #Opens the web browser
            clearscreen()
            appselection()

        if answer == "2": #Returns

            clearscreen()
            appselection()

    if answer == "3": #Hibit Uninstaller selected
        clearscreen()

        print('[1] Download 7-Zip File Manager')
        print('[2] Go back')
        print('')

        answer = input('Select: ')

        if answer == "1": # Download Hibit Uninstaller

            clearscreen()
            print('Choose version')
            print('')
            print('[1] x64')
            print('[2] x86')
            print('[3] ARM64')
            print('')
            print('[4] Restart')
            print('')

            answer = input('Select: ')
            clearscreen()

            if answer == '1':
                webbrowser.open_new("https://www.7-zip.org/a/7z2407-x64.exe") #Opens the web browser
                clearscreen()
                appselection()

            if answer == '2':
                webbrowser.open_new("https://www.7-zip.org/a/7z2407.exe") #Opens the web browser
                clearscreen()
                appselection()

            if answer == '3':
                webbrowser.open_new("https://www.7-zip.org/a/7z2407-arm64.exe") #Opens the web browser
                clearscreen()
                appselection()

            if answer == '4':
                clearscreen()
                appselection()

        if answer == "2": #Returns

            clearscreen()
            appselection()

    if answer == "4": # Rufus selected
        clearscreen()

        print('[1] Download ')
        print('[2] Go back')
        print('')

        answer = input("Select: ")

        if answer == "1": # Download Rufus
            clearscreen()

            print('Choose version')
            print('')
            print('[1] x64')
            print('[2] x86')
            print('[3] ARM64')
            print('[4] x64 Portable')
            print('')
            print('[5] Restart')
            print('')
            
            answer == input('Select: ')

            if answer == '1':
                webbrowser.open_new("https://github.com/pbatard/rufus/releases/download/v4.5/rufus-4.5.exe") #Opens the web browser
                clearscreen()
                appselection()

            if answer == '2':
                webbrowser.open_new("https://github.com/pbatard/rufus/releases/download/v4.5/rufus-4.5_x86.exe") #Opens the web browser
                clearscreen()
                appselection()

            if answer == '3':
                webbrowser.open_new("https://github.com/pbatard/rufus/releases/download/v4.5/rufus-4.5_arm64.exe") #Opens the web browser
                clearscreen()
                appselection()

            if answer == '4':
                webbrowser.open_new("https://github.com/pbatard/rufus/releases/download/v4.5/rufus-4.5p.exe") #Opens the web browser
                clearscreen()
                appselection()

            if answer == '5':
                clearscreen()
                appselection()

        if answer == "2": #Returns

            clearscreen()
            appselection()

    if answer == "5": #Download Notepad++ selected
        clearscreen()

        print('[1] Download Notepad++')
        print('[2] Go back')
        print('')

        answer = input("Select: ")

        if answer == "1": # Download Notepad++
            clearscreen()

            print('[1] x64')
            print('[2] x32, x86')
            print('[3] ARM64')
            print('')
            print('[4] Go Back')
            print('')

            answer = input('Select: ')

            if answer == '1': # x64 version chosen
                clearscreen()

                print('[1] Installer')
                print('[2] Portable')
                print('[3] Mini-portable (7z)')
                print('')
                print('[4] Return')
                print('')

                answer = input("Select: ")

                if answer == '1': #Installer selected
                    webbrowser.open_new("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.7/npp.8.6.7.Installer.x64.exe") #Opens the web browser
                    clearscreen()
                    appselection()


                if answer == '2': # Portable options
                    clearscreen()

                    print('[1] Portable zip')
                    print('[2] Portable 7z')
                    print('')
                    print('[3] Return')
    
                    answer = input('Select: ')

                    if answer == '1':
                        webbrowser.open_new("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.7/npp.8.6.7.portable.x64.zip") #Opens the web browser
                        clearscreen()
                        appselection()

                    if answer == '2':
                        webbrowser.open_new("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.7/npp.8.6.7.portable.x64.7z") #Opens the web browser
                        clearscreen()
                        appselection()

                    if answer == '3':
                        clearscreen()
                        appselection()
                        


                if answer == '3': #Mini Portable selected
                    webbrowser.open_new("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.7/npp.8.6.7.portable.minimalist.x64.7z") #Opens the web browser
                    clearscreen()
                    appselection()


            if answer == '2': # x32 Version chosen
                clearscreen()

                print('[1] Installer')
                print('[2] Portable')
                print('[3] Mini-portable (7z)')
                print('')
                print('[4] Return')
                print('')

                answer = input("Select: ")

                if answer == '1': #Installer selected
                    webbrowser.open_new("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.7/npp.8.6.7.Installer.exe") #Opens the web browser
                    clearscreen()
                    appselection()


                if answer == '2': # Portable options
                    clearscreen()

                    print('[1] Portable zip')
                    print('[2] Portable 7z')
                    print('')
                    print('[3] Return')
    
                    answer = input('Select: ')

                    if answer == '1':
                        webbrowser.open_new("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.7/npp.8.6.7.portable.zip") #Opens the web browser
                        clearscreen()
                        appselection()

                    if answer == '2':
                        webbrowser.open_new("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.7/npp.8.6.7.portable.7z") #Opens the web browser
                        clearscreen()
                        appselection()

                    if answer == '3':
                        clearscreen()
                        appselection()
                        


                if answer == '3': #Mini Portable selected
                    webbrowser.open_new("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.7/npp.8.6.7.portable.minimalist.7z") #Opens the web browser
                    clearscreen()
                    appselection()


            if answer == '3': # ARM64 Version chosen
                clearscreen()

                print('[1] Installer')
                print('[2] Portable')
                print('[3] Mini-portable (7z)')
                print('')
                print('[4] Return')
                print('')

                answer = input("Select: ")

                if answer == '1': #Installer selected
                    webbrowser.open_new("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.7/npp.8.6.7.Installer.arm64.exe") #Opens the web browser
                    clearscreen()
                    appselection()


                if answer == '2': # Portable options
                    clearscreen()

                    print('[1] Portable zip')
                    print('[2] Portable 7z')
                    print('')
                    print('[3] Return')
    
                    answer = input('Select: ')

                    if answer == '1':
                        webbrowser.open_new("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.7/npp.8.6.7.portable.zip") #Opens the web browser
                        clearscreen()
                        appselection()

                    if answer == '2':
                        webbrowser.open_new("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.7/npp.8.6.7.portable.7z") #Opens the web browser
                        clearscreen()
                        appselection()

                    if answer == '3':
                        clearscreen()
                        appselection()
                        


                if answer == '3': #Mini Portable selected
                    webbrowser.open_new("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.7/npp.8.6.7.portable.minimalist.7z") #Opens the web browser
                    clearscreen()
                    appselection()
                
                

            if answer == '4':
               clearscreen()
               appselection()


        if answer == "2": #Returns
            clearscreen()
            appselection()

    if answer == '6':
        print('[1] Download GIMP') # Download GIMP
        print('[2] Go back')
        print('')


appselection() #Basically restarts the program
