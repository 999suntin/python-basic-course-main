# Dictionary (Object)
student = {
    "name":'Daisy',
    "age":20,
    "passedExam":False
}
#Key-value pair
print(student)
print(f'student是{type(student)}, 長度{len(student)}')

# 讀取Dictionary值
print(student["name"])

#加新 / 更新 key-value pair
student["teacher"] = '梁浩賢'
student["age"] = 21
print(f'加左新key後 : {student}')

#刪除key-value pair
student.pop('teacher')
print(f'刪除左key後 : {student}')

#For Loop through Dictionary
for info in student:
    print(info, student[info])

#考考你 順便溫習下
pythonClass = [
    {"name":'Daisy',"age":20,"passedExam":False},
    {"name":'Peter',"age":19,"passedExam":True},
    {"name":'Patrick',"age":20,"passedExam":True},
    {"name":'Lulu',"age":22,"passedExam":True}
]

print(f'Name\tAge\t合格/肥佬') #Fail
for st in pythonClass:

    """ passed = '肥佬'
    if st["passedExam"]:
        passed = '合格' """
    
    passed = '合格'if st["passedExam"] else '肥佬'

    print(f'{st["name"]}\t{st["age"]}\t{passed}')