def filter_badwords(text, bad_words, replace_with) -> str:
    words = text.split(' ')
    filterd = []
    for word in words:
        if word.lower() in bad_words:
            filterd.append(replace_with)
        else:
            filterd.append(word)
    filterd = ' '.join(filterd)

    return filterd