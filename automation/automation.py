import re

def read_file():
    with open('./assets/potential-contacts.txt','r') as file:
        all_lines = file.read()
    return all_lines


def emails():
    content = read_file()
    email_validation = r'([\w\.-]+)@([\w\.-]+)'
    valid_emails = re.findall(email_validation,content)
    for i in range(len(valid_emails)):
        valid_emails[i]= '@'.join(valid_emails[i])

    valid_emails.sort()    

    unique =[]
    with open('./assets/emails.txt','w') as file:
        for i in valid_emails:
            if i not in unique:
                file.write(str(i)+'\n')
            unique.append(i)
    with open ('./assets/existing-contacts.txt' , 'r') as compare_f:
        lst_emails = []
        count = 0
        for line in compare_f:
            if count % 2 !=0:
                stripped_line = line.strip()
                lst_emails.append(stripped_line)
            count+=1
        for i in lst_emails:
            if i not in unique:
                unique.append(i)    
            

def phone_numbers():
    content = read_file()
    phone_validation = r'([+]?[(]?[0-9]{1,4}[)]?)([-|.]?[0-9]{1,4})([-|.]?[0-9]{1,4})([-|.]?([0-9]{1,4})?)([x]?([0-9]{1,7})?)'
    valid_phone_numbers = re.findall(phone_validation,content)
    for i in range(len(valid_phone_numbers)):
        valid_phone_numbers[i]= list(valid_phone_numbers[i])
        valid_phone_numbers[i][4]=''
        valid_phone_numbers[i][6]=''
        valid_phone_numbers[i]= ''.join(valid_phone_numbers[i])

    valid_phone_numbers.sort()    

    unique =[]
    with open('./assets/phone_numbers.txt','w') as file:
        for i in valid_phone_numbers:
            if i not in unique:
                if i[0]== '+' or i[0] == '(':
                    file.write(str(i)+'\n')
                elif i[0]=='0' and i[1]=='0' and i[2]=='1':
                    file.write(str(i)+'\n')
                else:
                    file.write('206-'+str(i)+'\n')
            unique.append(i)
            
    with open ('./assets/existing-contacts.txt' , 'r') as compare_f:
        lst_phones = []
        count = 0
        for line in compare_f:
            if count % 2 ==0:
                stripped_line = line.strip()
                lst_phones.append(stripped_line)
            count+=1
        for i in lst_phones:
            if i not in unique:
                unique.append(i)

emails()
phone_numbers()