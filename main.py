import pandas as pd
import matplotlib.pyplot as plt
import csv
import DIAEngineAnalysis  # Feature 1
import DIAFuelMixture     # Feature 2
import DistAvg            # Feature 2
import Pothole            # Feature 3
import SpeedBreaker       # Feature 3
import DIASpeedVoilation  # Feature 4
import Traffic            # Feature 5

df= pd.read_csv("Dataset-1.csv") # DataSet Selection
#with open('Dataset-1.csv') as df:
#    csv_reader = csv.reader(df, delimiter=',')
EngineLoad = df['Engine Load(%)'].replace(to_replace="-", value="0")
EngineRPM = df['Engine RPM(rpm)'].replace(to_replace="-", value="0")
VehicleSpeed = df['Speed (GPS)(km/h)'].replace(to_replace="-", value="0")
TripTime = df['Trip Time(Since journey start)(s)'].replace(to_replace="-", value="0")
CoolantTemperatureC = df.iloc[0:,30].replace(to_replace="-", value="0")
#print(CoolantTemperatureC)

O2_Volts = df['O2 Volts Bank 1 sensor 1(V)']
Distance = df['Trip Distance(km)']
Fuel = df['Fuel Remaining (Calculated from vehicle profile)(%)']
Kmpl = df['Kilometers Per Litre(Long Term Average)(kpl)']

Latitude = df[' Latitude']
Longitude = df[' Longitude']
ThresholdSpeed = 25          # Threshold value for Speed violation

# Feature 1
print("\nFeature 1 :")       # There is some problem
#DIAEngineAnalysis.Coolant(CoolantTemperatureC,EngineLoad,TripTime)
#DIAEngineAnalysis.LoadAnalysis(EngineLoad,EngineRPM,VehicleSpeed, TripTime)

# Feature 2
print("\nFeature 2 :")
Lean, Rich, Nrml = DIAFuelMixture.FuelMixture(O2_Volts)
print("No. of instances of Lean mixture: ", Lean.size/2 )
print("No. of instances of Rich mixture: ", Rich.size/2 )
print("No. of instances of Nrml mixture: ", Nrml.size/2 )
#.plot(Lean)
#DistAvg.AverageDistance(Distance, Fuel, Kmpl)

# Feature 3
print("\nFeature 3 : Shown in plots")
Pothole.pothole()
SpeedBreaker.pothole()

# Feature 4
print("\nFeature 4 :")
SpeedVoilation = DIASpeedVoilation.SpeedVoilation(VehicleSpeed, Latitude,Longitude,ThresholdSpeed)
print("\nSpeed violations have occurred at the following locations: ")
print(SpeedVoilation)

# Feature 5
print("\nFeature 5 :")
Traffic.traffic(VehicleSpeed,Latitude,Longitude)
