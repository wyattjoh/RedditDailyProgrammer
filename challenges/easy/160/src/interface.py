

class Interface:

	def run(self):
		size = input()
		inputs = {}

		for i in range(0, int(size)):
			the_input = input()
			key, value = the_input.split('=')
			inputs[key] = value

		sides = {}
		angles = {}

		for key in inputs:
			if key.isupper():
				angles[key] = inputs[key]
			else:
				sides[key] = inputs[key]

		return sides, angles

if __name__ == '__main__':
	interface = Interface()
	interface.run()
