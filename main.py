from diaries.DiarySample import DiarySample
from diaries.GoDiary import GoDiary
from diaries.GoDiary import GoDiary

#↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    GoDiary(),
    ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()