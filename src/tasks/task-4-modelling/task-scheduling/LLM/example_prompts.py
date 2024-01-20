from langchain.prompts import PromptTemplate
from example_templates import example_template_list


task_name_example_prompt = PromptTemplate(
      input_variables=["input", "task name"],
      template=example_template_list[5]
        )

days_example_prompt = PromptTemplate(
      input_variables=["input", "days"],
      template=example_template_list[4]
        )

time_example_prompt = PromptTemplate(
      input_variables=["input", "time"],
      template=example_template_list[3]
        )

duration_example_prompt = PromptTemplate(
      input_variables=["input", "duration"],
      template=example_template_list[2]
        )

recurring_example_prompt = PromptTemplate(
      input_variables=["input", "a day"],
      template= example_template_list[1]
        )
 
sessions_example_prompt = PromptTemplate(
      input_variables=["input", "sessions"],
      template=example_template_list[0]
        )

example_prompt_list = [sessions_example_prompt, recurring_example_prompt, duration_example_prompt, time_example_prompt, days_example_prompt, task_name_example_prompt] 









