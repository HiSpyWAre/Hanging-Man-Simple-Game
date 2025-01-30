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









