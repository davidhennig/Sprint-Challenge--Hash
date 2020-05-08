def has_negatives(a):

    """
    YOUR CODE HERE
    """

    result = []
    dic = {}


    for num in a:

        if abs(num) not in dic:
            if num > 0:
                dic[abs(num)] = 'positive'
            else:
                dic[abs(num)] = 'negative'
        else:
            if num > 0 and dic[abs(num)] == 'negative':
                result.append(abs(num))
            elif num < 0 and dic[abs(num)] == 'positive':
                result.append(abs(num))




    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
