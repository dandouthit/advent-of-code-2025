position = 50 # initial position on the dial is 50
password_counter_inc = 0
iteration = 0 
with open("/home/dandouthit/advent-of-code-2025/input/day1.txt", 'r') as file:
    for line in file:
        direction = line[0]

        if direction == "L":
            movement = (int(line[1:]) % 100) * -1
        elif direction == "R":
            movement = (int(line[1:]) % 100)

        new_position = position + movement
        if new_position < 0:
            position = 100 + new_position
        elif new_position > 100:
            position -= 100
        else:
            position = new_position

        if position == 0:
            password_counter_inc += 1

print("Ending password is: " + str(password_counter_inc))