name = input("What's your name? ")
#if name == "Harry" or name == "Hermione" or name == "Ron":
#    print("Gryffindor")
#elif name == "Draco":
#    print("Slytherin")
#else:
#    print("WHO?")
    
    # here we are using the match and case keywords.
    #this syntax can expand on the if, elif, and else.
    
match name:
    case "Ron" | "Hermione" | "Harry":
      print("Gryffindor")
    case "Draco":
      print("Slytherin")
    case _:
      print("WHO?")
      
    
