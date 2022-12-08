from diaries.DiarySample import DiarySample
from diaries.RemiDiary import RemiDiary
from diaries.GoDiary import GoDiary
from diaries.K21142Diary import K21142Diary
from diaries.MitsukiDiary import MitsukiDiary
from diaries.AkashiDiary import AkashiDiary

#↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    RemiDiary(),
    GoDiary(),
    K21142Diary(),
    MitsukiDiary(),
    AkashiDiary(),
    ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()