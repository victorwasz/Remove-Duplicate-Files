# Remove-Duplicate-Files
If you have duplicated files in a folder, they may have diferent names but the exactly same contents inside, and you dont want to remove them by hand, then this code is for you. The code I made uses the SHA256 algorithym to find identical files inside a folder and copy the duplicates to another folder. The idea for copying and not deleting is just for a security reason and tracebility, this way you can know from where the files where removed. All you need to do is to change inside the code the directy where you want to scan the files and the directory where the files are going to be copied. Also you can chose you want to include subfolders or not. The code is written in Python 3.9.7
