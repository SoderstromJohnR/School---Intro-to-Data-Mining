
import pprint

#Returns a list of probabilities for each keyword given a numeric list
#The first interior list contains probabilities of each keyword when the
#label is 1 (or True/CS) and the probability of the label being 1.
#The second interior list contains probabilities of each keyword when the
#label is 0 (or False/Not CS) and the probability of the label being 0.
def getTrainingProbability(trainingResults):
    #Create a list of probabilities to determine expected test results
    probList = [[], []]
    for i in range(len(trainingResults[0]) - 1):
        probList[0].append(0)
        probList[1].append(0)
        
    countYes = 0
    countNo = 0
    for index, line in enumerate(trainingResults):
        probLine = 0
        if line[-1][0] is 1:
            countYes += 1
        else:
            countNo += 1
            probLine = 1
        for inIndex, element in enumerate(line[:-1]):
            probList[probLine][inIndex] += element
            
    for index, line in enumerate(probList):
        for inIndex, element in enumerate(line):
            if index is 0:
                line[inIndex] /= countYes
            else:
                line[inIndex] /= countNo
    probList[0].append([countYes / (countYes + countNo)])
    probList[1].append([countNo / (countYes + countNo)])
    return probList

#
def getSingleTestResult(probList, testLine):
    probYes = probList[0][-1][0]
    probNo = probList[1][-1][0]
    probLine = 1 - testLine[-1][0]
    for index, element in testLine:
        if element is 1:
            probYes *= probList[probLine][index]
        else:
            probNo *= 1 - probList[probLine][index]
    if probYes > probNo:
        testLine[-1].extend(1)
    else:
        testLine[-1].extend(0)

#
def getTestResults(training, test):
    probList = getTrainingProbability(training)
    for index, line in enumerate(test):
        #Get expected result
        tempExtend = 0
        tempError = line[-1][0] - tempExtend
        line[-1].extend([tempExtend, tempError])
        

#Stores the presence of keywords across all lines in training data
#with labels. Returns a list aligned with the keywords list passed in.
def storeResults(fileName, keywords, warningLabel):
    try:
        with open(fileName) as inFile:
            results = []
            #Splits input lines one by one and scans for presence of keywords
            #Appends class label after scanning of a line is complete
            for line in inFile:
                checkLine = line.rstrip('\n').rsplit(' ', 1)
                results.append(testLineKeywords(checkLine[0], keywords))
                results[-1].append([int(checkLine[1])])
            return results
    except IOError:
        print("Unable to open " + fileName + ".")

#Test a line of text for presence of keywords in given list
#Returns a list of 0/1 describing their presence
def testLineKeywords(line, keywords):
    iterList = []
    tempLine = line.split(' ')
    for keyword in keywords:
        #Testing for presence, not number of times keyword exists
        if keyword in tempLine:
            iterList.append(1)
        else:
            iterList.append(0)
    return iterList

#Stores a list of keywords based on an input file
#Expects each keyword on its own line
def storeKeywords(fileName, listName, warningLabel):
    try:
        with open(fileName) as inFile:
            for line in inFile:
                listName.append(line.rstrip('\n'))
            if not listName:
                print("Warning: " + warningLabel + " is empty.")
            else:
                listName = list().append(listName)
    except IOError:
        print("Unable to open " + fileName + ".")

trainingFileName = "trainingData.txt"
testFileName = "testData.txt"
keywordFileName = "keywords.txt"
keywords = []

storeKeywords(keywordFileName, keywords, "Keyword Data")
trainingResults = storeResults(trainingFileName, keywords, "Training Data")
testResults = storeResults(testFileName, keywords, "Test Data")

print(keywords)
pprint.pprint(trainingResults)
#print(testResults)

getTestResults(trainingResults, testResults)
#print(testResults)

tempList = getTrainingProbability(trainingResults)
pprint.pprint(tempList)

