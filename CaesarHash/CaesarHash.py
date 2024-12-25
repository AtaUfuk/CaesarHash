from Business.CommonMethods import CommonMethods as cm
from Business.Hashing import Hashing

filePath=input('Please insert file path:')
if(cm.check_file_path_exist(filePath)==False):
    print('Please check file path...')
    cm.exit_project(0)
is_encryption=input('Encryption or Decryption(Please write E or D)')

content=cm.read_file_content(filePath)
myHashing=Hashing()
result=''
if(is_encryption=='E'):
    result=myHashing.caesar_encryption(content)
else:
    result=myHashing.caesar_decryption(content)
print(result)