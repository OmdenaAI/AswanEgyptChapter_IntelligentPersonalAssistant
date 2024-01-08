from automation.todoist import todoist
from automation.parse_time import parse_time 
from automation.user_schema import schema
from automation.convert_to_time import convert_to_time
from automation.time_ranges import Ranges
from automation.convert_time_to_string import convert_time_to_string
from automation.add_time_durations import add_time_durations
from automation.determine_time import determine_time
from automation.connection_with_user_db import connection_with_user_db
from automation.save_changes_to_db import save_changes_to_db




def task_scheduling(username: str,
                      password : str ,
                      project_name : str, 
                      days: list,
                      day_period: str ,
                      recurring_tasks :  bool ,
                      num_sessions : int ,
                      session : str ,
                      duration: str,
                                    ):

    user_schema = connection_with_user_db(username , schema )

    with todoist(username, password, project_name) as bot:
        bot.go_to_first_page()
        bot.login()
        bot.Add_project()
        bot.go_to_upcoming_section()
        for i , day in enumerate(days):
            if recurring_tasks :
                for i in  range(num_sessions):
                    period , start_time = determine_time(day , day_period , user_schema , Ranges , "0 minutes")
                    end_time = parse_time(start_time, duration)
                    user_schema[day][period].append([start_time , end_time])                
                    bot.adding_sub_task(f"{project_name} {session}_{i+1}")
                    bot.adding_time(start_time)
                    bot.Adding_date(day)
                    bot.insert_child_task_to_parent_task()
                    bot.end()
            else:
                    period , start_time = determine_time(day , day_period , user_schema , Ranges , "0 minutes")
                    end_time = parse_time(start_time, duration)
                    user_schema[day][period].append([start_time , end_time])               
                    bot.adding_sub_task(f"{project_name} session")
                    bot.adding_time(start_time)
                    bot.Adding_date(day)
                    bot.insert_child_task_to_parent_task()
                    bot.end()

    save_changes_to_db(username , user_schema)
    

task_scheduling("",
                      "" ,
                      "medical consultation", 
                      ["Monday", "Thursday"],
                      "afternoon" ,
                      True ,
                      3 ,
                      "session" ,
                      "30 minutes"
                                    )
    



