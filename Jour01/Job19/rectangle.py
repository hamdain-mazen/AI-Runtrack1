def draw_rectangle(width, height):
    filled_bar = "|"+'-'*width+"|"
    empty_bar = "|"+' '*width+"|"
    print(filled_bar)
    for i in range(height-2):

        print(empty_bar)
    print(filled_bar)
draw_rectangle(10,3)
