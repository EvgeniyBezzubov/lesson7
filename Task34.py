#Максимально странное ТЗ
class Winni_Puh():  # в ТЗ ничего не скзано про крассы, но я сделал, т.к. у нас домашка про это
    vowels = ["й", "у", "е", "ы", "а", "о", "э", "я", "и", "ю"]  # атрибут класса

    def __init__(self, phrase):
        self.pharse = phrase

    def count_vowels(self):

        lst = self.pharse.split(" ")
        vowels_count = 0
        vowels_count_word = []
        for word in lst:  # считаем количество гласных в каждом слове
            vowels_count = 0
            for letter in word:
                if letter in self.vowels:
                    vowels_count += 1
            vowels_count_word.append(vowels_count)  # заносим количество гласных в каждом слове в лист

        if len(set(
                vowels_count_word)) != 1:  # избавляемся от дублей в листе и если количество больше 1, то это значит что в разных словах разное количество гласных
            return "“Пам парам”"
        else:
            return "“Парам пам-пам”"


pharse = input("Введите фразы, фразы должны быть разделены пробелами,В каждой фразе может быть больше однгшо слова, "
               "если слдов больше одного, они разделены дефисами:")
obj1 = Winni_Puh(pharse)
print(obj1.count_vowels())
