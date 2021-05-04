import urllib.request

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    book = urllib.request.urlopen(book_url).read().decode()
    words = book.split()
    maxLen = len(max(words, key=len))
    return radix(maxLen, words)

def radix(maxLen, words):
    zeroToMax = range(0, maxLen)
    #We dont know character codes for evreything in the book
    #We can append to buckets as needed
    buckets = [] 
    for i in zeroToMax.__reversed__():
        for string in words:
            charCode = None
            if i < len(string):
                charCode = ord(string[i]) 
            else:
                #always make this one first
                charCode = 0
            #add to buckets until we support the new character
            while len(buckets) <= charCode:
                buckets.append([])
            buckets[charCode].append(string) 
            
        words = []
        for bucket in buckets:
            words += bucket
            del bucket[:]
    return words


# Test code

# def sortTest(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
#     book = urllib.request.urlopen(book_url).read().decode()
#     words = book.split()
#     words.sort()
#     return words

# print(radix_a_book())
# print(sortTest())

# print(radix_a_book() == sortTest())


