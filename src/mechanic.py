from src.Block import Block
from src.Color import Color
import random


def del_color(colors: list, del_color: tuple):
    for index, color in enumerate(colors):
        if color == del_color:
            del colors[index]


def build_blocks():
    colors = [Color.red, Color.green, Color.yell]
    red_count = 0
    yell_count = 0
    green_count = 0
    x_first, y_first = (80, 80)
    x, y = (x_first, y_first)
    x_ex, y_ex = (x_first, 20)
    diff = 5
    blocks = []
    w, h = (x_first, y_first)
    block_value = dict()
    example_blocks = []
    for _ in range(3):
        example_blocks.append((x_ex + w // 4, y_ex, w // 2, h // 2))
        x_ex += 2 * (w + diff)
    for i in range(5):
        for j in range(5):
            left_extreme_block = False
            right_extreme_block = False
            up_extreme_block = False
            down_extreme_block = False
            if i == 0:
                up_extreme_block = True
            if j == 0:
                left_extreme_block = True
            if i == 4:
                down_extreme_block = True
            if j == 4:
                right_extreme_block = True
            extreme_block = (up_extreme_block, left_extreme_block, down_extreme_block, right_extreme_block)
            if j == 0 or j == 2 or j == 4:
                rnd_color = random.choice(colors)
                if rnd_color == Color.yell:
                    yell_count += 1
                elif rnd_color == Color.red:
                    red_count += 1
                elif rnd_color == Color.green:
                    green_count += 1
                if yell_count == 5:
                    del_color(colors, Color.yell)
                if green_count == 5:
                    del_color(colors, Color.green)
                if red_count == 5:
                    del_color(colors, Color.red)
                blocks.append((rnd_color, (x, y, w, h)))
                block_value[(x, y, w, h)] = Block(x, y, w, h, rnd_color, extreme_block, free=False)
            elif i % 2 == 0:
                blocks.append((Color.gray, (x, y, w, h)))
                block_value[(x, y, w, h)] = Block(x, y, w, h, Color.gray, extreme_block, free=False)
            else:
                blocks.append((Color.black, (x, y, w, h)))
                block_value[(x, y, w, h)] = Block(x, y, w, h, Color.black, extreme_block, free=True)
            if i == 2 and j == 2:
                middle_coord = (x, y, w, h)
            x += (w + diff)
        y += (h + diff)
        x = x_first
    return block_value, middle_coord, example_blocks


def check_end_game(colors: tuple, blocks: dict, middle_coord: Block):
    left_block = blocks[blocks[middle_coord.left_coor()].left_coor()]
    right_block = blocks[blocks[middle_coord.right_coor()].right_coor()]
    three_block = [left_block, middle_coord, right_block]
    for index, block in enumerate(three_block):
        if block.color != colors[index]:
            return False
        if blocks[block.up_coor()].color != colors[index] or \
                blocks[blocks[block.up_coor()].up_coor()].color != colors[index]:
            return False
        if blocks[block.down_coor()].color != colors[index] or \
                blocks[blocks[block.down_coor()].down_coor()].color != colors[index]:
            return False
    return True