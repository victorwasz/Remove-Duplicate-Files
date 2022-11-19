import os
import hashlib
import shutil

rootdir = 'C:/Users/Victor/Desktop/SHA_256'        # Define where to look for duplicate files
address_dest = 'C:/Users/Victor/Desktop/Copy'  # Define where to copy the files that are duplicade
Include_subdirectories = 1                              # Use 1 for including subdirectories and 0 for not including

def search(address_org,address_dest):
    
    files = os.listdir(address_org)

    for file in files:

        if os.path.isdir(address_org +"/" + file):
            pass
        else:
            
            with open(address_org +"/" + file,"rb") as f: 
                bytes = f.read()
                f.close()
                SHA_256 = hashlib.sha256(bytes).hexdigest();
                
            if SHA_256 in list_sha256:
                shutil.move(address_org +"/"+file, address_dest+"/"+address_org.replace("\\","/").replace("/","_").replace(":","")+"_"+file)
                
            else:  
                list_sha256.append(SHA_256)


def listdirs(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            list_dir.append(it.path)
            listdirs(it)

list_dir = [rootdir]
list_sha256 = []

if Include_subdirectories == 1: listdirs(rootdir) 

for i in list_dir:
    search(i,address_dest)
    print(i.replace("\\","/"))