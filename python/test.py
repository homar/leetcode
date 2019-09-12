f = open("/home/konrad/Downloads/Ankieta.csv", "r")
biggest_company = []
for line in f:
    columns = line.split("\",\"")
    if "150 pracowni" in columns[6]:
        biggest_company.append(line)

print "firm z ponad 150 jest " + str(len(biggest_company))
biggest_and_foreign = []
for line in biggest_company:
    columns = line.split("\",\"")
    if "zagraniczny" in columns[9]:
        biggest_and_foreign.append(line)

print "firm z kapitalem zagranicznym jest " + str(len(biggest_and_foreign))
bigget_foreign_1_on_1_very_often = []
bigget_foreign_1_on_1_often = []
bigget_foreign_1_on_1_rare = []
for line in biggest_and_foreign:
    columns = line.split("\",\"")
    if "tak w" in columns[12]:
        bigget_foreign_1_on_1_very_often.append(line)
    elif "tak raz w miesi" in columns[12]:
        bigget_foreign_1_on_1_often.append(line)
    else:
        bigget_foreign_1_on_1_rare.append(line)
print "firm gdzie czesciej niz raz w mieisacu sa 1:1 jest " + str(len(bigget_foreign_1_on_1_very_often))

bigget_foreign_1_on_1_very_often_boss_trusts = []
bigget_foreign_1_on_1_very_often_ppl_trust_boss = []
bigget_foreign_1_on_1_very_often_can_rely_on_boss = []
for line in bigget_foreign_1_on_1_very_often:
    columns = line.split("\",\"")
    if "ony okazuje zaufanie do pracownik" in columns[27]:
        bigget_foreign_1_on_1_very_often_boss_trusts.append(line)
    elif "zaufanie do prze" in columns[27]:
        bigget_foreign_1_on_1_very_often_ppl_trust_boss.append(line)
    elif "na swojego prze" in columns[27]:
        bigget_foreign_1_on_1_very_often_can_rely_on_boss.append(line)

bigget_foreign_1_on_1_often_boss_trusts = []
bigget_foreign_1_on_1_often_ppl_trust_boss = []
bigget_foreign_1_on_1_often_can_rely_on_boss = []
for line in bigget_foreign_1_on_1_often:
    columns = line.split("\",\"")
    if "ony okazuje zaufanie do pracownik" in columns[27]:
        bigget_foreign_1_on_1_often_boss_trusts.append(line)
    elif "zaufanie do prze" in columns[27]:
        bigget_foreign_1_on_1_often_ppl_trust_boss.append(line)
    elif "na swojego prze" in columns[27]:
        bigget_foreign_1_on_1_often_can_rely_on_boss.append(line)

bigget_foreign_1_on_1_rare_boss_trusts = []
bigget_foreign_1_on_1_rare_trust_boss = []
bigget_foreign_1_on_1_rare_can_rely_on_boss = []
for line in bigget_foreign_1_on_1_rare:
    columns = line.split("\",\"")
    if "ony okazuje zaufanie do pracownik" in columns[27]:
        bigget_foreign_1_on_1_rare_boss_trusts.append(line)
    elif "zaufanie do prze" in columns[27]:
        bigget_foreign_1_on_1_rare_trust_boss.append(line)
    elif "na swojego prze" in columns[27]:
        bigget_foreign_1_on_1_rare_can_rely_on_boss.append(line)

print "szef ufa {}".format(len(bigget_foreign_1_on_1_very_often_boss_trusts))
print "ufa szefowi {}".format(len(bigget_foreign_1_on_1_very_often_ppl_trust_boss))
print "polega na szefie {}".format(len(bigget_foreign_1_on_1_very_often_can_rely_on_boss))
print "Firm z kadra liczaca ponad 150 ludzi z kapitalem zagranicznym jest {}, w {} 1:1 odbywaja sie czesciej niz raz w miesiacu, w {} raz w miesiacu i w {} rzadziej ".format(len(biggest_and_foreign), len(bigget_foreign_1_on_1_very_often), len(bigget_foreign_1_on_1_often), len(bigget_foreign_1_on_1_rare))
print "Tam gdzie czesciej niz raz w miesiacy {}% ufa szefowi ".format((len(bigget_foreign_1_on_1_very_often_boss_trusts) + len(bigget_foreign_1_on_1_very_often_ppl_trust_boss) + len(bigget_foreign_1_on_1_very_often_can_rely_on_boss)) * 100 / len(bigget_foreign_1_on_1_very_often))
print "Tam gdzie raz w miesiacy {}% ufa szefowi ".format((len(bigget_foreign_1_on_1_often_boss_trusts) + len(bigget_foreign_1_on_1_often_ppl_trust_boss) + len(bigget_foreign_1_on_1_often_can_rely_on_boss)) * 100 / len(bigget_foreign_1_on_1_often))