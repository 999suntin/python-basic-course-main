# List 列表 / 清單 (Indexed Array)
marks = [12,55,98,70,40,60] #每個值叫element(元素)

print(f'marks資料類別是{type(marks)}')
print(f'總共有{len(marks)}個分數')

#print list value
print(marks[0]) #索引 index
print(marks[1])
#索引(index)位係0開始

print(marks[-1])
print(marks[-2])

print(marks[2:5])
#note that the item in position 5 is NOT included

#改list值
marks[0] = 25
print(marks[0])

#加list element
marks.append(95) # 加到最後
print(marks)

marks.insert(1,30)
print(marks)

#刪list element
marks.remove(40)
print(marks)

marks.pop(2)
marks.clear()
print(marks)

#for loop 
studentMarks = [25, 30, 55, 98, 70, 40, 60, 95]
studentMarks1 = []

for mark in studentMarks1:
    print(mark)
else:
    print('無資料')
#for with else (萬一個list無野可以通知度個user)

#while loop print list都得
i = 0
while (i < len(studentMarks)):
    print(studentMarks[i])
    i = i + 1