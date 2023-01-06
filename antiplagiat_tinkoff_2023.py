import sys


def distance(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    if len(a) == len(b) == 0:
        return 1.0

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return 1 - current_row[n] / len(b)


input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

input_file = open(input_file_path, 'r')
output_file = open(output_file_path, 'w')

requests = input_file.readlines()
input_file.close()
answers = []
for q in requests:
    file1_path, file2_path = q.split()
    file1 = open(file1_path, 'r', encoding="utf8")
    file2 = open(file2_path, 'r', encoding="utf8")
    str1 = file1.read()
    str2 = file2.read()
    answers.append(str(distance(str1, str2)) + '\n')
    file1.close()
    file2.close()

output_file.writelines(answers)
output_file.close()
