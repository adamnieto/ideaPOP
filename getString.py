import getImage

def getSearchValues(indexValues, textBox):
    searchTerms = []
    for values in indexValues:
        splitValueList = values.split(',')
        value1 = int(splitValueList[0])
        value2 = int(splitValueList[1])
        result = textBox[value1 + 1:value2]
        searchTerms.append(result)
    return searchTerms

def processString(textBox):
    indexValues = []
    counter = -1 #bc index is zero
    tempValueHold = -1
    for char in textBox:
        counter += 1
        if char == "*":
            tempValueHold = counter
        elif char == "/":
            indexValues.append(str(tempValueHold) + "," + str(counter))
            tempValueHold = -1
        else:
            None
    return indexValues

def main(textBox):
    indexValues = processString(textBox.strip('\n'))
    searchTerms = getSearchValues(indexValues, textBox)
    getImage.main(searchTerms)
