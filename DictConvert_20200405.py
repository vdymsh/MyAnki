import codecs
from datetime import date, timedelta


# total_assignments = 0
# solved_assignments = 0


class AddedWords:
    def __init__(self, entries=dict()):
        self.entries = entries

    def add_entry(self, word, translation):
        # word - the word, translation - list of translation words
        self.entries[word] = translation


def read_added_words(filename, words_dict):
    try:
        with codecs.open(filename, "r", encoding="utf-8-sig") as ff:
            for line in ff:
                line = line.strip().lower()
                n = line.find(' ')
                if n == -1:
                    n = 9999
                m = line.find('\t')
                if m == -1:
                    m = 9999
                pos = min(n, m)
                if pos != 9999:
                    entry = line[:pos]
                    translation = line[pos + 1:].lstrip()
                    words_dict.entries[entry] = translation
    except FileNotFoundError:
        print("File not found")


def write_assignments(base_filename, assignments):
    today = date.today()
    today_str = today.strftime("%d.%m.%Y")

    ff = codecs.open(base_filename, "w", encoding='utf-8-sig')
    counter = 0
    for key, value in assignments.items():
        ff.write('$\n')
        ff.write(key + '\n')
        ff.write('%\n')
        ff.write(value + '\n')
        ff.write('@\n')
        ff.write('0 ' + today_str + '\n')
        counter += 1

    if counter > 0:
        ff.write('&\n')
        ff.write('& ' + str(counter) + '\n')
        ff.write('&\n')
    ff.close()


def main():
    now = date.today()
    dict_filename = input("Dictionary Filename: ")
    added_words = AddedWords()
    read_added_words(dict_filename, added_words)

    base_filename = input("Base Filename: ")
    write_assignments(base_filename, added_words.entries)

    print("All done!")


if __name__ == "__main__":
    main()
