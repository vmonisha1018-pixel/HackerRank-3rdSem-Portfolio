def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []

    for query in queries:
        query_type = query[0]
        x = query[1]
        y = query[2]

        idx = (x ^ lastAnswer) % n

        if query_type == 1:
            arr[idx].append(y)

        elif query_type == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)

    return answers
