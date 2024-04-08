def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    printBookData(file_contents)

def countListSortResolver(dict):
    return dict["count"]

def getWordCount(text):
    words = text.split()

    return len(words)

def getLetterCount(text):
    lowers = text.lower()
    counts = {}
    for char in lowers:
        if char in counts:
            counts[char]+= 1
        else:
            counts[char] = 1
    
    return counts
    
def printLetterData(charCounts):
    countList = []
    for count in charCounts:
        if count.isalpha(): 
            countList.append({"char":count, "count":charCounts[count]})
    countList.sort(reverse = True, key = countListSortResolver)
    
    for count in countList:
        print(f"{count["char"]}: {count["count"]}")
        
def printBookData(text):
    print("--- REPORT ---\n")
    print(f"total word count: {getWordCount(text)}\n")
    print("-- Letter Counts --")
    printLetterData(getLetterCount(text))
    print("\n--- END REPORT ---") 

main()
