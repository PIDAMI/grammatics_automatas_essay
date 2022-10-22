import pydot

def first_example_trees_1():
    graph = pydot.Dot("g1_1", graph_type="graph", bgcolor="white")

    graph.add_node(pydot.Node("a", label="E"))

    # Or, without using an intermediate variable:
    graph.add_node(pydot.Node("b", label="E"))
    graph.add_node(pydot.Node("prod", label="*", color="red"))
    graph.add_node(pydot.Node("c", label="E"))
    
    
    graph.add_edge(pydot.Edge("a", "b", color="blue"))
    graph.add_edge(pydot.Edge("a", "prod", color="blue"))
    graph.add_edge(pydot.Edge("a", "c", color="blue"))

    graph.add_node(pydot.Node("cx", label="a", color="red"))
    graph.add_edge(pydot.Edge("c", "cx", color="blue"))

    
    graph.add_node(pydot.Node("d", label="E"))
    graph.add_node(pydot.Node("sum", label="+", color="red"))
    graph.add_node(pydot.Node("e", label="E"))


    graph.add_edge(pydot.Edge("b", "e", color="blue"))
    graph.add_edge(pydot.Edge("b", "sum", color="blue"))
    graph.add_edge(pydot.Edge("b", "d", color="blue"))


    graph.add_node(pydot.Node("ex", label="a", color="red"))
    graph.add_edge(pydot.Edge("e", "ex"))

    graph.add_node(pydot.Node("dx", label="a", color="red"))
    graph.add_edge(pydot.Edge("d", "dx"))
    
    return graph

def first_example_trees_2():
    graph = pydot.Dot("g1_2", graph_type="graph", bgcolor="white")

    graph.add_node(pydot.Node("a", label="E"))

    # Or, without using an intermediate variable:
    graph.add_node(pydot.Node("b", label="E"))
    graph.add_node(pydot.Node("sum", label="+", color="red"))
    graph.add_node(pydot.Node("c", label="E"))
    
    
    graph.add_edge(pydot.Edge("a", "b", color="blue"))
    graph.add_edge(pydot.Edge("a", "sum", color="blue"))
    graph.add_edge(pydot.Edge("a", "c", color="blue"))

    graph.add_node(pydot.Node("bx", label="a", color="red"))
    graph.add_edge(pydot.Edge("b", "bx", color="blue"))

    
    graph.add_node(pydot.Node("d", label="E"))
    graph.add_node(pydot.Node("prod", label="*", color="red"))
    graph.add_node(pydot.Node("e", label="E"))


    graph.add_edge(pydot.Edge("c", "e", color="blue"))
    graph.add_edge(pydot.Edge("c", "prod", color="blue"))
    graph.add_edge(pydot.Edge("c", "d", color="blue"))


    graph.add_node(pydot.Node("ex", label="a", color="red"))
    graph.add_edge(pydot.Edge("e", "ex"))

    graph.add_node(pydot.Node("dx", label="a", color="red"))
    graph.add_edge(pydot.Edge("d", "dx"))
    
    return graph


def second_example():
    graph = pydot.Dot("g2", graph_type="graph", bgcolor="white")

    graph.add_node(pydot.Node("a", label="E"))

    # Or, without using an intermediate variable:
    graph.add_node(pydot.Node("b", label="E"))
    graph.add_node(pydot.Node("prod", label="*", color="red"))
    graph.add_node(pydot.Node("c", label="T"))
    
    graph.add_edge(pydot.Edge("a", "b", color="blue"))
    graph.add_edge(pydot.Edge("a", "prod", color="blue"))
    graph.add_edge(pydot.Edge("a", "c", color="blue"))


    graph.add_node(pydot.Node("cx", label="a", color="red"))
    graph.add_edge(pydot.Edge("c", "cx", color="blue"))

    
    graph.add_node(pydot.Node("d", label="E"))
    graph.add_node(pydot.Node("sum", label="+", color="red"))
    graph.add_node(pydot.Node("e", label="T"))


    graph.add_edge(pydot.Edge("b", "e", color="blue"))
    graph.add_edge(pydot.Edge("b", "sum", color="blue"))
    graph.add_edge(pydot.Edge("b", "d", color="blue"))


    graph.add_node(pydot.Node("ex", label="a", color="red"))
    graph.add_edge(pydot.Edge("e", "ex"))

    graph.add_node(pydot.Node("dx", label="T"))
    graph.add_edge(pydot.Edge("d", "dx"))

    graph.add_node(pydot.Node("dxx", label="a", color="red"))
    graph.add_edge(pydot.Edge("dx", "dxx"))
    

    return graph


