import codecs
from datetime import date, timedelta

assignments = []
total_assignments = 0
solved_assignments = 0
comments = []


def write_assignments(newfilename, assignments, total_assignments, comments):
    today = date.today()
    today_str = today.strftime("%d.%m.%Y")

    ff = codecs.open(newfilename, "w", encoding='utf-8-sig')
    counter = 0
    for item in assignments:
        ff.write('$\n')
        ff.write(item[0])
        ff.write('%\n')
        ff.write(item[1])
        ff.write('@\n')
        ff.write('0 ' + today_str + '\n')
        counter += 1
    for c in comments:
        ff.write('& ' + c + '\n')

    if counter > 0:
        ff.write('&\n')
        ff.write('& ' + str(counter) + '\n')
        ff.write('&\n')

    ff.close()


now = date.today()
oldfilename = input("Old Filename: ")
f = codecs.open(oldfilename, 'r', encoding='utf-8-sig')
line = f.readline().strip()
while len(line) == 0:
    line = f.readline().strip()

while True:
    try:
        ch = line[0]
        if ch == '&':
            break
        if ch == '$':
            # читаем следующие две единицы информации и добавляем юнит в список assignment
            new_item = []
            next_string = ''
            line = f.readline().rstrip()
            while len(line) == 0 or line[0] != '%':
                next_string += (line + '\n')
                line = f.readline().rstrip()
            new_item.append(next_string)
            next_string = ''
            line = f.readline().rstrip()
            while len(line) == 0 or line[0] != '$' and line[0] != '&':
                next_string += (line + '\n')
                line = f.readline().rstrip()
            new_item.append(next_string)
            new_item += [0, 0, 0]
            assignments.append(new_item)
            total_assignments += 1
            continue
        line = f.readline().rstrip()
    except EOFError:
        break

while line:
    comments.append(line[1:].strip())
    line = f.readline().strip()

f.close()

newfilename = input("New Filename: ")

write_assignments(newfilename, assignments, total_assignments, comments)

print("All done!")

