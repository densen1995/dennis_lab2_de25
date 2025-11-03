"""plotting various 2D shapes (circle and rectangle in one plot)"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle as CirclePatch, Rectangle as RectPatch

class Shape2DPlotter:
    """
    A helper class to plot multiple 2D shapes (Circles, Rectangles) on the same axes.

    Usage:
        plotter = Shape2DPlotter()
        plotter.add_circle(circle_obj, color='red')
        plotter.add_rectangle(rect_obj, color='blue')
        plotter.show()
    """

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal', adjustable='box')
        self.ax.grid(True)
        self._shapes = []  # store shape info for later

    def add_circle(self, circle, color='blue'):
        """Add a circle shape to the plot."""
        patch = CirclePatch(
            (circle.x, circle.y),
            circle.radius,
            edgecolor=color,
            fill=False,
            linewidth=2,
            label=f"Circle(r={circle.radius})"
        )
        self.ax.add_patch(patch)
        self._shapes.append(("circle", circle))

    def add_rectangle(self, rect, color='green'):
        """Add a rectangle shape to the plot."""
        lower_left_x = rect.x - rect.width / 2
        lower_left_y = rect.y - rect.height / 2
        patch = RectPatch(
            (lower_left_x, lower_left_y),
            rect.width,
            rect.height,
            edgecolor=color,
            fill=False,
            linewidth=2,
            label=f"Rectangle({rect.width}x{rect.height})"
        )
        self.ax.add_patch(patch)
        self._shapes.append(("rectangle", rect))

    def _auto_adjust_limits(self):
        """Automatically adjust axes limits to fit all shapes."""
        if not self._shapes:
            return
        all_x = []
        all_y = []
        for shape_type, shape in self._shapes:
            if shape_type == "circle":
                all_x.extend([shape.x - shape.radius, shape.x + shape.radius])
                all_y.extend([shape.y - shape.radius, shape.y + shape.radius])
            elif shape_type == "rectangle":
                all_x.extend([shape.x - shape.width / 2, shape.x + shape.width / 2])
                all_y.extend([shape.y - shape.height / 2, shape.y + shape.height / 2])

        # Add padding for visibility
        padding = 1
        self.ax.set_xlim(min(all_x) - padding, max(all_x) + padding)
        self.ax.set_ylim(min(all_y) - padding, max(all_y) + padding)

    def show(self):
        """Display all added shapes."""
        if not self._shapes:
            print(" No shapes added to plot.")
            return
        self._auto_adjust_limits()
        self.ax.legend()
        self.ax.set_title("All Shapes in One Plot")
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")
        plt.show()