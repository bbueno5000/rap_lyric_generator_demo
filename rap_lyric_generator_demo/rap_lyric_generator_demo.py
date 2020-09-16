"""
DOCSTRING
"""
import random
import re

def add_to_dict(file_name, freq_dict):
    """
    freq_dict: a dict of dict containing frequencies
    """
    f = open(file_name, 'r')
    words = re.sub("\n", " \n", f.read()).lower().split(' ')
    for curr, succ in zip(words[1:], words[:-1]):
        if curr not in freq_dict:
            freq_dict[curr] = {succ: 1}
        else:
            if succ not in freq_dict[curr]:
                freq_dict[curr][succ] = 1;
            else:
                freq_dict[curr][succ] += 1;
    prob_dict = {}
    for curr, currDict in freq_dict.items():
        prob_dict[curr] = {}
        currTotal = sum(currDict.values())
        for succ in currDict:
            prob_dict[curr][succ] = currDict[succ] / currTotal
    return prob_dict

def make_rap(curr, prob_pict, T = 50):
    """
    DOCSTRING
    """
    rap = [curr]
    for t in range(T):
        rap.append(markov_next(rap[-1], prob_pict))
        return " ".join(rap)

def markov_next(curr, prob_dict):
    """
    DOCSTRING
    """
    if curr not in prob_dict:
        return random.choice(list(prob_dict.keys()))
    else:
        succ_probs = prob_dict[curr]
        rand_prob = random.random()
        curr_prob = 0.0
        for succ in succ_probs:
            curr_prob += succ_probs[succ]
            if rand_prob <= curr_prob:
                return succ
        return random.choice(list(prob_dict.keys()))

if __name__ == '__main__':
    rap_freq_dict = {}
    rap_freq_dict = add_to_dict('lyrics1.txt', rap_freq_dict)
    rap_freq_dict = add_to_dict('lyrics2.txt', rap_freq_dict)
    start_word = input("What do you want to start your rap with?\n > ")
    print("Alright, here's your rap:")
    print(make_rap(start_word, rap_prob_dict))
