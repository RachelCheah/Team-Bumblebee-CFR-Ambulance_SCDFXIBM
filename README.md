# CFR Ambulance
Our team, consisting of Rachel, Joey, and Shreya, came up with a Non-Emergency Ambulance Service, as an extension of the myResponder App.

## Contents

1. Short Description
2. Pitch Video
3. Architecture of Solution
4. Hyperlink to Detailed Solution
5. Project Roadmap
6. Getting Started
7. Built with

### Short Description

#### What's the Problem?

As of 1st April 2019, SCDF officially announced that it will no longer take non-emergency patients to hospitals in their ambulances. Hoping to focus emergency vehicle manpower allocation on emergency incidents, it ceased this operation. With this, people with non-emergency conditions need to find their own mode of transport to reach the nearest hospital. This is especially difficult for populations such as the elderly, who, when ill, may not be able to travel to a hospital on their own.

#### How can technology help?

Location services technology on smartphones can be used in real-time to share the data with nearby available smartphone users of the situation faced by the non-emergency patient.

#### The idea

SCDF currently uses an app called myResponder to encourage certified Community First Responders (CFRs) to respond to nearby fire and medical cases, and thereby save lives. We propose creating an extended feature of myResponder that alerts nearby certified CFRs of the situation, encouraging them to help transport non-emergency patients to hospitals, should the non-emergency patient require assistance.

### Pitch Video

### Architecture of Solution

#### Procedure when non-emergency patient needs to use service

1. Caller dials 995, verbally explains situation & location, classified as Non-Emergency Patient by SCDF Staff

2. IBM Cloud Speech to Text API converts caller's speech to text

3. IBM Natural Language Understanding API identifies location of caller based on text

4. Google Maps API identifies all available CFRs (users of myResponder app) in 1km radius of location of caller

5. IBM Cloud Notifications API is used to send a push notification to all available CFRs of situation

6. CFR opens notification to app and accepts or rejects job, is given more information accordingly by myResponder app interface

#### Performing data analytics on app feature to make improvements on CFRs demographic

Note: For data analysis, locations in Singapore are split into districts according to [this](https://www.singaporeexpats.com/housing-in-singapore/singapore-district-guide.htm).



1. Collect data on all incidents when a non-emergency patient is redirected by 995 to the CFR Ambulance feature of the my Responder app.

2. Use Python to refine & manipulate raw data to show each District Number's corresponding '% of Successful Responses' and 'Average Number of Available CFRs'

3. Use IBM Watson Studio's Data Visualisation tools to express relationship between each 'District Number' and '% of Successful Responses'.

4.  Use IBM Watson Studio's Data Visualisation tools to express relationship between each 'District Number' and 'Average Number of Available CFRs'

5. Based on the two graphs, identify District Numbers with '% of Successful Responses' < 0.5 OR 'Average Number of Available CFRs' < 1.5. 

These districts are identified to have an insufficient supply of active CFRs, and should attempt to recruit more CFRs accordingly.


### Hyperlink to Detailed Solution

[Click here.](https://github.com/shreyasriram4/Bumblebee-CFR-Ambulance_SCDFXIBM/blob/master/DESCRIPTION.md)

### Project Roadmap

[![Blue-and-Black-Timeline-Presentation.jpg](https://i.postimg.cc/TPnk3r0y/Blue-and-Black-Timeline-Presentation.jpg)](https://postimg.cc/jWd68nGK)

### Getting Started

## Prerequisites

curl -V

### Built with

Flask: to build App Feature

Node-Red: to integrate APIs to App Feature

IBM Cloud Speech to Text Service: to convert 995 call speech to text

IBM Natural Language Understanding API: to identify location of caller

Google Maps API: to identify nearby CFRs

IBM Notifications API: to send notification to identified CFRs

Python: for Data Refinement

IBM Watson Studio: for Data Visualisation





