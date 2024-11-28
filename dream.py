"""
Bonita McBride
CS 521 - Fall 1
October 12, 2024
Final Project - Dream Log - Dream Class
"""
import string

class Dream:
    ''' dream details'''
    
    # req: tuple container
    VALID_TYPES = ("Lucid", "Nightmare", "Recurring", "Funny", "Sad", "Happy", 
                   "Frustrating", "Peaceful", "Other")
   
    def __init__(self, date, description, dream_types):  
        # req: private and public attributes
       self._date = date                
       self._description = description   
       self.types = self.validate_types(dream_types)         
       self.keywords = self.get_keywords()  
        
   # req: class method
    def validate_types(self, dream_types):
        ''' check that type is valid and more than one type can be chosen'''
        
        invalid_types = [t for t in dream_types if t not in Dream.VALID_TYPES]
        if invalid_types:
            raise ValueError(f"Invalid dream type(s): {', '.join(invalid_types)}. \
                             Valid types are: {', '.join(Dream.VALID_TYPES)}")
        return set(dream_types)
        
    # req: class method
    def get_keywords(self):
        ''' small list of words to ignore bc they don't make good keywords
        list not exhaustive, but good enough for now'''
        
        ignore_words = {'the', 'and', 'is', 'in', 'of', 'to', 'a', 'an', 'for',
        'on', 'with', 'as', 'by', 'at', 'from', 'about', 'that', 'which', 'it',
        'this', 'these', 'those', 'or', 'but', 'if', 'then', 'so', 'such', 
        'because', 'like', 'be', 'been', 'being', 'am', 'are', 'was', 'were',
        'do', 'does', 'did', 'has', 'have', 'having', 'had', 'i', 'he', 'she', 
        'they', 'we', 'you', 'me', 'him', 'her', 'them', 'us', 'my', 'your', 
        'his', 'its', 'our', 'their', 'mine', 'yours', 'hers', 'ours', 
        'theirs', 'who', 'whom', 'whose', 'why', 'how', 'what', 'where', 'when'}
        
        #get rid of punctuation, split words into set, and remove ignored words
        description = ''.join([char for char in self._description 
                      if char not in string.punctuation])
        # req: set container
        words = set(description.lower().split())
        return words - ignore_words  
    
    def __contains__(self, keyword):
        '''find dreams with keywords'''
        return keyword.lower() in self.keywords

    def __str__(self):
        types_str = ', '.join(self.types)
        return f"Dream on: {self._date}\nType(s): {types_str}\nDescription: {self._description}"
    