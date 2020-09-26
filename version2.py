import re
file = open("D:/Лабы/ЛОГпрог/лаба1/Tree.ged", "r")
file_w = open("D:/Лабы/ЛОГпрог/лаба1/out.pl", "w")
list_person=[]
for line in file:
    if  re.search(r'GIVN', line):
        name=line[7:]
        name=name.lower()
        name=name.replace("\n", "")
    if re.search(r"SURN", line):
        surname = line[7:]
        surname=surname.lower()
        surname=surname.replace("\n", "")
        list_person.append(name+"_"+surname)
    if re.search(r"SEX", line):
        sex = line[6:]
        sex=sex.lower()
        sex=sex.replace("\n", "")
        q="sex(" + name+"_"+ surname+ ", "+ sex+ ").\n"
        file_w.write(q)
    if re.search(r"HUSB", line):
        Husb = int(line[10:15])
    if re.search(r"WIFE", line):
        Wife = int(line[10:15])
    if re.search(r"CHIL", line):
        Chil = int(line[10:15])
        parent="parent("+list_person[Husb-1]+", "+list_person[Chil-1]+").\n"
        file_w.write(parent)
        parent = "parent(" + list_person[Wife - 1] + ", " + list_person[Chil - 1] + ").\n"
        file_w.write(parent)
file.close()
file_w.close()