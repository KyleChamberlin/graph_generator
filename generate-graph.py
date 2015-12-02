import sys
import argparse
import csv
from random import randint

parser = argparse.ArgumentParser(description='graph generator for stops on Santa\'s route.')
parser.add_argument('nodes', help='number of nodes to generate in this graph')
parser.add_argument('cities_file', type=str, help='location of the cities file')

class City:
    def __init__(self, name):
        self.name = name

class Route:
    def __init__(self, stop1, stop2, distance):
        self.stop1 = stop1
        self.stop2 = stop2
        self.distance = distance

def get_cities(file):
    city_list = []
    with open(file) as f:
        reader = csv.reader(f)
        for line in reader:
            if line[0] == 'us':
                city_list.append(line[1])

    return city_list


def create_graph(origin, node_count, city_list):
    edge_list = []
    cities = []

    children_count = 1 if node_count <= 1 else randint(1, 10)

    for i in range(0, children_count):
        name = city_list[randint(0, len(city_list))]
        city = City(name)

        cities.append(city)
        edge_list = edge_list + [Route(origin, city, randint(1,200))]

        if node_count - children_count > 0:
            edge_list = edge_list + create_graph(city, (node_count-children_count)/children_count,city_list)

    for i in range(0, len(cities)):
        for j in range(1, len(cities)):
            if i == 0:
                edge_list = edge_list + [Route(cities[i], cities[j], randint(1,200))]

    return edge_list

if __name__ == "__main__":
    args = parser.parse_args()
    city_list = get_cities(args.cities_file)
    origin = City('North Pole')

    edges = create_graph(origin, int(args.nodes), city_list)
    for edge in edges:
        print "{},{},{}".format(edge.stop1.name, edge.stop2.name, edge.distance)



