# Lyf-Wire

# Getting Started



This repo contains the files for simulation of two sensors, namely Force sensor and MPU 60501 . 
## Simulation Softwares

We have used Tinkercad to simulate Force Sensor and workwi to simulate MPU 60501 module



## Description Of The Sensors

```
 Force Sensor
 ```
Force sensor is a type of transducer, specifically a force transducer. It converts an input mechanical force such as load, weight, tension, compression or pressure into another physical variable, in this case, into an electrical output signal that can be measured, converted and standardized. As the force applied to the force sensor increases, the electrical signal changes proportionally(From 0 to 1023).

```
 MPU-6050
 ```
MPU-6050 is a 6 axis motion tracking device generally used in smartphones and wearable sensors. It has 3-axis MEMS (Micro-Electro-Mechanical Systems) gyroscope and accelerometer. 
 

## Simulation
**See Simulation of Force Sensor** [here](https://shrt.cx/qC5taD)

![ckt](https://user-images.githubusercontent.com/74849719/159123948-974a8f50-81ae-4c7d-a293-d220533a53a4.JPG)


```
The code for the simulation is given in the repo.
```

If we increase the force beyond a certain threshold, the led light will start glowing. This is a simple demonstration of force sensor. We can also get its electrical signal as output in the serial monitor, which varies from values 0 to 1023.


**See Simulation of MPU-6065** [here](https://wokwi.com/projects/305937156771152449)


```
Upload the files given in the repo to wokwi in order to simulate.
```

![1234](https://user-images.githubusercontent.com/74849719/159123991-edac2640-30d9-487a-b103-a0edd946c2c8.JPG)

This sensor gives the values of acceleration and rotation in three different axes. Alongside it also has a temperature sensor. It plots a graph of acceleration and rotation vs time and the data can be transmitted to cloud via wifi module.













