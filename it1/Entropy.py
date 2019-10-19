from Distrib import ProbCounter
import sys
import math


class Entropy:
    def __init__(self):
        pass

    @staticmethod
    def get_entropy(nums):
        return -sum(map(lambda x: (float(x) * math.log2(float(x)) if x != 0 else 0), nums))

def main():

    prob_counter = ProbCounter(sys.argv[1])
    probabilities = prob_counter.get_symbol_probabilities()
    double_probabilities = prob_counter.get_double_symbol_probabilities()

    output = open(sys.argv[2],'w+')

    entropy = Entropy.get_entropy(probabilities)
    double_entropy = Entropy.get_entropy(double_probabilities)

    output.write('%.7f\n' % entropy)
    output.write('%.7f\n' % double_entropy)
    output.write('%.7f\n' % (double_entropy - entropy))


if __name__ == "__main__":
    main()

