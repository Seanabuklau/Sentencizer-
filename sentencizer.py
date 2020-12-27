import re

BOUNDARIES = [r'(?<=[0-9]|[^0-9.])(\.)(?=[^0-9.]|[^0-9.]|[\s]|$)(?![\n\r]+)',
                               r'\.{2,}', r'\!+', r'\:+', r'\?+', r'\;+', r'[\n\r]+']
                               
"""
Breaking the regex BOUNDARIES list down:

(?<=[0-9]|[^0-9.])(\.)(?=[^0-9.]|[^0-9.]|[\s]|$) -> Looks for a period that is not preceded or succeded by a digit or other period to 
avoids the function from splitting sentences at decimal numbers.

\.{2,} -> Looks for 2 or more periods 
\!+ -> Looks for a series of of exclamation marks
\:+ -> Looks for a series of colons
\?+ -> Looks for a series of question marks
\;+ -> Looks for a series of semi-colons 
[\n\r]+ -> Looks for a series of newlines or 
"""

def sentencize(document, boundaries=BOUNDARIES, sent_tag='<SPLIT>'):
    """
    Function that reads a text file and looks for sentence boundaries like periods, exclaimation marks etc
    and adds a split tag to each sentence after the each boundary. The text in the sentences will then be split on the tag and appended
    into a new list that contains each sentence from the text file
    """
    
    lis = []
    list_of_sentences = []
            
    with open(document, 'r') as f:
            
        for sentences in f:
            for bounds in boundaries:
                sentences = re.sub(bounds, r'\g<0>' + sent_tag, sentences) # sub function takes in 3 parameters; 1-What to match 2-what to put in place of the match 3-String to be processed 
            lis.append(sentences)            

        list_of_sentences = [text.strip(" ") for text in lis[0].split(sent_tag) if text.strip(" ") != ""]
        
    return list_of_sentences
    
# Test run with test file. It's a lorem ipsum text file edited with added boundaries 
sentencize('Test.txt') 
