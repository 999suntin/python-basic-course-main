#變數 Varialbe
course = "Python進階課程"
price = 99

#其他設定變數方式
name, age, gender = 'David',50,'M'
""" print(name)
print(age)
print(gender)
print(name,age,gender)

a = b = c = 1
print(a,b,c) """

# 變數命名規則
# 1. LowerCase (a-z) and UpperCase (A-Z) characters and digits(0-9) and underscore (_)
# 2. 唔能夠以數字開頭
# 3. 不能使用Python保留的關鍵字 (Reserved Keyword)
User_1 = 'jason'

# Naming convention (命名傳統)
# 1. 最好要有語意/意思的名字
# 2.多過一個字時 python(underscore) / 其他大小揩
location = 'Hong Kong'
l = 'Hong Kong'

hong_kong_time = '下午6時'
hongKongTime = '下午6時'

# Assignment指派
d=2
e=4
e=d #由右去左
print(f'e ={e}')
print(f'd ={d}')

#知道變數類別
print(type(d))
print(type(hongKongTime))