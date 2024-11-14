class HashTable:
    def __init__(self, collision_type, params):
        self.collision_type = collision_type
        self.z = params[0]
        self.table_size = params[-1]
        self.table = [None] * self.table_size
        self.count = 0

        # For double hashing
        if collision_type == "Double":
            self.z2, self.c2 = params[1], params[2]
    
    def polynomial_hash(self, key, z):
        hash_value = 0
        for i, char in enumerate(key):
            p_value = ord(char.lower()) - ord('a') + (0 if char.islower() else 26)
            hash_value += p_value * (z ** i)
        return hash_value
    
    def compress(self, hash_value):
        return hash_value % self.table_size
    
    def secondary_hash(self, key):
        hash_value = self.polynomial_hash(key, self.z2)
        return self.c2 - (hash_value % self.c2)
    
    def get_slot(self, key):
        return self.compress(self.polynomial_hash(key, self.z))
    
    def get_load(self):
        return self.count / self.table_size


class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
    
    def insert(self, key):
        slot = self.get_slot(key)
        
        if self.collision_type == "Chain":
            if self.table[slot] is None:
                self.table[slot] = []
            if key not in self.table[slot]:
                self.table[slot].append(key)
                self.count += 1
            return

        elif self.collision_type == "Linear":
            original_slot = slot
            while True:
                if self.table[slot] is None:
                    self.table[slot] = key
                    self.count += 1
                    return
                if self.table[slot] == key:
                    return
                slot = (slot + 1) % self.table_size
                if slot == original_slot:
                    return  # Table is full

        elif self.collision_type == "Double":
            original_slot = slot
            step_size = self.secondary_hash(key)
            i = 0
            while True:
                current_slot = (slot + i * step_size) % self.table_size
                if self.table[current_slot] is None:
                    self.table[current_slot] = key
                    self.count += 1
                    return
                if self.table[current_slot] == key:
                    return
                i += 1
                if (slot + i * step_size) % self.table_size == original_slot:
                    return  # Table is full
    
    def find(self, key):
        slot = self.get_slot(key)
        
        if self.collision_type == "Chain":
            return self.table[slot] is not None and key in self.table[slot]
        
        elif self.collision_type == "Linear":
            original_slot = slot
            while True:
                if self.table[slot] is None:
                    return False
                if self.table[slot] == key:
                    return True
                slot = (slot + 1) % self.table_size
                if slot == original_slot:
                    return False

        elif self.collision_type == "Double":
            original_slot = slot
            step_size = self.secondary_hash(key)
            i = 0
            while True:
                current_slot = (slot + i * step_size) % self.table_size
                if self.table[current_slot] is None:
                    return False
                if self.table[current_slot] == key:
                    return True
                i += 1
                if (slot + i * step_size) % self.table_size == original_slot:
                    return False

    def __str__(self):
        s = ''
        if self.collision_type == "Chain":
            c = 0
            for i in self.table:
                c += 1
                if i is None:
                    s += '<EMPTY>'
                else:
                    d = 0
                    for j in i:
                        d += 1
                        s += str(j)
                        if d < len(i):
                            s += ' ; '
                if c < self.table_size:
                    s += ' | '
        else:
            c = 0
            for i in self.table:
                c += 1
                if i is None:
                    s += '<EMPTY>'
                else:
                    s += str(i)
                if c < self.table_size:
                    s += ' | '
        return s


class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def insert(self, x):
        original_index = self.get_slot(x[0])
        index=original_index

        if self.collision_type == "Chain":
            if self.table[index] is None:
                self.table[index] = []
            for i in self.table[index]:
                if i == x: return
            self.table[index].append(x)
            self.count += 1

        elif self.collision_type == "Linear":
            while self.table[index] is not None:
                if self.table[index] == x:
                    return
                index = (index + 1) % self.table_size
                if index == original_index: return
            self.count += 1
            self.table[index] = x

        else:
            step = (self.secondary_hash(x[0]))
            j = 1
            while self.table[index] is not None:
                if self.table[index] == x:
                    return
                index = (original_index + j * step) % self.table_size
                j += 1
                if index == original_index: return
            self.count += 1
            self.table[index] = x
    
    def find(self, key):
        slot = self.get_slot(key)

        if self.collision_type == "Chain":
            if self.table[slot] is None:
                return None
            for entry in self.table[slot]:
                if entry[0] == key:
                    return entry[1]
            return None

        elif self.collision_type == "Linear":
            original_slot = slot
            while True:
                if self.table[slot] is None:
                    return None
                if self.table[slot][0] == key:
                    return self.table[slot][1]
                slot = (slot + 1) % self.table_size
                if slot == original_slot:
                    return None

        elif self.collision_type == "Double":
            original_slot = slot
            step_size = self.secondary_hash(key)
            i = 0
            while True:
                current_slot = (slot + i * step_size) % self.table_size
                if self.table[current_slot] is None:
                    return None
                if self.table[current_slot][0] == key:
                    return self.table[current_slot][1]
                i += 1
                if (slot + i * step_size) % self.table_size == original_slot:
                    return None

    def __str__(self):
        s = ''
        if self.collision_type == "Chain":
            c = 0
            for i in self.table:
                c += 1
                if i is None:
                    s += '<EMPTY>'
                else:
                    d = 0
                    for j in i:
                        d += 1
                        s += f'({j[0]}, {j[1]})'
                        if d < len(i):
                            s += ' ; '
                if c < self.table_size:
                    s += ' | '
        else:
            c = 0
            for i in self.table:
                c += 1
                if i is None:
                    s += '<EMPTY>'
                else:
                    s += f'({i[0]}, {i[1]})'
                if c < self.table_size:
                    s += ' | '
        return s