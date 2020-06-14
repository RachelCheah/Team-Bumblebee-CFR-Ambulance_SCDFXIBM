# Proposed CFR Ambulance Service in myResponder App
Our group would like to propose a new feature in myResponder app that would alert certified CFRs if there is a non-emergency patient nearby that requires transport to the hospital. 

Step 1: Obtaining address of patient

When a case is classified as a non-emergency case by a SCDF staff,the details given by the caller through the call will be processed by Node RED which uses IBM cloud's speech to text to convert the speech to an address in text. The address given, now in text, will go through IBM Natural Language Understanding API for the system to identify the location coordinates. 

[![Step1.png](https://i.postimg.cc/KKMVJvzb/Step1.png)](https://postimg.cc/KKMVJvzb)
Step 2: Finding CFRs

The location coordinates will be used by Google Maps API to search for all nearby available CFRs that are of 1km radius of the location. Upon identifying the CFRs, a notification will be sent out to these users by IBM Cloud Notifications API regarding the situation. If a CFR were to accept, more information such as the detailed address and patient's name will be provided in the app. The patient will be notified of the CFR's car license plate number.

Results: 

Our group hopes that through this service,the community will not have to worry about transport in the event where they need medical aid but do not have access to transport.

