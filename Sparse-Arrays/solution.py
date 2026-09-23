def matchingStrings(stringList, queries):
    frequency = {}

    for string in stringList:
        if string in frequency:
            frequency[string] += 1
        else:
            frequency[string] = 1

    result = []

    for query in queries:
        result.append(frequency.get(query, 0))

    return result
