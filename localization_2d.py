
# This problem is from an excercise in udacity's https://classroom.udacity.com/courses/cs373 course
# Understand how localization works
import numpy as np

class Localization:
    def __init__(self):
        # 2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
        # This defines the "world", can be of any size.
        self.maps = np.array([
                       ['R','G','G','R','R'],
                       ['R','R','G','R','R'],
                       ['R','R','G','G','R'],
                       ['R','R','R','R','R']
                      ])
        # list of measurements taken by the robot, each entry either 'R' or 'G'
        # This is what the robot sees / senses
        self.measurements = np.array(['G','G','G','G','G'])
        
        # list of actions taken by the robot, each entry of the form [dy,dx],
        # where dx refers to the change in the x-direction (positive meaning
        # movement to the right) and dy refers to the change in the y-direction
        #  [0,0] - stay
        #  [0,1] - right
        #  [0,-1] - left
        #  [1,0] - down
        #  [-1,0] - up
	self.motions = np.array([[0,0],[0,1],[1,0],[1,0],[0,1]])
        
        # for this example, each movement must have a sensed value
        assert np.shape(self.measurements)[0] == np.shape(self.motions)[0], "measurements not equal to motions"
        
        # float between 0 and 1, giving the probability that any given
        # measurement is correct; the probability that the measurement is
        # incorrect is 1-sensor_right
        self.sensor_right = 0.7
        
        # float between 0 and 1, giving the probability that any given movement
        # command takes place; the probability that the movement command fails
        # (and the robot remains still) is 1-p_move; the robot will NOT overshoot
        # its destination in this exercise
        self.p_move = 0.8
	
        # initializes p to a uniform distribution over a grid of the same dimensions as colors
	pinit = 1.0 / float(len(self.maps)) / float(len(self.maps[0]))
	self.p = np.full(self.maps.shape, pinit, np.float64)

    def move(self, motion):
        "Move to the required motion with a certainty of p_move by motion"
        if np.array_equal(motion,[0,0]):
            pass
        elif np.array_equal(motion,[0,1]):
            self.p = self.p*(1-self.p_move) + np.roll(self.p, 1, axis = 1)*self.p_move
        elif np.array_equal(motion,[0,-1]):
            self.p = self.p*(1-self.p_move) + np.roll(self.p, -1, axis = 1)*self.p_move
        elif np.array_equal(motion,[1,0]):
            self.p = self.p*(1-self.p_move) + np.roll(self.p, 1, axis = 0)*self.p_move
        elif np.array_equal(motion,[-1,0]):
            self.p = self.p*(1-self.p_move) + np.roll(self.p, -1, axis = 0)*self.p_move
        else:
            assert False, "Unsupported motion defined : %s"%motion
        #normalize
        #normalize to 1
        self.p = self.p / np.sum(self.p)

    def measure(self, measurement):
        "Sense after motion, where you are, what you see. Sensor error probability is given in sensor_right"
        multiplier = np.full(self.maps.shape, 1, np.float64)
        # Multiply with sensor_right probability wherever the objects observation is present
        multiplier[self.maps == measurement] *= self.sensor_right
        # Multiply with 1 - sensor_right probability wherever the objects observation is present
        multiplier[self.maps != measurement] *= (1 - self.sensor_right)
        #actually do the multiplication
        self.p = np.multiply(self.p, multiplier)
        #normalize to 1
        self.p = self.p / np.sum(self.p)

    def localize(self):
        "Move / sense / move / sense loop"
        for motion,measurement in zip(self.motions, self.measurements):
            self.move(motion)
            self.measure(measurement)

if __name__ == "__main__":
    obj = Localization()
    obj.localize()
    print "Localized the object it is present in the location from below matrix with highest probability : \n%s"%obj.p
