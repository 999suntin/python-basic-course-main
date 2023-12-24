import os
from PIL import Image

def resizeImage(srcPath,destPath):

    dir = os.listdir(srcPath)

    print(f'資料夾內有{len(dir)}張圖片')

    newName = input('請輸入新檔案名 : ')
    ratioInput = input("請告訴我想縮小多少% (例 : 輸入50相當於結果圖片大小是原圖片的50%):")
    ratio = int(ratioInput)/100 #0.5

    for index,fileName in enumerate(dir,start = 1):
        
        print(f'正在處理第{index}/{len(dir)}張')
        
        #縮小圖片
        img = Image.open(srcPath+fileName)

        width, height = img.size # (1920,1080)

        newWidth = int(width * ratio)
        newHeight = int(height * ratio)
        
        newImg = img.resize((newWidth, newHeight))
        
        newImg.save(f'{destPath}{newName}{index}.jpg')

        print(f'原大小：闊{width}px x 高{height}px\n處理後闊{newWidth}px x 高{newHeight}px\n')


    print(f'所有圖片處理完成！\n成品可在{destPath}找到')

def batchRename(path):

    dir = os.listdir(path)

    print(f'資料夾內有{len(dir)}張圖片')

    newName = input('請輸入新檔案名 : ')

    for index,fileName in enumerate(dir,start = 1):
        print(f'正在處理第{index}/{len(dir)}張')
        os.rename(path+fileName,path+f'{newName}_{index}.jpg')

    print(f'任務成功完成！')