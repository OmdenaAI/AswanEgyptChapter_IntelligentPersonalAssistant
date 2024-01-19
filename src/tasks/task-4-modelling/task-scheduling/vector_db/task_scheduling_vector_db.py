from dotenv import load_dotenv, find_dotenv
import pandas as pd
import os
import chromadb
from chromadb.utils import embedding_functions
import math



def create_task_scheduling_vector_db(vdb_path: str,collection_name:str , df: pd.DataFrame) -> None:
    """This function processes the dataframe into the required format, and then creates the following collections in a ChromaDB instance
    1. task_scheduling_collection - Contains input text embeddings, and the metadata the other columns

    Args:
        collection_name (str) : name of database collection
        vdb_path (str): Relative path of the location of the ChromaDB instance.
        df (pd.DataFrame): task scheduling dataset.
        
    """
    load_dotenv(find_dotenv())

    #identify the saving location of the ChromaDB
    chroma_client = chromadb.PersistentClient(path=vdb_path)

    #extract the embedding from hugging face 
    embedding_function = embedding_functions.HuggingFaceEmbeddingFunction(
        api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"],
        model_name="sentence-transformers/all-MiniLM-L6-v2",
    )

    #creating the collection
    q_collection = chroma_client.create_collection(
        name=collection_name,
        embedding_function=embedding_function,
    )

    
    # the main text "input text" that will be embedded
    task_scheduling_documents = [row.input for row in df.itertuples()]
    
    # the metadata
    task_scheduling_metadata = [
        {"job": row.job , "sessions": row.sessions, "a day": row.a_day, "duration": row.duration, "days":row.days, "time":row.time} 
        for row in df.itertuples()
    ]
    
    #index
    q_ids = ["task_id " + str(row.Index) for row in df.itertuples()]
    
    
    length = len(df)
    num_iteration = length / 166
    num_iteration = math.ceil(num_iteration)
    
    start = 0
    # start adding the the vectors
    for i in range(num_iteration):
        if i == num_iteration - 1 :
            q_collection.add(documents=task_scheduling_documents[start:], metadatas=task_scheduling_metadata[start:], ids=q_ids[start:])
        else:    
            end = start + 166
            q_collection.add(documents=task_scheduling_documents[start:end], metadatas=task_scheduling_metadata[start:end], ids=q_ids[start:end])
            start = end
    return None

   

def delete_collection_from_vector_db(vdb_path: str, collection_name: str) -> None:
    """Deletes a particular collection from the persistent ChromaDB instance.

    Args:
        vdb_path (str): Path of the persistent ChromaDB instance.
        collection_name (str): Name of the collection to be deleted.
    """
    chroma_client = chromadb.PersistentClient(path=vdb_path)
    chroma_client.delete_collection(collection_name)
    return None


def list_collections_from_vector_db(vdb_path: str) -> None:
    """Lists all the available collections from the persistent ChromaDB instance.

    Args:
        vdb_path (str): Path of the persistent ChromaDB instance.
    """
    chroma_client = chromadb.PersistentClient(path=vdb_path)
    print(chroma_client.list_collections())


def get_collection_from_vector_db(
    vdb_path: str, collection_name: str
) -> chromadb.Collection:
    """Fetches a particular ChromaDB collection object from the persistent ChromaDB instance.

    Args:
        vdb_path (str): Path of the persistent ChromaDB instance.
        collection_name (str): Name of the collection which needs to be retrieved.
    """
    load_dotenv(find_dotenv())
    chroma_client = chromadb.PersistentClient(path=vdb_path)

    huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(
        api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"],
        model_name="sentence-transformers/all-MiniLM-L6-v2",
    )

    collection = chroma_client.get_collection(
        name=collection_name, embedding_function=huggingface_ef
    )

    return collection