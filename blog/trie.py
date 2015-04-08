# -*- coding: utf-8 -*-

class TrieNode:
    __slots__ = ('valid', 'children')

    def __init__(self):
        self.valid = False
        self.children = {}

    def setValid(self, bValue):
        self.valid = bValue

    def getValid(self):
        return self.valid

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.setValid(True)

    def delete(self, word):
        node = self.root
        pnode = None
        ch = None

        for c in word:
            if c not in node.children:
                return False

            if len(node.children):
                pnode = node
                ch = c
                    
            node = node.children[c]

        if not node.getValid():
            return False

        if len(node.children):
            node.setValid(False)
        else:
            del pnode.children[ch]
        return True

    def match(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

            if node.getValid():
                return True

        return False
