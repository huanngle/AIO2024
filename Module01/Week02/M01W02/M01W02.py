#Bài 1: Max_in_slidinglist
def max_in_slidingwin(list, k):
    result = []
    for i in range(len(list) - k + 1):
        max_num = max(list[i:i+k])
        result.append(max_num)

    return result

#Bài 2. count word in string
def count_word_in_string(string):
    result = {}
    for word in string:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result

#Bài 3. count word in files:
def count_words_in_file(file):
    result = {}
    try:
        with open(file,'r') as file:
            for line in file:
                list_words = line.lower().split()
                for word in list_words:
                    if word in result:
                        result[word] += 1
                    else:
                        result[word] = 1
    except FileExistsError:
        print(f'file {file} is not found')

    return  result

#Bài 4:
def levenshtein_distance(S, T):
    m = len(S)
    n = len(T)
    D = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        D[i][0] = i
    for j  in range(n+1):
        D[0][j] = j

    for i in range(1,m+1):
        for j in range(1, n+1):
            cost = 0 if S[i - 1] == T[j - 1] else 1

            D[i][j] = min(D[i - 1][j] + 1,
                          D[i][j - 1] + 1,
                          D[i - 1][j - 1] + cost)

    return D[m][n]




