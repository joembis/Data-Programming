import random
import matplotlib.pyplot as plt

num_samples = 50000
radius = 3
pi_count = 0

insidex, insidey, outsidex, outsidey = [], [], [], []

for i in range(num_samples):
	x = random.random()*radius
	y = random.random()*radius
	if x**2+ y **2<=radius**2:
		pi_count +=1
		insidex.append(x)
		insidey.append(y)
	else:
		outsidex.append(x)
		outsidey.append(y)

pi = 1/(num_samples/pi_count)*4
print("pi : ", pi)

plt.figure(figsize=(9,9))

circx = [(i/100) for i in range(0, 100*radius+1)]
circy = [(radius**2-x**2)**0.5 for x in circx]
plt.plot(circx, circy, c="black", linewidth=0.7)

graph = plt.scatter(insidex, insidey, c="blue", s=1)
graph = plt.scatter(outsidex, outsidey, c="red", s=1)

plt.axis([0, radius, 0, radius])

plt.show()