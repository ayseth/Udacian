class udacian:
	def __init__(self,name,city,enrollment,nanodegree,status):
	 self.name= name
	 self.city= city
	 self.enrollment=enrollment
	 self.nanodegree = nanodegree
	 self.status = status

	def myfunc(self):
		user="name = {} \n City= {} \n Enrollment = {} \n Nanodegree = {} \n Status = {}".format(self.name,self.city,self.enrollment,self.nanodegree,self.status)
		return user

	 # user = ("name " + self.name +"\n" + "city " + self.city +"\n" + "enrollment "+ self.enrollment +"\n"+ "nanodegree " + self.nanodegree+"\n"+ "status " + self.status )
	 # return user


# p1 = udacian("Abeer","Jeddah","Afternoon","FSND","student")
# p1 = udacian("Abeer","Jeddah","Nanodegree","FSND","abc")
# p1.myfunc()



