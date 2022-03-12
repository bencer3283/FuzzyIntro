import numpy as np
import skfuzzy as fuzzy
import skfuzzy.control as fuzzyControl
import matplotlib.pyplot as plt

# Range

## range of temp. & soil & watering 
x_temp_range = np.arange(5,40,1,np.float32)
x_humid_range = np.arange(20,90,0.1,np.float32)
y_time_range=np.arange(0,10,1,np.float32)
##　variable and membership functions
x_temp = fuzzyControl.Antecedent(x_temp_range,"temp")
x_humid= fuzzyControl.Antecedent(x_humid_range,"humid")
y_time = fuzzyControl.Consequent(y_time_range,"time")

close = [5, 5, 10, 20]
x_temp["close"] = fuzzy.trapmf(x_temp_range, close)
temp_medium = [10,20,25,35]
x_temp["medium"] = fuzzy.trapmf(x_temp_range, temp_medium)
far = [25,35,40,40]
x_temp["far"] = fuzzy.trapmf(x_temp_range, far)


dry = [20,20,35,50]
x_humid["dry"] = fuzzy.trapmf(x_humid_range,dry)
humid_medium = [35,50,65,80]
x_humid["medium"] = fuzzy.trapmf(x_humid_range, humid_medium)
wet = [65,80,90,90]
x_humid["wet"] = fuzzy.trapmf(x_humid_range, wet)

short = [0,0,1,4]
y_time["short"] = fuzzy.trapmf(y_time_range,short)
medium = [1,4,5,7]
y_time["medium"] = fuzzy.trapmf(y_time_range,medium)
long = [5,7,10,10]
y_time["long"] = fuzzy.trapmf(y_time_range,long)

# Visualize these universes and membership functions
fig,(figure1,figure2,figure3)=plt.subplots(nrows=3,figsize=(8,9))
figure1.plot(x_temp_range,fuzzy.trapmf(x_temp_range, close),'b',linewidth=1.5,label='close')
figure1.plot(x_temp_range,fuzzy.trapmf(x_temp_range,temp_medium),'g',linewidth=1.5,label='medium')
figure1.plot(x_temp_range,fuzzy.trapmf(x_temp_range,far),'r',linewidth=1.5,label='far')
figure1.set_title('Air Temperature Error(C)')
figure1.legend()

figure2.plot(x_humid_range,fuzzy.trapmf(x_humid_range,dry),'b',linewidth=1.5,label='dry')
figure2.plot(x_humid_range,fuzzy.trapmf(x_humid_range,humid_medium),'g',linewidth=1.5,label='medium')
figure2.plot(x_humid_range,fuzzy.trapmf(x_humid_range,wet),'r',linewidth=1.5,label='wet')
figure2.set_title('Moisture (%)')
figure2.legend()

figure3.plot(y_time_range,fuzzy.trapmf(y_time_range,short),'b',linewidth=1.5,label='short')
figure3.plot(y_time_range,fuzzy.trapmf(y_time_range,medium),'g',linewidth=1.5,label='medium')
figure3.plot(y_time_range,fuzzy.trapmf(y_time_range,long),'r',linewidth=1.5,label='long')
figure3.set_title('Compressor Duration (min)')
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