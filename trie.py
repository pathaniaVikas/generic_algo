class Node:
    __slots__ = ['dict']
    def __init__(self):
        self.dict= {}

class value:
    __slots__ = ['isLast', 'word_count', 'next']
    def __init__(self):
        self.next = None
        self.isLast = 0
        self.word_count = 1

root = None

def insert(word):
    global root
    node = root
    previous_char = ''
    previous_node = None
    for w in word:
        if node:
            if node.dict.get(w):
                previous_node = node
                node.dict[w].word_count = node.dict[w].word_count + 1
                node = node.dict[w].next
            else:
                val = value()
                node.dict[w] = val
                previous_node = node
                node = None
        else:
            node = Node()
            val = value()
            node.dict[w] = val
            if previous_node:
                val_prev = previous_node.dict[previous_char]
                val_prev.next = node
            if not root:
                root = node
            previous_node = node
            node = None

        previous_char = w
        

    previous_node.dict[word[len(word)-1]].isLast = 1

def search(word):
    node = root
    parent_node = None
    for w in word:
        if node:
            if node.dict.get(w):
                parent_node = node
                node = node.dict[w].next
            else:
                return 0
        else:
            return 0
        
    return parent_node.dict[word[len(word)-1]].word_count


if __name__ == '__main__':

    N = int(input().strip())

    while N:
        op = input()

        if op[0] == 'a':
            word = op[4:len(op)]
            insert(word)
        else:
            word = op[5:len(op)]
            print(search(word))
        N = N-1
    # insert('to')
    # insert('tea')
    # insert('ted')
    # insert('ten')
    # insert('i')
    # insert('in')
    # insert('inn')

    # print(search('tea'))
    # print(search('t'))
    # print(search('te'))
    # print(search('teas'))