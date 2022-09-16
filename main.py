import table
import fun

lexico = []
with open('lexico_v3.0.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    a = lines[i].split(',')
    a[3] = a[3][0]
    lexico.append(a)

H = table.HTable()
H.take_f(fun.f2)
H.put(lexico)
# H.print_table()
print(H.col_cont)
print(H.meantime_put)