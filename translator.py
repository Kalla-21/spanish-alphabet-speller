import streamlit as st

def english_to_spanish(word):
    spanish_letters = {
        'a': 'a',
        'b': 'be',
        'c': 'ce',
        'd': 'de',
        'e': 'e',
        'f': 'efe',
        'g': 'ge',
        'h': 'hache',
        'i': 'i',
        'j': 'jota',
        'k': 'ka',
        'l': 'ele',
        'm': 'eme',
        'n': 'ene',
        'ñ': 'enye',
        'o': 'o',
        'p': 'pe',
        'q': 'cu',
        'r': 'erre',  # will handle double r separately
        's': 'ese',
        't': 'te',
        'u': 'u',     # keep 'u' as "u"
        'v': 'uve',
        'w': 'uve doble',
        'x': 'equis',
        'y': 'ye',
        'z': 'zeta'
    }

    word = word.lower()
    result = []
    i = 0

    while i < len(word):
        # Special case: double r → "erre"
        if i + 1 < len(word) and word[i] == 'r' and word[i+1] == 'r':
            result.append('erre')
            i += 2
            continue

        ch = word[i]
        if ch in spanish_letters:
            result.append(spanish_letters[ch])
        else:
            result.append(ch)
        i += 1

    return '/'.join(result)

# --- Streamlit UI ---
st.title("English to Spanish Letter Speller")
st.write("Type any English word to see its spelling in Spanish letters.")

word = st.text_input("Enter an English word:")

if word:
    translation = english_to_spanish(word)
    st.success(f"**Spanish spelling:** {translation}")
