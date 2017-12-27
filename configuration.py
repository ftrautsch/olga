class Configuration(object):
    def __init__(self):
        self.baseline_time = 60
        self.cell_types = ["all"]
        self.treatments = ["all"]
        self.input = None
        self.output = None

    def isValid(self):
        if self.baseline_time != "" and self.cell_types != "" and self.treatments != "" and self.input != None \
                and self.output != None:
            return True
        return False

    def set_cell_types(self, cell_types):
        self.cell_types = cell_types.split(",")

    def set_treatments(self, treatments):
        self.treatments = treatments.split(",")

    def get_cell_types(self):
        return ','.join(self.cell_types)

    def get_treatments(self):
        return ','.join(self.treatments)

    def __str__(self):
        return "Baseline Time: %s; Cell-Types: %s; Treatments: %s; Input: %s" % (self.baseline_time, self.cell_types,
                                                                                 self.treatments, self.input)

class Measurement(object):

    # Initialization
    def __init__(self, name, cell_type, treatment):
        self.name = name
        self.cell_type = cell_type
        self.treatment = treatment

        self.lm1 = []
        self.lm2 = []

    # Add a value to a specific time for a lm to the measurements. Store it as tuple in a list
    def add_value(self, time, value, lm_number):
        if lm_number == 1:
            self.lm1.append((time, value))
        else:
            self.lm2.append((time, value))

    # Calculates the ratio. Uses the baseline_time to generate a normalization value
    def calculate_ratio(self, baseline_time):
        results = []

        # Get the normalization value: It is the arithmetic mean of all measurements to time t, where t<baseline_time
        normalization_value = self.get_normalization_value(baseline_time)

        # Calculate all ratios
        for i in range(0, len(self.lm1)):
            if self.lm1[i][1] is not None and self.lm2[i][1] is not None:
                results.append((self.lm1[i][0], (self.lm1[i][1] / self.lm2[i][1]) / normalization_value))
            else:
                results.append((self.lm1[i][0], None))
        return results

    def get_normalization_value(self, baseline_time):
        sum = 0
        cnt = 0
        # Calculate arithmetic mean over all measurements to time t, where t<baseline_time
        for i in range(0, len(self.lm1)):
            if self.lm1[i][0] < baseline_time and self.lm1[i][1] is not None and self.lm2[i][1]:
                cnt += 1
                sum += float(self.lm1[i][1] / self.lm2[i][1])

        return float(sum/cnt)

    def __str__(self):
        return "%s: LM1: %s\n LM2: %s" % (self.name, self.lm1, self.lm2)

