### playto.py - Logic and reasoning structures
### IMPORTS AND MODULES For Plato.py


### Global variables for Plato.py
ascii_art = r"""
      /$$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$| $$$$$$$
     /$$/ $$$$                                                        | $$$$ /$$
    /$$/|_  $$       /$$$$$$$  /$$             /$$                    | $$_/|  $$    
   /$$/   | $$      | $$__  $$| $$            | $$                    | $$   \  $$ 
  /$$/    | $$      | $$  \ $$| $$  /$$$$$$  /$$$$$$    /$$$$$$       | $$    \  $$
 /$$/     | $$      | $$$$$$$/| $$ |____  $$|_  $$_/   /$$__  $$      | $$     \  $$
|  $$     | $$      | $$____/ | $$  /$$$$$$$  | $$    | $$  \ $$      | $$      /$$/ 
 \  $$    | $$      | $$      | $$ /$$__  $$  | $$ /$$| $$  | $$      | $$     /$$/ 
  \  $$   | $$      | $$      | $$|  $$$$$$$  |  $$$$/|  $$$$$$/      | $$    /$$/  
   \  $$  | $$      |__/      |__/ \_______/   \___/   \______/       | $$   /$$/    
    \  $$/$$$$                                                        | $$$$/$$/
     \__$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ | $$$/|_/ 
"""
module_name = "Plato"
# module_version = "0.0.1" Initial version basic text input and file path input
# module_version = "0.0.2" Added help command and more acurate input handling to the later versions as well as basic pattern recognition
module_version = "0.0.3" 
module_description = "Logic and reasoning structures module for Socrates.net"

plato_help = """Plato Module Help:
-t "some text" : Process text input through reasoning engine
-p "file_path" : Process file path input through reasoning engine
-Plato --help : Display this help message
"""

question_starts = ["who", "what", "when", "where", "why", "how", 
                   "is", "are", "can", "could", "would", "should", 
                   "do", "does", "did", "will", "may", "might", 
                   "tell", "explain", "describe", "define"]

# secondary_question_starts = ["will", "shall", "isn't", "aren't", "can't", "couldn't",
#                             "doesn't", "don't", "didn't", "has", "have", "had",
#                             "was", "were", "won't", "shouldn't", "wouldn't", "mightn't"]

conditionals_1 = ["if", "when", "unless", "because", "give", "provided"]
conditionals_2 = ["then", "so", "therefore", "else", "hence", "thus"]
multiword_conditionals = ["as long as", "only if", "even though", "in case", "in the event that"]


### Functions for Plato.py
def plato_module_info():
    return {"Module Name" : module_name,
            "Module Version" : module_version,
            "Module Description" : module_description}

def conditional_check(normalized_data):
    condition_type = "none"
    condition = ""
    effect = ""
    data = None
    Confidence = "Unclassified"
    ### Multi-word conditional check
    for phrase in multiword_conditionals:

        split_phrase = phrase.split(" ")
        phrase_length = len(split_phrase)

        for i in range(len(normalized_data)): 
            segmant = normalized_data[i:i + phrase_length]
            if segmant == split_phrase:
                start_indexof_phrase = i
                end_indexof_phrase = start_indexof_phrase + phrase_length - 1

                condition = " ".join(normalized_data[:start_indexof_phrase])
                effect = " ".join(normalized_data[end_indexof_phrase + 1:])
                condition_type = "explicit"
                Confidence = "Unclassified"
                data = {"Condition" : condition,   
                        "Conditional Phrase" : phrase,
                        "Effect" : effect,}
                continue
    ### Single-word conditional check
    for i, word in enumerate(normalized_data):
        if word in conditionals_2:
            for prev_word in normalized_data[:i]:
                if prev_word in conditionals_1:
                    condition_type = "explicit"
                    condition = " ".join(normalized_data[:i])
                    conditional_words = f"{prev_word}, {word}"
                    effect = " ".join(normalized_data[i+1:])
                    data = {"Condition" : condition,   
                            "Conditional Words" : conditional_words,
                            "Effect" : effect}
                    Confidence = "Unclassified"

        ### reverse check       
        elif word in conditionals_1:
            for next_word in normalized_data[i+1:]:
                if next_word in conditionals_2:
                    condition_type = "explicit"
                    condition = " ".join(normalized_data[:i])
                    conditional_words = f"{word}, {next_word}"
                    effect = " ".join(normalized_data[i+1:])
                    data = {"Condition" : condition,   
                            "Conditional Words" : conditional_words,
                            "Effect" : effect}
                    Confidence = "Unclassified"
                
            condition_type = "implicit"
            condition = " ".join(normalized_data[:i])
            conditional_words = word
            effect = " ".join(normalized_data[i+1:])
            data = {"Condition" : condition,   
                    "Conditional Words" : conditional_words,
                    "Effect" : effect}
            Confidence = "Unclassified"

    if data:
        return {"Model": f"{module_name} v{module_version}",
                "Classification" : condition_type,
                "Data" : data,
                "Confidence" : Confidence}
    return False

    ### TODO: Handle cases where multiple conditionals are present in a single statement. 
    ### Add weights to conditionals to determine primary conditional in complex statements.
    ### Add confidence scoring system for conditional detection.
    ### Add negation handling for conditionals.

def reasoning_engine(input_data, input_type):
    print("Processing input data through reasoning engine...")
    
    match input_type:
        ### TEXT PROCESSING / PATTERN RECOGNITION
        case "-t": 
            classification = "unclassified"
            Confidence = "unclassified"
            normalized_data = input_data.lower().strip(" '\"\t\n").split()

            ### QUESTION RECOGNITION
            if normalized_data[-1].endswith("?") or normalized_data[0]in question_starts: # and normalized_data[1] in secondary_question_starts):  this need to be fixed look at Notes.txt
                data = {"Question" : input_data}
                classification = "question"
                Confidence = "unclassified"

            else:
                ### CONDITIONAL STATEMENT RECOGNITION
                conditional_result = conditional_check(normalized_data)
                if conditional_result:
                    return conditional_result
                
                ### LOGICAL STATEMENT RECOGNITION
                elif any(token in ["and", "or", "not", "if", "then"] for token in normalized_data):
                    data = f"Logical operator received: {input_data}"
                    classification = "logical statement"
                    Confidence = "unclassified"
                    
                ### GENERAL TEXT RECOGNITION
                else:
                    data = f"Statement received: {input_data}"
                    classification = "statement"
                    Confidence = "unclassified"

            return {"Model": f"{module_name} v{module_version}",
                    "Classification" : classification,
                    "Data" : data,
                    "Confidence" : Confidence}

        ### FILE PATH PROCESSING / VALIDATION
        case "-p": 
            processed_data = f"File path received: {input_data}" 
            return {"Model": f"{module_name} v{module_version}",
                    "Classification" : "File Path",
                    "Data" : processed_data,
                    "Confidence" : "Unclassified"}

        
        case _:
            processed_data = "Command not recognized. please use -Plato --help for options."
    
    return processed_data 

### Build area for code not developed yet
# def future_function():
#     pass  


### TESTING AREA
# print(reasoning_engine("if it rains then we stay inside", "-t"))
# print(reasoning_engine("when it rains we stay inside", "-t"))
# print(reasoning_engine("what is truth?", "-t"))
# print(reasoning_engine("this is just a statement", "-t"))