#Tuple
""" tup1 = ('people', True, 1997, 2022)

print(type(tup1))
print(tup1[0])

# Tuple一但定義，其順序 和 element值都不能更改

tup2 = ('op',)
print(type(tup2)) """

import os

path = 'C:\\Users\\user\\Desktop\\rename\\'

dir = os.listdir(path)
print(f'資料夾內有{len(dir)}張圖片')

#print(type(dir))
#print(dir)
newName = input('請輸入新檔案名 : ')

for index,fileName in enumerate(dir,start = 1):
    #print(index, fileName)
    print(f'正在處理第{index}/{len(dir)}張')
    os.rename(path+fileName,path+f'{newName}_{index}.jpg')

print(f'任務成功完成！')