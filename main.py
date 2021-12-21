import pygame

from src.Color import Color
from src.Frame import Frame
from src.mechanic import build_blocks, check_end_game


def main():
    pygame.init()
    win = pygame.display.set_mode((600, 563))
    pygame.display.set_caption("2D GAME")
    all_blocks, middle_coord, example_blocks = build_blocks()
    example_colors = (Color.red, Color.green, Color.yell)
    x, y, w, h = middle_coord
    moving_frame = Frame(x, y, w, h, (0, 0, 255), 8)
    bg = pygame.image.load('image/bg.jpg')
    fn = pygame.image.load('image/finish.png')
    st = pygame.image.load('image/start.jpg')
    play = True
    was_enter = False
    draw_circle = False
    start_play = False
    enter_coord = 0
    FPS = 60
    clock = pygame.time.Clock()
    win.blit(st, (0, 0))
    pygame.display.update()
    while not start_play:
        for event in pygame.event.get(): #события из очереди
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                start_play = True
            elif event.type == pygame.QUIT:
                start_play = True
                play = False
    while play:
        if check_end_game(example_colors, all_blocks, all_blocks[middle_coord]) and not was_enter:
            win.blit(fn, (0, 0))
            pygame.display.update()
            pygame.time.delay(2000)
            play = False
            continue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if was_enter:
                    all_blocks[enter_coord].free = True
                    all_blocks[moving_frame.get_coord()].free = False
                    draw_circle = False
                    was_enter = False
                else:
                    if not all_blocks[moving_frame.get_coord()].is_unbreakable() and \
                            not all_blocks[moving_frame.get_coord()].free:
                        was_enter = True
                        draw_circle = True
                        enter_coord = moving_frame.get_coord()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                if was_enter:
                    if draw_circle and not all_blocks[moving_frame.get_coord()].left_extreme_block and \
                            not all_blocks[moving_frame.left_coor()].is_unbreakable() and \
                            (all_blocks[moving_frame.left_coor()].free or enter_coord == moving_frame.left_coor()):
                        all_blocks[moving_frame.left_coor()].color = all_blocks[moving_frame.get_coord()].color
                        all_blocks[moving_frame.get_coord()].color = Color.black
                        moving_frame.step_left()

                else:
                    if not all_blocks[moving_frame.get_coord()].left_extreme_block and \
                            not all_blocks[moving_frame.left_coor()].is_unbreakable():
                        moving_frame.step_left()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if was_enter:
                    if draw_circle and not all_blocks[moving_frame.get_coord()].right_extreme_block and \
                            not all_blocks[moving_frame.right_coor()].is_unbreakable() and \
                            (all_blocks[moving_frame.right_coor()].free or enter_coord == moving_frame.right_coor()):
                        all_blocks[moving_frame.right_coor()].color = all_blocks[moving_frame.get_coord()].color
                        all_blocks[moving_frame.get_coord()].color = Color.black
                        moving_frame.step_right()
                else:
                    if not all_blocks[moving_frame.get_coord()].right_extreme_block and \
                            not all_blocks[moving_frame.right_coor()].is_unbreakable():
                        moving_frame.step_right()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if was_enter:
                    if draw_circle and not all_blocks[moving_frame.get_coord()].down_extreme_block and \
                            not all_blocks[moving_frame.down_coor()].is_unbreakable() and \
                            (all_blocks[moving_frame.down_coor()].free or enter_coord == moving_frame.down_coor()):
                        all_blocks[moving_frame.down_coor()].color = all_blocks[moving_frame.get_coord()].color
                        all_blocks[moving_frame.get_coord()].color = Color.black
                        moving_frame.step_down()
                else:
                    if not all_blocks[moving_frame.get_coord()].down_extreme_block and \
                            not all_blocks[moving_frame.down_coor()].is_unbreakable():
                        moving_frame.step_down()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                if was_enter:
                    if draw_circle and not all_blocks[moving_frame.get_coord()].up_extreme_block and \
                            not all_blocks[moving_frame.up_coor()].is_unbreakable() and \
                            (all_blocks[moving_frame.up_coor()].free or enter_coord == moving_frame.up_coor()):
                        all_blocks[moving_frame.up_coor()].color = all_blocks[moving_frame.get_coord()].color
                        all_blocks[moving_frame.get_coord()].color = Color.black
                        moving_frame.step_up()
                else:
                    if not all_blocks[moving_frame.get_coord()].up_extreme_block and \
                            not all_blocks[moving_frame.up_coor()].is_unbreakable():
                        moving_frame.step_up()

        win.blit(bg, (0, 0))
        for id, ex_block in enumerate(example_blocks):
            x, y, w, h = ex_block
            pygame.draw.rect(win, example_colors[id], (x, y, w, h))
        for block in all_blocks.values():
            block.draw(win)
        moving_frame.draw(win)
        if draw_circle:
            moving_frame.draw_circle(win)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
