
def single_root_words(root_word, *other_words):
    same_words = []
    my_root_word = root_word.lower()
    for i in range(len(other_words)):
        elem_ = other_words[i]
        if my_root_word in elem_.lower() or elem_.lower() in my_root_word:
            same_words.append(elem_)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

#['richiest', 'orichalcum', 'richies']
#['Able', 'Disable']