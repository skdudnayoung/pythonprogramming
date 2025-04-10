guguLine = ""

# 단 제목 출력
for i in range(2, 10):
    guguLine += " #%2d단 #  " % i
print(guguLine)

# 구구단 본문 출력
for i in range(1, 10):
    guguLine = ""
    for k in range(2, 10):
        guguLine += "%2dX%2d=%2d  " % (k, i, k * i)
    print(guguLine)