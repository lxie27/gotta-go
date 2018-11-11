from Classes import network
from Classes import transporter
from Classes import drop
from find_best import find_best
from key import key
from googlemaps import *

node1 = drop()
node2 = drop()
node3 = drop()
node4 = drop()
node5 = drop()

truck3 = transporter(node1, node2)
truck2 = transporter(node4, node5)

net = network()

net.addNode(truck3)
net.addNode(truck2)

user = Client(key)

#simulation loop

user_posn = []
user_posn['lat'] = user.geolocate(key)['location'][0]['lat']
user_posn['lng'] = user.geolocate(key)['location'][0]['lng']

print(user_posn['lat'])

# gets the distance of all vehicles from the user
vehicles_dist = []
vehicles_dist = user.distance_matrix(user_posn, net_posns)

count = 1
shortest = int(vehicles_dist[0]['rows']['elements']['distance']['text'].split(' ')[0])


closest = 0
for v in range(len(vehicles_dist)):
	if int(v[0]['rows']['elements']['distance']['text'].split(' ')[0]) < shortest:
		closest = count
		shortest = v
		count = count + 1

# get the directions from the selected vehicle to the user
distance = shortest
while(duration > 30):
	userDestination = user.directions(user_posn, net_posns[closest])[routes]
	toUser = user.directions(net_posns[closest], user_posn)[routes]
	duration = userDestination[routes][legs][duration][value]

