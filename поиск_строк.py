import linecache

input_file = 'update_base_employee.sql'
output_file = 'new_update_base_employee.sql'
line_str = [438, 168, 483, 187, 413, 311, 75, 275, 265, 440, 157, 364, 171, 304, 109, 255, 149, 201, 1, 459, 162, 26, 14, 196, 430, 222, 295, 388, 387, 89, 332, 433, 41, 334, 3, 308, 330, 456, 202, 405, 457, 284, 154, 45, 69, 401, 178, 68, 19, 474, 328, 368, 344, 282, 454]

with open(output_file,'w', encoding="utf-8") as fout:
        for str in range(len(line_str)):
            with open(input_file,'r', encoding="utf-8") as fin:
                l = line_str[str]
                for line in fin:
                    result = fin.readlines()[l - 2]
                    print(result)
                    print(result, file=fout)
        