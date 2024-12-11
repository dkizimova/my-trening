def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    other_words = map(str.lower, other_words)
    for word in other_words:
        if root_word in word or word in root_word:
            same_words.append(word)
    return same_words


print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
