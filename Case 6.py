subj = {}
with open('file_6.txt', 'r', encoding='utf-8') as init_f:
    for line in init_f:
        subject, lecture = line.split(':')
        subj[subject] = sum(map(int, ''.join([i for i in lecture if i == ' ' or ('0' <= i <= '9')]).split()))
    print(f'Общее количество часов по предмету - \n {subj}')
