from attractor import Attractor, ODE
import colour_scheme
import random

# TODO - an after image effect using previous generated points that fade out
# based on how long theyve been around. would tie opacity to time step. but also
# seriously increase the amount of memory needed to run?

class Model:

    def __init__(self, config):
        self.config = config
        self.attractor_width = config.ATTRACTOR_WIDTH
        self.number_of_attractors = config.NUMBER_OF_ATTRACTORS
        self.coordinate_history_limit = config.COORDINATE_HISTORY_LIMIT
        self.attractors = []
        self.colour_sets = []
        r = random.random
        d = config.DISTANCE 
        for x in range(self.number_of_attractors):
            x, y, z = r()*d, r()*d, r()*d
            attractor = Attractor(x, 
                                  y, 
                                  z, \
                                  config.ODE_PARAMETERS, \
                                  config.TIME_STEP, \
                                  config.ODE, \
                                  self.coordinate_history_limit)
            self.attractors.append(attractor)
            colours = colour_scheme.generate_colour_set(config.COLOUR_SCHEME)
            self.colour_sets.append(colours)

    #@classmethod
    def load_config(self, config):
        # does this require also updating config set inside self.attractors?
        print("todo")

    def get_config(self):
        return self.config

    def get_number_of_attractors(self):
        return self.number_of_attractors

    def get_attractor(self, i):
        return self.attractors[i]

    def get_attractor_coords(self, i):
        return self.attractors[i].get_current_coord_dict()
    
    def get_all_attractors_coords(self):
        coords = []
        for attractor in self.attractors:
            coords.append(attractor.get_current_coord_dict())
        return coords

    def generate_random_coordainte(self):
        print("TODO")

    def generate_next_coordinates(self):
        next_coords = []
        for attractor in self.attractors:
            attractor.generate_next_coordinate()
            next_coords.append(attractor.get_current_coord_dict())
        return next_coords


        # return array of new coord dicts

    def get_colour_set(self, index):
        colour_set = self.colour_sets[index]
        return (colour_set["red"], 
                colour_set["green"], 
                colour_set["blue"], 
                255)

    def get_colour_dict(self, index):
        colour_set = self.colour_sets[index]
        return  { "red": colour_set["red"], \
                  "green": colour_set["green"], \
                  "blue": colour_set["blue"] }

    def get_width(self):
        return self.attractor_width

if __name__ == "__main__":
    class Test_Conf:
        TIME_STEP = 0.01 #0.009
        ODE = ODE.lorenz
        BETA = 8/3 #8/3
        RHO = 28 #28
        SIGMA = 10 #10
        ODE_PARAMETERS = { "beta": BETA, "rho": RHO, "sigma": SIGMA }
        SCALE = 10
        ANGLE = 0 #-100
        ATTRACTOR_LENGTH_LIMIT = 10000 # min 2 (needs prev value to calc)
        NUMBER_OF_ATTRACTORS = 3
        ATTRACTOR_WIDTH = 4
        COLOUR_SCHEME = colour_scheme.Static_White
        DISTANCE = 1
        COORDINATE_HISTORY_LIMIT = 3


    model = Model(Test_Conf)
    for index in range(Test_Conf.NUMBER_OF_ATTRACTORS):
        attractor = model.attractors[index]
        print("-----attractor" + str(index) + " config-----")
        print(attractor.get_config())
        print("colour_sets[0].red:" + str(model.colour_sets[index]["red"]))
        print("colour_sets[0].green:" + str(model.colour_sets[index]["green"]))
        print("colour_sets[0].blue:" + str(model.colour_sets[index]["blue"]))

