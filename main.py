import pygame
from pygame.locals import *

def main():
    size = w,h =750,1200    #设置开始页面的大小
    white = (255,255,255)   #红色
    black = (10,10,10)      #黑色
    n = 0
    #初始化 画面
    pygame.init()
    screen = pygame.display.set_mode((size))#设定窗口大小
    pygame.display.set_caption('飞机大战')#设定标题


    #填充背景
    background = pygame.Surface(screen.get_size())#以screen的大小创建一个矩形
    background = background.convert()#格式化为 统一的像素标准
    background.fill(white)#填充黄色颜色

    # 加入文字
    font = pygame.font.Font(None,88)
    text = font.render('Start the game ',1,black)
    textpos = text.get_rect()
    textpos.center = (750 / 2, 1200 / 2)  # 居中的坐标

    text_end = font.render('Exit the game',1,black)
    textpos_text_end = text_end.get_rect()
    textpos_text_end.center = (750 / 2, 1200 / 2+90)  # 居中的坐标+90像素


    background.blit(text,textpos)
    background.blit(text_end,textpos_text_end)
    #可以用循环打印开始的标签  继续优化
    # for i in range(6,8):
    #     n = n+1
    #     bq = {1:'Start the game',2:'Exit the game'}
    #     i = i*100
    #     font = pygame.font.Font(None, 88)
    #     text = font.render(f'{bq[n]} ', 1, black)
    #     textpos = text.get_rect()
    #     textpos.center = (750 / 2, i)  # 居中的坐标
    #     background.blit(text, textpos)


    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        screen.blit(background,(0,0))#绑定背景的位子
        pygame.display.flip()
if __name__ == '__main__':
    main()
