print("")
print ("PENDAHULUAN")
print("------------")

'''          ====SHORTCUT====            '''    
'''  1. shift + alt + drag               '''       
'''  2. alt + drag                       '''       
'''  3. ctrl + D                         '''       
'''  4. alt + panah atas/bawah           '''   
'''  5. shift + ctrl + panah atas/bawah  '''

print("") # hanya spasi

print("BAB 1")
print("------")

'''                 ====BAB 1 (VARIABEL)====                           '''                        
'''larangan dalam menulis variable                                     '''                                                                
'''   1. 10data =     (tidak boleh, angka tidak boleh di depan huruf)  '''                                            
'''      data10 =     (boleh)                                          '''                    
'''   2. data 10 =    (tidak boleh ada spasi)                          '''            
'''      data-10 =    (tidak boleh )                                   '''        
'''      data_10 =    (boleh)                                          '''    
'''   3. 1000 = 10    (tidak boleh angka)                              '''                        
'''      a = 10       (boleh)                                          '''                                

a = 10
b = 25 

print ("a" , "b")

print("") # hanya spasi





print("BAB 2")
print("------")
'''             ====BAB 2 (TIPE DATA)====            '''
#   1. Integer adalah tipe data angka tanpa koma atau bilangan bulat. cth: 1, 2, 3
a = 100
print ("data = ", a)
print ("- bertipe =", type (a))

#   2. Float adalah tipe data angka dengan koma. cth: 1.2, 1.3, 4.5
b = 100.5
print ("data = ", b)
print ("- bertipe = ", type (b))

#   3. String adalah tipe data kumpulan karakter cth: jarwo, cerek, curuk
c = "jarwo"     # harus di kasih tanda petik "...", jarwo 10 juga termasuk string meski ada angka nya
print ("data = ", c)
print ("- bertipe = ", type (c))

#   4. boolean adalah tipe data yang hanya ada 2 pilihan yaitu true atau false 
d = True # bisa juga diganti False, harus kapital di awal kata
print ("data = ", d)
print ("- bertipe = ", type (d))

print("") # hanya spasi





print("BAB 3")
print("------")
'''             ====BAB 3 (TIPE DATA KHUSUS)====            '''
#   1. Bilangan kompleks yaitu yang terdiri dari bilangan real dan imajiner 
e = complex (5,6) # 5 adalah bilangan real, 6 adalah biangan imajiner 
print ("data = ", e)
print ("- bertipe = ", type (e))


#   2. Tipe data dari bahasa C adalah kita bisa menggunakan tipe data dari bahasa C 

from ctypes import c_double # bisa menggunakan tipe bahasa yang lain seperti float dan lain-lain 
f = c_double(100.5)
print ("data = ", f)
print ("- bertipe = ", type (f))

print("") # hanya spasi






print ("BAB 4")
print("------")
'''             ====BAB 4 (CASTING ATAU MENGUBAH TIPE DATA)====            '''
print ("====INTEGER====")

#   1. Mengubah tipe data "integer" ke tipe data lain
a = 10          # data integer      # bentuk bilangan bulat
b = float(a)    # diubah ke float   # bentuk bilangan desimal
c = str (a)     # diubah ke string  # bentuk karakter bukan angka karna string
d = bool (a)    # diubah ke boolean # hasilnya false jika a = 0, dan true jika a = selain 0 

print ("data =", a , ",type =",type (a))
print ("data =", b , ",type =",type (b))
print ("data =", c , ",type =",type (c))
print ("data =", d , ",type =",type (d))

print("") # hanya spasi

print ("====FLOAT====")

#   2. Mengubah tipe data "float" ke tipe data lain
a = 10.9        # data float        # bentuk bilangan desimal       # akan di bulatkan ke bawah meskipun 10.9 menjadi 10 bukan 11 
b = int(a)      # diubah ke integer # bentuk bilangan bulat
c = str (a)     # diubah ke string  # bentuk karakter bukan angka karna string
d = bool (a)    # diubah ke boolean # hasilnya false jika a = 0, dan true jika a = selain 0 

print ("data =", a , ",type =",type (a))
print ("data =", b , ",type =",type (b))
print ("data =", c , ",type =",type (c))
print ("data =", d , ",type =",type (d))

print("") # hanya spasi

print ("====STRING====")

#   3. Mengubah tipe data "string" ke tipe data lain
a = 10          # data string       # bentuk karakter bukan angka karna string
b = int(a)      # diubah ke integer # bentuk bilangan bulat
c = float (a)   # diubah ke float   # bentuk bilangan desimal
d = bool (a)    # diubah ke boolean # hasilnya false jika a = 0, dan true jika a = selain 0 

print ("data =", a , ",type =",type (a))
print ("data =", b , ",type =",type (b))
print ("data =", c , ",type =",type (c))
print ("data =", d , ",type =",type (d))

print("") # hanya spasi

print ("====BOOLEAN====")

#   4. Mengubah tipe data "boolean" ke tipe data lain
a = True        # data boolean      # hasilnya false jika a = 0, dan true jika a = selain 0 
b = int(a)      # diubah ke integer # bentuk bilangan bulat
c = float (a)   # diubah ke float   # bentuk bilangan desimal
d = str (a)     # diubah ke boolean # bentuk karakter bukan angka karna string 

print ("data =", a , ",type =",type (a))
print ("data =", b , ",type =",type (b))
print ("data =", c , ",type =",type (c))
print ("data =", d , ",type =",type (d))

print("") # hanya spasi




print ("BAB 5")
print("------")
'''             ====BAB 5 (INPUT ATAU MENGAMBIL TIPE DATA)====            '''
a = input ("Masukkan data = ")
print ("data = ", a, ", type = ", type (a)) # hasil pasti string

b = int(input ("Masukkan data = "))
print ("data = ", b, ", type = ", type (b)) # data yang dimasukkan harus integer

c = float(input ("Masukkan data = "))
print ("data = ", c, ", type = ", type (c)) # data yang dimasukkan harus float

d = bool(int(input ("Masukkan data = ")))
print ("data = ", d, ", type = ", type (d)) # data yang dimasukkan harus integer jika memasukkan data float maka error

e = bool(float(input ("Masukkan data = ")))
print ("data = ", e, ", type = ", type (e)) # data yang dimasukkan bisa integer bisa float, hasil false jika data yang dimasukkan 0 


print("") # hanya spasi
print ("=======================================")