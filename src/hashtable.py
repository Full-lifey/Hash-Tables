# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value, next_pair=None):
        self.key = key
        self.value = value
        self.next = next_pair


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        # self.counter = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # self.counter += 1
        # if self.counter / self.capacity >= 0.7:
        #     self.resize()
        # print('self.counter', self.counter)
        # print('self.capacity', self.capacity)
        index = self._hash_mod(key)
        current_pair = self.storage[index]
        if current_pair:
            if key == current_pair.key:
                current_pair.value = value
                return
            else:
                # Insert at head instead of tail
                # Create LinkedPair and set next to current_pair
                new_pair = LinkedPair(key, value, current_pair)
                # Set new_pair to hash table index
                self.storage[index] = new_pair
                # if current_pair.next:
                #     while current_pair.next:
                #         current_pair == current_pair.next
                #     else:
                #         current_pair.next = LinkedPair(key, value)
                #         # return
                # else:
                #     current_pair.next = LinkedPair(key, value)
        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_pair = self.storage[index]
        if current_pair:
            if key == current_pair.key:
                # self.counter -= 1
                if current_pair.next:
                    self.storage[index] = current_pair.next
                else:
                    self.storage[index] = None
                return
            elif current_pair.next:
                value = None
                while current_pair.next:
                    next = current_pair.next
                    if key == next.key:
                        # self.counter -= 1
                        value = next.value
                        current_pair.next = next.next
                        # return
                    current_pair = current_pair.next
                else:
                    print("warning, key given is not in HashTable")
                    # return
            else:
                print("warning, key given is not in HashTable")
                # return
        else:
            print("warning, key given is not in HashTable")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_pair = self.storage[index]
        if current_pair:
            if key == current_pair.key:
                return current_pair.value
            elif current_pair.next:
                while current_pair.next:
                    current_pair = current_pair.next
                    if key == current_pair.key:
                        return current_pair.value
                else:
                    return None
            else:
                return None
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        print('called resize')
        # Save current counter value
        # self.counter = 0
        # Double self.capacity
        self.capacity = self.capacity * 2
        # creates new storage of twice the size
        new_storage = [None] * self.capacity
        # copies self.storage to old storage
        old_storage = self.storage
        # sets self.storage to new, empty storage with 2x size
        self.storage = new_storage
        for i in range(len(old_storage)):
            if old_storage[i] != None:
                if old_storage[i].next:
                    current = old_storage[i]
                    while current.next:
                        self.insert(current.key, current.value)
                        current = current.next
                    else:
                        self.insert(current.key, current.value)
                else:
                    self.insert(old_storage[i].key, old_storage[i].value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
