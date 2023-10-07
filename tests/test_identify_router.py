"""Test cases for identify_router."""
import pytest
from challenge1.identify_router import DirectedGraph, identify_router


def test_identify_router_simple():
    """Test case 1.

    Testing with a simple network where router 2 has the most connections.
    """
    network = DirectedGraph()
    network.add_node(1, 2)
    network.add_node(2, 3)
    network.add_node(3, 1)

    network.add_edge(1, 2)
    network.add_edge(2, 3)
    network.add_edge(3, 1)

    result = identify_router(network)
    assert result == 2  # router 2 should have the most connections


def test_identify_router_complex():
    """Test case 2.

    Testing with a simple network where router 4 has the most connections.
    """
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

    result = identify_router(network)
    assert result == 4  # router 4 should have the most connections


def test_identify_router_empty_network():
    """Test case 3.

    Testing with an empty network, result should be None
    """
    network = DirectedGraph()

    result = identify_router(network)
    # The network is empty, so the result should be None
    assert result is None


if __name__ == "__main__":
    pytest.main()
