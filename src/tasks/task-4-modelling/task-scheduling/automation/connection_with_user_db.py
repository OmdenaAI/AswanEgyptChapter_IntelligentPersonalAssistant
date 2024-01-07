import pandas as pd
from automation.user_schema import schema



def connection_with_user_db(username, schema):
   
    user = username
    
    users = pd.read_csv("users_database/users.csv")



    exist = users['user'].str.contains(user)


    if exist.any() :
        filtered_df = users[exist]
        
        schedules = filtered_df["schedules"]
        
        for schedule in schedules :
            
            user_schema = eval(schedule)  
        
        return user_schema

    else:
        length = len(users)
        
        users.loc[ length+1 , "user"] = user
        
        users.to_csv("users_database/users.csv")
        
        user_schema = schema
            
        return user_schema