def main():
    path_to_file = "books/frankenstein.txt"
    text = get_text(path_to_file)
    word_count = count_words(text)
    
    print(f"\n--- Begin report of books/frankenstein.txt ---\n\n{word_count} words found in the document\n\n")
    count_letters(text)
    
def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    characters = "".join(text.split()).lower()
    letters = list(filter(lambda c: c.isalpha(), characters))
    letters.sort()
    log = {}
    for letter in letters:
        if letter in log:
            log[letter] += 1
        else:
            log[letter] = 1
    for k in log:
        print (f"The '{k}' character was found {log[k]} times")

main()