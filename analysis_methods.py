import mpld3
from scipy.stats import spearmanr
import numpy as np
import matplotlib.pyplot as plt
import file_paths as fp

def pearson(freqs_list = [], filenames = []):
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        for j, ax in enumerate(axes.flatten()):
            # Расчет корреляции Пирсона
            common_words = set(freqs_list[0].keys()) & set(freqs_list[j+1].keys())
            # Получение точек
            x = np.array([freqs_list[0][word] for word in common_words], dtype=np.float64)
            y = np.array([freqs_list[j+1][word] for word in common_words], dtype=np.float64)
            pearson_corr = np.corrcoef(x, y)[0, 1]
            # Названия осей
            ax.set_xlabel(f'Частоты в {filenames[0]}')
            ax.set_ylabel(f'Частоты в {filenames[j]}')
            ax.scatter(x, y)
            ax.set_title(f'Корреляция Пирсона: {pearson_corr:.2f}')  
        mpld3.save_html(fig, fp.default_path_figures + "pearson.html")
        plt.tight_layout()
        plt.show()

def spearman(freqs_list = [], filenames = []):  
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        for j, ax in enumerate(axes.flatten()):
            # Расчет корреляции Спирмена
            common_words = set(freqs_list[0].keys()) & set(freqs_list[j+1].keys())
            # Получение точек
            x = np.array([freqs_list[0][word] for word in common_words], dtype=np.float64)
            y = np.array([freqs_list[j+1][word] for word in common_words], dtype=np.float64)
            spearman_corr = spearmanr(x, y)[0]
            # Названия осей
            ax.set_xlabel(f'Частоты в {filenames[0]}')
            ax.set_ylabel(f'Частоты в {filenames[j]}')
            ax.scatter(x, y)
            ax.set_title(f'Корреляция Спирмена: {spearman_corr:.2f}')
        mpld3.save_html(fig, fp.default_path_figures + "spearman.html")
        plt.tight_layout()
        plt.show()

def odds_ratios(freqs_list = [], filenames = []):  
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        for j, ax in enumerate(axes.flatten()):
            # Расчет корреляции Отношения шансов
            common_words = set(freqs_list[0].keys()) & set(freqs_list[j+1].keys())
            odds_ratios = {}
            for word in common_words:
                a = np.array([freqs_list[0][word]], dtype=np.float64)
                b = np.array([sum(freqs_list[0].values()) - a], dtype=np.float64)
                c = np.array([freqs_list[j+1][word]], dtype=np.float64)
                d = np.array([sum(freqs_list[j+1].values()) - c], dtype=np.float64)
                odds_ratio = (a * d) / (b * c)
                odds_ratios[word] = odds_ratio
            # Получение точек
            words = list(odds_ratios.keys())
            values = list(odds_ratios.values())
            # Названия осей
            ax.set_xlabel(f'Частоты в {filenames[0]}')
            ax.set_ylabel(f'Частоты в {filenames[j]}')
            ax.scatter(words, values)
            ax.set_title('Отношение шансов')
        mpld3.save_html(fig, fp.default_path_figures + "odds_ratios.html")
        plt.tight_layout()
        plt.show()

        # Определение функции для вычисления корреляции
def calculate_pearson_correlation(freqs1, freqs2):
    common_words = set(freqs1.keys()) & set(freqs2.keys())
    x = [freqs1[word] for word in common_words]
    y = [freqs2[word] for word in common_words]
    return np.corrcoef(x, y)[0, 1]

def calculate_spearman_correlation(freqs1, freqs2):
    common_words = set(freqs1.keys()) & set(freqs2.keys())
    x = [freqs1[word] for word in common_words]
    y = [freqs2[word] for word in common_words]
    return spearmanr(x, y)[0]

def calculate_odds_ratio(freqs1, freqs2):
    common_words = set(freqs1.keys()) & set(freqs2.keys())
    odds_ratios = {}
    for word in common_words:
        a = freqs1[word]
        b = sum(freqs1.values()) - a
        c = freqs2[word]
        d = sum(freqs2.values()) - c
        odds_ratio = (a * d) / (b * c)
        odds_ratios[word] = odds_ratio
    return odds_ratios