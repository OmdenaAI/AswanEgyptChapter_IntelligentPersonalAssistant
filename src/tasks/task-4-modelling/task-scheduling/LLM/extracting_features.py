from langchain import FewShotPromptTemplate
from langchain.prompts import PromptTemplate
from LLM_inference import llm_inference
from example_prompts import example_prompt_list
from prefix_prompts import prefix_list
from suffix_prompts import suffix_list
from creating_vector_db.task_scheduling_vector_db import get_collection_from_vector_db
import re
import ast  
from extract_first_list import extract_first_list
from remove_dot_at_end import remove_dot
from string_to_boolean import string_to_boolean
from extract_first_integer import extract_first_integer

def extract_features(input):
    examples = []
    collections = get_collection_from_vector_db("creating_vector_db/vector_db", "task_scheduling")



    times = ["morning", "afternoon", "evening"]
    num_examples  = 5
    for time in times:
            
            fetched_examples = collections.query(
                query_texts = [input],
                where = {"time": time},
                n_results = num_examples,
            )
            examples.append(fetched_examples)

    #start adding examples
    """
    num_nested_list = 6
    1: num_sessions
    2: recurring tasks
    3: duration 
    4: time 
    5: days
    6: task name
    """
    main_list = []

    for ex in range(len(example_prompt_list)):
        main_list.append([])
        
        for i in range(len(examples)):
            
            for j in range(num_examples) : 
                main_list[-1].append({})
                main_list[-1][-1]["input"] = examples[i]["documents"][0][j]
    
                if ex == 0: 
        
                    main_list[-1][-1]["sessions"] = str(examples[i]["metadatas"][0][j].get("sessions", ""))
                    
                elif ex == 1 :
                    
                    main_list[-1][-1]["a day"] = str(examples[i]["metadatas"][0][j].get("a day", ""))
                    
                elif ex == 2:
                    
                    main_list[-1][-1]["duration"] = str(examples[i]["metadatas"][0][j].get("duration", ""))
                    
                elif ex == 3:
                    
                    main_list[-1][-1]["time"] = str(examples[i]["metadatas"][0][j].get("time", ""))
                    
                elif ex == 4:
                
                    main_list[-1][-1]["days"] = str(examples[i]["metadatas"][0][j].get("days", ""))
                
                elif ex == 5:
                    
                    main_list[-1][-1]["task name"] = str(examples[i]["metadatas"][0][j].get("task name", ""))
                
                
                
    responses_list = []            
    for k in range(len(prefix_list)):
        
        example = main_list[k]
        example_prompt = example_prompt_list[k]
        prefix = prefix_list[k]
        suffix = suffix_list[k]
        
        few_shot_prompt_template = FewShotPromptTemplate(examples=example,
            example_prompt=example_prompt,
            prefix=prefix,
            suffix=suffix,
            input_variables=["input"],
            example_separator="\\\n\\\n" )


        # send prompt to LLM using the common function
        print(k)
        response = llm_inference(
                    model_type="huggingface",
                    input_variables_list=[input],
                    few_shot_prompt=few_shot_prompt_template,
                    hf_repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
                    temperature=0.5,
                    max_length=32000,
                )
        if k == 0 :
            response = extract_first_integer(response)
            response = str(response)
        
        if k ==4:
            response = extract_first_list(response)
            response = str(response)
            
            
            
        response = response.replace("\n", "")
        response = remove_dot(response)
        
        responses_list.append(response)    
    
    return responses_list
                        
                    
                
                
            


        
        

        
        
        