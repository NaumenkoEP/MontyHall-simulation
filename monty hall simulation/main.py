import random
from bokeh.plotting import figure, show
def montyhall_game(number, chosen_door, swap_doors):
    wins = 0
    for _ in range(number):
        doors = [1, 2, 3]
        winning_door = random.randint(1,3)
        for door in doors:
            if door != winning_door and door != chosen_door:
                doors.remove(door)
                break
        if swap_doors == True:
            for door in doors: 
                if door != chosen_door:
                    new_choice = door
                    break 
            if new_choice == winning_door:
                wins += 1
        elif swap_doors == False:
            if chosen_door == winning_door:
                wins += 1
    prob = wins/number
    return prob

lines = []
y_sets = []
colors = ["red", "green", "blue", "brown", "black"]
trials_number = range(1, 400) # number of games played
trials = list(trials_number) # x - values
lines_number = 10
for _ in range(lines_number):
    swap_door_probs = [] # y - values
    for i in trials_number:
        swap_door_probs.append(montyhall_game(i, random.randint(1, 3), True))
    y_sets.append(swap_door_probs)
plot = figure(
    title = "Monty Hall Winning Probability, always swapping doors", 
    x_axis_label="Number of trials", 
    y_axis_label="Probability of winning", 
    width = 1400, height = 700, 
    background_fill_color="gray"
    )
plot.x_range.start = 1
plot.x_range.end = 400
plot.y_range.start = 0
plot.y_range.end = 1 
i = 0
for y_set in y_sets:
    if i == len(colors):
        i = 0
    line = plot.line(x = trials, y = y_set, line_width = 1, line_color = colors[i])
    lines.append(line)
    i += 1
show(plot)