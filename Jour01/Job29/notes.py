
import math
scores = [30,72, 63, 84, 90, 50]

passed = []

def fonction_arrondi(scores):

    for score in scores:
        if score >= 40:

            passed.append(score)

    print(passed)


    passed_corr = []
    for item in passed:
        reste = item % 5
        if 5 - reste < 3 :
            passed_corr.append( math.ceil(item/5)*5)
        else:
            passed_corr.append(item)
    print(passed_corr)
    return passed_corr
