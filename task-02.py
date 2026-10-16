import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    t.hideturtle()
    window.mainloop()


# Введення рівня рекурсії користувачем
try:
    order = int(input("Введіть рівень рекурсії (0–5): "))

    if 0 <= order <= 5:
        draw_koch_snowflake(order)
    else:
        print("Помилка: введіть число від 0 до 5.")

except ValueError:
    print("Помилка: потрібно ввести ціле число.")
