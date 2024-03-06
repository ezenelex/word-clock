import math
import colorsys
import os
import time
import random
from datetime import datetime
from rpi_ws281x import *

LED_COUNT = 130
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 40
LED_INVERT = False
LED_CHANNEL = 0

os.environ['TZ'] = 'Canada/Pacific'
time.tzset()
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

words = []
year = month = day = yday = hour24 = hour12 = minute = minute5 = second = decimalTime = 0
bdayHue = 0
bdayRBG = [0, 0, 0]
bday = [11, 9]
stripState = ['off'] * 28

nightRGB = [255, 51, 0]

# lati = math.radians(49)
# longi = math.radians(123)

sunrise = 0.2
sunset = 0.7

#twinklePoints = [6,6,6,6,6,6]
#previousTwinklePoints = [6,6,6,6,6,6]
#print(previousTwinklePoints)
#twinkleRange = list(range(0,6)) + list(range(11,15)) + list(range(22,32)) + list(range(37,41)) + list(range(45,48)) $#print(twinkleRange)
#twinkled = 0

class word:
	def __init__(self, start, end, direction):
		self.start = start
		self.end = end
		self.length = end - start + 1
		self.direction = direction
		self.state = 'off'
		self.bdayHue2 = 0
		words.append(self)

	def turnOn(self):
		global decimalTime
		global sunrise
		global sunset
		global nightRGB

		if self.state == 'off':
			for i in range(self.length):
				strip.setPixelColor(i + self.start, Color(255, 0, 0))
				if i > 0:
					if decimalTime < sunrise or decimalTime > sunset:
						strip.setPixelColor(i + self.start - 1, Color(nightRGB[0],nightRGB[1],nightRGB[2]))
					else:
						strip.setPixelColor(i + self.start - 1, Color(255,255,255))
				time.sleep(0.1)
				strip.show()
			if decimalTime < sunrise or decimalTime > sunset:
				strip.setPixelColor(self.start + self.length - 1, Color(nightRGB[0],nightRGB[1],nightRGB[2]))
			else:
				strip.setPixelColor(self.start + self.length - 1, Color(255,255,255))
			strip.show()
		self.state = 'on'
	def turnOff(self):
		if self.state == 'on':
			for i in range(self.length):
				strip.setPixelColor(i + self.start, Color(255, 0, 0))
				if i > 0:
					strip.setPixelColor(i + self.start - 1, Color(0,0,0))
				time.sleep(0.1)
				strip.show()
			strip.setPixelColor(self.start + self.length - 1, Color(0,0,0))
			strip.show()
		self.state = 'off'

	def Birthday(self, index):
		global bdayHue
		global bdayRGB
		if bdayHue >= 1:
			bdayHue = 0
		else:
			bdayHue += 0.001
		self.bdayHue2 = bdayHue * index
		bdayRGB = colorsys.hsv_to_rgb(self.bdayHue2, 1, 1)
		for i in range(self.length):
			strip.setPixelColor(i + self.start, (Color(round(bdayRGB[0]*255), round(bdayRGB[1]*255), round(bdayRGB[2]*255))))
		strip.show()

	def setColor(self,r,g,b):
		if self.state == 'on':
			for i in range(self.length):
				strip.setPixelColor(self.start + i, Color(r,g,b))
			strip.show()

# def isDay ():
# 	global lati
# 	global longi
# 	global yday
# 	global year
# 	global sunrise
# 	global sunset
# 	n = ( year - 2000 ) * 365 + yday + hour/24 + minute/60/10 + second/60/10/10 + (year-2000)/4 + 0.0008 -12/24
# 	jDate = n + 2451545 - 0.0008
# 	jStar = n + math.degrees(longi)/360
# 	M = (357.5291 + 0.98560028*jStar)%360
# 	C = 1.9148*math.sin(math.radians(M)) + 0.02*math.sin(math.radians(2*M)) + 0.0003*math.sin(math.radians(3*M))
# 	eclipticLongi = (M + C + 180 + 102.9372)%360
# 	declination = math.asin(math.sin(math.radians(eclipticLongi))*math.sin(math.radians(23.44)))
# 	hourAngle = math.degrees(math.acos(-math.tan(lati) * math.tan(declination)))
# 	jTransit = 2451545 + jStar + 0.0053*math.sin(math.radians(M)) - 0.0069*math.sin(math.radians(2*eclipticLongi))
# 	sunrise = jTransit - hourAngle/360
# 	sunset = jTransit + hourAngle/360
# 	print("sunrise: " + str(sunrise) + ' sunset: ' + str(sunset))

