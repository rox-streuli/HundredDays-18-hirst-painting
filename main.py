import colorgram

colours = colorgram.extract('hirst_dot_paint.jpg', 30)
rgb_colour_list = []
for item in colours:
    rgb_colour_list.append((item.rgb.r, item.rgb.g, item.rgb.b))
print(rgb_colour_list)