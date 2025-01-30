# import bahan
# import random

# print(bahan.title)
# print('''Aturan Permainan :
# 1. Selamatkan Budi dengan cara menjawab 1 pertanyaan dengan benar
# 2. Budi hanya memiliki 6 nyawa!
# 3. 1 kesalahan akan mrngurangi 1 nyawa Budi!''')

# #input siap/tidak
# siap = input("apakah anda sudah siap? (y/n)").lower().strip()

# if siap == "y":

#     pertanyaan = open('Day14HangingMan\pertanyaan.txt', 'r')
#     list_pertanyaan = pertanyaan.readlines()
#     jawaban  = open('Day14HangingMan\jawaban.txt', 'r')
#     list_jawaban = jawaban.readlines()

# #looping sebanyak jumlah nyawa budi
#     for i in range(0,6):
# #print hangman sesuai jumlah kalah dan jumlah menang
#         print(bahan.hangman[i])
# #pilih pertanyaan random
#         choose = random.randint(0, len(list_pertanyaan) - 1)
# #print pertanyaan
#         print(f'Pertanyaan : {list_pertanyaan[choose]}', end='')

#         user_answer = input("Enter your answer :").strip().lower()
#         #cek jawaban benar/salah pakai if else

#         if user_answer == (list_jawaban[choose]).strip().lower():
#             #jika benar print congrats
#             print(bahan.congrats)
#             print("terima kasih! Budi selamat berkatmu!")
#             break

#     #cek apabila nyawa budi sudah habis/blm
#         # elif i == 5:
#         else:
#             print(bahan.hangman[5])
#             print("Terima kasih! Budi selamat berkatmu")

#         # else:
#         #     print("Jawaban salah! coba lagi")

#     #tutup file
#         pertanyaan.close()
#         jawaban.close()

#         # else:
#         # #print hangman terkahir
#         # print(bahan.hangman[5])
#         #     print("Terima kasih! Budi selamat berkatmu")
        
# elif siap.lower().strip() == "n":
#     print(bahan.rose)
#     print("yah! kamu gagal menyelamatkan budi!")
# else :
#      ("Invalid input!")
     

import bahan
import random

# print judul dari module bahan
print(bahan.title)
# print aturan permainan
print('''Aturan Permainan :
1. Selamatkan 'Budi' dengan cara menjawab 1 pertanyaan dengan benar!
2. Budi hanya memiliki 6 nyawa!
3. 1 Kesalahan akan mengurangi 1 nyawa Budi!
''')

# input siap atau engga
ready = input('Nyawa Budi ada di tanganmu, apakah kamu siap (y/n)?').lower()

# jika siap
if ready == 'y':

    # buka semua pertanyaan dan jawaban
    pertanyaan = open(r'Day14HangingMan\pertanyaan.txt', 'r')
    list_pertanyaan = pertanyaan.readlines()
    jawaban = open(r'Day14HangingMan\jawaban.txt', 'r')
    list_jawaban = jawaban.readlines()

    # looping sebanyak jumlah nyawa Budi
    for i in range(0, 6):
        
        # print hangman dari bahan sesuai dengan jumlah kalah dan jumlah menang
        print(bahan.hangman[i])

        # pilih pertanyaan random
        choose = random.randint(0, 99)

        # print pertanyaan
        print(f'Pertanyaan : {list_pertanyaan[choose]}', end='')
        
        # minta user untuk jaswab
        user_answ = input('Jawabanmu : ').strip().lower()

        # cek jawaban user apakah benar atau salah
        if user_answ == (list_jawaban[choose]).strip().lower():
            # jika benar print congrats
            print(bahan.congrats)
            print('Terima kasih atas dedikasimu, Budi selamat berkatmu!')
            break

        # cek apabila nyawa Budi sudah habis atau belum
        elif i == 5:
            print(bahan.rose)
            print('Kamu gagal menyelamatkan Budi!')

    # tutup file
    pertanyaan.close()
    jawaban.close()


# jika tidak siap
else :
    # print hangman terakhir
    print(bahan.hangman[5])
    print('Terima kasih, Budi tidak selamat berkatmu!')





# import bahan
# import random

# # print judul permainan
# print(bahan.title)

# # aturan permainan
# print('''Aturan Permainan :
# 1. Selamatkan Budi dengan cara menjawab 1 pertanyaan dengan benar
# 2. Budi hanya memiliki 6 nyawa!
# 3. 1 kesalahan akan mrngurangi 1 nyawa Budi!''')

# #input siap/tidak
# siap = input("apakah anda sudah siap? (y/n)")
# # jika siap -> if else
# if siap.lower().strip() =="y":

# #buka semua pertanyaan dan jawaban -> open file
# pertanyaan = open('Day14HangingMan\pertanyaan.txt', 'r')
# list_pertanyaan = pertanyaan.readlines()
# jawaban  = open('Day14HangingMan\jawaban.txt', 'r')
# list_jawaban = jawaban.readlines()

# #looping sebanyak jumlah nyawa budi
# for i in range(0,6):
# #print hangman sesuai jumlah kalah dan jumlah menang
#     print(bahan.hangman[i])
# #pilih pertanyaan random
#     choose = random.randint(0, 99)
# #print pertanyaan
#     print(f'Pertanyaan : {pertanyaan[choose]}', end ='')

# user_answer = input("Enter your answer :").strip().lower()
# #cek jawaban benar/salah pakai if else

#     if user_answer ==(jawaban[choose]).strip().lower():
#     #jika benar print congrats
#         print(bahan.congrats)
#         print("terima kasih! Budi selamat berkatmu!")
    

# #cek apabila nyawa budi sudah habis/blm
# elif i == 5:
#     print(bahan.rose)
#     print("Kamu gagal menyelamatkan Budi")

# #tutup file
# pertanyaan.close()
# jawaban.close()

# else:
# #print hangman terkahir
# print(bahan.hangman[5])
# print("Terima kasih! Budi selamat berkatmu")



# #Garuda Wisnu Kencana
# .strip() -> GarudaWisnuKencana
# .lower() ->garudawisnuKencana

