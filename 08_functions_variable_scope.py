# 功能 Function

# 內建功能 Build-in function
""" print()
int()
len() """

#自定義功能 Custom function
#define 定義
def sayHello():
    print('hello')

# Function Parameter參數
def sayHelloTo(name):
    print(f'Hello {name}')

def getRectangleArea(width,height=10):
    area = width*height
    return area

#sayHelloTo('Chris')
r1 = getRectangleArea(5,6)
r2 = getRectangleArea(2,3)
print(f'總面績是{r1+r2}')

#Default parameter 預設參數

# Return statement

# 變數作用範圍 Variable scope
outside = '外面' #Global scope 全域變數

def printVar():
    inside = '功能內' #Local Scope 本地變數
    print(f'{outside}   {inside}')

printVar()
print(inside)