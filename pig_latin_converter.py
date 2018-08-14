from string import ascii_letters
vowels = ["a","e", "i", "o", "u", "A", "E", "I", "O", "U"]
def vowel_position(word):
    pos = 0
    for letter in word:
        if letter in vowels:
            return pos
        pos += 1
    else:
        return "no_vowel"

def add_suffix(word):
    ls_word = list(word)
    vp = vowel_position(word)
    if vp == 0:
        ls_word.append("way")
        return "".join(ls_word)
    elif vp == "no_vowel":
        ls_word.append("ay")
        return "".join(ls_word)
    else:
        suf = ls_word[0:vp]
        ls_word = ls_word[vp:]
        for i in suf:
            ls_word.append(i)
        ls_word.append("ay")
        return "".join(ls_word)

