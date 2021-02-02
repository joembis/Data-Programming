from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
	"""A class to generate a random walk"""

	def __init__(self, num_points=5000):
		"""initialising the random walk attributes"""
		self.num_points=num_points

		"""all walks start at 0, 0"""
		self.point_num = [i for i in range(num_points)]
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		"""calculates the steps in the random walk"""

		"""refactored lines that calculate steps"""
		def get_step():
			direction = choice([-1, 1])
			distance = choice([0, 1, 2, 3, 4])
			return direction*distance

		"""keep stepping until the walk length is reached"""
		while len(self.x_values)< self.num_points:
			"""calculate new x, y positions"""
			x_change = self.x_values[-1] + get_step()
			y_change = self.y_values[-1] + get_step()

			"""update list of x, y, positions"""
			self.x_values.append(x_change)
			self.y_values.append(y_change)

rand_w = RandomWalk(num_points=1000)
rand_w.fill_walk()

plt.scatter(rand_w.x_values, rand_w.y_values, c=rand_w.point_num, edgecolor="none", cmap=plt.cm.Blues, s=10)
"""emphasise the start and end points"""
plt.scatter(0, 0, c="green", s=100)
plt.scatter(rand_w.x_values[-1], rand_w.y_values[-1], c="red", s=100)
plt.plot(rand_w.x_values, rand_w.y_values, color = "black", linewidth = 0.5)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()