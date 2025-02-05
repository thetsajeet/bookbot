def count_words_frequencies(text: str):
    freq = {}
    text = text.lower()
    for w in text:
        freq[w] = freq[w] + 1 if freq.get(w) is not None else 1
    return freq

def count_words(text: str):
    return len(text.split())

def main():

    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        total_words = count_words(file_contents)
        words_frequencies = count_words_frequencies(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{total_words} words found in the document")
        print('\n')

        for k, v in words_frequencies.items():
            if k.isalpha():
                print(f"The '{k}' character was found {v} times")
        
        print("--- End report ---")
main()
