# TODO  Напишите функцию count_letters
def count_letters(text):
    return {x: text.lower().count(x) for x in text.lower() if x.isalpha()}


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_data: dict):
    return {letter: amount/amount_of_all_letters for letter, amount in letters_data.items()}


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
amount_of_all_letters = len([x for x in main_str if x.isalpha()]) #считаем сколько всего букв в тексте
amount_of_each_letter = count_letters(main_str) # словарь с буквами и их количествами каждой

for key, value in calculate_frequency(amount_of_each_letter).items():
    print(f'{key}: {value:s.2f}')
