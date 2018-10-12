class Logger(object):
    #
    # Utility class responsible for logging all interactions of note during the
    # simulation.
    # _____Attributes______
    # - file_name: the name of the file that the logger will be writing to.
    #
    #
    # _____Methods_____
    # __init__(self, file_name):
    # write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
    #     basic_repro_num):
    #     - 1. Writes the first line of a logfile, which will contain metadata on the
    #         parameters for the simulation.
    #
    #
    # log_interaction(self, person1, person2, did_infect=None, person2_vacc=None, person2_sick=None):
    #     - 1. Expects person1 and person2 as person objects.
    #     - 2. Expects did_infect, person2_vacc, and person2_sick as Booleans, if passed.
    #     - 3. Between the values passed with did_infect, person2_vacc, and person2_sick, this method
    #         should be able to determine exactly what happened in the interaction and create a String
    #         saying so.
    #     - 4. The format of the log should be "{person1.ID} infects {person2.ID}", or, for other edge
    #         cases, "{person1.ID} didn't infect {person2.ID} because {'vaccinated' or 'already sick'}"
    #     - 5. Appends the interaction to logfile.
    #
    #
    # log_infection_survival(self, person, did_die_from_infection):
    #     - 1. Expects person as Person object.
    #     - 2. Expects bool for did_die_from_infection, with True denoting they died from
    #         their infection and False denoting they survived and became immune.
    #     - 3. The format of the log should be "{person.ID} died from infection" or
    #         "{person.ID} survived infection."
    #     - 4. Appends the results of the infection to the logfile.
    #
    #
    # log_time_step(self, time_step_number):
    #     - 1. Expects time_step_number as an Int.
    #     - 2. This method should write a log telling us when one time step ends, and
    #         the next time step begins.  B) The format of this log should be:
    #             "Time step {time_step_number} ended, beginning {time_step_number + 1}..."
    #
    #
    #     - STRETCH CHALLENGE DETAILS:
    #         - 1. If you choose to extend this method, the format of the summary statistics logged
    #             are up to you.  At minimum, it should contain:
    #                 - 2. The number of people that were infected during this specific time step.
    #                 - 3. The number of people that died on this specific time step.
    #                 - 4. The total number of people infected in the population, including the newly
    #                     infected
    #                 - 5. The total number of dead, including those that died during this time step.


    def __init__(self, file_name):
        # TODO:  Finish this initialization method.  The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name
        #Come back to self.saved = 0

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        # TODO: Finish this method.  The simulation class should use this method
        # immediately upon creation, to log the specific parameters of the simulation
        # as the first line of the file.  This line of metadata should be tab-delimited
        # (each item separated by a '\t' character).
        # NOTE: Since this is the first method called, it will create the text file
        # that we will store all logs in.  Be sure to use 'w' mode when you open the file.
        # For all other methods, we'll want to use the 'a' mode to append our new log to the end,
        # since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        file = open(self.file_name, "w")
        file.write("Population size is: " + population_size)
        file.write("Vaccine percentage is: " + vacc_percentage + "%")
        file.write("The name of the virus is: " + virus_name)
        file.write("The mortality rate is: " + mortality_rate)
        file.write("The basic reproduction number is " + basic_repro_num)

        #file.write("Population size is: " population_size + "\t The Vaccine percentage is: " + vacc_percentage + "%" + "\t The name of the virus is: " + virus_name + "\t The mortality rate is: " + mortality_rate + "\t The basic reproduction number is: " + basic_repro_num)


    def log_interaction(self, person1, person2, did_infect = None,
                        person2_vacc = None, person2_sick = None):
        # TODO: Finish this method.  The Simulation object should use this method to
        # log every interaction a sick individual has during each time step.  This method
        # should accomplish this by using the information from person1 (the infected person),
        # person2 (the person randomly chosen for the interaction), and the optional
        # keyword arguments passed into the method.  See documentation for more info
        # on the format of the logs that this method should write.
        # NOTE:  You'll need to think
        # about how the booleans passed (or not passed) represent
        # all the possible edge cases!
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!

        file = open(self.file_name, "a")
        if(did_infect):
            file.write("Person: " + str(person1._id) + " infected Person: " + str(person2._id) + ". \t")
        elif(person2_vacc):
            file.write("Person: " + str(person1._id) + " couldn't infect: " + str(person2._id) + " because they already got vaccinated. \t")
        elif(person2_sick):
            file.write("Person: " + str(person1._id) + " can't infect person: " + str(person2._id) + " because person: " + str(person2._id) + " was already sick. \t")
        else:
            file.write("Person: " + str(person1._id) + " wasn't able to infect person: " + str(person2._id) + ". \t")


    def log_infection_survival(self, person, did_die_from_infection): #Maybe did_die_from_infection should be did_survive_infection ????
        # TODO: Finish this method.  The Simulation object should use this method to log
        # the results of every call of a Person object's .resolve_infection() method.
        # If the person survives, did_die_from_infection should be False.  Otherwise,
        # did_die_from_infection should be True.  See the documentation for more details
        # on the format of the log.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        file = open(self.file_name, "a")
        if did_die_from_infection == False:
            file.write("Sweet! person: " + person._id + " survived the infection! \t")
        else:
            file.write("Oh no! person: " + person._id + " did not survive the infection! :( \t")


    def log_time_step(self, time_step_number):
        # TODO: Finish this method.  This method should log when a time step ends, and a
        # new one begins.  See the documentation for more information on the format of the log.
        # NOTE: Stretch challenge opportunity! Modify this method so that at the end of each time
        # step, it also logs a summary of what happened in that time step, including the number of
        # people infected, the number of people dead, etc.  You may want to create a helper class
        # to compute these statistics for you, as a Logger's job is just to write logs!
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        file = open(self.file_name, "a")
        file.write("This is the beginning of time step: " + str(time_step_number))
