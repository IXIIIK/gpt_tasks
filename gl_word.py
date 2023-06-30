def search_word(text):
    gl_words = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0,
                }
    
    for i in text:
        if i in gl_words:
            gl_words[i] += 1
    return gl_words
        
