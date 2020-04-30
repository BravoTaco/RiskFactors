class StateInformation:
    heart_disease_death_rate = -1
    motor_vehicle_death_rate = -1
    teen_birth_rate = -1
    adult_smoking = -1
    adult_obesity = -1
    state_name = ""

    information = []

    def __init__(self, state_name, heart_disease_death_rate, motor_vehicle_death_rate, teen_birth_rate, adult_smoking,
                 adult_obesity):
        self.state_name = state_name
        self.heart_disease_death_rate = float(heart_disease_death_rate)
        self.motor_vehicle_death_rate = float(motor_vehicle_death_rate)
        self.teen_birth_rate = float(teen_birth_rate)
        self.adult_smoking = float(adult_smoking)
        self.adult_obesity = float(adult_obesity)
        self.information = [heart_disease_death_rate, motor_vehicle_death_rate, teen_birth_rate, adult_smoking,
                            adult_obesity]

    def __repr__(self):
        return "State: %s, Heart Disease Death Rate: %s, Motor Vehicle Death Rate: %s, Teen Birth Rate: %s, " \
               "Adult Smoking: %s, Adult Obesity: %s" % (self.state_name, self.heart_disease_death_rate,
                                                         self.motor_vehicle_death_rate, self.teen_birth_rate,
                                                         self.adult_smoking, self.adult_obesity)