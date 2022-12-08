from diaries.DiarySample import DiarySample
from diaries.K21142Diary import K21142Diary
#↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    K21142Diary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()