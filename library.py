import hash_table as ht

def merge(arr, low, mid, high):
    v = []
    left = low
    right = mid + 1
    
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            v.append(arr[left])
            left += 1
        else:
            v.append(arr[right])
            right += 1
    
    while left <= mid:
        v.append(arr[left])
        left += 1
    
    while right <= high:
        v.append(arr[right])
        right += 1
    
    # Copy merged elements back to original array
    for i in range(low, high + 1):
        arr[i] = v[i - low]


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)


class DigitalLibrary:
    def __init__(self):
        pass

class MuskLibrary(DigitalLibrary):
    def __init__(self, book_titles, texts):
        self.library = []
        for i in range(len(texts)):
            text = texts[i][:]
            merge_sort(text, 0, len(text) - 1)
            txt = []
            txt.append(text[0])
            for j in range(1, len(text)):
                if text[j - 1] != text[j]:
                    txt.append(text[j])
            self.library.append((book_titles[i], txt))
        merge_sort(self.library, 0, len(self.library) - 1)

    def distinct_words(self, book_title):
        a = []
        i = 0
        low, high = 0, len(self.library) - 1
        while low <= high:
            mid = (low + high)//2
            if self.library[mid][0] == book_title:
                i = mid
                break
            elif self.library[mid][0] < book_title:
                low = mid + 1
            else:
                high = mid - 1
        a = self.library[i][1][:]
        return a

    def count_distinct_words(self, book_title):
        i = 0
        low, high = 0, len(self.library) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.library[mid][0] == book_title:
                i = mid
                break
            elif self.library[mid][0] < book_title:
                low = mid + 1
            else:
                high = mid - 1
        return len(self.library[i][1])

    def search_keyword(self, keyword):
        a = []
        for i in self.library:
            j = -1
            low, high = 0, len(i[1]) - 1
            while low <= high:
                mid = (low + high) // 2
                if i[1][mid] == keyword:
                    j = mid
                    break
                elif i[1][mid] < keyword:
                    low = mid + 1
                else:
                    high = mid - 1
            if j != -1:
                a.append(i[0])
        return a

    def print_books(self):
        for i in self.library:
            c = 0
            s = ''
            s += i[0]
            s += ': '
            for j in i[1]:
                c += 1
                s += j
                if c < len(i[1]): s += ' | '
            print(s)

class JGBLibrary(DigitalLibrary):
    def __init__(self, name, params):
        self.name = name
        self.params = params
        
        if name == "Jobs":
            self.collision_type = "Chain"
        elif name == "Gates":
            self.collision_type = "Linear"
        else:  # Bezos
            self.collision_type = "Double"
            
        self.hash_map_books = ht.HashMap(self.collision_type, self.params)

    def add_book(self, book_title, text):
        hash_set = ht.HashSet(self.collision_type, self.params)
        for word in text:
            hash_set.insert(word)
            
        self.hash_map_books.insert((book_title, hash_set))

    def distinct_words(self, book_title):
        a = []
        found_book = self.hash_map_books.find(book_title)
        if found_book is None:
            return a
            
        for i in found_book.table:
            if i is not None:
                if self.name == "Jobs":
                    for j in i:
                        a.append(j)
                else:
                    a.append(i)
        # a.sort()
        return a

    def count_distinct_words(self, book_title):
        return self.hash_map_books.find(book_title).count

    def search_keyword(self, keyword):
        a = []
        for i in self.hash_map_books.table:
            if i is not None:
                if self.name == "Jobs":
                    for j in i:
                        if j[1].find(keyword):
                            a.append(j[0])
                else:
                    if i[1].find(keyword):
                        a.append(i[0])
        # a.sort()
        return a

    def print_books(self):
        for i in self.hash_map_books.table:
            if i is not None:
                if self.name == "Jobs":
                    for j in i:
                        print(j[0] + ':', j[1].__str__())
                else:
                    print(i[0] + ':', i[1].__str__())

# find =JGBLibrary("Bezos",(5,4,4,50))
# text=["Harry", "Potter", "is", "about", "a", "young", "wizard", "facing", "adventures", "with", "his", "friends", "against", "dark", "forces"]
# find.add_book("HarryPotter",text)
# print(find.distinct_words("HarryPotter"))
# print(find.count_distinct_words("HarryPotter"))
# print(find.search_keyword("is"))
# find.print_books()