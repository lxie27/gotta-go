import Classes
from find_best import find_best

node1 = drop(0)
node2 = drop(0)
node3 = drop(0)
node4 = drop(0)
node5 = drop(0)

truck3 = transporter(node1, node2)
truck2 = transporter(node4, node5)

net = network()

truck10.addDrop(node3)
net.addNode(truck3)
net.addNode(truck2)

closest = find_best(0, net)

#print the closest's posn




