import random
# TODO: Import the virus clase

class Person(object):


    # Person objects will populate the simulation.
    # _____Attributes______:
    # - _id: Int. 1. A unique ID assigned to each person.
    #
    # - is_vaccinated: 1. Bool.  Determines whether the person object is vaccinated against
    #     the disease in the simulation.
    #
    # - is_alive: Bool. All person objects begin alive (value set to true). 1. Changed
    #     to false if person object dies from an infection.
    #
    # - infection:  None or Virus object.  1. Set to None for people that are not infected.
    #     2. If a person is infected, will instead be set to the virus object the person
    #     is infected with.
    #
    #
    # _____Methods_____:
    # __init__(self, _id, is_vaccinated, infection=None):
    #     - 1. self.alive should be automatically set to true during instantiation.
    #     - 2. all other attributes for self should be set to their corresponding parameter
    #         passed during instantiation.
    #     - 3. a) If person is chosen to be infected for first round of simulation, then
    #         the object should create a Virus object and set it as the value for
    #         self.infection.
    #          3. b) Otherwise, self.infection should be set to None.
    #
    # did_survive_infection(self):
    #     - 1. Only called if infection attribute is not None.
    #     - 2. Takes no inputs.
    #     - 3. Generates a random number between 0 and 1.
    #     - 4. Compares random number to mortality_rate attribute stored in person's infection
    #         attribute.
    #         - 5. If random number is smaller, person has died from disease.
    #             is_alive is changed to false.
    #         - 6. If random number is larger, person has survived disease.
    #         7. Person's is_vaccinated attribute is changed to True, and set self.infection to None.
    #

    def __init__(self, _id, is_vaccinated, infection = None):
        # TODO:  Finish this method.  Follow the instructions in the class documentation
        # to set the corret values for the following attributes.
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infection = infection


    def did_survive_infection(self, mortality_rate):
        # TODO:  Finish this method. Follow the instructions in the class documentation
        # for resolve_infection.  If person dies, set is_alive to False and return False.
        # If person lives, set is_vaccinated = True, infection = None, return True.
        mortality_chance = random.randint(0, 1)
        while self.infection != None:
            if mortality_chance < mortality_rate:  ### Possibly come back to this if you have an error, MAYBE change the order
                self.is_alive = False
                print("Oh no! They Died!")

            elif mortality_chance > mortality_rate:
                self.is_alive = True
                self.is_vaccinated = True
                self.infection = None
                print("Woohoo, they beat the virus!")
        pass