# def twinkle():
# 	global twinklePoints
# 	global previousTwinklePoints
# 	global twinkleRange
# 	global twinkled
# 	if second != time.localtime().tm_sec and twinkled == 0:
# 		twinkled = 1
# 		for i in range(len(twinklePoints)):
# 			twinklePoints[i] = twinkleRange[random.randint(0, len(twinkleRange)-1)]
# 		print(twinklePoints, previousTwinklePoints)
# 		for i in range(len(twinklePoints)):
# 			strip.setPixelColor(previousTwinklePoints[i], Color(0,0,0))
# 			strip.setPixelColor(twinklePoints[i], Color(255,255,255))
# 		for i in range(len(twinklePoints)):
# 			previousTwinklePoints[i] = twinklePoints[i]
# 	else:
# 		twinkled = 0
# 	strip.show()

# create words
Oclock = word(0,5, "L")
One = word(65,67, "R")
Two = word(39,41, "R")
Three = word(73,77, "R")
Four = word(55,58, "L")
Five2 = word(26,29, "L")
Six = word(13,15, "R")
Seven = word(30, 34, "L")
Eight = word(46, 50, "R")
Nine = word(35,38, "L")
Ten2 = word(23,25, "R")
Eleven = word(59, 64, "L")
Twelve = word(7,12, "L")
#
Five = word(91,94, "R")
Ten = word(123,125, "R")
Quarter = word(110,116, "L")
Twenty = word(104,109, "L")
Half = word(126,129, "R")
#
Minutes = word(96,102, "R")
To = word(79,80, "L")
Past = word(81,84, "L")
#
Happy = word(85,89, "L")
Birth = word(68,72, "R")
Day = word(52,54, "L")
To2 = word(42,43,"R")
You = word(16,19, "R")
#
It = word(117,118, "R")
Is = word(120,121, "R")

# turn on 'it' 'is' and 'oclock'
It.turnOn()
It.state = 'on'
Is.turnOn()
Is.state = 'on'
Oclock.turnOn()
Oclock.state = 'on'

bdayVisible = False

