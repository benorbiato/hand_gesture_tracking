import os

class AppService:
    def __init__(self):
        self.word_open = False
        self.firefox_open = False
        self.excel_open = False
        
    def process_left_hand(self, fingers):
        if fingers == const.FINGER_1 and not self.word_open:
            self.word_open = True
            os.startfile(r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE')
            
        if fingers == const.FINGER_1_2 and not self.excel_open:
            self.excel_open = True
            os.startfile(r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE')
            
        if fingers == const.FINGER_1_2_3 and not self.firefox_open:
            self.firefox_open = True
            os.startfile(r'C:\Program Files\Mozilla Firefox\firefox.exe')
            
        if fingers == const.FINGER_NONE and self.firefox_open:
            self.firefox_open = False
            os.system('TASKKILL /IM firefox.exe')