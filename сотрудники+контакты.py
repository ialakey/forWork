input_file = 'id_users_actual.txt'
output_file = 'update.txt'

with open(input_file,'r', encoding="utf-8") as fin:
    with open(output_file,'w', encoding="utf-8") as fout:
        for line in fin:
            temp_line = line.strip().split(",")
            result = "update COMPANYADDON_BASE_EMPLOYEE set CONTACTS_ID='~' where ID='"+ temp_line [0] +"';"
            print(result)
            print(result, file=fout)

