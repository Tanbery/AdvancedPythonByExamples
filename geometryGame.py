from random import randint

class GeoPoint:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def show(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"
	def fall_in_rect(self,rect):
		return ((rect.lwCorner.x <= self.x <= rect.upCorner.x) and (rect.lwCorner.y <= self.y <= rect.upCorner.y))

class GeoRect:
	def __init__(self,p1,p2):
		self.lwCorner  = p1
		self.upCorner  = p2

	def show(self):
		return "{" + self.lwCorner.show() + "} {" + self.upCorner.show() + "}"

p1 = GeoPoint(randint( 0, 50)	, randint( 0, 50))
p2 = GeoPoint(randint(50,100)	, randint(50,100))

print("Point1: " + p1.show())
print("Point2: " + p2.show())

p0 = GeoPoint(int(input("Guess X:")),int(input("Guess Y:")))
print("Point0: " + p0.show())

geo_rect= GeoRect(p1,p2)
print(geo_rect.show())

print(p0.fall_in_rect(geo_rect))