
def testLineKeywords(line, keywords):
    for token in line.split(' '):
        if token in keywords.keys():
            keywords[token] = 1

def storeFileData(fileName, listName, warningLabel):
    try:
        with open(fileName) as inFile:
            for line in inFile:
                listName.append(line.rstrip('\n').rsplit(' ', 1))
            if not listName:
                print("Warning: " + warningLabel + " is empty.")
    except IOError:
        print("Unable to open " + filename)

def storeKeywords(fileName, dictName, warningLabel):
    try:
        with open(fileName) as keywordFile:
            for line in keywordFile:
                dictName[line.rstrip('\n')] = 0
            if not dictName:
                print("Warning: " + warningLabel + " is empty.")
    except IOError:
        print("Unable to open " + filename)

def resetKeywords(keywords):
    return {x:0 for x in keywords}

trainingFileName = "trainingData.txt"
testFileName = "testData.txt"
keywordFileName = "keywords.txt"
trainingData = []
testData = []
keywords = {}

storeFileData(trainingFileName, trainingData, "Training Data")
storeFileData(testFileName, testData, "Test Data")
storeKeywords(keywordFileName, keywords, "Keyword Data")

testLineKeywords(trainingData[1][0], keywords)
print(keywords)

