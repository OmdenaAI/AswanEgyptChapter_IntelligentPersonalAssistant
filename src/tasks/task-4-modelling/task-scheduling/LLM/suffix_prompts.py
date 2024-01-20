task_name_suffix_prompt = """
        the input : {input} .\
        task name :


          """
          
days_suffix_prompt = """
      the input : {input} .\
      days :


    """
time_suffix_prompt = """
        the input : {input} .\
        the time :


          """

duration_suffix_prompt = """
        the input : {input} .\
        the duration :


          """
          
recurring_task_suffix_prompt = """
        the input : {input} .\
        a day :
        
        """
number_of_sessions_suffix_prompt =  """
        the input : {input} .\
        sessions :


          """
          
suffix_list = [number_of_sessions_suffix_prompt, recurring_task_suffix_prompt, duration_suffix_prompt, time_suffix_prompt, days_suffix_prompt, task_name_suffix_prompt]
