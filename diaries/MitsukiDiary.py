from diaries.AbstractDiary import AbstractDiary
class MitsukiDiary(AbstractDiary):
    
    def get_date(self):
        return "2021-10-18"
   
    def get_summary(self):
        return "ライブに行った。席も良くてサイコーだった！"
    
    def get_author(self):
        return "みつき"