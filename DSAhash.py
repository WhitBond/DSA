
import csv
class DSAHashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.state = "free"  # Possible states: "used", "free", "previously-used"


class DSAHashTable:
    def __init__(self, size):
        self.size = size
        self.count = 0  # Number of elements in the hash table
        self.hashArray = [None] * size

    def hash(self, key):
        # Simple hash function - sum of ASCII values of characters in the key
        return sum(ord(char) for char in key) % self.size

    def resize(self, new_size):
        old_hash_array = self.hashArray
        self.size = new_size
        self.hashArray = [None] * new_size
        self.count = 0
    
        for entry in old_hash_array:
            if entry and entry.state == "used":
                self.put(entry.key, entry.value)



    def put(self, key, value):
        # Check if resize is needed
        if (self.count +1) / self.size > 0.7:  # Example load factor threshold: 0.7
            new_size = int(self.size * 2)  # Double the size
            self.resize(new_size)

        index = self.hash(key)
        if self.hashArray[index] is None or self.hashArray[index].state != "used":
            self.hashArray[index] = DSAHashEntry(key, value)
            self.hashArray[index].state = "used"
            self.count += 1
        else:
            # Linear probing to handle collisions
            next_index = (index + 1) % self.size
            while next_index != index:
                if self.hashArray[next_index] is None or self.hashArray[next_index].state != "used":
                    self.hashArray[next_index] = DSAHashEntry(key, value)
                    self.hashArray[next_index].state = "used"
                    self.count += 1
                    return
                next_index = (next_index + 1) % self.size
            raise Exception("Hash table is full")

    def hasKey(self, key):
        index = self.hash(key)
        if self.hashArray[index] is None:
            return False
        elif self.hashArray[index].key == key and self.hashArray[index].state == "used":
            return True
        else:
            next_index = (index + 1) % self.size
            while next_index != index:
                if self.hashArray[next_index] is None:
                    return False
                elif self.hashArray[next_index].key == key and self.hashArray[next_index].state == "used":
                    return True
                next_index = (next_index + 1) % self.size
            return False

    def get(self, key):
        index = self.hash(key)
        if self.hashArray[index] is None:
            raise KeyError("Key not found")
        elif self.hashArray[index].key == key and self.hashArray[index].state == "used":
            return self.hashArray[index].value
        else:
            next_index = (index + 1) % self.size
            while next_index != index:
                if self.hashArray[next_index] is None:
                    raise KeyError("Key not found")
                elif self.hashArray[next_index].key == key and self.hashArray[next_index].state == "used":
                    return self.hashArray[next_index].value
                next_index = (next_index + 1) % self.size
            raise KeyError("Key not found")

    def remove(self, key):
        index = self.hash(key)
        if self.hashArray[index] is None:
            raise KeyError("Key not found")
        elif self.hashArray[index].key == key and self.hashArray[index].state == "used":
            self.hashArray[index].state = "previously-used"
            self.count -= 1
        else:
            next_index = (index + 1) % self.size
            while next_index != index:
                if self.hashArray[next_index] is None:
                    raise KeyError("Key not found")
                elif self.hashArray[next_index].key == key and self.hashArray[next_index].state == "used":
                    self.hashArray[next_index].state = "previously-used"
                    self.count -= 1
                    return
                next_index = (next_index + 1) % self.size
            raise KeyError("Key not found")
    def export(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Key', 'Value'])  # Write header
            for entry in self.hashArray:
                if entry and entry.state == "used":
                    writer.writerow([entry.key, entry.value])
"""
has_table = DSAHashTable(1)
with open("RandomNames7000.csv", "r") as fileobj:
    data = fileobj.readlines()
    for line in data :
        splitline = line.strip().split(",")
        has_table.put(splitline[1],splitline[0])
    fileobj.close()
has_table.export("hash table.csv")
print(has_table.size)
"""
