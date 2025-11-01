import urllib.request

class Node:
    def __init__(self, word: str):
        self.word = word
        self.left = None
        self.right = None


class BST:
    def __init__(self, url: str):
        self.root = None
        self.results = []
        self._load_from_url(url)

    def _load_from_url(self, url: str):
        response = urllib.request.urlopen(url)
        data = response.read().decode("utf-8")
        words = [w.strip() for w in data.splitlines() if w.strip()]
        self.root = self._build_balanced_bst(words)

    def _build_balanced_bst(self, words):
        if not words:
            return None
        mid = len(words) // 2
        node = Node(words[mid])
        node.left = self._build_balanced_bst(words[:mid])
        node.right = self._build_balanced_bst(words[mid + 1:])
        return node

    def autocomplete(self, prefix: str):
        self.results = []
        self._collect(self.root, prefix)
        return self.results

    def _collect(self, node: Node, prefix: str):
        if node is None:
            return
        self._collect(node.left, prefix)
        if node.word.startswith(prefix):
            self.results.append(node.word)
        self._collect(node.right, prefix)
