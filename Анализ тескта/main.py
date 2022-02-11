import zipfile

zip_archive = zipfile.ZipFile("voyna-i-mir.zip", 'r')
zip_archive.extract("voyna-i-mir.txt")
zip_archive.close()

open_file = open("voyna-i-mir.txt", 'r', encoding='utf-8')
voyna_i_mir = open_file.read()
open_file.read()

tuple_list = {}
count_symbol = 0
for i_letter in voyna_i_mir:
    count_symbol += 1
    if i_letter.isalpha():
        if i_letter in tuple_list:
            tuple_list[i_letter] += 1
        else:
            tuple_list[i_letter] = 1

open_file = open("analysis.txt", 'w+', encoding='utf-8')
for i_key, i_value in sorted(tuple_list.items(), key=lambda x: (-x[1], x[0])):
    open_file.write(f"{i_key} {round(i_value / count_symbol, 3)}\n")
open_file.seek(0)
print(f"Содержимое файла analysis.txt:\n{open_file.read()}\n")
open_file.close()

