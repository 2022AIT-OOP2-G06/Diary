from diaries.DiarySample import DiarySample
from diaries.RemiDiary import RemiDiary
from diaries.GoDiary import GoDiary
from diaries.GoDiary import GoDiary

#↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    RemiDiary(),
    GoDiary(),
    ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()