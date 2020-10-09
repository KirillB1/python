subj = {}
with open('les5_dz6_file.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture,lecture_sk, practice,practice_sk, lab,lab_sk = line.split()
        
     
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')
