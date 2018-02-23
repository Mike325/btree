#!/usr/bin/env python

__header__ = """
                              -`
              ...            .o+`
           .+++s+   .h`.    `ooo/
          `+++%++  .h+++   `+oooo:
          +++o+++ .hhs++. `+oooooo:
          +s%%so%.hohhoo'  'oooooo+:
          `+ooohs+h+sh++`/:  ++oooo+:
           hh+o+hoso+h+`/++++.+++++++:
            `+h+++h.+ `/++++++++++++++:
                     `/+++ooooooooooooo/`
                    ./ooosssso++osssssso+`
                   .oossssso-````/osssss::`
                  -osssssso.      :ssss``to.
                 :osssssss/  Mike  osssl   +
                /ossssssss/   8a   +sssslb
              `/ossssso+/:-        -:/+ossss'.-
             `+sso+:-`                 `.-/+oso:
            `++:.                           `-/+/
            .`                                 `/
"""


class BNode(object):
    """Node for the Btree"""

    def __init__(self, node=None, capacity=2):
        super(BNode, self).__init__()
        self.elements = node if node is not None else []
        self.capacity = 2

    def insert(self, element):
        """Insert new object into the object

        :element: TODO
        :returns: TODO

        """
        pass

    def remove(self, element):
        """Remove the given object from the node

        :element: TODO
        :returns: TODO

        """
        pass

    def update(self, element, value):
        """Update the value of a given object

        :element: TODO
        :value: TODO
        :returns: TODO

        """
        pass

    def link_index(self, element):
        """Return the link index that should be assign to the given element

        :element: Element, outside the node, that is being compare to all given
                  elements in the node to give an index
        :returns: int: The index of the pointing to the new node

        """
        pass

    def full(self):
        """TODO: Docstring for full.
        :returns: bool: True if the node is full, False otherwise

        """
        return (len(self.elements) == (self.capacity * 2 - 1))

    def min(self, root=False):
        """Return whether or not the node has the minimun size

        :root: TODO
        :returns: bool: True if the node has the minimun elements, False otherwise

        """
        return (len(self.elements) <= self.capacity)


class BTree(object):
    """BTree data structure implementation"""

    def __init__(self, btree=None, size=2):
        super(BTree, self).__init__()
        self.root = btree
        self.size = size

    def __str__(self):
        """String representation of the tree
        :returns: String representation of the tree

        """
        pass

    def _divide(self):
        """Divide nodes as part of the insertion process
        :returns: TODO

        """
        pass

    def _merge(self):
        """Merge two nodes as part of the deletion process
        :returns: TODO

        """
        pass

    def _promote(self, node):
        """Promote a node to its parent

        :node: TODO
        :returns: TODO

        """
        pass

    def _demote(self, node):
        """Demote a node to one of its children

        :node: TODO
        :returns: TODO

        """
        pass

    def _delete_leaf(self, node):
        """Remove a leaf from the BTree

        :node: TODO
        :returns: TODO

        """
        pass

    def _exchange(self, target, leaf):
        """Change the position of a node to a leaf

        :target: TODO
        :leaf: TODO
        :returns: TODO

        """
        pass

    def _delete_inner_node(self, node):
        """Remove a inner element from a node

        :node: TODO
        :returns: TODO

        """
        pass

    def insert(self, node):
        """Insert an element in the tree

        :node: TODO
        :returns: bool: True if insertion was successful, False otherwise

        """
        pass

    def delete(self, node):
        """remove a node from the tree

        :node: todo
        :returns: Node: Returns the deleted node if it exists in the tree, None otherwise

        """
        pass

    def search(self, node):
        """Search for node inside the tree

        :node: TODO
        :returns: Node: Returns the Node if it exists in the tree, None otherwise

        """
        pass

    def update(self, node, value):
        """Update the value of a node

        :node: TODO
        :value: TODO
        :returns: True if the node was updated, False otherwise

        """
        pass


if __name__ == "__main__":
    raise Exception("This module can't run by its own")
