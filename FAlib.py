import string
from collections import Counter
import os
import sys
import nltk 
from nltk.corpus import stopwords



def print_chars(text, num_chars):
    print(text[:num_chars]+ "...")

def print_chars(texts = []):
    counter = 1
    for text in texts:
        lines = text.split('\n')  # Разделить текст на строки
        if lines:  # Проверить, что есть хотя бы одна строка
            print(f"{counter} text: " + lines[0])  # Вывести первую строку
            counter += 1


def read_file(path):
    f = open(path, "r", encoding="utf-8")
    return f.read()

def freq_analyze(text):
    string.punctuation += "…’„»«1234567890–-—"
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

def analyze(freqs_arr = [],average_arr = []):
    text_counter = 1
    for freqs,average in zip(freqs_arr,average_arr):
        # ���������� ���������� ������� �� �������� �������
        sorted_freqs = dict(sorted(freqs.items(), key=lambda x: (-x[1], x[0])))

       # Открытие файла для записи результатов
        with open(f"C:/Users/vyach/Documents/GitHub/Frequency-Analisys/Result/Result.txt", "a", encoding="utf-8") as f:

            f.write(f"{text_counter} текст.")
            # Вывод среднего значения слов в каждом предложении
            f.write(f"\nСреднее значение слов в каждом предложении: {average}\n")

            # Вывод частот слов в тексте
            f.write("Частоты слов в тексте:\n")

            # Вывод отформатированных частот слов
            i = 0
            x = 0
            for word, freq in sorted_freqs.items():
                if freq != x:
                    x = freq
                    if x == freq:
                        i = 0
                        f.write("\n")
                    f.write(f"{freq}:\n{word}, ")
                else:
                    if i == 9:
                        f.write("\n")
                        i = 0
                    if freq > 1:  # Выводим слова, частота которых больше 1
                        f.write(f"{word}, ")
                        i += 1
            f.write("\n")
        # Вывод завершенного сообщения
        print(f"{text_counter} text: done...")
        text_counter += 1