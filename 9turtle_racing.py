import turtle
import random


WIDTH, HEIGHT = 500, 500
COLORS = ["red", "black", "green", "blue", "brown", "pink", "grey", "orange", "violet"]

def get_no_of_racers():
    while True:
        try:
            racers = int(input("Enter a number of racers(2 - 5): "))
            if 2<= racers <=5:
                return racers
            else:
                print("Racers must be between (2 - 5).")
                continue
        except:
            print("Invalid Input! Please enter a valid number.")

def create_turtle(colors):
    turtles = []
    spacing = WIDTH // (len(colors)+1)
    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacing, (-HEIGHT // 2) + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = create_turtle(colors)
    while True:
        for racer in turtles:
            distance = random.randint(1,20)
            racer.forward(distance)

            x,y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                winner_index = turtles.index(racer)
                return colors[winner_index], winner_index

def setup():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race!")

racers = get_no_of_racers()
setup()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner, winner_index = race(colors)
print(f"The winner is number {winner_index + 1} and colour is {winner}.")
turtle.done()







