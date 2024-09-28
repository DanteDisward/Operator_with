class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        clear_chars = [',', '.', '=', '!', '?', ';', ':', ' - ', '…']
        for file_name in self.file_names:
            new_string = ''
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    for char in line.lower():
                        if char not in clear_chars:
                            new_string += char
                all_words[str(file_name)] = new_string.split()
        return all_words

    def find(self, word):
        text = self.get_all_words()
        file_name = {}
        for name, words in text.items():
            if word.lower() in words:
                file_name[name] = words.index(word.lower())
        return file_name

    def count(self, word):
        text = self.get_all_words()
        count_word = {}
        for name, words in text.items():
            if word.lower() in words:
                count_word[name] = words.count(word.lower())
        return count_word


finder2 = WordsFinder('Самых_честных_правил.txt', 'Узник.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('мОй'))  # 3 слово по счёту
print(finder2.count('тудА'))  # 4 слова teXT в тексте всего
