# Import dependencies
# ----------------------------------------
import pandas as pd
from datetime import timedelta
import re
import scraping
# ----------------------------------------

# Scrape and clean data
# ----------------------------------------
def cleanAll():
    data = scraping.scrapeAll()
    F1_Data = cleanData(data)
    print(F1_Data)
    return F1_Data
# ----------------------------------------

# Concatenate and clean all data
# ----------------------------------------
def cleanData(data):
    raceNames = [
        'Bahrain',
        'Saudi Arabia',
        'Australia',
        'Emilia Romagna',
        'Miami',
        'Spain',
        'Monaco',
        'Azerbaijan',
        'Canada',
        'Great Britain',
        'Austria',
        'France',
        'Hungary'
    ]

    master_df = pd.DataFrame()
    race_df_list = []

    # loop over the list of csv files, converting >100 tables into individual race dataframes
    for count, (key, fileLocation) in enumerate(data.items()):

        # read the csv file
        df = fileLocation

        # print the location and filename
        print('Location:', key)
        fileName = f'{key}'
        raceIndex = key[0:2]
        tableIndex = int(key[3])
        print('File Name:', fileName)
        print(f'Race Number Index: {raceIndex}')
        print(f'Table Number Index: {tableIndex}')

        # Races 3 and 10 have sprints and need to be concatted differently
        if (raceIndex == '03') or (raceIndex == '10'):
            if fileName == f'{raceIndex}_0_df':
                master_df['Final Race Position'] = df['Pos']
                master_df['No'] = df['No']
                master_df['Driver Name'] = df['Driver']
                master_df['Car'] = df['Car']
                master_df['Race Laps'] = df['Laps']
                master_df['Race Time'] = df['Time/Retired']
                master_df['Race Points'] = df['PTS']
                master_df['Race'] = raceNames[int(raceIndex)]
                master_df.set_index('No', inplace=True)
            elif fileName == f'{raceIndex}_1_df':
                df.set_index('No', inplace=True)
                master_df = master_df.join(df[['Lap', 'Time of day', 'Time', 'Avg Speed']], on='No')
                master_df.rename(columns={"Lap": "Fastest Lap No", "Time": "Fastest Lap Time"}, inplace=True)
            elif fileName == f'{raceIndex}_2_df':
                df.set_index('No', inplace=True)
                df.sort_values(by=['Driver', 'Stops'])
                df.drop_duplicates(subset=['Driver'], keep='last', inplace=True)
                master_df = master_df.join(df[['Stops', 'Total']], on='No')
                master_df.rename(columns={"Total": "Total Pit Time"}, inplace=True)
            elif fileName == f'{raceIndex}_3_df':
                df.set_index('No', inplace=True)
                master_df = master_df.join(df[['Pos']], on='No')
                master_df.rename(columns={"Pos": "Starting Grid Pos"}, inplace=True)
            elif fileName == f'{raceIndex}_4_df':
                df.set_index('No', inplace=True)
                master_df = master_df.join(df[['Pos', 'Laps', 'Time/Retired', 'PTS']], on='No')
                master_df.rename(columns={"Pos": "Final Sprint Postition", "Laps": "Sprint Laps", "Time/Retired": "Sprint Time/Retired", "PTS": "Sprint PTS"}, inplace=True)
            elif fileName == f'{raceIndex}_5_df':
                df.set_index('No', inplace=True)
                master_df = master_df.join(df[['Pos', 'Time']], on='No')
                master_df.rename(columns={"Pos": "Starting Sprint Postition", "Time": "Sprint Grid Time"}, inplace=True)
            elif fileName == f'{raceIndex}_6_df':
                df.set_index('No', inplace=True)
                master_df = master_df.join(df[['Pos', 'Time', 'Gap', 'Laps']], on='No')
                master_df.rename(columns={"Pos": "P2 Postition", "Time": "P2 Time", "Gap": "P2 Gap", "Laps": "P2 Laps"}, inplace=True)
            elif fileName == f'{raceIndex}_7_df':
                df.set_index('No', inplace=True)
                master_df = master_df.join(df[['Pos', 'Q1', 'Q2', 'Q3', 'Laps']], on='No')
                master_df.rename(columns={"Pos": "Qualifying Postition", "Laps": "Qualifying Laps"}, inplace=True)
            elif fileName == f'{raceIndex}_8_df':
                df.set_index('No', inplace=True)
                master_df = master_df.join(df[['Pos', 'Time', 'Gap', 'Laps']], on='No')
                master_df.rename(columns={"Pos": "P1 Postition", "Time": "P1 Time", "Gap": "P1 Gap", "Laps": "P1 Laps"}, inplace=True)
            else:
                print("SOMETHING WENT WRONG")
        else:
            if fileName == f'{raceIndex}_0_df':
                master_df['Final Race Position'] = df['Pos']
                master_df['No'] = df['No']
                master_df['Driver Name'] = df['Driver']
                master_df['Car'] = df['Car']
                master_df['Race Laps'] = df['Laps']
                master_df['Race Time'] = df['Time/Retired']
                master_df['Race Points'] = df['PTS']
                master_df['Race'] = raceNames[int(raceIndex)]
                master_df.set_index('No', inplace=True)
            elif fileName == f'{raceIndex}_1_df':
                df.set_index('No', inplace=True)
                master_df = master_df.join(df[['Lap', 'Time of day', 'Time', 'Avg Speed']], on='No')
                master_df.rename(columns={"Lap": "Fastest Lap No", "Time": "Fastest Lap Time"}, inplace=True)
            elif fileName == f'{raceIndex}_2_df':
                df.set_index('No', inplace=True)
                df.sort_values(by=['Driver', 'Stops'])
                df.drop_duplicates(subset=['Driver'], keep='last', inplace=True)
                master_df = master_df.join(df[['Stops', 'Total']], on='No')
                master_df.rename(columns={"Time": "Fastest Lap Time"}, inplace=True)
            elif fileName == f'{raceIndex}_3_df':
                df.set_index('No', inplace=True)
                master_df = master_df.join(df[['Pos', 'Time']], on='No')
                master_df.rename(columns={"Lap": "Fastest Lap No", "Total": "Total Pit Time", "Pos": "Starting Grid Pos", "Time": "Starting Grid Quali Time"}, inplace=True)
            elif fileName == f'{raceIndex}_4_df':
                df.set_index('No', inplace=True)
                master_df = master_df.join(df[['Pos', 'Q1', 'Q2', 'Q3', 'Laps']], on='No')
                master_df.rename(columns={"Pos": "Qualifying Postition", "Laps": "Qualifying Laps"}, inplace=True)
            elif fileName == f'{raceIndex}_5_df':
                df.set_index('No', inplace=True)
                master_df = master_df.join(df[['Pos', 'Time', 'Gap', 'Laps']], on='No')
                master_df.rename(columns={"Pos": "P3 Postition", "Time": "P3 Time", "Gap": "P3 Gap", "Laps": "P3 Laps"}, inplace=True)
            elif fileName == f'{raceIndex}_6_df':
                df.set_index('No', inplace=True)
                master_df = master_df.join(df[['Pos', 'Time', 'Gap', 'Laps']], on='No')
                master_df.rename(columns={"Pos": "P2 Postition", "Time": "P2 Time", "Gap": "P2 Gap", "Laps": "P2 Laps"}, inplace=True)
            elif fileName == f'{raceIndex}_7_df':
                df.set_index('No', inplace=True)
                master_df = master_df.join(df[['Pos', 'Time', 'Gap', 'Laps']], on='No')
                master_df.rename(columns={"Pos": "P1 Postition", "Time": "P1 Time", "Gap": "P1 Gap", "Laps": "P1 Laps"}, inplace=True)
            else:
                print("SOMETHING WENT WRONG")

        # The sprint races have one more raceIndex, so the master_df needs to be reset at 7 and 8
        if (raceIndex != '03' and raceIndex != '10') and (tableIndex == 7):
            master_df.reset_index(inplace=True)
            race_df_list.append(master_df)
            print(f"{raceNames[int(raceIndex)]}_DF has been added successfully")
            print()
            master_df = pd.DataFrame()
        elif (tableIndex == 8):
            master_df.reset_index(inplace=True)
            race_df_list.append(master_df)
            print(f"{raceNames[int(raceIndex)]}_DF has been added successfully")
            print()
            master_df = pd.DataFrame()


    # Concat the race DataFrames into one F1 DataFrame
    f1_df = pd.concat(race_df_list, axis=0, ignore_index=True)


    # # Data Cleaning
    # ## Filling Null Values
    master_df = f1_df.copy()

    # Fill NaN values
    master_df['Starting Grid Pos'] = master_df['Starting Grid Pos'].fillna(99)

    master_df['Fastest Lap No'] = master_df['Fastest Lap No'].fillna(0)
    master_df['Time of day'] = master_df['Time of day'].fillna('99:99:99')
    master_df['Fastest Lap Time'] = master_df['Fastest Lap Time'].fillna('99:99')
    master_df['Avg Speed'] = master_df['Avg Speed'].fillna(0)

    master_df['Stops'] = master_df['Stops'].fillna(99)
    master_df['Total Pit Time'] = master_df['Total Pit Time'].fillna('99:99')

    master_df['P1 Postition'] = master_df['P1 Postition'].fillna(99)
    master_df['P1 Time'] = master_df['P1 Time'].fillna('99:99')
    master_df['P1 Laps'] = master_df['P1 Laps'].fillna(0)

    master_df['P2 Postition'] = master_df['P2 Postition'].fillna(99)
    master_df['P2 Time'] = master_df['P2 Time'].fillna('99:99')
    master_df['P2 Laps'] = master_df['P2 Laps'].fillna(0)

    master_df['P3 Postition'] = master_df['P3 Postition'].fillna(99)
    master_df['P3 Time'] = master_df['P3 Time'].fillna('99:99')
    master_df['P3 Laps'] = master_df['P3 Laps'].fillna(0)

    master_df['Starting Grid Quali Time'] = master_df['Starting Grid Quali Time'].fillna('99:99')
    master_df['Q1'] = master_df['Q1'].fillna('99:99')
    master_df['Q2'] = master_df['Q2'].fillna('99:99')
    master_df['Q3'] = master_df['Q3'].fillna('99:99')

    master_df['Sprint Laps'] = master_df['Sprint Laps'].fillna(0)
    master_df['Sprint Time/Retired'] = master_df['Sprint Time/Retired'].fillna('0')
    master_df['Sprint Grid Time'] = master_df['Sprint Grid Time'].fillna('00:00')
    master_df['Sprint PTS'] = master_df['Sprint PTS'].fillna(0)
    master_df['Starting Sprint Postition'] = master_df['Starting Sprint Postition'].fillna(0)
    master_df['Final Sprint Postition'] = master_df['Final Sprint Postition'].fillna(0)

    def formatPos(race):
        for i, value in enumerate(race):
            if (value == 'NC'):
                race.iloc[i] = 99
            else:
                race.iloc[i] = pd.to_numeric(value)

        return pd.to_numeric(race)

    # Change NC to 99th place
    racePos = master_df['Final Race Position']
    racePos = formatPos(racePos)
    master_df['Final Race Position'] = racePos

    sprintPos = master_df['Final Sprint Postition']
    sprintPos = formatPos(sprintPos)
    master_df['Final Sprint Postition'] = sprintPos

    # ## Strip Times of '+' and 's'
    # Remove '+' and 's' from Race Time column
    master_df['Race Time']= master_df['Race Time'].astype('str')
    master_df['Race Time']= master_df['Race Time'].map(lambda x: x.lstrip('+-'))
    master_df['Race Time']= master_df['Race Time'].map(lambda x: x.rstrip('s'))

    # Remove '+' and 's' from P3 Gap column
    master_df['P3 Gap']= master_df['P3 Gap'].astype('str')
    master_df['P3 Gap']= master_df['P3 Gap'].map(lambda x: x.lstrip('+-'))
    master_df['P3 Gap']= master_df['P3 Gap'].map(lambda x: x.rstrip('s'))

    # Remove '+' and 's' from P2 Gap column
    master_df['P2 Gap']= master_df['P2 Gap'].astype('str')
    master_df['P2 Gap']= master_df['P2 Gap'].map(lambda x: x.lstrip('+-'))
    master_df['P2 Gap']= master_df['P2 Gap'].map(lambda x: x.rstrip('s'))

    # Remove '+' and 's' from P1 Gap column
    master_df['P1 Gap']= master_df['P1 Gap'].astype('str')
    master_df['P1 Gap']= master_df['P1 Gap'].map(lambda x: x.lstrip('+-'))
    master_df['P1 Gap']= master_df['P1 Gap'].map(lambda x: x.rstrip('s'))

    # Remove '+' and 's' from P1 Gap column
    master_df['Sprint Time/Retired'] = master_df['Sprint Time/Retired'].astype('str')
    master_df['Sprint Time/Retired'] = master_df['Sprint Time/Retired'].map(lambda x: x.lstrip('+-'))
    master_df['Sprint Time/Retired'] = master_df['Sprint Time/Retired'].map(lambda x: x.rstrip('s'))

    # ## Convert All HH:MM:SS and MM:SS Times To Seconds
    def raceTimeToSeconds(time):
        time_copy = time.copy()
        raceCount = 0
        for count, race in enumerate(time_copy):
            # Check to get the leading time for each race
            if (raceCount == 20):
                raceCount = 0

            # Race time is always first index
            if (raceCount == 0):
                end_time = race
                my_list = end_time.split(':')
                if len(my_list) == 3:
                    time_f = timedelta(hours=int(my_list[0]),minutes=int(my_list[1]), seconds=float(my_list[2])).total_seconds()
                    time_copy.iloc[count] = time_f
                elif len(my_list) == 2:
                    time_f = timedelta(minutes=int(my_list[0]), seconds=float(my_list[1])).total_seconds()
                    time_copy.iloc[count] = time_f
            # If race contains substring 'lap' indicating 1+ Lap. Will add the number of laps indicated so 1+ Lap
            # Will add 1 whole lap, 2+ Lap will add two laps, etc.
            elif 'lap' in race:
                time_copy.iloc[count] = time_f+(int(race[0])*time_f)
            # Use regex to check if a float value exists
            elif re.match(r'^-?\d+(?:\.\d+)$', race) is not None:
                time_copy.iloc[count] = (time_f + float(race))
            # Anything else such as DNF, DSQ will get 999999
            elif (race== "DNF"):
                time_copy.iloc[count] = 999999
            elif (race== "DNS"):
                time_copy.iloc[count] = 0

            # Increment raceCount
            raceCount += 1

        return time_copy

    race_time = master_df['Race Time']
    new_race_time = raceTimeToSeconds(race_time)
    master_df['Race Time'] = pd.to_numeric(new_race_time)

    sprint_time = pd.DataFrame(master_df[['Race', 'Sprint Time/Retired']]).set_index(['Race'])
    sprint_time.sort_values(by=['Sprint Time/Retired'])
    # print(sprint_time)
    # new_sprint_time = raceTimeToSeconds(sprint_time)
    # master_df['Sprint Time/Retired'] = new_sprint_time

    # Convert non-race times to seconds (eg. lap times)
    def timeToSeconds(time):
        time_copy = time.copy()
        for count, race in enumerate(time_copy):
            # Check first if value is float (eg. time is already in seconds)
            if (race != "DNF"):
                if re.match(r'^-?\d+(?:\.\d+)$', str(race)) is not None:
                    time_f = timedelta(seconds=float(race)).total_seconds()
                    time_copy.iloc[count] = time_f
                else:
                    end_time = race
                    my_list = end_time.split(':')
                    if len(my_list) == 3:
                        time_f = timedelta(hours=int(my_list[0]), minutes=int(my_list[1]), seconds=float(my_list[2])).total_seconds()
                        time_copy.iloc[count] = time_f
                    elif len(my_list) == 2:
                        time_f = timedelta(minutes=int(my_list[0]), seconds=float(my_list[1])).total_seconds()
                        time_copy.iloc[count] = time_f
            # Anything else such as DNF, DSQ will get 999999
            else:
                time_copy.iloc[count] = 999999

        return time_copy

    tod_time = master_df['Time of day']
    new_tod_time = timeToSeconds(tod_time)
    master_df['Time of day'] = new_tod_time

    fastest_lap_copy = master_df['Fastest Lap Time']
    new_fastlap_time = timeToSeconds(fastest_lap_copy)
    master_df['Fastest Lap Time'] = new_fastlap_time

    pit_time_copy = master_df['Total Pit Time']
    new_pit_time = timeToSeconds(pit_time_copy)
    master_df['Total Pit Time'] = new_pit_time

    starting_grid_quali_copy = master_df['Starting Grid Quali Time']
    new_quali_time = timeToSeconds(starting_grid_quali_copy)
    master_df['Starting Grid Quali Time']= new_quali_time

    Q1_copy = master_df['Q1']
    new_q1_time = timeToSeconds(Q1_copy)
    master_df['Q1'] = new_q1_time

    Q2_copy = master_df['Q2']
    new_q2_time = timeToSeconds(Q2_copy)
    master_df['Q2'] = new_q2_time

    Q3_copy = master_df['Q3']
    new_q3_time = timeToSeconds(Q3_copy)
    master_df['Q3'] = new_q3_time

    P3_time_copy = master_df['P3 Time']
    new_p3_time = timeToSeconds(P3_time_copy)
    master_df['P3 Time'] = new_p3_time

    P2_time_copy = master_df['P2 Time']
    new_p2_time = timeToSeconds(P2_time_copy)
    master_df['P2 Time'] = new_p2_time

    P1_time_copy = master_df['P1 Time']
    new_p1_time = timeToSeconds(P1_time_copy)
    master_df['P1 Time'] = new_p1_time

    Sprint_grid_time_copy = master_df['Sprint Grid Time']
    new_sprint_grid_time = timeToSeconds(Sprint_grid_time_copy)
    master_df['Sprint Grid Time'] = new_sprint_grid_time

    # Convert gap times to numeric values
    def gapToNumeric(gap):
        for i, value in enumerate(gap):
            if (value == 'nan'):
                gap.iloc[i] = 999
            else:
                gap.iloc[i] = pd.to_numeric(value)

        return pd.to_numeric(gap)

    p3Gap = master_df['P3 Gap']
    new_p3Gap = gapToNumeric(p3Gap)
    master_df['P3 Gap'] = new_p3Gap

    p2Gap = master_df['P2 Gap']
    new_p2Gap = gapToNumeric(p2Gap)
    master_df['P2 Gap'] = new_p2Gap

    p1Gap = master_df['P1 Gap']
    new_p1Gap = gapToNumeric(p1Gap)
    master_df['P1 Gap'] = new_p1Gap

    return master_df
# ----------------------------------------

# Main method
# ----------------------------------------
if __name__ == "__main__":
    # If running as script, print scraped data
    print(cleanAll())
# ----------------------------------------
