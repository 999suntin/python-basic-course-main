#Boolean 布林值
#print(1!=1)
#print(1>5)

# Comparison Operators 比較運算子
# == 相等
# != 不相等
# > 大於
# < 小於
# >= 大過或等於
# <= 小過或等於

# 條件判斷 if else
mark = input('請輸入積分')
print(type(mark))

# 合格 >=504
if(int(mark) >= 50):
    print('合格')
    print('Yes')
elif(int(mark) < 50 and int(mark) >= 30):
    print('唔合格，還需努力')
else:
    print('唔合格')
    print('OH NO，見家長')

# Logical Operators 邏輯運算子
#and 同埋
#or  或者
#not 非

if(attendClass==False or int(mark)<30)
    print('見家長')

if(not(loggedIn))