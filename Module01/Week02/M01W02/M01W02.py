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
def count_words_in_file(file_path):
    result = {}
    try:
        with open(file_path,'r') as file:
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
def levenshtein_distance(start, target):
    m = len(start)
    n = len(target)
    D = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        D[i][0] = i
    for j  in range(n+1):
        D[0][j] = j

    for i in range(1,m+1):
        for j in range(1, n+1):
            cost = 0 if start[i - 1] == target[j - 1] else 1

            D[i][j] = min(D[i - 1][j] + 1,
                          D[i][j - 1] + 1,
                          D[i - 1][j - 1] + cost)

    return D[m][n]

def main():
    print(max_in_slidingwin([1,3,-1,-3,5,3,6,7],3),'\n')
    print(count_word_in_string('hello world'),'\n')
    print(count_words_in_file('Module01/Week02/M01W02/P1_data.txt'),'\n')
    print(levenshtein_distance('kitten','sitting'), 'is levenshtein distance between kitten and sitting')

if __name__ == '__main__':
    main()
    

