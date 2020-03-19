# Ashwini Pandey
# EMP_ID - 142871
import matplotlib.pyplot as plt

# Rash Driving detection

def detect_rash_driving(df, pos_d, pos_e, Threshold):
    lat = df.loc[0:, ' Latitude'];
    long = df.loc[0:, ' Longitude'];
    plt.figure();
    plt.plot(lat, long);
    plt.title('Rash driving detection');
    plt.xlabel('Latitude');
    plt.ylabel('Longitude');
    for i in range(0, len(lat)):
        if (float(pos_d[i]) > Threshold):
            if (float(pos_e[i]) > Threshold/2):
                plt.scatter(lat[i], long[i], color=['green']);
    plt.legend(['Route', 'Rash driving spots']);
    plt.show();
    print("The green spots show that the rash driving was done there.")
