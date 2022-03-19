# Lyf-Wire

	
                                           SENSORS USED IN THE IOT DEVICE



->Wemos D1 mini board: uploads tested value to cloud storage and extracts to local database

->Force Sensor (FSR402): located at the front of the knee
->IMU MPU-60501: located at the inside or outside of the knee
->WiFi MCU


IMPLEMENTATION

The main algorithm of device code is in Arduino loop(). The steps consist of the following methods. 
1.Read the angle of MPU6050. 
2.when the angles are changed, the data of the force sensor are retrieved through analog read (A0). 
3.payload messages are created for transfer to the Cloud server while the data structure contains: -device_id is device identification number. -rawGyroXAxis is the value of the changed angle from the X axis. -rawGyroYAxis is the value of the changed angle from the Y axis. -rawGyroZAxis is the value of the changed angle from the Z axis. -forceSensorValue is data that is received from a force sensor. -token is a permitted value from writing to Cloud. 
4.“push_data()” is a command that is used for sending data to Cloud.

Here we have simulated two sensors 
1.Force Sensor: We have shown the implementation of this sensor using an led light. The light gets switched on after it crosses a certain threshold limit(700 in computer limits). The force is also shown as an output in the serial monitor. We have simulated our code and circuit in tinkercad

2. MPU-60501: This is a combinationn of three sensors , namely accelerometer, gyroscope and temperature sensor .

