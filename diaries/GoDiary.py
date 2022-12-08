from diaries.AbstractDiary import AbstractDiary
class GoDiary(AbstractDiary):
    
    def get_date(self):
        return "2021-10-10"
   
    def get_summary(self):
        return "ただただお腹の空いた日だった。ラーメン食べたい。"
    
    def get_author(self):
        return "ごう"