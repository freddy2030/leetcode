def groupAnagrams(strs):
    letter_hash = {}
    word_hash = {}
    result = []
    for i in strs:
        hash_sum = 0
        for j in i:
            if j in letter_hash.keys():
                j_hash = letter_hash[j]
            else:
                j_hash = hash(j)
            hash_sum += j_hash
        if hash_sum in word_hash.keys():
            word_hash[hash_sum].append(i)
        else:
            word_hash[hash_sum] = [i]
    for k, v in word_hash.items():
        result.append(v)
    return result


if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    result = groupAnagrams(strs)
    print(result)