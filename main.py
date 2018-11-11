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

net_posns = []
for n in range(net.couriers):
	truck = Client(key)
	transp_posn = []
	transp_posn = truck.geolocate(key)['location'][0]['lat']
	transp_posn = truck.geolocate(key)['location'][0]['lng']
	n.updatePosn(transp_posn)
	net_posns.append(transp_posn)

# gets the distance of all vehicles from the user
vehicles_dist = []
vehicles_dist = user.distance_matrix(user_posn, net_posns)

count = 0
shortest = int(vehicles_dist[0]['rows']['elements']['distance']['text'].split(' ')[0])

# determines which vehicle is closest to the user
closest = 0
for v in range(len(vehicles_dist)):
	count = count + 1
	if int(v[0]['rows']['elements']['distance']['text'].split(' ')[0]) < shortest:
		closest = count
		shortest = int(v[0]['rows']['element']['distance']['text'].split(' ')[0])


# get the directions from the selected vehicle to the user
distance = shortest
while(distance > 100):
	userInstruction = user.directions(user_posn, net_posns['closest'])['routes']
	toUser = user.directions(net_posns['closest'], user_posn)['routes']
	distance = userDestination['routes']['legs']['duration']['value']



