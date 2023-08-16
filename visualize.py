import pandas as pd
import plotly.express as px


claims_path = 'claims_data.csv'

try:
    with open(claims_path, "r") as file:
        lines = file.readlines()
        vehicle_id = ['87055861', '150986252'] # Insert list Vehicle ID to generate charts for
        for id in vehicle_id: 
            vehicle_data_path = 'telematics_data/final/' + id + '.csv'
            
            df = pd.read_csv(vehicle_data_path)
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            
            desired_day = '2022-02-15' # Select any day you want within the dataset dates
            single_day_data = df[df['timestamp'].dt.date == pd.to_datetime(desired_day).date()]

            try:
                fig = px.line(single_day_data, x='timestamp', y='speed', 
                                title=f'Speed on {desired_day} for Vehicle {id}', 
                                text='heading', line_shape='linear', color='SP_NAME')
                fig.show()
            except FileNotFoundError:
                print("Vehicle data file not found")

except FileNotFoundError:
    print("File not found")        