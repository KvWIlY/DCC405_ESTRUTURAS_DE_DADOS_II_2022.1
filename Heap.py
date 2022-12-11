from turtle import right

class PriorityQueue():
    def __init__(self):
        self.size = -1
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * (i + 1)

    def getMax(self):
        return self.heap[0]

    def shiftUp(self, i):
        while (i > 0 and self.heap[self.parent(i)] < self.heap[i]):
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def shiftDown(self, i):
        max_i = i

        left = self.left(i)
        right = self.right(i)

        if left <= self.size and self.heap[left] > self.heap[max_i]: 
            max_i = left

        if right <= self.size and self.heap[right] > self.heap[max_i]: 
            max_i = right

        if i != max_i:
            self.heap[i], self.heap[max_i] = self.heap[max_i], self.heap[i]
            self.shiftDown(max_i)
        
    def extractMax(self):
        result = self.heap[0]

        self.heap[0] = self.heap.pop(-1)
        self.size -= 1

        self.shiftDown(0)

        return result

    def insertKey(self, value):
        self.size += 1
        self.heap.append(value)

        self.shiftUp(self.size)

    def deleteKey(self, i):
        self.heap[i] = self.getMax() + 1
        self.shiftUp(i)
        self.extractMax()

    def changePriority(self, i, new_value):
        old_priority = self.heap[i]
        self.heap[i] = new_value

        if new_value > old_priority:
            self.shiftUp(i)
        else:
            self.shiftDown(i)

    def printPQ(self):
        print("| HEAP | Size = {} | ".format(self.size + 1), end="")
        print(self.heap)

def main():
    pq = PriorityQueue()

    pq.insertKey(90)
    pq.insertKey(3)
    pq.insertKey(2)
    pq.insertKey(1)
    pq.insertKey(85)
    pq.insertKey(80)
    pq.insertKey(75)

    pq.printPQ()

main()