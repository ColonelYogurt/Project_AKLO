import pandas as pd
import random as rand

def random():
    return rand.int(0,1)

csv_input = pd.read_csv(column)

csv_input['new_column'] = csv_input[random()]

csv_input['new_column_2'] = csv_input[random()]

csv_input.to_csv(output_csv_file, index=False)