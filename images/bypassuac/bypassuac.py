import os 
from subprocess import * 
 
path = 'c:\windows\system32' 
files = os.listdir(path) 
print(files) 
def GetFileList(path, fileList): 
    newDir = path 
    if os.path.isfile(path): 
        if path[-4:] == '.exe': 
            fileList.append(path) 
    elif os.path.isdir(path): 
        try: 
            for s in os.listdir(path): 
                newDir=os.path.join(path,s) 
                GetFileList(newDir, fileList) 
        except Exception as e: 
            pass 
    return fileList 
files = GetFileList(path, []) 
print(files) 

for eachFile in files: 
    if eachFile[-4:] == '.exe': 
        command = r'.\sigcheck64.exe -m {} | findstr auto'.format(eachFile) 
        print(command) 
        p1 = Popen(command, shell=True, stdin=PIPE, stdout=PIPE) 
        if '<autoElevate>true</autoElevate>' in p1.stdout.read().decode('gb2312'): 
            copy_command = r'copy {} .\success'.format(eachFile) 
            Popen(copy_command, shell=True, stdin=PIPE, stdout=PIPE) 
            print('[+] {}'.format(eachFile)) 
            with open('success.txt', 'at') as f: 
                f.writelines('{}\n'.format(eachFile))