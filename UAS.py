from prettytable import PrettyTable

# Data opsi pilihan makanan / minuman
menu = {
    "1": {"nama": "Nasi Goreng", "harga": 10000},
    "2": {"nama": "Ayam Geprek", "harga": 15000},
    "3": {"nama": "Mie Ayam", "harga": 8000},
    "4": {"nama": "Jus Alpukat", "harga": 6000},
    "5": {"nama": "Sprite", "harga": 5000},
    "6": {"nama": "Kwetiaw", "harga": 12000},
}

# Program utama
def main():
    # Menampilkan daftar menu menggunakan tabel
    print("Daftar Menu:")
    tabel_menu = PrettyTable(["No", "Nama Makanan/Minuman", "Harga",])
    for key, value in menu.items():
        tabel_menu.add_row([key, value['nama'], value['harga']])
    print(tabel_menu)

    # Meminta input pilihan makanan
    pilihan = input("\nMasukkan pilihan makanan (angka): ")

    # Menghitung total harga
    jumlah = int(input("Masukkan jumlah (angka): "))
    total_harga = menu[pilihan]['harga'] * jumlah

    # Menampilkan struk pembelian
    print("\nStruk Pembelian:")
    print("-" * 45)
    print("{:<15} {:<15}".format('Nama Makanan/Minuman', menu[pilihan]['nama']))
    print("{:<15} {:<15}".format('Jumlah', jumlah))
    print("{:<15} {:<15}".format('Harga Satuan', menu[pilihan]['harga']))
    print("{:<15} {:<15}".format('Total Harga', total_harga))
    print("-" * 45)
    print("\nTerima kasih atas kunjungan Anda!")

if __name__ == "__main__":
    main()