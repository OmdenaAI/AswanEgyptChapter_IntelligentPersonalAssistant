from automation.user_schema import schema
from automation.convert_to_time import convert_to_time
from automation.parse_time import parse_time
from automation.time_ranges import Ranges
from automation.convert_time_to_string import convert_time_to_string
from automation.add_time_durations import add_time_durations


def determine_time(day, period, user_data, ranges , addition):
    
    initial_time = user_data[day][period]
    
    length = len(initial_time)
    
    if length == 0 :
        
        time = ranges[period]["start"]
        
        time = parse_time(time , addition)
        
        return period ,  time
    else:
        
        last_task = initial_time[-1]
        
        end = last_task[-1]
        end_of_current_interval = ranges[period]["end"]

        time_end = convert_to_time(end)
        
        time_end_of_current_interval = convert_to_time(end_of_current_interval)
        
        if time_end >= time_end_of_current_interval :
            
            
            add = time_end - time_end_of_current_interval 
            
            
            add = str(add)
            
            add = convert_time_to_string(add)   
            
            add = add_time_durations(add , "5 minutes")    
                             
            keys = list(ranges.keys())
    
            index = keys.index(period)
            
            next_period = keys[index + 1]
            
            time = determine_time(day , next_period , user_data , ranges, add)
            
            return time

        else :
            time = parse_time(end , "5 minutes")
           
            return period ,  time