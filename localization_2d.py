# The function localize takes the following arguments:
#
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up


def move(p, motion, p_move):
    dy = motion[0]
    dx = motion[1]
    if dx == dy == 0:
        return p
    q = []

    for i in range(len(p)):
        row = []
        for j in range(len(p[i])):
            update_probability = 0.0

            # The below if-else can be consolidated into a single line, 
            # because we move in only one direction.
            # Either dx or dy will always be 0, so the index will be same
            # i.e. we will either move on the same column, or on the same row.
            # if dy:
            #     update_probability = p[(i - dy)%len(p)][j] * p_move
            # elif dx:
            #     update_probability = p[i][(j - dx)%len(p[i])] * p_move
            # NOTE : the modulous for the second index is always p[i], 
            # because the row and columns may have different lengths. This easy to miss
            
            column_index = (i - dy)%len(p)
            row_index = (j - dx)%len(p[i])
            update_probability = p[column_index][row_index] * p_move
            update_probability += p[i][j] * (1 - p_move)
            row.append(update_probability)
        q.append(row)
    return q

def sense(p, measurement, colors, sensor_right):
    q = []
    total_prob =  0.0
    for i in range(len(p)):
        row = []
        for j in range(len(p[i])):
            if measurement == colors[i][j]:
                p[i][j] = p[i][j] * sensor_right
            else:
                p[i][j] = p[i][j] * (1 - sensor_right)
            row.append(p[i][j])
            total_prob += p[i][j]
        q.append(row)

    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] = q[i][j] / total_prob
    return q

def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    
    # >>> Insert your code here <<<
    num_steps = len(motions)
    for i in range(num_steps):
        p = move(p, motions[i], p_move)
        p = sense(p, measurements[i], colors, sensor_right)
    
    return p

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print ('[' + ',\n '.join(rows) + ']')
