from Business.CommonMethods import CommonMethods as cm
class Hashing(object):
    """description of class"""
    
    def caesar_encryption(self,text:str)->str:
        hashedArray=[]
        if(cm.check_text_is_not_exist(text)):
            return None
        settings=cm.get_settings("./Settings/appSettings.json")
        for c in text:
            asciiCode=ord(c)+settings["ShiftCount"]
            if(asciiCode>int(settings["AsciiMaxCount"])):
                asciiCode-=int(settings["AsciiMaxCount"])
            hashedArray.append(chr(asciiCode))
        return ''.join(hashedArray)

    def caesar_decryption(self,text:str)->str:
        decryptedArray=[]

        if(cm.check_text_is_not_exist(text)):
            return None
        settings=cm.get_settings("./Settings/appSettings.json")
        for c in text:
            asciiCode=ord(c)-settings["ShiftCount"]
            if(asciiCode<0):
                asciiCode+=int(settings["AsciiMaxCount"])
            decryptedArray.append(chr(asciiCode))
        return ''.join(decryptedArray)





