
from pprint import pprint as pp

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

    #Counts the number of 1 and 0 classifications from passed data
    #Used to calculate probability of both values across all data.
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

    #Calculates probability that each keyword exists in each classification
    #Probabilities are separated based on 1 and 0 classification
    for index, line in enumerate(probList):
        for inIndex, element in enumerate(line):
            #Check a need for smoothing
            if probList[0][inIndex] is 0 or probList[1][inIndex] is 0:
                if index is 0:
                    line[inIndex] = (element + 1) / (countYes + 2)
                else:
                    line[inIndex] = (element + 1) / (countNo + 2)
            #Don't apply smoothing if both entries have something already
            else:
                if index is 0:
                    line[inIndex] /= countYes
                else:
                    line[inIndex] /= countNo

    #Adds the final probability that a randomly selected line will
    #be classified as either 1 or 0
    probList[0].append([countYes / (countYes + countNo)])
    probList[1].append([countNo / (countYes + countNo)])
    return probList

#Calculates required parts of probability that a given line
#is either 0 or 1 (CS or not CS in this project, but usable outside of it)
#Appends the expected classification to the list containing the
#actual classification of the line.
def getSingleTestResult(probList, testLine):
    #Final probability will always include P(y=1) or P(y=0), so start with them
    probYes = probList[0][-1][0]
    probNo = probList[1][-1][0]
    #Iterates through list, multiplying probabilities by given y=1 and y=0
    #respectively. Index is aligned with keyword values.
    for index, element in enumerate(testLine):
        if element is 1:
            probYes *= probList[0][index]
            probNo *= probList[1][index]
        elif element is 0:
            probYes *= 1 - probList[0][index]
            probNo *= 1 - probList[1][index]

    #Compares final probabilities of both classifications. While not
    #true probabilities, the ratios are the same and they may be
    #compared safely.
    if probYes > probNo:
        testLine[-1].append(1)
    else:
        testLine[-1].append(0)

#Passed both the training and test data indicating presence of
#keywords in each line, expecting the final values of both
#to be a list containing only the actual classification
#Will modify the test data to append both the predicted classification
#and the error value to the list containing actual classification
def getTestResults(training, test):
    probList = getTrainingProbability(training)
    count = 0
    #Runs each line through getting expected classification and
    #appends the error value
    for line in test:
        getSingleTestResult(probList, line)
        result = 0
        if line[-1][0] is not line[-1][1]:
            result = 1
        line[-1].append(result)
        
#Cleans a string for learning, removing non-alphanumeric characters
#and changing case to lower.
def cleanString(string):
    string = string.lower()
    firstIndex = 0
    secondIndex = 0
    newString = ""
    for char in string:
        if not (char.isalnum() or ord(char) is 32):
            newString += string[firstIndex:secondIndex]
            firstIndex = secondIndex + 1
        secondIndex += 1
    return newString

#Use for deciding keywords, modifies a dictionary to contain each
#word in the training data with a count, ignoring classification
def potentialKeywords(keywordDict, line):
    tempLine = line.split(' ')
    for word in tempLine:
        if word in keywordDict:
            keywordDict[word] += 1
        else:
            keywordDict[word] = 1

#Includes two lines to uncomment to generate word counts for potential
#keywords.
#Stores the presence of keywords across all lines in training data
#with labels. Returns a list aligned with the keywords list passed in.
def storeResults(fileName, keywords, warningLabel):
    try:
        with open(fileName) as inFile:
            #Uncomment to store potential keywords
##            potentialKey = {}
            results = []
            #Splits input lines one by one and scans for presence of keywords
            #Appends class label after scanning of a line is complete
            for line in inFile:
                #I was getting strange behavior and could not get it
                #to stop without adding this if statement
                if line[-1] is not '\n':
                    line += '\n'
                line = cleanString(line)
                checkLine = line.rstrip('\n').rsplit(' ', 1)
                #Uncomment to add potential keywords to dictionary
##                potentialKeywords(potentialKey, checkLine[0])
                results.append(testLineKeywords(checkLine[0], keywords))
                results[-1].append([int(checkLine[1])])
            #Uncomment to print potential keyword dictionary
##            pp([(k, v) for k, v in sorted(potentialKey.items(),
##                                          key=lambda x: x[1], reverse=True)])
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

#Gets error rate on test data through error results added to test data
def getErrorRate(test):
    #Count the number of lines in test data and the number of found errors
    errorCount = 0
    totalCount = 0
    for line in test:
        totalCount += 1
        errorCount += line[-1][-1]

    #Returns the error rate
    return errorCount / totalCount
        
trainingFileName = "trainingData.txt"
testFileName = "testData.txt"
keywordFileName = "keywords.txt"
keywords = []

storeKeywords(keywordFileName, keywords, "Keyword Data")
trainingResults = storeResults(trainingFileName, keywords, "Training Data")
testResults = storeResults(testFileName, keywords, "Test Data")

#print(keywords)
#pp(trainingResults)
#print(testResults)

getTestResults(trainingResults, testResults)
tempList = getTrainingProbability(trainingResults)
#pp(tempList)
#pp(testResults)
for test in testResults:
    pp(test[-1])

errorRate = getErrorRate(testResults)
print(errorRate)

altTrainingResults = storeResults(trainingFileName, keywords, "Training Data")
getTestResults(trainingResults, altTrainingResults)
errorRate = getErrorRate(altTrainingResults)
for test in altTrainingResults:
    pp(test[-1])

print(errorRate)

