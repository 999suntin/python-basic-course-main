# 模組 (Module) 與 import
""" import myModule
myModule.sayHello()
print(myModule.teacher) """

# 只係import一小部份
#from myModule import sayHello,teacher
from myModule import *
sayHello()
print(teacher)

# 內建模組 Build-in module
# 例如 Math Datetime OS
import os
print(os.getcwd())
#os.mkdir('my-project')

import random
print(random.random())