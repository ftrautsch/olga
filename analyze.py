import csv


class PlateAnalysis(object):
    def __init__(self, file, output_file_path, measurements):
        # Open output file
        with open(file, 'r') as text_file:
            file_lines = text_file.readlines()

        relevant_block = False
        lm2_start = False

        # Initialize measurements
        self.measurements = measurements

        self.output_file_path = output_file_path

        for line in file_lines:
            line = line.lstrip()

            # If we find "Temperature" in the line, the relevant block is starting
            if line.strip('\t').startswith("Temperature"):
                relevant_block = True
                continue

            # If we have a empty line, we know that the second lm is coming
            if relevant_block and not line:
                lm2_start = True
                continue

            # If we find ~End, we know that the last values were parsed
            if line.strip('\t').startswith("~End"):
                relevant_block = False
                continue

            # Add values to the specific lms
            if relevant_block and not lm2_start:
                filtered_measurements = self._filter_measurements(line)
                self._add_values_to_measurements(filtered_measurements, 1)

            if relevant_block and lm2_start:
                filtered_measurements = self._filter_measurements(line)
                self._add_values_to_measurements(filtered_measurements, 2)

    def _add_values_to_measurements(self, filtered_measurements, lm_number):
        j = 0
        k = 0
        for i in range(1, len(filtered_measurements)-1, 2):
            self.measurements[j][k].add_value(filtered_measurements[i], filtered_measurements[i + 1], lm_number)
            k += 1

            if k == 12:
                k = 0
                j += 1

    def _filter_measurements(self, line):
        return [(float(measurement.replace(",", ".")) if measurement.strip() else None) for measurement in line.split('\t')]

    def print_plate(self):
        for i in range(0, 12):
            for j in range(0, 8):
                print(self.measurements[j][i])

    def create_output(self, baseline_time, cell_types, treatments):
        print("Generating output for baseline_time %d, cell_types %s, and treatments: %s" %
              (baseline_time, cell_types, treatments))
        outputs = []
        for i in range(0, 12):
            for j in range(0, 8):
                # Filter measurements
                if (self.measurements[j][i].cell_type in cell_types or "all" in cell_types)\
                        and (self.measurements[j][i].treatment in treatments or "all" in treatments):
                    outputs.append(self.measurements[j][i])

        # Sort by cell_type and treatment
        sorted_output = sorted(outputs, key = lambda x: (x.cell_type, x.treatment, int(x.name[1:])))

        header = []
        all_results = []
        for output in sorted_output:
            print("Using measurement %s..." % output.name)
            header.extend([output.name+"T", output.name+"("+output.cell_type+", "+output.treatment+")"])
            all_results.append(output.calculate_ratio(baseline_time))

        zipped_results = zip(*all_results)
        # Output
        with open(self.output_file_path, "w") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
            for zipped_result in zipped_results:
                row = []
                for measuremnt in zipped_result:
                    row.extend(measuremnt)
                csv_writer.writerow(row)
        print("Generated output in %s" % self.output_file_path)
