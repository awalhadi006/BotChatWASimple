import csv
import pywhatkit
from datetime import datetime
import time

# Mengimpor data calon santri dari file CSV
def import_data(filename):
    data = []
    with open(filename, 'r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Import data calon santri dari file CSV
data = import_data('testing.csv')

# Loop melalui data calon santri
for index, santri in enumerate(data):
    nama = santri['Nama']
    nomor_hp_1 = santri['Nomor_HP1']
    nomor_hp_2 = santri['Nomor_HP2']
    nomor_hp_3 = santri['Nomor_HP3']
    berkas1 = santri['Berkas1']
    berkas2 = santri['Berkas2']
    berkas3 = santri['Berkas3']
    berkas4 = santri['Berkas4']
    berkas5 = santri['Berkas5']
    berkas6 = santri['Berkas6']

    # Membuat daftar nomor HP
    nomor_hp = []
    if nomor_hp_1:
        nomor_hp.append(nomor_hp_1)
    if nomor_hp_2:
        nomor_hp.append(nomor_hp_2)
    if nomor_hp_3:
        nomor_hp.append(nomor_hp_3)

    # Membuat daftar berkas yang dibutuhkan
    berkas_dibutuhkan = []
    if berkas1:
        berkas_dibutuhkan.append(berkas1)
    if berkas2:
        berkas_dibutuhkan.append(berkas2)
    if berkas3:
        berkas_dibutuhkan.append(berkas3)
    if berkas4:
        berkas_dibutuhkan.append(berkas4)
    if berkas5:
        berkas_dibutuhkan.append(berkas5)
    if berkas6:
        berkas_dibutuhkan.append(berkas6)

    # Menentukan pesan berdasarkan data calon santri
    pesan = f"_Assalamu'alaikum Wr. Wb_\n\nSelamat siang Bapak/Ibu/Wali dari santri baru *{nama}*.\nSaya selaku admin dari Panitia Penerimaan Santri Baru (PSB) Pondok Pesantren AL-Lathifah ingin menginformasikan bahwa ada beberapa berkas yang *harus dilengkapi untuk pendaftaran*, yaitu: \n"
    pesan += f"\n"

    for berkas in berkas_dibutuhkan:
        pesan += f"- *{berkas}*\n"

    pesan += "\nHarap agar bisa dikumpulkan *hari ini*, paling lambat *hari Ahad, 24 Juli 2023* (berkasnya sementara bisa difotokan terlebih dahulu untuk penginputan datanya).\nJika rumah Bapak/Ibu jauh dari pondok pesantren, berkas dapat dikirim via ekspedisi.\n\nTerima kasih.\n_Wassalamu'alaikum Wr. Wb_"

    for nomor in nomor_hp:
        try:
            # Mengirim pesan WhatsApp pada jam sekarang ke setiap nomor HP
            pywhatkit.sendwhatmsg_instantly(nomor, pesan, 20, True, 15)
            print(f"Message sent to {nama} | {nomor}.")
        except pywhatkit.exceptions.CountryCodeException:
            print(f"Failed to send message to {nama} | {nomor}. The number is not registered on WhatsApp.")
        except Exception as e:
            print(f"Failed to send message to {nama} | {nomor}. Error: {str(e)}")

        # Menunggu beberapa saat sebelum mengirim pesan ke nomor selanjutnya
        time.sleep(10)

    # Jeda waktu sebelum pengiriman pesan berikutnya
    if index < len(data) - 1:
        time.sleep(10)  # Ubah waktu jeda sesuai kebutuhan Anda
