sentence = input("Enter an sentence: ")

count = 0

for word in list(sentence.split(" ")):
    print(word)
    count += 1

print("THE TOTAL NUMBER OF WORDS IN THE SENTENCE: ", count)
