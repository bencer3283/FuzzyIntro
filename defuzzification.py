from cProfile import label
from os import system
import skfuzzy.control as fuzzyControl

from memberFunction import x_temp, x_humid, y_time

y_time.defuzzify_method = 'centroid'

ruleLong = fuzzyControl.Rule(antecedent=((x_temp["far"]&x_humid["wet"])|(x_temp["far"]&x_humid["medium"])|(x_temp["medium"]&x_humid["wet"])), consequent=y_time['long'], label='Long')
ruleMedium = fuzzyControl.Rule(antecedent=((x_temp["medium"]&x_humid["medium"])|(x_temp["far"]&x_humid["dry"])|(x_temp["close"]&x_humid["wet"])|(x_temp["close"]&x_humid["medium"])), consequent = y_time["medium"], label="Medium")
ruleShort = fuzzyControl.Rule(antecedent=((x_temp["close"]&x_humid["dry"])|(x_temp["medium"]&x_humid["dry"])), consequent=y_time["short"], label="Short")

system = fuzzyControl.ControlSystem([ruleLong, ruleMedium, ruleShort])
systemSimu = fuzzyControl.ControlSystemSimulation(system)

if __name__=='__main__':
    while True :
        # Case test
        input_temp=input("Please enter air temperature error in Celsiust (5-40)\nor enter exit to leave \n")
        if input_temp == 'exit':
            break
        input_humid=input("Please enter air moisture in percent (20-90)\n")

        systemSimu.input["temp"]=int(input_temp)
        systemSimu.input["humid"]=int(input_humid)

        ## system compute
        systemSimu.compute()
        print(systemSimu.output["time"])