from spellchecker import SpellChecker

spell = SpellChecker()

def check_spelling(text):
    words = text.split()
    misspelled = spell.unknown(words)

    corrections = {}
    for word in misspelled:
        corrections[word] = spell.correction(word)

    corrected_words = []
    for word in words:
        corrected_words.append(corrections.get(word, word))

    corrected_text = " ".join(corrected_words)

    return corrected_text, corrections