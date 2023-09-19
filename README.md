Repository Untuk Deploy Aplikasi pada adaptable.io

## Tugas 3
Apa Perbedaan antara POST dan GET dalam Django?
:	Perbedaan diantara POST dan GET adalah cara mereka mengirim data kita ke database. 
	1. Untuk POST pengirim data dilakukan secara secret, sedangkan pada GET pengiriman data dilakukan secara terbuka sehingga pada url terlihat data yang dikirim, sedangkan pada POST tidak terlihat. 
	2. POST juga tidak dibatasi panjang string, sedangkan GET dibatasi sampai 2047 Karakter.
	3. POST digunakan untuk mengirim data-data penting dan yang lebih dari 2047 Karakter, sedangkan pada GET digunakan untuk data-data yang tidak penting.

Apa perbedaan utama antara XML,JSON, dan HTML dalam konteks pengiriman data?
:	Perbedaan utama bisa dilihat dari kegunaan serta cara penyajian/penyimpanan data.
	1. Pada XML, penyimpanan data dilakukan dengan fleksibilitas yang tinggi. XML juga dapat mendefinisikan struktur data.
	2. Pada JSON, lebih ringan diatara keduanya, sehingga biasa digunakan untuk pengiriman data dari server ke klien.
	3. Pada HTML, biasanya digunakan pada tampilan web. Biasanya didampingi dengan CSS agar tampilan lebih menarik.

Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
:	Seperti pada soal sebelumnya, pertukaran data antara server dengan klien lebih ringan menggunakan JSON. Dengan JSON, kerja server lebih ringan dan lebih cepat sampai pada klien dan dapat lebih banyak menampung klien.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
:	Berikut step-by-step mengimplementasikan checklist diatas:
	1. Saya Membuat Kerangka tampilan web, menambahkan isi pada content web berupa table untuk main.html dan tampilan form untuk create_product.html
	2. Saya menambahkan objek model yang sebelumnya berupa name, amount, description menjadi name, price, dan link.
	3. Saya membuat fungsi views.py untuk melihat data dalam bentuk HTML, JSON, XML, JSON by ID, dan XML by ID.
	4. Lalu menambahkan routing URL pada masing-masing fungsi.
	5. Pada main.html, yang sebelumnya description hanya memasukkan String, saya merubahnya dengan link dengan memakai <a href="{{product.link}}">link</a> agar dapat dibuka dengan mudah.

Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
1. ![Postman with HTML](images/postman_html)
2. ![Postman with XML](images/postman_xml)
3. ![Postman with JSON](images/postman_json)
4. ![Postman with XML by ID](images/postman_xml_id)
5. ![Postman with JSON by ID](images/postman_json_id)

## Tugas 2
Jelaskan bagaimana cara kamu mengimplementasikan checklist step-by-step?
: 	1. Membuat Repository baru dengan nama BananaApp untuk projectnya, lalu membuat Repository baru lagi dengan nama BananaAppAdaptable untuk main app.
	2. Membuat model pada aplikasi dengan name, amount, dan description dengan tipe yang ditentukan
	3. Membuat fungsi pada views.py untuk mengembalikan templates/main.html untuk menampilkan nama aplikasi, nama, serta kelas.
	4. Melakukan deploy app di adaptable dengan repo BananaAppAdaptable dan sudah dapat diakses via online dengan link.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Jelaskan mengapa kita menggunakan virtual environment? apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
: Alasan mengapa kita menggunakan virtual environment adalah untuk membuat lingkungan isolasi yang terpisah untuk setiap proyek python, menjadi lebih bersih dan terorganisir, dan dengan mudah membagikan proyek ke orang lain. Tetapi kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi itu tidak disarankan.

Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
: MVC adalah Model-View-Control dengan pemisahan yang strict antara Model, View, dan Controller. Perubahan yang satu jarang mempengaruhi yang lainnya
MVT adalah Model-View-Template, biasanya digunakan jika berfokus pada tampilan atau Template
MVVM adalah Model-View-ViewModel dengan tujuan memperkecil kode pada View dan berfokus pada tampilan dan interaksi pengguna.