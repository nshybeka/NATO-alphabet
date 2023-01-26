import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
user_word = input("Enter word: ").upper()
output_word = [phonetic_dict[letter] for letter in user_word]
print(output_word)
