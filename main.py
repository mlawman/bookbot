def main():
    print(getReport("books/frankenstein.txt"))

def getReport(bookFile):
    with open(bookFile) as f:
        file_contents = f.read()
    
    words = countWords(file_contents)
    chars = charCount(file_contents)

    report = f"--- Begin report of {bookFile} ---\n"
    report += f"{words} words found in the document\n\n"
    for char in chars:
        report += f"The '{char}' character was found {chars[char]} times\n"

    report += f"--- End report ---"
    
    return report


def countWords(book_text):
    return len(book_text.split())

def charCount(book_text):
    chars = {}
    for char in book_text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars


main()