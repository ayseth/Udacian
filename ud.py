class udacian:
	def __init__(self,name,city,enrollment,nanodegree,status):
	 self.name= name
	 self.city= city
	 self.enrollment=enrollment
	 self.nanodegree = nanodegree
	 self.status = status

	def myfunc(self):
	 print("name " + self.name +"\n" + "city " + self.city +"\n" + "enrollment "+ self.enrollment +"\n"+ "nanodegree " + self.nanodegree+"\n"+ "status " + self.status )



# p1 = udacian("Abeer","Jeddah","Afternoon","FSND","student")
p1 = udacian("Abeer","Jeddah","Nanodegree","FSND","abc")
p1.myfunc()



