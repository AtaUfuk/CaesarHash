from os import path
import sys
import json

class CommonMethods(object):
    """description of class"""
    @staticmethod
    def exit_project(param:int):
        sys.exit(param)

    @staticmethod
    def get_settings(settingPath:str):
        if(settingPath is None or settingPath=='' or CommonMethods.check_file_path_exist(settingPath)==False):
            return None

        setting_file= open(settingPath,'r')
        data=json.load(setting_file)
        setting_file.close()
        return data

    @staticmethod
    def check_text_is_not_exist(text:str)->bool:
        return (text == None or text =='' or text ==' ')

    @staticmethod
    def check_file_path_exist(full_path:str)->bool:
        return path.isfile(full_path)

    def read_file_content(file_path:str,encode_format:str)->str:
        file=open(file_path,'r',encoding=encode_format)
        return file.read()

