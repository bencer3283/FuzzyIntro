# Getting started
This program is written fully in Python. Necessary packages are listed in `packages.txt`. If you use conda as python package and environment manager, install required packages by running the following command in your terminal.
```
$ conda create --name <env> --file packages.txt
```

## Programs
- Member functions are defined in `memberFunction.py`, run this file to see the member function graph.
- Run `defuzzification.py` to test the control system by enter air temp. and soil moisture. Enter "exit" to leave the control system.
- Run `drawSurface.py` to check out the performance graph. 

# The initial settings
Roll back to [this commit](https://github.com/bencer3283/FuzzyIntro/tree/f8c130db03f7717e3be07e111ea787a6a3fa1187) for initial MF parameters (defined in `memberFeunction.py`). 
## Member function
![](graphs/iniMF.png)

## Some case test
### Extreme end of universe:
At the extreme end the time seems to go to the same value of ~2.8.
- Temp: -5, Soil: 0
    - Time: 2.8000000145037967
- Temp: -5, Soil: 100
    - Time: 2.8000000145037967
- Temp: 45, Soil: 0
    - Time: 24.55555552181113
- Temp: 45, Soil: 100
    - Time: 2.8000000145037967
### Extreme end of each MF:
Watering time seems wiredly low at end of MFs.
- Temp: 10, Soil: 50
    - Time: 3.523809523809524
- Temp: 8, Soil: 50
    - Time: 3.4352941244359383
- Temp: 20, Soil: 17
    - Time: 12.499999999999998
- Temp: 32, Soil: 100
    - Time: 3.187096760318533
- Temp: 35, Soil: 66
    - Time: 12.44622626691289

### MF overlaps: 
It seems like the system hesitate to raise watering time too much.
- Temp: 9, Soil: 30
    - Time: 11.104804798990116
- Temp: 19, Soil: 74
    - Time: 10.353458111049935
- Temp: 27, Soil: 30
    - Time: 17.0306432075052

## Performance surface
Some problems observed here:
1. Watering time seems overwhelmingly dominated by soil moisture.
1. The control system hesitate too much to raise watering time.
2. Some cutoffs are clearly too sharp. 
![](graphs/initPS.png)

# The revised settings
The current version. Following modifitaions made:
- Increased overlap to reduce sharp cutoff.
- Increasde range of normal and above temperature.
- Increased membership towards longer time.
- Rules are modified. Cool & moist is added to medium.
## Member function
![](graphs/newMF.png)

## Some case test
### Extreme end of universe:
Not much difference here, extreme cold/wet case still always leads to low watering.
- Temp: -5, Soil: 0
    - Time: 3.307692321564789
- Temp: -5, Soil: 100
    - Time: 3.307692321564789
- Temp: 45, Soil: 0
    - Time: 24.399999996473394
- Temp: 45, Soil: 100
    - Time: 3.307692321564789

### Extreme end of each MF:
These middle range ends of MF all seems to yeild middle range watering.
- Temp: 13, Soil: 46
    - Time: 13.39862544732253
- Temp: 20, Soil: 35
    - Time: 13.120765718985432
- Temp: 15, Soil: 66
    - Time: 13.349196021984913
- Temp: 32, Soil: 66
    - Time: 12.869082115105352
- Temp: 32, Soil: 46
    - Time: 12.951948050753762

### MF overlaps:
All resulting watering are a bit higher.
- Temp: 9, Soil: 30
    - Time: 9.19252148304985
- Temp: 19, Soil: 74
    - Time: 12.212077396151347
- Temp: 27, Soil: 30
    - Time: 18.604120117725422

## Performance surface
The steep cutoff are removed. High watering regions are increased.
![](graphs/newPS.png)