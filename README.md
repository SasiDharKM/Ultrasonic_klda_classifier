# Ultrasonic_klda
Contains our pattern recognition project files, which is about performing a dimensional reduction using the KLDA technique and performing a classification by employing a probabilistic approach.

The operations are performed on a dataset named "Ultrasonic flowmeter diagnostics Data Set" hosted in the UCI Machine Learning Repository.

The Dataset can be found [here](https://archive.ics.uci.edu/ml/datasets/Ultrasonic+flowmeter+diagnostics).

Some details regarding the dataset:

Task to be done | Classification
----|----
Count of data available | 540

The data is collected from four different ultrasonic flow meters(USM) named Meter A, Meter B, Meter C, and Meter D are separated into four different files.
The Attributes collected for the different meters also differs.

### **Meter A** 

The data is collected from a 8-path USM.

Data Count | 87
---|---
Number of Attributes | 37
Number of Classes | 2
Class '1' | Healthy
Class '2' | Installation effects (mostly defects)

Attribute Information:

Columns | Attribute
---|---
 1 | Flatness ratio 
 2 | Symmetry
 3 | Crossflow
 4-11 | Flow velocity in each of the eight paths 
 12-19 | Speed of sound in each of the eight paths 
 20 | Average speed of sound in all eight paths 
 21-36 | Gain at both ends of each of the eight paths 
 37 | Class Attribute (1,2)
 

### **Meter B** 

The data is collected from a 4-path USM.

Data Count | 92
---|---
Number of Attributes | 52
Number of Classes | 3
Class '1' | Healthy
Class '2' | Gas Injection 
Class '3' | Waxing

Attribute Information:

Columns | Attribute
---|---
 1 | Flatness ratio 
 2 | Symmetry
 3 | Crossflow
 4 | Swirl angle 
 5-8 | Flow velocity in each of the four paths 
 9 | Average flow velocity in all four paths  
 10-13 | Speed of sound in each of the four paths 
 14 | Average speed of sound in all four paths 
 15-22 | Signal strength at both ends of each of the four paths 
 23 -26 | Turbulence in each of the four paths 
 27 | Meter performance 
 28-35 | Signal quality at both ends of each of the four paths 
 36-43 | Gain at both ends of each of the four paths  
 44-51 | Transit time at both ends of each of the four paths 
 52 | Class Attribute (1,2,3)
 

### **Meter C and Meter D**

The data collected for both the meters is from from a 4-path USM.

Data Count for Meter C | 181
---|---
Data Count for Meter D | 180

The attributes of Meter C and Meter D is the same.

Number of Attributes | 44
---|---
Number of Classes | 4
Class '1' | Healthy
Class '2' | Gas Injection 
Class '3' | Installation effects (mostly defects)
Class '4' | Waxing

Attribute Information:

Columns | Attribute
---|---
 1 | Flatness ratio 
 2 | Symmetry
 3 | Crossflow
 4-7 | Flow velocity in each of the four paths 
 8-11 | Speed of sound in each of the four paths 
 12-19 | Signal strength at both ends of each of the four paths 
 20-27 | Signal quality at both ends of each of the four paths 
 28-35 | Gain at both ends of each of the four paths 
 36-43 | Transit time at both ends of each of the four paths 
 44 | Class attribute (1,2,3,4)

### Running the codes
To run the codes, please install the requisite packages from the requirements.txt provided. \
This can be done as follows
```bash
pip install -r requirements.txt
```
Please make sure you have python and python-pip installed in your system first though

