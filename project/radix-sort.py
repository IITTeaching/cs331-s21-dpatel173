import urllib.request

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    words = book_to_words(book_url)
    words=[x.decode('utf-8') for x in words]
    maxLen = len(max(words, key=len))
    return radix(maxLen, words)

def radix(maxLen, words):
    zeroToMax = range(0, maxLen)
    #We dont know character codes for evreything in the book
    #We can append to buckets as needed
    buckets = [] 
    for i in zeroToMax.__reversed__():
        for string in words:
            # string = string.decode('utf-8')
            charCode = None
            if i < len(string):
                try:
                    charCode = ord(str(string[i])) 
                except:
                    print(string)
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
#     words = book_to_words(book_url)
#     words=[x.decode('utf-8') for x in words]
#     words.sort()
#     return words

# print(radix_a_book())
# print(sortTest())
# radix_a_book()
# print(radix_a_book() == sortTest())
