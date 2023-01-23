import turtle
import math

BOUNDING_HEIGHT = 800
BOUNDING_WIDTH = 1200
HOUSE_HEIGHT = 500
HOUSE_WIDTH = 700
TREE_HEIGHT = 250
TREE_WIDTH = 30


def draw_bounding_box(t):
    t.penup()
    t.left(180)
    t.forward(550)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.pendown()
    t.forward(BOUNDING_WIDTH)
    t.left(90)
    t.forward(BOUNDING_HEIGHT)
    t.left(90)
    t.forward(BOUNDING_WIDTH)
    t.left(90)
    t.forward(BOUNDING_HEIGHT)

def draw_house(t):
    t.penup()
    t.left(90)
    t.forward((BOUNDING_WIDTH - HOUSE_WIDTH)/2)
    t.pendown()
    t.left(90)
    t.forward(HOUSE_HEIGHT)
    t.right(90)
    t.forward(HOUSE_WIDTH)
    t.right(90)
    t.forward(HOUSE_HEIGHT)


def draw_branches(t, tree_width):
    """Draw branches for the tree

    Params:
        t: the Tutle object.
        tree_width: width of the tree
    """

    t.fillcolor('green')
    t.begin_fill()
    t.forward(tree_width)
    t.left(135)
    t.forward(tree_width * 2 / math.sqrt(2))
    t.left(90)
    t.forward(tree_width * 2 / math.sqrt(2))
    t.left(135)
    t.forward(tree_width)
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(tree_width)
    t.right(90)
    t.pendown()

def draw_tree(t):
    """Draw a tree 

    Params:
        t: the Tutle object.
    """

    # tree trunk
    t.fillcolor('brown')
    t.begin_fill()
    t.left(90)
    t.forward(TREE_HEIGHT)
    t.right(90)
    t.forward(TREE_WIDTH)
    t.right(90)
    t.forward(TREE_HEIGHT)
    t.right(90)
    t.forward(TREE_WIDTH / 2 )
    t.end_fill()

    # move to branch location
    t.penup()
    t.right(90)
    t.forward(TREE_HEIGHT)
    t.right(90)
    t.pendown()

    # draw branches
    draw_branches(t, TREE_WIDTH * 4) 
    draw_branches(t, TREE_WIDTH * 3) 
    draw_branches(t, TREE_WIDTH * 2) 


def draw_all_trees(t):
    """Draw two trees, one on each side of the house

    Params:
        t: the Tutle object.
    """

    # move to right tree
    gap = (BOUNDING_WIDTH - HOUSE_WIDTH)/4 - TREE_WIDTH/2
    t.left(90)
    t.forward(gap)

    # draw right tree 
    draw_tree(t)

    # move to left tree 
    gap = (BOUNDING_WIDTH - HOUSE_WIDTH)/4 + HOUSE_WIDTH
    t.penup()
    t.goto(400.00, -400.00)
    t.pendown()
    t.right(180)
    t.forward(gap)
    t.right(180)

    # draw left tree 
    draw_tree(t)


def main():
    t = turtle.Turtle()
    draw_bounding_box(t)
    draw_house(t)
    draw_all_trees(t)
    turtle.done()

if __name__ == "__main__":
    main()
