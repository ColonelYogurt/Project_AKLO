import pandas as pd
import random as rand

def random(rows):
    return [rand.randint(0,1) for i in range(rows)]

csv_input = pd.read_csv('Standard-10-20-Cap25.ced')

rows = len(csv_input)

csv_input['Sensor'] = random(rows)

csv_input['Transducer'] = random(rows)

csv_input.to_csv('Assets/Test.csv', index=False)