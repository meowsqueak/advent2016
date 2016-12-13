import argparse
import networkx as nx


def create_node(graph, type, id):
    if type == "bot":
        name = id
        if id not in graph:
            graph.add_node(id, low=None, high=None)
    else:
        assert type == "output"
        name = "output{0}".format(id)
        if name not in graph:
            graph.add_node(name, value=None)
    return name


def add_to_graph(graph, line):
    """bot x gives low to bot y and high to bot z"""
    _, x, _, _, _, y_type, y, _, _, _, z_type, z = line.split()
    x, y, z = [int(x) for x in (x, y, z)]

    x = create_node(graph, "bot", x)
    y = create_node(graph, y_type, y)
    z = create_node(graph, z_type, z)

    graph.add_edge(x, y, type='low')
    graph.add_edge(x, z, type='high')


def add_to_values(values, line):
    """value v goes to bot x"""
    _, value, _, _, _, bot = line.split()
    value, bot = [int(x) for x in (value, bot)]
    values.append((bot, value))


def find_neighbor(graph, bot, type):
    for edge in graph.out_edges_iter(bot, data=True):
        if edge[2]['type'] == type:
            return edge[1]
    return None


def process_bot(graph, bot, value):
    node = graph.node[bot]

    if isinstance(bot, str):
        if node['value'] is None:
            node['value'] = value
    else:
        if node['low'] is None:
            node['low'] = value
        elif node['high'] is None:
            low = node['low']
            node['low'] = min(low, value)
            node['high'] = max(low, value)
            process_bot(graph, find_neighbor(graph, bot, "low"), node['low'])
            process_bot(graph, find_neighbor(graph, bot, "high"), node['high'])


def inject_values(graph, values):
    for bot, value in values:
        process_bot(graph, bot, value)


def find_bot(graph, low, high):
    assert low < high
    for node in graph:
        try:
            if graph.node[node]['low'] == low and graph.node[node]['high'] == high:
                return node
        except KeyError:
            pass
    # not found
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()

    graph = nx.DiGraph()
    values = []

    for line in args.file.readlines():
        if line.startswith("bot "):
            add_to_graph(graph, line)
        elif line.startswith("value "):
            add_to_values(values, line)

    print(sorted(values))

    inject_values(graph, values)

    print(find_bot(graph, 17, 61))

    # part two:
    print(graph.node["output0"]["value"] *
          graph.node["output1"]["value"] *
          graph.node["output2"]["value"])

if __name__ == "__main__":
    main()
