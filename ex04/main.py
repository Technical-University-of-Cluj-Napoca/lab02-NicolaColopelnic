from BST import BST
from search_engine import search_loop

def main():

    bst = BST("https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words.txt")
    search_loop(bst)

if __name__ == "__main__":
    main()
