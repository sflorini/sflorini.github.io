words = ["color" , "color", "colour" , "amok" , "amok" , "amuk"]

canonical = ["color" , "amok"]

mappings = {"colour": "color" , "amuk": "amok"}

new_list = []

for word in words:
    if word in mappings:
        #if a word is mispelled do something
        #correct the spelling using the mappings dictionary

        corrected_word = mappings[word]

        #add that corrected word

        new_list.append(corrected_word)
else:
    new_list.append(word)

print(new_list)
