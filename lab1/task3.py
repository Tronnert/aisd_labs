import matplotlib.pyplot as plt
import networkx as nx
import random
from task2 import parse_file, simple_binary_tree


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.  
    Licensed under Creative Commons Attribution-Share Alike 

    If the graph is a tree this will return the positions to plot this in a 
    hierarchical layout.

    G: the graph (must be a tree)

    root: the root node of current branch 
    - if the tree is directed and this is not given, 
      the root will be found and used
    - if the tree is directed and this is given, then 
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given, 
      then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vert_gap: gap between levels of hierarchy

    vert_loc: vertical location of root

    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError(
            'cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            # allows back compatibility with nx version 1.11
            root = next(iter(nx.topological_sort(G)))
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width/len(children)
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc-vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


def make_nx_tree(g: nx.Graph, layers, tree, prev, ans):
    if len(tree) == 1:
        id[0] += 1
        labels[id[0]] = f"{ans}\n{tree[0]}"
        g.add_edge(prev, id[0])
    else:
        id[0] += 1
        labels[id[0]] = f"{ans}\n{layers[0]}"
        g.add_edge(prev, id[0])
        cur_id = id[0]
        make_nx_tree(g, layers[1:], tree[0], cur_id, "да")
        make_nx_tree(g, layers[1:], tree[1], cur_id, "нет")


if __name__ == "__main__":
    questions, students = parse_file("lab1\students.csv")
    binary_tree = simple_binary_tree(students)
    G = nx.Graph()
    id = [0]
    labels = {0: questions[0]}
    make_nx_tree(G, questions[1:], binary_tree[0], 0, "да")
    make_nx_tree(G, questions[1:], binary_tree[1], 0, "нет")
    # print(G.edges)
    # print(labels)
    # pos = nx.spring_layout(G, seed=3113794652)
    # nx.draw(G, with_labels=True)
    plt.figure(figsize=(50,6))
    pos = hierarchy_pos(G, 0, width=3)
    nx.draw(G, pos=pos)
    nx.draw_networkx_labels(G, pos, labels, font_size=6, font_color="black")
    plt.show()
