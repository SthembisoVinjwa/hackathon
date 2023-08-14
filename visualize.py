import pandas as pd
import plotly.express as px


claims_path = 'claims_data.csv'

try:
    with open(claims_path, "r") as file:
        lines = file.readlines()
        for line in lines[1:2]:
            vehicle_id = line.split(',')[0]

            vehicle_id = '90293012'

            vehicle_data_path = 'telematics_data/final/' + vehicle_id + '.csv'
            try:
                vehicle_data = pd.read_csv(vehicle_data_path)
                fig = px.scatter(vehicle_data, x='coordinate_latitude', y='coordinate_latitude', title='Timestamp vs. Speed Vehicle ID ' + vehicle_id)
                fig.show()
            except FileNotFoundError:
                print("Vehicle data file not found")

except FileNotFoundError:
    print("File not found")        