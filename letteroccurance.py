sentence = input("Enter a sentence : ")

occurance = {}


for ch in sentence:
    if(ch not in occurance):
        occurance[ch] = 1
    else:
        occurance[ch] += 1

print(occurance)
