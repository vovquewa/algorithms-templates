def is_correct_bracket_seq(seq: str):
    brackets = ['[]', '{}', '()']
    while '[]' in seq or '{}' in seq or '()' in seq:
        for bracket in brackets:
            seq = seq.replace(bracket, '')
    return seq == ''


print(is_correct_bracket_seq('{[()]}'))