while True:
	localTime = time.localtime()
	year = localTime.tm_year
	month = localTime.tm_mon
	day = localTime.tm_mday
	hour24 = localTime.tm_hour
	minute = localTime.tm_min
	second = localTime.tm_sec
	yday = localTime.tm_yday

	minute5 = round(minute/5)
	if minute5 == 12:
		minute5 = 0

	if hour24 > 12:
		hour12 = hour24 - 12
	elif hour24 == 0:
		hour12 = 12
	else:
		hour12 = hour24

	# isDay()

	decimalTime = ( ( (hour24 * 100 / 24) + (minute / 60) ) / 100 )
	if (decimalTime < sunrise or decimalTime > sunset):
		if(bdayVisible == False):
			for i in range(len(words)):
				words[i].setColor(nightRGB[0], nightRGB[1], nightRGB[2])
	else:
		if(bdayVisible == False):
			for i in range(len(words)):
				words[i].setColor(255, 255, 255)

	if (month == bday[0] and day == bday[1] and second < 30):
		if bdayVisible == False:
			for i in range(len(words)):
				if i < 21 or i > 25:
					# save strips state before showing HBD
					stripState[i] = words[i].state
					words[i].turnOff()
			Happy.turnOn()
			Birth.turnOn()
			Day.turnOn()
			To2.turnOn()
			You.turnOn()
		bdayVisible = True
		Happy.Birthday(1)
		Birth.Birthday(2)
		Day.Birthday(3)
		To2.Birthday(4)
		You.Birthday(5)
		#twinkle()
	elif (month == bday[0] and day == bday[1] and second >= 30):
		if bdayVisible == True:
			# for i in range(len(twinklePoints)):
			# 	strip.setPixelColor(twinklePoints[i], Color(0,0,0))
			Happy.turnOff()
			Birth.turnOff()
			Day.turnOff()
			To2.turnOff()
			You.turnOff()
			for i in range(len(words)):
				if i < 21 or i > 25:
					if stripState[len(words)-i-1] == 'on':
						words[len(words)-1-i].turnOn()
			stripState = ['off'] * 28
		bdayVisible = False

	if (month == bday[0] and day == bday[1] and second > 30) or (month != bday[0] or day != bday[1]):
		# On the hour
		if minute5 == 0:
			Five.turnOff()
			Minutes.turnOff()
		# 5 past / 5 to
		elif (minute5 == 1 or minute5 == 11):
			Ten.turnOff()
			Five.turnOn()
			Minutes.turnOn()
		# 10 past / 10 to
		elif (minute5 == 2 or minute5 == 10):
			Five.turnOff()
			Quarter.turnOff()
			Ten.turnOn()
			Minutes.turnOn()
		# Quarter past / Quarter to
		elif (minute5 == 3 or minute5 == 9):
			Ten.turnOff()
			Twenty.turnOff()
			Minutes.turnOff()
			Quarter.turnOn()
		# Twenty past / twenty to
		elif (minute5 == 4 or minute5 == 8):
			Quarter.turnOff()
			Five.turnOff()
			Twenty.turnOn()
			Minutes.turnOn()
		# Twenty five past / twenty five to
		elif minute5 == 5 or minute5 == 7:
			Half.turnOff()
			Twenty.turnOn()
			Five.turnOn()
			Minutes.turnOn()
		# Half past
		elif minute5 == 6:
			Twenty.turnOff()
			Five.turnOff()
			Minutes.turnOff()
			Half.turnOn()


	if (month == bday[0] and day == bday[1] and second >= 30) or (month != bday[0] or day != bday[1]):
		# Past / to [hour]
		if minute5 == 0:
			Past.turnOff()
			To.turnOff()
			if minute > 30:
				if hour12 == 12:
					Eleven.turnOff()
					Twelve.turnOff()					
					One.turnOn()
				elif hour12 == 1:
					Twelve.turnOff()
					One.turnOff()
					Two.turnOn()
				else:
					words[hour12 - 1].turnOff()
					words[hour12].turnOff()
					words[hour12 + 1].turnOn()
			else:
				if hour12 == 12:
					One.turnOff()
					Eleven.turnOff()
					Twelve.turnOn()
				elif hour12 == 1:
					Twelve.turnOff()
					Two.turnOff()
					One.turnOn()
				else:
					words[hour12 + 1].turnOff()
					words[hour12 - 1].turnOff()
					words[hour12].turnOn()
		elif minute5 < 7 and minute5 != 0:
			Past.turnOn()
			To.turnOff()
			if hour12 == 12:
				One.turnOff()
				Eleven.turnOff()
				Twelve.turnOn()
			elif hour12 == 1:
				Twelve.turnOff()
				Two.turnOff()
				One.turnOn()
			else:
				words[hour12 + 1].turnOff()
				words[hour12 - 1].turnOff()
				words[hour12].turnOn()
		elif minute5 >= 7:
			To.turnOn()
			Past.turnOff()
			if hour12 == 12:
				Eleven.turnOff()
				Twelve.turnOff()
				One.turnOn()
			elif hour12 == 1:
				Twelve.turnOff()
				One.turnOff()
				Two.turnOn()
			else:
				words[hour12 - 1].turnOff()
				words[hour12].turnOff()
				words[hour12 + 1].turnOn()

	# print("Year: " + str(year) + " Month: " + str(month) + " Day: " + str(day) + " Hour: " + str(hour24) + " M$
	if bdayVisible == False:
		time.sleep(0.5)


