import turtle
command_key = None
while command_key != 'q':
    print('How many iterations ? (int)')
    iteration_number = int(input())
    print('How many pixels for a line ? (int)')
    line_size = int(input())

    for i in range(iteration_number):
        turtle.forward(line_size)
        turtle.left(360 / iteration_number)

    print('Next command ? (\'q\' for quit, any key for repeat)')
    command_key = input()
