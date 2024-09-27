totalMatches = 609
totalBatted = 1014
timesNotOut = 162
totalRuns = 48426
completedInnings = totalBatted - timesNotOut

battingAverage = totalRuns / completedInnings
if __name__ == '__main__':
    print(round(battingAverage, 2))