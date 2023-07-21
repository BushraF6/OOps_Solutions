# Opening file to extract data.
with open('football.dat','r') as soccer_file:
    soccer_reader=soccer_file.readlines()

 # To calculate differences.   
score_diff=[]
for match in soccer_reader[1:]:
    # To ignore the row containing no data.
    if match[3]=='-':
        score_diff.append(101)   # appending value to get correct index of the minimum difference.
    else:
        diff=abs(int(match[43:45])-int(match[50:52]))
        score_diff.append(diff)
# Calculate minimum difference and find its index to find the team.
index=score_diff.index(min(score_diff))
print(soccer_reader[index+1][7:20])
    

