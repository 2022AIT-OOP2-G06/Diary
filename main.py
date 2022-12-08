from diaries.DiarySample import DiarySample
from diaries.MitsukiDiary import MitsukiDiary

#↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    MitsukiDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()