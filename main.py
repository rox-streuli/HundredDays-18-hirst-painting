# use following code only once to generate the rgb-colour-list and then
# coment out
# import colorgram
#
# colours = colorgram.extract('hirst_dot_paint.jpg', 30)
# rgb_colour_list = []
# for item in colours:
#     rgb_colour_list.append((item.rgb.r, item.rgb.g, item.rgb.b))
# print(rgb_colour_list)
import turtle
from turtle import Turtle, Screen
from random import choice

colour_list = [(17, 22, 51), (156, 72, 49), (199, 149, 115), (45, 26, 15),
               (56, 17, 28), (235, 228, 94), (133, 164, 199), (135, 25, 38),
               (145, 71, 88), (73, 88, 127), (188, 143, 157), (189, 86, 120),
               (24, 43, 25), (140, 27, 17), (73, 107, 73), (145, 175, 157),
               (97, 110, 183), (34, 46, 127), (191, 97, 79), (225, 172, 185),
               (191, 128, 52), (171, 185, 224), (231, 173, 164), (47, 83, 42),
               (167, 207, 198), (165, 204, 211)]

dot = Turtle()
turtle.colormode(255)

dot.shape('circle')

screen = Screen()
screen.exitonclick()
