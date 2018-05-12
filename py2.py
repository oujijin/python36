
class student(object):
	"""docstring for student"""
	def __init__(self, name,age,course):
		self.name = name
		self.age=age
		self.course=course
	def get_name(self):
		return self.name
	def get_age(self):
		return self.age
	def get_course(self):
		li=self.course
		for i in li:
			if not isinstance(i,int): 
				return "555"
			else:
				return "成绩最好的是:%d"%max(li)

def main():
	s1=student("zhangxiaomao",20,[24,52,98])
	s2=student('liqiang',23,[82,60,99])
	assert s1.get_name()=="zhangxiaomao" 
	print(s1.get_name())
	print(s1.get_course())
	print(s1.get_age())
	print(s2.get_course())
	print("哈哈哈")


if __name__ == '__main__':
	main()

	

