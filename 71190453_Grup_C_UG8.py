class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = "" #isi sesuai dengan ketentuan soal
    def __init__(self): #konstruktor
        pass
        self._head = None
        self._tail = None
        self._size = 0
       #tulis kode anda di sini
       
    def __len__(self): #mengembalikan ukuran Queue
        pass
        # tulis kode anda di sini
        return self._size

    def is_empty(self): #mengecek apakah Queue kosong ?
        pass
        # tulis kode anda di sini
        if self._size == 0:
            return True
        else:
            return False

    def dequeue(self): #menghapus data paling depan (front)
        pass
        # tulis kode anda di sini
        if self.is_empty() == False:
            if self._size == 1:
                bantu = self._head
                self._head = None
                self._tail = None
                del bantu
            else:
                min_priority = self._head._priority
                hapus = self._head
                while hapus != None:
                    if hapus._priority < min_priority:
                        min_priority = hapus._priority
                    hapus = hapus._next
                hapus = self._head
                while hapus._priority != min_priority:
                    hapus = hapus._next
                if hapus == self._head:
                    self._head = self._head._next
                    del hapus
            self._size = self._size - 1

    def enqueue(self, namaPelanggan): #menambah data ke list
        pass
        # tulis kode anda di sini
        baru = NodePelanggan(namaPelanggan)
        if self.is_empty(): 
            self._head = baru
            self._tail = baru
        else: 
            self._tail._next = baru
            self._tail = baru
        self._size = self._size + 1

    def resize(self, cap): #mengubah ukuran queue pada list
        pass
        # tulis kode anda di sini
    
    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        pass
        # tulis kode anda di sini
        if self.is_empty() == True:
            print('Priority Queue is empty')
        else:
            bantu = self._head
            while bantu != None:
                print(bantu._namaPelanggan)
        print()

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

