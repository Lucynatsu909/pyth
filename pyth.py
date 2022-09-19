def findAlphabeticallyLastWord(listofwords):
    listofwords.sort()
    print(listofwords[-1])
    return
if __name__ == '__main__':
    listofwords = ["Stray","zoo","line","share"]
    findAlphabeticallyLastWord(listofwords)
