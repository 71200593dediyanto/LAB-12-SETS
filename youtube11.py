# Dedi Yanto
# 71200593
# Universitas Kristen Duta Wacana
# Prodi Teknik Informatika
# Sets

'''

Suatu hari Gita yang sedang gabut ingin mengetahui himpunan apa saja
yang berbeda di antara dua kata. Karena pacar nya Gita adalah mahasiswa IT,
Gita meminta pacarnya untuk membuat kan sebuah program yang dapat mencari 
himpunan apa saja yang berbeda dalam sebuah kata dengan membandingkannya 
dengan kata lain, Gita memberikan contoh, jika diberikan kata ke-1 kamu, 
kata ke-2 dia,dan kata ke-3 aku, Gita ingin mengetahui himpunan apa saja 
yang berbeda di kata kamu dan dia, kamu dan aku, dan dia dan aku. 
Anggap lah anda adalah pacarnya Gita, bantulah Gita membuat program 
yang dapat membantu permasalahannya!

'''

'''
Input:
masukkan banyaknya data : 3
kata 1 : mendung
kata 2 : cerah
kata 3 : hujan

Proses:
{'mendung','cerah','hujan'}

mendung 
cerah

d g m n u
a c h r

d g m n u a c h r

Output:
huruf yang berbeda di kata mendung dan kata cerah adalah d g m n u a c h r
huruf yang berbeda di kata mendung dan kata hujan adalah . . . .
huruf yang berbeda di kata cerah dan kata hujan adalah . . . .

'''

# Source Code

data_kata = set()
banyak = int(input("Masukkan banyak data : "))
c = []

for i in range(banyak):
    data_kata.add(input("Masukkan kata : "))

for i in data_kata:
    a = set(i)
    for j in data_kata:
        b = set(j)
        if [a|b] not in c and a != b:
            print(f'Himpunan yang berbeda di kata "{i}" dan kata "{j}" adalah {a.symmetric_difference(b)}')
            c.append([a|b])
        
