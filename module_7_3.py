class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
    def get_all_words(self):
        words_ = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding = 'utf-8') as file:
                text_words = []
                for text_ in file:
                    text_ = text_.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for symbol in punctuation:
                        text_ = text_.replace(symbol, '' if symbol != ' - ' else ' ')
                    text_words.extend(text_.split())
                words_[file_name] = text_words
        return words_

    def find(self, word):
         word = word.lower()
         result = {}
         for file_name, words in self.get_all_words().items():
             result[file_name] = words.index(word) + 1
         return result

    def count(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

