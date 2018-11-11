# gotta-go
Boston Hacks 2018 submission

Gotta-go network of transporters carrying private, personal, and modular restrooms.
The network handles coordination of transporters. Implementation of user requests and recovery of used restrooms requires the Google Maps API, specifically Geolocation for dynamically tracking both vehicle and user movement. The Distance Matrix and Directions APIs are used to calculate distances, and implementation of a GUI using Google Places to generate a dynamic map will be coming in the future.

The network is populated with nodes and transporters in a Python Dictionary, a hashtable to enable constant time functions.

The framework of the network is as follows:

A network, made of transporters, which have slots for drops.


Compile with:   python main.py
