import datetime
def second_from_midnight(time):
    final_time = []
    my_time = time.split(":")
    for i in my_time:
        
    final_time.append(my_time[0]*3600)
    final_time.append(my_time[1]*60)
    final_time.append(my_time[2])
    return sum(final_time)

print(second_from_midnight('01:00:00'))