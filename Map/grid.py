class Grid:
    def __init__(self, width=0, height=0, fill=0, json_rebuild={}):
        if json_rebuild:
            self.width = json_rebuild['width']
            self.height = json_rebuild['height']

            self.the_grid = json_rebuild['the_grid']

        else:
            self.width = width
            self.height = height

            self.the_grid = []
            for i in range(0, width * height):
                self.the_grid.append(fill)

        self.calc = CoordinatesCalc(width, height)

    def set_cell(self, x, y, value):
        self.the_grid[self.calc.get_grid_position(x, y)] = value

    def get_cell(self, x, y):
        return self.the_grid[self.calc.get_grid_position(x, y)]

    def fill(self, value):
        for i in range(0, self.width * self.height):
            self.the_grid[i] = value

    def __str__(self):
        results = ""
        for y in range(0, self.height):
            for x in range(0, self.width):
                results += str(self.the_grid[self.calc.get_grid_position(x, y)]) + " "
            results += "\n"
        return results

    def __dict__(self):
        return {"width": self.width, "height": self.height, "the_grid": self.the_grid}

    def clone(self):
        results = Grid(self.width, self.height)
        results.the_grid = self.the_grid[:]
        return results

    def resize(self, new_width, new_height, grid_x=0, grid_y=0, fill=0):
        """Fill only used if additional cells created, no warning given for lost cells.
            Will wrap around with negative grid coordinates because of how python handles negative
            number coordinates in a list"""

        temp_grid = []
        new_calc = CoordinatesCalc(new_width, new_height)

        for i in range(0, new_width * new_height):
            temp_grid.append(fill)

        for y in range(0, self.height):
            for x in range(0, self.width):
                if new_width > x + grid_x >= 0 and new_height > y + grid_y >= 0:
                    temp_grid[new_calc.get_grid_position(x + grid_x, y + grid_y)] = \
                        self.the_grid[self.calc.get_grid_position(x, y)]

        self.calc = new_calc
        self.the_grid = temp_grid
        self.width = new_width
        self.height = new_height


class CoordinatesCalc:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_grid_position(self, x, y):
        return self.width * y + x

    def get_x(self, coordinates):
        return coordinates % self.width

    def get_y(self, coordinates):
        return abs(coordinates / self.width)