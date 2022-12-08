from diaries.DiarySample import DiarySample
from diaries.AkashiDiary import AkashiDiary

#↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    AkashiDiary(),
    ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()