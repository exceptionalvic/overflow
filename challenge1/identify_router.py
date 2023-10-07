"""Identify router with highest number of connection."""
import time

# NOTE: Matplotlib library was not used in
# in actual identify_router function. It is optional to plot
# time complexity graph for demonstration when
# plot_graph is set to True.
import matplotlib.pyplot as plt


class Node:
    """Set outbound and inbound links."""

    def __init__(self, label):
        self.label = label
        self.outbound_links = []
        self.inbound_links = []

    def add_outbound_link(self, node):
        self.outbound_links.append(node)

    def add_inbound_link(self, node):
        self.inbound_links.append(node)

    def __str__(self):
        return str(self.label)


class DirectedGraph:
    """Directed graph of nodes."""

    def __init__(self):
        self.nodes = {}

    def add_node(self, label, connections=0):
        if label not in self.nodes:
            self.nodes[label] = Node(label)
        self.nodes[label].connections = connections

    def add_edge(self, from_label, to_label):
        if from_label in self.nodes and to_label in self.nodes:
            from_node = self.nodes[from_label]
            to_node = self.nodes[to_label]
            from_node.add_outbound_link(to_node)
            to_node.add_inbound_link(from_node)


def identify_router(graph):
    """Identify router with highest number of connections."""
    max_connections = -1
    router_label = None

    for label, node in graph.nodes.items():
        if hasattr(node, "connections"):
            total_connections = node.connections
        else:
            total_connections = len(node.inbound_links) + len(
                node.outbound_links
            )
        if total_connections > max_connections:
            max_connections = total_connections
            router_label = label

    return router_label


def time_complexity_for_identify_router():
    """Computes and plots time complexity of identify_router.

    In this time complexity testing function, nodes are varied from 2 - 100 and the
    time execution complexity computed as node increase.
    Plotted graphical image in PNG format is included
    in root folder.
    """
    execution_times = []

    # Vary the number of nodes from 2 to 100.
    # This is used to test time complexity as a
    # function of increase in input amount/length.
    for num_nodes in range(2, 101):
        network = DirectedGraph()
        for i in range(1, num_nodes + 1):
            network.add_node(i)

        for i in range(1, num_nodes):
            network.add_edge(i, i + 1)

        start_time = time.time()
        # Measure execution time of identify_router.
        identify_router(network)
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)

    return execution_times


def main():
    """Main function.

    Sample connections were included to test function.
    To use, remove sample connection values and use live
    connection value.
    """
    # Creating a directed graph with sample connections
    network = DirectedGraph()
    network.add_node(1, 4)
    network.add_node(2, 6)
    network.add_node(3, 2)
    network.add_node(4, 8)
    network.add_node(5, 3)
    network.add_node(6, 5)

    network.add_edge(1, 2)
    network.add_edge(2, 3)
    network.add_edge(2, 4)
    network.add_edge(3, 1)
    network.add_edge(4, 5)
    network.add_edge(5, 6)
    network.add_edge(6, 1)

    # Identify the router with the most connections
    start_time = time.time()  # records start time
    router = identify_router(network)
    end_time = time.time()  # record end_time

    execution_time = end_time - start_time
    """Time complexity of the identify_function is recorded as
    execution_time. 
    
    The higher the number of nodes, the longer the execution_time.
    A graph of execution time complexity can be plotted.
    To plot graph, set plot_graph to True.
    """
    print(
        f"The router with the most connections is:  {router}; Execution Time: {execution_time:.4f}"
    )

    # Toggle graph plotting for time complexity illustration.
    plot_graph = True

    if plot_graph:
        execution_times = time_complexity_for_identify_router()

        # Plot the execution time complexity graph
        # This graph attached shows how execution time
        # increases with increased nodes.
        num_nodes = range(2, 101)
        plt.plot(num_nodes, execution_times, marker="o", linestyle="-")
        plt.xlabel("Number of Nodes")
        plt.ylabel("Execution Time (seconds)")
        # Plot the graphical explanation.
        plt.title(
            "This Grpah Explains Execution Time Complexity of identify_router Function"
        )
        plt.grid(True)
        plt.show()

    if __name__ == "__main__":
        main()
