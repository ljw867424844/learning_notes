class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
            
    def set_gender(self,s):
        self.__gender = s

    def get_gender(self):
        return self.__gender
    
# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
