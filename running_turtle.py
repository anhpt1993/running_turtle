import turtle as t
import random
import datetime

# Vẽ trường đua "rùa"

def draw_racecourse(t):
    screen = t.Screen()
    screen.setup(height=500, width=600)
    t.hideturtle()
    t.penup()
    t.speed(100)
    t.goto(-250, 200)
    x = -250
    for i in range(21):
        t.write(i)
        t.right(90)
        for j in range(9):
            t.pendown()
            t.forward(20)
            t.penup()
            t.forward(10)
        t.forward(5)
        t.left(90)
        t.write(i)
        t.goto(x + (i + 1) * 25, 200)

# Tạo mấy con ngựa còm

def create_horse(t):
    all_turtles = []
    y_position = [190, 130, 70, 10, -50]
    colors = ["red", "orange", "yellow", "green", "blue"]
    for i in range(5):
        turtles = t.Turtle(shape="turtle")
        turtles.penup()
        
        # Di chuyển rùa về vị trí xuất phát
        turtles.goto(-250, y_position[i])
        
        # Tô màu cho mấy con ngựa còm
        turtles.color(colors[i])
        
        # Lưu vào danh sách ngựa còm
        all_turtles.append(turtles)

    return all_turtles

def choice_race():
    while True:
        try:
            option = int(input("""
            Do you want to start the race?
            1. Yes
            2. No
            
            Your choice (1 or 2): """))

            if 1 <= option <= 2:
                return option
                break
            else:
                print("\nInvalid value. Try again!!!\n")
        except ValueError:
            print("\nInvalid value. Try again!!!\n")

if __name__ == '__main__':
    draw_racecourse(t)
    all_turtles = create_horse(t)

    # chạy đi, chờ chi
    option = choice_race()
    if option == 1:
        start_time = datetime.datetime.now()
        run = True
        while run:
            for turtle in all_turtles:
                turtle.forward(random.randint(1, 10))

                #kiểm tra điều kiện về đích
                if turtle.xcor() > 250:
                    finish_time = datetime.datetime.now()
                    print("{} is winning!!!".format(turtle.color()[0].upper()))
                    print("It took {:.2f} seconds to reach the finish line.".format((finish_time - start_time).total_seconds()))
                    run = False

        t.exitonclick()
    else:
        exit()