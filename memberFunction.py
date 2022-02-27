import numpy as np
import skfuzzy as fuzzy
import skfuzzy.control as fuzzyControl
import matplotlib.pyplot as plt

# Range

## range of temp. & soil & watering 
x_temp_range = np.arange(-5,45,1,np.float32)
x_soil_range = np.arange(0,100,0.1,np.float32)
y_time_range=np.arange(0,31,1,np.float32)
##　variable and membership functions
x_temp = fuzzyControl.Antecedent(x_temp_range,"temp")
x_soil= fuzzyControl.Antecedent(x_soil_range,"soil")
y_time = fuzzyControl.Consequent(y_time_range,"time")

cold = [-5, -5, 6, 13]
x_temp["cold"] = fuzzy.trapmf(x_temp_range, cold)
cool = [7.5,13,15,20]
x_temp["cool"] = fuzzy.trapmf(x_temp_range,cool)
normal = [15,18,22,32]
x_temp["normal"] = fuzzy.trapmf(x_temp_range,normal)
warm = [23,28,35]
x_temp["warm"] = fuzzy.trimf(x_temp_range,warm)
hot = [32,36,45,45]
x_temp["hot"] = fuzzy.trapmf(x_temp_range,hot)

dry = [0,0,28,46]
x_soil["dry"] = fuzzy.trapmf(x_soil_range,dry)
moist = [35,42.5,72.5,88.6]
x_soil["moist"] = fuzzy.trapmf(x_soil_range,moist)
wet = [65.5,88.6,100,100]
x_soil["wet"] = fuzzy.trapmf(x_soil_range,wet)

short = [0,0,5,8]
y_time["short"] = fuzzy.trapmf(y_time_range,short)
medium = [2,12,17.5,23]
y_time["medium"] = fuzzy.trapmf(y_time_range,medium)
long = [14,26,30,30]
y_time["long"] = fuzzy.trapmf(y_time_range,long)

# Visualize these universes and membership functions
fig,(figure1,figure2,figure3)=plt.subplots(nrows=3,figsize=(8,9))
figure1.plot(x_temp_range,fuzzy.trapmf(x_temp_range, cold),'b',linewidth=1.5,label='cold')
figure1.plot(x_temp_range,fuzzy.trapmf(x_temp_range,cool),'g',linewidth=1.5,label='cool')
figure1.plot(x_temp_range,fuzzy.trapmf(x_temp_range,normal),'r',linewidth=1.5,label='normal')
figure1.plot(x_temp_range,fuzzy.trimf(x_temp_range,warm),'y',linewidth=1.5,label='warm')
figure1.plot(x_temp_range,fuzzy.trapmf(x_temp_range,hot),'k',linewidth=1.5,label='hot')
figure1.set_title('Air Temperature (C)')
figure1.legend()

figure2.plot(x_soil_range,fuzzy.trapmf(x_soil_range,dry),'b',linewidth=1.5,label='dry')
figure2.plot(x_soil_range,fuzzy.trapmf(x_soil_range,moist),'g',linewidth=1.5,label='moist')
figure2.plot(x_soil_range,fuzzy.trapmf(x_soil_range,wet),'r',linewidth=1.5,label='wet')
figure2.set_title('Soil Moisture (%)')
figure2.legend()

figure3.plot(y_time_range,fuzzy.trapmf(y_time_range,short),'b',linewidth=1.5,label='short')
figure3.plot(y_time_range,fuzzy.trapmf(y_time_range,medium),'g',linewidth=1.5,label='medium')
figure3.plot(y_time_range,fuzzy.trapmf(y_time_range,long),'r',linewidth=1.5,label='long')
figure3.set_title('Watering Duration (min)')
figure3.legend()

# plot 2d figures
for fi in (figure1,figure2,figure3):
  fi.spines['top'].set_visible(False)
  fi.spines['right'].set_visible(False)
  fi.get_xaxis().tick_bottom()
  fi.get_yaxis().tick_left()

plt.tight_layout()

if __name__=='__main__':
    plt.show()