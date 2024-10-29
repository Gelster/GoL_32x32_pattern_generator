pattern_folder = 'C:\\Users\\Podhr\\Documents\\GoL\\PatternGenerator\\patterns\\'

with open(pattern_folder+'20240629_00-59-32.csv') as f:
    lines = f.readlines()

temp_list = ''
len_counter = 0
for line in  lines:
       for char in line:
              if (char == '0') or (char == '1'):
                     temp_list += char
                     len_counter+=1
              if len_counter == 32:
                     temp_list += "\n"
                     len_counter= 0


with open("C:\\Users\\Podhr\\Documents\\GoL\\PatternGenerator\\txt_export\\File.txt", "w") as f:   # Opens file and casts as f
    f.write(temp_list)