import string
from collections import Counter
import os
import sys
import nltk 
from nltk.corpus import stopwords 

def read_file(path):
    f = open(path, "r", encoding="utf-8")
    return f.read()

def freq_analyze(text):
    string.punctuation += "…’„»«1234567890–-"
    filter = string.punctuation
    stop_wordsRU=(stopwords.words('russian')) 
    stop_wordsEN=(stopwords.words('english'))
    #nltk.download('stopwords') # Загрузка стоп-слов, если необходимо
    words = [word for word in text.translate(str.maketrans("", "", filter)).lower().split()]
    words = [word for word in words if word not in stop_wordsRU]
    words = [word for word in words if word not in stop_wordsEN]
    words = [word for word in words if words.count(word) >= 1]
    return Counter(words)
    
# Анализ текста по предложениям
def sents_analyze(text):
    sentences = sent_tokenize(text) 
    word_counts = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        word_counts.append(len(words))
    return word_counts, len(sentences)

# Разбитие текста на предложения
def sent_tokenize(text):
    sentences = []
    sentence = ""
    for char in text:
        sentence += char
        if check_mark(char):
            sentences.append(sentence)
            sentence = ""
    return sentences

# Проверка символа is mark? 
def check_mark(char):
    if char in ['?', '!', '.']:
        return True
    return False

# Разбитие текста на слова
def word_tokenize(sentence):
    chars = ""
    words = []
    for char in sentence:
        chars += char
        if char == " " or check_mark(char):
            words.append(chars.strip())
            chars = ""

    return words


# Пример текста для анализа
text = read_file("C:\Coding\Python\\tol.txt")

# ������ ���������� ���� � ������������
sents_info = sents_analyze(text)
    
# Вычисляем количество слов в предложениях
# for words in sents_info[0]:
#         word_count += words
word_count = sum(sents_info[0])
    
# Вычисляем среднее значение слов в каждом предложении
average = round(word_count / sents_info[1], 2)

# Вызываем функцию частотного анализа и выводим результат
freqs = freq_analyze(text)


#####################################################################################

# ���������� ���������� ������� �� �������� �������
sorted_freqs = dict(sorted(freqs.items(), key=lambda x: (-x[1], x[0])))

# ��������� ���� ��� ������ ������
sys.stdout = open("C:\Coding\Python\FrequencyAnalisys v.2\\result_filteredFreq.txt", "w", encoding="utf-8")

# ������� ������� ���������� ���� � ������������
print(f"Среднее значение слов в каждом предложении:{average}")

# ������� ��������� ��� ������ ������ ���� � ������
print("Частоты слов в тексте:")

# ������� ��������� �����
i = 0
x = 0
for word, freqs in sorted_freqs.items():
    if freqs != x:
        x = freqs
        if x == freqs:
            i = 0
            print("")
        print(f"{freqs}:\n{word}, ",end="")
    else:
        if i == 9:
            print("")
            i = 0
        if freqs > 1:  # ��������� �����, ������� ����������� ������ 1 ���
            print(f"{word}, ",end="")
            i = i + 1

# ��������� ���� ������
sys.stdout.close()
sys.stdout = sys.__stdout__  # ��������������� ����������� �����
print("Done...")
