import string
from collections import Counter
import os
import sys
import nltk 
from nltk.corpus import stopwords
import FAlib 

print("Loading first text...")
text1 = FAlib.read_file(r"C:\Users\vyach\Documents\GitHub\Frequency-Analisys\Text Examples\1. 12 chairs.txt")
print("Loading second text...")
text2 = FAlib.read_file(r"C:\Users\vyach\Documents\GitHub\Frequency-Analisys\Text Examples\2. Moscow from dawn to dawn.txt")
print("Loading third text...")
text3 = FAlib.read_file(r"C:\Users\vyach\Documents\GitHub\Frequency-Analisys\Text Examples\3. A story about one sun.txt")
print("Loading fourth text...")
text4 = FAlib.read_file(r"C:\Users\vyach\Documents\GitHub\Frequency-Analisys\Text Examples\4. Dog's heart.txt")

FAlib.print_chars([text1,text2,text3,text4])

sents_info1 = FAlib.sents_analyze(text1)
sents_info2 = FAlib.sents_analyze(text2)
sents_info3 = FAlib.sents_analyze(text3)
sents_info4 = FAlib.sents_analyze(text4)

word_count1 = sum(sents_info1[0])
word_count2 = sum(sents_info2[0])
word_count3 = sum(sents_info3[0])
word_count4 = sum(sents_info4[0])

average1 = round(word_count1 / sents_info1[1], 2)
average2 = round(word_count2 / sents_info2[1], 2)
average3 = round(word_count3 / sents_info3[1], 2)
average4 = round(word_count4 / sents_info4[1], 2)

freqs1 = FAlib.freq_analyze(text1)
freqs2 = FAlib.freq_analyze(text2)
freqs3 = FAlib.freq_analyze(text3)
freqs4 = FAlib.freq_analyze(text4)

FAlib.analyze([freqs1,freqs2,freqs3,freqs4], [average1,average2,average3,average4])

# text = FAlib.read_file("C:\Coding\Python\\tol.txt")

# sents_info = FAlib.sents_analyze(text)
    

# word_count = sum(sents_info[0])
    
# average = round(word_count / sents_info[1], 2)

# freqs = FAlib.freq_analyze(text)


