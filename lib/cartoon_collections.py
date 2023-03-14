def roll_call_dwarves(dwarf_list):

    [print(f"{dwarf_list.index(dwarf)+1}. {dwarf}") for dwarf in dwarf_list] 

def summon_captain_planet(planateer_calls_list):
    return [f"{each_planateer_call.capitalize()}!" for each_planateer_call in planateer_calls_list]

def long_planeteer_calls(list_of_calls):
    
    return any(i>=5 for i in [len(eachCall) for eachCall in list_of_calls])   



def find_the_cheese():
    pass

#The Testing List

long_planeteer_calls(["dog", "goatt", "top"])