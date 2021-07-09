stu = 5
score = []
for i in range(5):
    score.append(int(input("請輸入學生的數學成績: ")))
s = (sum(score))
avg = s/5
print("全班平均:",avg,"分")