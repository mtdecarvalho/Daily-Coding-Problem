# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def elementsAddUpToNumber(numberList, k):
    for i in range(0, len(numberList)-1, 1):
        for j in range(i+1, len(numberList), 1):
            if numberList[i] + numberList[j] == k:
                return True
    return False


if __name__ == '__main__':
    numberList = [10, 15, 3, 7]
    print(elementsAddUpToNumber(numberList, 17))
