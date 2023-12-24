# 1 - 批次縮小圖片 (Pillow Package)
# 2 - 加批次命名 功能合并 --> 一個程式 兩個功能
# 溫習functions module import

import myTools

srcPath = 'C:\\Users\\user\\Desktop\\image\\'
destPath = 'C:\\Users\\user\\Desktop\\output\\'

renamePath = 'C:\\Users\\user\\Desktop\\rename\\'

#問用家想做甚麼
mode = input("你想 (1 = 批次命名, 2 = 批次縮小圖片, 其他輸入 = 離開)")

if(mode=='1'):
    myTools.batchRename(renamePath)
elif(mode=='2'):
    myTools.resizeImage(srcPath,destPath)
else:
    print('88')
