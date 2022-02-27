from cProfile import label
from os import system
import skfuzzy.control as fuzzyControl

from memberFunction import x_temp, x_soil, y_time

y_time.defuzzify_method = 'centroid'

ruleLong = fuzzyControl.Rule(antecedent=((x_temp["hot"]&x_soil["dry"])|(x_temp["warm"]&x_soil["dry"])), consequent=y_time['long'], label='Long')
ruleMedium = fuzzyControl.Rule(antecedent=((x_temp["normal"]&x_soil["dry"])|(x_temp["cool"]&x_soil["dry"])|(x_temp["hot"]&x_soil["moist"])|(x_temp["warm"]&x_soil["moist"])|(x_temp["normal"]&x_soil["moist"])), consequent = y_time["medium"], label="Medium")
ruleShort = fuzzyControl.Rule(antecedent=((x_temp["cool"]&x_soil["moist"])|(x_temp["cold"]&x_soil["moist"])|(x_temp["hot"]&x_soil["wet"])|(x_temp["warm"]&x_soil["wet"])|(x_temp["normal"]&x_soil["wet"])|(x_temp["cool"]&x_soil["wet"])|(x_temp["cold"]&x_soil["wet"])|(x_temp['cold']&x_soil['dry'])), consequent=y_time["short"], label="Short")

system = fuzzyControl.ControlSystem([ruleLong, ruleMedium, ruleShort])
systemSimu = fuzzyControl.ControlSystemSimulation(system)

if __name__=='__main__':
    while True :
        # Case test
        input_temp=input("Please enter air temperature in Celsiust\nor enter exit to leave \n")
        if input_temp == 'exit':
            break
        input_soil=input("Please enter soil moisture in percent\n")

        systemSimu.input["temp"]=int(input_temp)
        systemSimu.input["soil"]=int(input_soil)

        ## system compute
        systemSimu.compute()
        print(systemSimu.output["time"])