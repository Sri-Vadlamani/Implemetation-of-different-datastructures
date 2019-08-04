import hashlib
from datetime import datetime

#Block class to represent a block and calc_hash() function to calculate hash
class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)

    def calc_hash(self, data):
      sha = hashlib.sha256()
      hash_str = data.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.next = self.head
        else:
            temp = self.next.hash
            self.next = Block(timestamp, data, temp)
            self.next.previous_hash = temp

temp = LinkedList()
Blockchain = ['Block1','Block2','Block3','Block4','Block5']
for data in Blockchain:
    temp.append(datetime.now(),data)
    while temp is not None:
        print("Timestamp:",temp.next.timestamp)
        print("Data:",temp.next.data)
        print("SHA256Hash:",temp.next.hash)
        print("Prev_hash:",temp.next.previous_hash)
        print("-------------------------------------------------------------------------")
        break
