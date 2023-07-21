# Open file to extract data.
def file_reader(filename):
    with open(filename,'r') as readfile:
        data_reader=readfile.readlines()
        return data_reader
# Calculates and prints the day with minimum temperature difference.
def get_day(filename):

    weather_data=file_reader(filename)
    diff_l=[]

    for data in weather_data[2:len(weather_data)-1]:
        diff=int(data[6:8])-int(data[12:14])
        diff_l.append(diff)

    print(diff_l.index(min(diff_l))+1)

# Calculates and prints the team with minimum difference.
def get_team(filename):

    match_data=file_reader(filename)
    diff_l=[]
    team_l=[]
    for match in match_data[1:]:
        if match[3]!='-':
            diff=abs(int(match[43:45])-int(match[50:52]))
            diff_l.append(diff)
            team_l.append(match[7:20])

    index=diff_l.index(min(diff_l))
    print(team_l[index])

get_day('weather.dat')          # prints day with minimum temperature difference.
get_team('football.dat')        # prints team with minimum score difference.