import turtle


class Drawing:
    def __init__(self):
        self.colors = [
            (147, 184, 196),  # 深蓝色
            (122, 202, 122),  # 深绿色
            (217, 211, 187),  # 深米色
            (184, 162, 184),  # 深紫色
            (217, 217, 190),  # 深黄色
            (217, 155, 164),  # 深粉色
            (179, 179, 179),  # 深灰色
            (217, 183, 0),  # 深橙色
            (179, 153, 119),  # 深棕色
            (149, 202, 202),  # 深青色
            (217, 173, 173),  # 深红色
            (129, 213, 129),  # 深绿色
            (217, 213, 174),  # 深黄色
        ]
        self.back = '#eeeeee'
        self.size = 20
        self.size3xstep = 3 * 0.866 * self.size
        self.size3ystep = 3 * self.size
        self.screensize_x = 27 * self.size
        self.screensize_y = 30 * self.size

        turtle.register_shape("hexagon", (
            (-2 * self.size, 0),
            (-self.size * 1.5, self.size * 0.866),
            (-self.size * 0.5, self.size * 0.866),
            (0, self.size * 2 * 0.866),
            (self.size, self.size * 2 * 0.866),
            (self.size * 1.5, self.size * 0.866),
            (self.size * 1, 0),
            (self.size * 1.5, -self.size * 0.866),
            (self.size * 1, -self.size * 2 * 0.866),
            (0, -self.size * 2 * 0.866),
            (-self.size * 0.5, -self.size * 0.866),
            (-self.size * 1.5, -self.size * 0.866),
            (-2 * self.size, 0)
        ))
        turtle.setup(self.screensize_x, self.screensize_y)
        turtle.speed(10)
        turtle.tracer(0, 0)
        turtle.shape("hexagon")

    def draw_three_hexagons_only_edge(self, x, y, color=-1, show_number=False):
        # _x = x * self.size3x - self.screensize / 2 + self.size3x / 2
        # _y = (y * 2 + x % 2) * self.size3y - self.screensize / 2 + self.size3y / 2
        # x
        # 列中心位置 ：(-4 + x) * x步进
        # y
        # 行中心位置 ：((-4 + x) * 1 / 2 + y) * y步进
        _x = (-4 + x) * self.size3xstep
        _y = ((-4 + x) * 0.5 + y - 4) * self.size3ystep
        turtle.penup()
        turtle.goto(_x, _y)
        turtle.begin_fill()
        if color < 0 or color >= len(self.colors):
            turtle.color(self.back)
        else:
            color_tuple = self.colors[color]
            color_string = "#{:02x}{:02x}{:02x}".format(*color_tuple)
            turtle.color(color_string)
        turtle.stamp()
        turtle.end_fill()

        if show_number:
            turtle.penup()
            turtle.goto(_x - 12, _y - self.size3ystep + 12)
            turtle.pendown()
            if 0 <= y <= 8 and 0 <= x <= 8:
                turtle.write(f"{x},{y}", font=("Arial", 12, "normal"))

    def draw_board(self):
        board = [
            [1, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 1, 1, 1]
        ]
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == 0:
                    self.draw_three_hexagons_only_edge(i, j)
        turtle.hideturtle()
        turtle.update()

    def change_cell_color(self, x, y, new_color):
        self.draw_three_hexagons_only_edge(x, y, color=new_color)
