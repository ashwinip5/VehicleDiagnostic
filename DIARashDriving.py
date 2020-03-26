# Ashwini Pandey
# EMP_ID - 142871

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Dataset-1.csv')
def detect_rash_driving(lat, long, pos_d, pos_e, Threshold):
    x=[]
    y=[]
    z=[]

    for i in range(0, len(lat)):
        if (float(pos_d[i]) > Threshold) and (float(pos_e[i]) > Threshold / 2):
            x.append(lat[i])
            y.append(long[i])
            z.append(i)
            #plt.scatter(lat[i], long[i], color=['green']);
    d = {'Latitude': x, 'Longitude': y, 'Index': z}
    print(d)
    df = pd.DataFrame(data=d)#, columns=['Latitude', 'Longitude', 'Index'])
    return df;

Location = detect_rash_driving(df[' Latitude'], df[' Longitude'], df['Accelerator PedalPosition D(%)'].replace(to_replace='-',value=0), df['Accelerator PedalPosition E(%)'].replace(to_replace='-',value=0), 30)

plt.figure()
plt.plot(Location['Latitude'],Location['Longitude'],'r.',label='RashDriving_Locations')
plt.title("Rash Driving")
plt.ylabel('Longitude')
plt.xlabel('Latitude')
plt.legend(loc='lower right')
plt.show()
