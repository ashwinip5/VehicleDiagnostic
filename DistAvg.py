# logic : Total Fuel is taken at the starting then the mileage is taken till that point. Using the mileage on the remaining
# Fuel the expected Distanceance is calculated and plotted.


def AverageDistance(Distance, Fuel, Kmpl):

        ExpectedDistance = []
        TotalDistance = Distance.iloc[-1]
        TotalDistance = float(TotalDistance)
        print("The total Distance covered:", TotalDistance)
        RemainingFuel = Fuel.iloc[-1]
        # RemainingFuel = float(RemainingFuel)
        # UsedFuel = 100 - RemainingFuel
        UsedFuel = Fuel.iloc[-1] - Fuel.iloc[1]
        print("UsedFuel:", UsedFuel)
        Mileage = TotalDistance / UsedFuel
        TimeIndex = input('Enter the Time : ')
        for i in Distance.index:
            ExpectedDistance.append([Fuel[i] * Mileage], i)
        if TimeIndex < range(len(Kmpl)):
            TempExpectedDistance = Fuel[TimeIndex] * Mileage
        else:
            TempExpectedDistance = RemainingFuel * Mileage
        print('Expected Distance', TempExpectedDistance)
        DistanceToZero = pd.DataFrame(data=ExpectedDistance, columns=['DistanceToZero', 'Index'])
        return DistanceToZero
