position = 50
password_counter_inc = 0

with open("input/day1.txt", "r") as file:
    for line in file:
        direction = line[0]
        movement = int(line[1:])
        clicks, rotation = divmod(movement, 100)
        password_counter_inc += clicks

        if direction == "R":
            if position + rotation >= 100:
                password_counter_inc += 1
            position = (position + rotation) % 100
        elif direction == "L":
            if position and position - rotation <= 0:
                password_counter_inc += 1
            position = (position - rotation) % 100

print(password_counter_inc)