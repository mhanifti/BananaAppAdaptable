Repository Untuk Deploy Aplikasi pada adaptable.io

Adaptable : https://bananaapp.adaptable.app

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