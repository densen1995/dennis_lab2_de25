"""plotting various 2D shapes (circle and rectangle in one plot)"""


import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from circle import Circle as CircleShape
from rectangle import Rectangle as RectangleShape

""" Create shape objects"""
circle1 = CircleShape(x=0, y=0, radius=2)
circle2=  CircleShape(x=1, y=2, radius= 3)
rectangle1 = RectangleShape(x=4, y=2, width=3, height=2)

""" Create a figure and axis"""
fig, ax = plt.subplots()

""" Plot the circle """
circle_patch1 = Circle((circle1.x, circle1.y),circle1.radius,
                      edgecolor='blue', fill=False, linewidth=2, label='Circle1')
ax.add_patch(circle_patch1)
circle_patch2 = Circle((circle2.x, circle2.y),circle2.radius,
                      edgecolor='green', fill=False, linewidth=2, label='Circle2')
ax.add_patch(circle_patch2)

"""Plot the rectangle"""
lower_left_x = rectangle1.x - rectangle1.width / 2
lower_left_y = rectangle1.y - rectangle1.height / 2
rect_patch = Rectangle((lower_left_x, lower_left_y), rectangle1.width, rectangle1.height,
                       edgecolor='red', fill=False, linewidth=2, label='Rectangle')
ax.add_patch(rect_patch)

""" Set up the plot display """
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-5, 10)
ax.set_ylim(-5, 8)
ax.set_title("Circle and Rectangle on Same Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()
ax.grid()

"""Show plot"""
plt.show()