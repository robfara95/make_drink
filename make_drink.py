import random

def determine_drink_tastes():
    
  questions = {
      "strong": "Do ye like yer drinks strong?",
      "salty": "Do ye like it with a salty tang?",
      "bitter": "Are ye a lubber who likes it bitter?",
      "sweet": "Would ye like a bit of sweetness with yer poison?",
      "fruity": "Are ye one for a fruity finish?"
  } 
  
  tasteDict = {}
  
  for taste, question in questions.items():
        
    answer = raw_input(question + ": ")
    
    if answer.upper() == 'Y' or answer.upper() == 'YES':
      tasteDict[taste] = True
    else:
      tasteDict[taste] = False
   
  return tasteDict  

def drink_contruction(tasteDict):

  ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
  }
  
  drinkContents = []
  
  for taste,ans in tasteDict.items():   
    if ans:
      ingredient = ingredients[taste]       
      drinkContents.append(random.choice(ingredient))
      
  return drinkContents   
  
### end of drink_contruction  

####main logic

if __name__ == '__main__':
    tasteDict = determine_drink_tastes()
    drinkContents = drink_contruction(tasteDict)
    print("\nList of drink contents")
    print("-" * 22)
    for ref in drinkContents:
      print(ref)
      
    if len(drinkContents) == 0:
      print("No drink selected")
      
      