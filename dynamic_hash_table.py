from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        self.collision_type = collision_type
        self.params = params
        super().__init__(collision_type, params)

    def rehash(self):
        new_size = get_next_size()
        old_table = self.table[:]
        self.table_size = new_size
        self.table = [None] * self.table_size
        z = self.params[0]

        for i in old_table:
            if i is not None:
                if self.collision_type == "Chain":
                    for element in i:
                        index = self.get_slot(element)
                        if self.table[index] is None:
                            self.table[index] = []
                        self.table[index].append(element)

                elif self.collision_type == "Linear":
                    index = self.get_slot(i)
                    while self.table[index] is not None:
                        index = (index + 1) % self.table_size
                    self.table[index] = i

                else:
                    step = self.secondary_hash(i)
                    j = 1
                    index = self.get_slot(i)
                    original_index = index
                    while self.table[index] is not None:
                        index = (original_index + j * step) % self.table_size
                        j += 1
                    self.table[index] = i

    def insert(self, key):
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        self.collision_type = collision_type
        self.params = params
        super().__init__(collision_type, params)

    def rehash(self):
        new_size = get_next_size()
        old_table = self.table[:]
        self.table_size = new_size
        self.table = [None] * self.table_size
        z = self.params[0]

        for i in old_table:
            if i is not None:
                if self.collision_type == "Chain":
                    for key, value in i:
                        index = self.get_slot(key)
                        if self.table[index] is None:
                            self.table[index] = []
                        self.table[index].append((key, value))

                elif self.collision_type == "Linear":
                    key, value = i
                    index = self.get_slot(key)
                    while self.table[index] is not None:
                        index = (index + 1) % self.table_size
                    self.table[index] = (key, value)

                else:
                    key, value = i
                    step = self.secondary_hash(key)
                    j = 1
                    index = self.get_slot(key)
                    original_index = index
                    while self.table[index] is not None:
                        index = (original_index + j * step) % self.table_size
                        j += 1
                    self.table[index] = (key, value)


    def insert(self, key):
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()