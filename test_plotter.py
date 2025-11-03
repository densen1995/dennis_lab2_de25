
from circle import Circle
from rectangle import Rectangle
from shape2D_plotter import Shape2DPlotter

# Create shapes
c1 = Circle(x=0, y=0, radius=2)
r1 = Rectangle(x=4, y=2, width=3, height=2)

# Create plotter
plotter = Shape2DPlotter()
plotter.add_circle(c1, color='blue')
plotter.add_rectangle(r1, color='green')

# Show both shapes in one plot
plotter.show()