import pandas as pd
    
    
def save_changes_to_db(username, schedules):
    
    
    users = pd.read_csv("users_database/users.csv")
    
    def insert_new_schedule(row):
        
        if row["user"] == f"{username}":
            return f"{schedules}"
        else: 
            print("please add user username first")
            
    users["schedules"] = users.apply(insert_new_schedule, axis = 1)
    
    users.to_csv("users_database/users.csv")
    
    
    
    
    
    
    