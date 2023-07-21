# Open file to extract data.
with open('weather.dat','r') as weather_file:
    weather_data=weather_file.readlines()
# To calculate the difference of max and min temperatures.
diff_l=[]
for data in weather_data[2:len(weather_data)-1]:
    diff=int(data[6:8])-int(data[12:14])
    diff_l.append(diff)
# Calculate the minimum difference and get its index to find the day.
print(diff_l.index(min(diff_l))+1)




        
