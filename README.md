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











# Table of Contents

- [Getting Started](#getting-started)
    - [Setting up softwares](#setting-up-softwares)
    - [Setting up git](#setting-up-git)
    - [Forking and Cloning](#forking-and-cloning)
    - [Making branches](#making-branches)
    - [Editing files](#editing-files)
    - [Adding and commiting changes](#adding-and-commiting-changes)
    - [Pushing changes and submitting a Pull Request](#pushing-changes-and-submitting-a-pull-request)
- [Resources](#resources)
- [Rules and Scoring System](#rules-and-scoring-system)
- [FAQ](#faq)

# Getting Started



This repo contains the files for simulation of two sensors, namely Force sensor and MPU 60501 . 
## Simulation softwares

We have used Tinkercad to simulate Force Sensor and workwi to simulate MPU 60501 module



## Description of The sensors


    - [Force Sensor]:
Force sensor is a type of transducer, specifically a force transducer. It converts an input mechanical force such as load, weight, tension, compression or pressure into another physical variable, in this case, into an electrical output signal that can be measured, converted and standardized. As the force applied to the force sensor increases, the electrical signal changes proportionally(From 0 to 1023).
    - [Forking and Cloning](#forking-and-cloning)
    - [Making branches](#making-branches)
    - [Editing files](#editing-files)


```
git clone [copied url here]
```

That should download the repo locally.

## Making branches

A **branch** is a parallel copy of the code. When we add new features to a project, we usually create a copy of the code and work on it. This is done so that the main working copy of the code is unaffected. In most GitHub repos, the master branch is the default branch. You should create a separate branch for every contribution you make. To create a new branch, execute this command:

```
git checkout -b [branch name here]
```

You should see the branch name change on the terminal prompt. Congratulations! You created a new branch.


## Editing files

Create a new text file in the [contributors](contributors/) folder with your github handle as the file name. This file should contain your name. A sample file [s-ayush2903.txt](https://github.com/NJACKWinterOfCode/Get-Started-NWoC20/blob/main/contributors/s-ayush2903.txt) has been provided.

## Adding and commiting changes

To create a **commit** means to save your work. But before you commit, you have to **add** your work to the commit. To do so, execute this command from the project root:

```
git add *
```

This adds all files to the upcoming commit. Now, to create the commit run this command:

```
git commit -m "[commit message here]"
```

Write any message in place of the commit message. If the command runs successfully, you should have committed your changes.

## Pushing changes and submitting a Pull Request

After committing your changes, you have to upload them to GitHub. This is known as **pushing**. To push your changes, run:

```
git push origin [branch name]
```

Where branch name is the name of your newly created branch. This should upload your changes to *your* GitHub account. Now, you can propose these changes to the actual project. To do so, click on the **Pull Request** button on GitHub. Most of the fields should be automatically filled out for you. Click Create Pull Request. If everything went correctly, you should have created a pull request with your changes. Now it is upto the repo owner to **merge** these changes.

Congratulations! You made your first Open Source Contribution! Now contribute to some other repos on NWoC. Have a great time!

# Resources

You can learn more about Git and GitHub here:

- https://www.youtube.com/watch?v=w3jLJU7DT5E
- https://codeburst.io/a-step-by-step-guide-to-making-your-first-github-contribution-5302260a2940

# Rules and scoring system

- **1 point** for contributing to this repo by adding a file, namely [YourGitHubUsername].txt which contains your name, to the [contributors](contributors) folder.
- **2 points** for opening a legitimate issue in any of the projects announced for NWoC.
- **5 points** for solving an issue labelled *“Beginner”*.
- **10 points** for solving an issue labelled *“Intermediate”*.
- **15 points** for solving an issue labelled *“Difficult”*.
- In case of equal scores, the one who has solved more number of difficult issues will be given priority.
- In case of any disputes/discrepancies, the final decision shall be taken by the mentors of the respective projects.


**Some other important points:**

- Any contributions made prior to the beginning of the coding period (1st December) will NOT be counted towards the final score.
- Students should NOT review other student’s Pull Requests under any circumstances. Let the mentors alone review the Pull Requests.
- Please try to Google your doubts before directly contacting mentors or posting on the Gitter channel itself.


# FAQ

1. **I have exams till mid-December. What to do? Can I still participate?**  
Yes, definitely! You can register anytime during the entire duration of the program and start contributing to the various projects. It is never late to contribute to the projects :-)

1. **What prizes shall I receive?**  
Apart from a digital certificate from NJACK IIT Patna, whatever merchandise and some swags we obtain from the sponsors, would be distributed among the active contributors. 

    **Letter of Recommendation (LoRs) from NJACK, IIT Patna can be provided to the top and active contributors on review of their work.**

    However, we would like to emphasise on the fact that this is more of a program to encourage Open Source, rather than a contest. So, your aim should be to learn along with the community and enjoy working on the projects, rather than to compete to get to the top. Cheers :-)

1. **Which language should I know to participate in NWoC?**  
We will try to include projects in almost all common programming languages. However, you will have to work with Git and GitHub to contribute to any of the projects. You can learn to use these during NWoC itself, or you can start learning them from https://classroom.udacity.com/courses/ud775.


