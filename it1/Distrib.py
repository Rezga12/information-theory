import sys
from decimal import *


class ProbCounter:
    def __init__(self,filename):
        self.file = open(filename,encoding='utf-8')
        self.characters = [' ', 'ა', 'ბ', 'გ', 'დ', 'ე', 'ვ', 'ზ', 'თ', 'ი', 'კ', 'ლ', 'მ', 'ნ', 'ო', 'პ', 'ჟ',
                           'რ', 'ს', 'ტ', 'უ', 'ფ', 'ქ', 'ღ', 'ყ', 'შ', 'ჩ', 'ც', 'ძ', 'წ', 'ჭ', 'ხ', 'ჯ', 'ჰ']
        self.dic = dict()
        for key in self.characters:
            self.dic[key] = 0

        self.dic_two = dict()
        for first in self.characters:
            for second in self.characters:
                self.dic_two[first + second] = 0


        self.total_count = 0
        char = self.file.read(1)
        prev_char = ' '

        while char:

            self.dic[char] += 1
            self.dic_two[prev_char + char] += 1
            self.total_count += 1

            prev_char = char
            char = self.file.read(1)

    def get_symbol_probabilities(self):
        return self.get_probs(self.dic)

    def get_double_symbol_probabilities(self):
        return self.get_probs(self.dic_two)

    def get_probs(self, dic):
        keys = dic.keys()
        keys = sorted(keys)
        result = []
        for k in keys:
            num = str(float(dic[k]) / float(self.total_count))
            # print(num + " " + str(Decimal(str(num)).quantize(Decimal('.0000001'), rounding=ROUND_DOWN)))
            number = float(num)
            result.append(number)
        return result


def main():

    prob_counter = ProbCounter(sys.argv[1])
    output = open(sys.argv[2], 'w+')

    probs = prob_counter.get_symbol_probabilities()
    for i in range(len(probs)):
        output.write(str(probs[i]) + ("\n" if (i == (len(probs) - 1)) else " "))

    double_probs = prob_counter.get_double_symbol_probabilities()

    for i in range(len(double_probs)):
        output.write(('%.7f' % str(double_probs[i])) + ("\n" if (i == (len(double_probs) - 1)) else " "))


if __name__ == "__main__":
    main()
