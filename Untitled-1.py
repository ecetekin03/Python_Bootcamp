class Bookcase:
    def __init__(self):
        self.books = []
        self.filename = "kitaplar.txt"
        self.file = open("kitaplar.txt","a+")
        
    def __del__(self):
        self.file.close() 

    def save_books(self):
        with open(self.filename, "w") as file:
            for book in self.books:
                file.write(f"Adı: {book['name']}, Yazarı: {book['author']}, Sayfa Sayısı: {book['pages']}, Tarih: {book['date']}\n")


    def insert(self):
        name = input('Kitap adını giriniz: ')
        author = input('Yazarını giriniz: ')
        pages = input('Sayfa sayısını giriniz: ')
        date = input('Tarihini giriniz: ')
        
        book = {'name': name, 'author': author, 'pages': pages, 'date': date}
        self.books.append(book)

        try:
            with open(self.filename, "a") as file:
                file.write(f"Adı: {book['name']}, Yazarı: {book['author']}, Sayfa Sayısı: {book['pages']}, Tarih: {book['date']}\n")
            print("Kitap başarıyla eklendi.")
        except Exception as e:
            print(f"Hata: {e}")

    def delete(self):
        name = input('Silmek istediğiniz kitabın adını giriniz: ')
        for book in self.books:
            if book['name'] == name:
                self.books.remove(book)
                print(f"{name} adlı kitap başarıyla silindi.")
                break
        else:
            print(f"{name} adlı kitap bulunamadı.")

    def list_books(self):
        print("Kitaplar:")
        for book in self.books:
            print(f"Adı: {book['name']}, Yazarı: {book['author']}, Sayfa Sayısı: {book['pages']}, Tarih: {book['date']}")


bookcase = Bookcase()

while True:
    print('*** Menü ***')
    print('1) Kitapları Listele')
    print('2) Kitap Ekle')
    print('3) Kitap Sil')
    print('4) Çıkış')

    choice = input('Seçiminizi yapınız: ')

    if choice == '1':
        bookcase.list_books()
    elif choice == '2':
        bookcase.insert()
    elif choice == '3':
        bookcase.delete()
    elif choice == '4':
        bookcase.save_books()  # Save books before exiting
        print("Programdan çıkılıyor...")
        break
    else: 
        print('Geçersiz seçim')