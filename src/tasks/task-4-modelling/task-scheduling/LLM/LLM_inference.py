from dotenv import load_dotenv, find_dotenv
from langchain.llms import HuggingFaceHub, OpenAI
from langchain.chains import LLMChain
import warnings
from typing import List


warnings.filterwarnings("ignore")


def llm_inference(
    model_type: str,
    input_variables_list: List[str] = [],
    few_shot_prompt: str = "",
    openai_model_name: str = "",
    hf_repo_id: str = "",
    temperature: float = 0.5,
    max_length: int = 5000,
) -> str :
    """Call HuggingFace/OpenAI model for inference

    Given a question, prompt_template, and other parameters, this function calls the relevant
    API to fetch LLM inference results.

    Args:
        model_str: Denotes the LLM vendor's name. Can be either 'huggingface' or 'openai'
        input_variables_list: List of the name of input variables for the prompt.
        few_shot_prompt: A prompt taken from few shot learning.
        hf_repo_id: The Huggingface model's repo_id.
        temperature: (Default: 1.0). Range: Float (0.0-100.0). The temperature of the sampling operation. 1 means regular sampling, 0 means always take the highest score, 100.0 is getting closer to uniform probability.
        max_length: Integer to define the maximum length in tokens of the output summary.

    Returns:
        A Python string which contains the inference result.

    HuggingFace repo_id examples:
        - mistralai/Mixtral-8x7B-Instruct-v0.1
        
        - mistralai/Mistral-7B-Instruct-v0.1
        


    """
    # Please ensure you have a .env file available with 'HUGGINGFACEHUB_API_TOKEN' and 'OPENAI_API_KEY' values.
    load_dotenv(find_dotenv())
    
    

    if model_type == "openai":
        # https://api.python.langchain.com/en/stable/llms/langchain.llms.openai.OpenAI.html#langchain.llms.openai.OpenAI
        llm = OpenAI(
            model_name=openai_model_name, temperature=temperature, max_tokens=max_length
        )
        llm_chain = LLMChain(prompt=few_shot_prompt, llm=llm)

        
        return llm_chain.run(
            #input_variables here

            )
        

    elif model_type == "huggingface":
        # https://python.langchain.com/docs/integrations/llms/huggingface_hub
        llm = HuggingFaceHub(
            repo_id=hf_repo_id,
            model_kwargs={"temperature": temperature, "max_length": max_length} )
        llm_chain = LLMChain(prompt=few_shot_prompt, llm=llm)

        return llm_chain.run(
            #input variables here

            )
        

    else:
        print(
            "Please use the correct value of model_type parameter: It can have a value of either openai or huggingface"
        )

        return ""