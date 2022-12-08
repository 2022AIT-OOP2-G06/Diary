from diaries.AbstractDiary import AbstractDiary
class RemiDiary(AbstractDiary):
    
    def get_date(self):
        return "2021-12-12"
   
    def get_summary(self):
        return "スキーの初滑りに行った。筋肉痛になった。"
    
    def get_author(self):
        return "れみ"