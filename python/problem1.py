position = 50 # initial position on the dial is 50
password_counter_inc = 0
with open("input/day1.txt", 'r') as file:
    for line in file:
        direction = line[0]

        if str(direction) == "L":
            movement = (int(line[1:]) % 100) * -1
        elif str(direction) == "R":
            movement = (int(line[1:]) % 100)

        new_position = position + movement
        if new_position < 0:
            position = 100 + new_position
        elif new_position > 99:
            position = new_position - 100
        else:
            position = new_position

        if position == 0:
            password_counter_inc += 1

print("Ending password is: " + str(password_counter_inc))