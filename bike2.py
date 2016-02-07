class Bike(object):
  def __init__(self, price, max_speed):
    print 'New Bike'
    self.price = price
    self.max_speed = max_speed
    self.miles = 0
  
  def displayInfo(self):
    print "Bike Price:", self.price
    print "Bike Max Speed:", self.max_speed
    if self.miles > 0:
        print "Miles riden:", self.miles
    else:
        print "What, no miles riden?"
        # return True

  def reverse(self):
    if self.miles >= 5:
      self.miles = self.miles - 5
      print "Reversing. Mile ridden now: ",self.miles
    
  def ride(self):
    self.miles = self.miles + 10
    print "Riding, nice job. Miles riden now: ",self.miles
    




bike1 = Bike(300, 20)
count = 0
while count < 4:
  bike1.ride()
  count += 1
bike1.reverse()
bike1.displayInfo()


bike2 = Bike(400, 30)
count2 = 0
count2a = 0
while count2 < 3:
  bike2.ride()
  count2 += 1
while count2a < 3:
  bike2.reverse()
  count2a += 1
bike2.displayInfo()

bike3 = Bike(200, 15)
count3 = 0
while count3 < 4:
  bike2.reverse()
  count3 += 1
bike3.displayInfo()
  

