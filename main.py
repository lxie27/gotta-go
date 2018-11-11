from Classes import network
from Classes import transporter
from Classes import drop
from find_best import find_best
import googlemaps
from key import key

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

user.setUp()
user_posn = []
user_posn['lat'] = user.geolocate()['location'][0]['lat']
user_posn['lng'] = user.geolocate()['location'][0]['lng']

print(user_posn['lat'])
