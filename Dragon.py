from Bad_Guy import Bad_Guy

class Dragon(Bad_Guy):
	def __init__(self):
		super(Dragon,self).__init__('Dragon',10000000,10000000)
		self.type = "FIRE"
	def breath_fire(self):
		print "THE DRAGON RAINS HELLFIRE!!!"
	def __repr__(self):
		return "%s" % (self.name)

