import turtle


def polygon(t, n, length):
	angle = 360.0 / n
	for i in range(n):
		fd(t, length)
		lt(t, angle)

bob = turtle.Turtle()
polygon(bob, 7, 70)