text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel.'
        ' Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
words = text.split()
print(text)
final_text = []
for word in words:
    if '.' in word:
        final_text.append(word.replace('.', '') + 'ing.')
    elif ',' in word:
        final_text.append(word.replace(',', '') + 'ing,')
    else:
        final_text.append(word + 'ing')
print(' '.join(final_text))
