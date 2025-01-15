class ChessPiece:
    board_size = 9
    board_mask = 2270874908986167672966671
    def __init__(self, shapes):
        self.shapes = shapes
        self.extension_masks = ChessPiece.generate_all_extension_masks(self.shapes)

    @staticmethod
    def generate_base_mask(shape):
        base_mask = 0
        for x, y in shape:
            base_mask |= 1 << (x * ChessPiece.board_size + y)
        return base_mask

    @staticmethod
    def generate_all_extension_masks(shapes):
        """
        生成所有可能的扩展掩码，表示棋子在棋盘上的不同位置和方向。

        Returns:
            list[int]: 所有有效的扩展掩码列表。
        """
        extension_masks = []
        for shape in shapes:
            max_x = max(point[0] for point in shape)
            max_y = max(point[1] for point in shape)
            base_mask = 0
            for x, y in shape:
                base_mask |= 1 << (x * ChessPiece.board_size + y)
            for i in range(ChessPiece.board_size - max_x):
                for j in range(ChessPiece.board_size - max_y):
                    # 检查形状是否在棋盘边界内
                    mask = base_mask << (i * ChessPiece.board_size + j)
                    if mask & ChessPiece.board_mask == 0:
                        extension_masks.append(mask)
        return extension_masks

    @staticmethod
    def get_shape_from_mask(mask):
        """
        从扩展掩码中获取棋子的形状。
        :param mask:
        :return:
        """
        shape = []
        for i in range(ChessPiece.board_size):
            for j in range(ChessPiece.board_size):
                if mask & (1 << (i * ChessPiece.board_size + j)):
                    shape.append((i, j))
        return shape