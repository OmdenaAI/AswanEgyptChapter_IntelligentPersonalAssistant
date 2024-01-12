import re

def remove_dot(input):

    def remove_dot_at_end(sentence):
        # Check if the last character is a dot and not part of a float number
        if sentence.endswith('.') and not re.search(r'\d+\.\d+$', sentence):
            # Remove the dot
            sentence = sentence[:-1]
        
        return sentence

    # Example usage:
    input_text = input

    # Split the text into sentences
    sentences = input_text.split('. ')

    # Remove the dot at the end of each sentence (excluding float numbers)
    modified_sentences = [remove_dot_at_end(sentence) for sentence in sentences]

    # Join the modified sentences back together
    output_text = '. '.join(modified_sentences)
    
    return output_text


