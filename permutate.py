def permutate(input):
    def helper(pool, curr):
        word_curr = curr
        if len(pool) == 0:
            print(word_curr)
        for i in range(len(pool)):
            helper(pool[0:i] + pool[i+1:], word_curr + pool[i])
    return helper(input, "")

# More space efficient since there are no temporary lists made via splicing
def permutate(input, curr=0, end=0):
    input = [i for i in input]
    end = len(input)
    if curr == end - 1: 
        print(input)
    for i in range(curr, len(input)):
        input[curr], input[i] = input[i], input[curr]
        permutate(input, curr+1, end)        
        input[curr], input[i] = input[i], input[curr]
