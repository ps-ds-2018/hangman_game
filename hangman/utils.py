def find_idx(word, ch):
    return [i for i, c in enumerate(word) if c == ch]

def replace_chars_at_indices(masked_word, indices, user_input):
    s_list = list(masked_word)
    for index in indices:
        s_list[index] = user_input
    return ''.join(s_list)