def third_example():
    graph = pydot.Dot("g2", graph_type="graph", bgcolor="white")

    graph.add_node(pydot.Node("a", label="E"))

    # Or, without using an intermediate variable:
    graph.add_node(pydot.Node("b", label="E"))
    graph.add_node(pydot.Node("sum", label="+", color="red"))
    graph.add_node(pydot.Node("c", label="T"))
    
    graph.add_edge(pydot.Edge("a", "b", color="blue"))
    graph.add_edge(pydot.Edge("a", "sum", color="blue"))
    graph.add_edge(pydot.Edge("a", "c", color="blue"))


    graph.add_node(pydot.Node("bx", label="T"))
    graph.add_edge(pydot.Edge("b", "bx", color="blue"))
    graph.add_node(pydot.Node("bxx", label="F"))
    graph.add_edge(pydot.Edge("bx", "bxx", color="blue"))
    graph.add_node(pydot.Node("bxxx", label="a", color="red"))
    graph.add_edge(pydot.Edge("bxx", "bxxx", color="blue"))
    

    
    graph.add_node(pydot.Node("d", label="T"))
    graph.add_node(pydot.Node("prod", label="*", color="red"))
    graph.add_node(pydot.Node("e", label="F"))


    graph.add_edge(pydot.Edge("c", "e", color="blue"))
    graph.add_edge(pydot.Edge("c", "prod", color="blue"))
    graph.add_edge(pydot.Edge("c", "d", color="blue"))


    graph.add_node(pydot.Node("ex", label="a", color="red"))
    graph.add_edge(pydot.Edge("e", "ex"))

    graph.add_node(pydot.Node("dx", label="F"))
    graph.add_edge(pydot.Edge("d", "dx"))

    graph.add_node(pydot.Node("dxx", label="a", color="red"))
    graph.add_edge(pydot.Edge("dx", "dxx"))
    
    return graph


def orgraph_example():
    graph = pydot.Dot("g1_1", graph_type="digraph", bgcolor="white")

    a = pydot.Node("a", label="E")
    b = pydot.Node("b", label="E + E")
    ab = pydot.Edge(src=a, dst=b, color="blue")
    # Or, without using an intermediate variable:
    graph.add_node(a)
    graph.add_node(b)

    graph.add_edge(ab)


    graph.add_node(pydot.Node("c", label="a + E"))
    graph.add_edge(pydot.Edge("b", "c", color="blue"))
    
    graph.add_node(pydot.Node("d", label="a + E * E"))
    graph.add_edge(pydot.Edge("c", "d", color="blue"))

    graph.add_node(pydot.Node("e", label="a + a * E"))
    graph.add_edge(pydot.Edge("d", "e", color="blue"))

    graph.add_node(pydot.Node("f", label="a + a * a", color="red"))
    graph.add_edge(pydot.Edge(src="e", dst="f", color="blue"))


    graph.add_node(pydot.Node("c2", label="E + E * E"))
    graph.add_edge(pydot.Edge("b", "c2", color="blue"))
    
    graph.add_node(pydot.Node("d2", label="E + E * a"))
    graph.add_edge(pydot.Edge("c2", "d2", color="blue"))

    graph.add_node(pydot.Node("e2", label="E + a * a"))
    graph.add_edge(pydot.Edge("d2", "e2", color="blue"))

    graph.add_node(pydot.Node("f2", label="a + a * a", color="red"))
    graph.add_edge(pydot.Edge("e2", "f2", color="blue"))


    return graph


def first_example_trees():
    return first_example_trees_1(), first_example_trees_2()

# t1,t2 = first_example_trees()

# t1.write_png("ex1_t1.png")
# t2.write_png("ex1_t2.png")

# g2_tree = second_example()
# g2_tree.write_png("ex2.png")


# g3_tree = third_example()
# g3_tree.write_png("ex3.png")

orgraph = orgraph_example()
orgraph.write_png("orgraph.png")