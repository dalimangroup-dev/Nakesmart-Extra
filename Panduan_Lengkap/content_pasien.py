# -*- coding: utf-8 -*-
"""Panduan Nakesmart untuk Pasien — content module."""

ROLE = "Pasien"
TAGLINE = "Platform Ekosistem Kesehatan Digital Indonesia · 100+ Faskes · AI Health Tools"

TOC = [
    ("Bab 1 — Mengenal Nakesmart dari Sisi Pasien", [
        "1.1 Apa Itu Nakesmart?",
        "1.2 Visi & Misi Nakesmart",
        "1.3 Jenis User di Nakesmart (5 Role)",
        "1.4 Mengapa Pasien Indonesia Membutuhkan Nakesmart",
    ]),
    ("Bab 2 — Kompetitor & Keunggulan Nakesmart untuk Pasien", [
        "2.1 Landscape Layanan Kesehatan Digital di Indonesia",
        "2.2 Kompetitor Nakesmart (dari Sisi Pasien)",
        "2.3 Keunggulan Nakesmart untuk Pasien",
        "2.4 Matriks Komparasi Layanan",
    ]),
    ("Bab 3 — Fitur Utama untuk Pasien", [
        "3.1 Cari Faskes — Temukan Klinik & Rumah Sakit Terdekat",
        "3.2 Telemedicine 3-Tier — Reguler, Premium, Exclusive",
        "3.3 Booking Appointment — Reservasi Online",
        "3.4 E-Resep — Resep Digital dari Nakes",
        "3.5 Health Diary — Catatan Kesehatan Pribadi",
        "3.6 Family Hub — Kelola Kesehatan Keluarga (Premium)",
        "3.7 AI Symptom Checker — Cek Gejala Awal",
        "3.8 Health Articles — Edukasi Kesehatan Terpercaya",
        "3.9 Komunitas — Diskusi & Tanya Jawab",
        "3.10 My Health Journey — Lacak Riwayat Kesehatan",
    ]),
    ("Bab 4 — Fitur Pelengkap untuk Pasien", [
        "4.1 Nakesmart Wallet — Saldo & Top Up",
        "4.2 Voucher & Promo — Diskon Layanan",
        "4.3 Referral Program — Ajak Teman, Dapat Poin",
        "4.4 Poin & Gamification — Reward Aktivitas",
        "4.5 Notification Center — Pengingat Cerdas",
        "4.6 Bookmarks — Simpan Artikel & Nakes Favorit",
        "4.7 Smart App Banner — Install Aplikasi Mobile",
    ]),
    ("Bab 5 — Flow Pasien Menggunakan Nakesmart", [
        "5.1 Overview: Dari Daftar hingga Konsultasi",
        "5.2 Phase 1: Registrasi & Verifikasi",
        "5.3 Phase 2: Setup Profil & Health Diary",
        "5.4 Phase 3: Pilih Layanan (Telemedicine / Booking / Cari Faskes)",
        "5.5 Phase 4: Pembayaran (Wallet, Midtrans, Manual Transfer)",
        "5.6 Phase 5: Sesi Konsultasi (Chat / Voice / Video)",
        "5.7 Phase 6: E-Resep & Follow-up",
        "5.8 Phase 7: Review & Rating",
    ]),
    ("Bab 6 — Maksimalkan Manfaat Nakesmart", [
        "6.1 Upgrade ke Pasien Premium — Family Hub & Diskon",
        "6.2 Gunakan Health Diary Konsisten",
        "6.3 Manfaatkan Telemedicine untuk Konsultasi Cepat",
        "6.4 Referral untuk Hemat Biaya",
        "6.5 Tukar Poin ke Saldo Wallet",
    ]),
    ("Bab 7 — Tips, Strategi & Best Practices", [
        "7.1 Memilih Nakes yang Tepat",
        "7.2 Persiapan Sebelum Konsultasi Telemedicine",
        "7.3 Mengelola E-Resep & Reminder Obat",
        "7.4 Health Diary untuk Penyakit Kronis",
        "7.5 Cara Aman Bertransaksi di Nakesmart",
    ]),
    ("Bab 8 — Fitur Baru, Mobile App & Roadmap", [
        "8.1 Aplikasi Mobile (Android APK + iOS PWA)",
        "8.2 Smart App Banner & Auto-Redirect iOS",
        "8.3 Halaman Install Otomatis Detect OS",
        "8.4 Sistem Keamanan Anti-Scraping AI",
        "8.5 Multi-Layer Security Update 2026",
        "8.6 Roadmap 2026-2028",
    ]),
    ("Bab 9 — Rekam Medis Digital EMR-CMS-HMS untuk Pasien", [
        "9.1 Rekam Medis Anda Tersimpan Aman & Terpusat",
        "9.2 E-Resep, Surat Medis & Reservasi Tanpa Antri",
        "9.3 Privasi, Keamanan & Riwayat Lintas Faskes",
    ]),
    ("Lampiran", [
        "A. Glossarium Pasien",
        "B. FAQ Khusus Pasien",
        "C. Daftar Tarif Telemedicine",
        "D. Kontak Customer Service & Emergency",
    ]),
]

CONTENT = {
    "9.1": """Saat Anda berobat di faskes (klinik/RS) yang memakai SIMRS Nakesmart (EMR-CMS-HMS), rekam medis Anda tersimpan digital — bukan lagi kertas yang mudah hilang.

Apa untungnya bagi Anda:
• Riwayat lengkap — diagnosis, obat, hasil lab & radiologi tercatat rapi
• Tidak perlu mengulang cerita — dokter melihat riwayat Anda sebelumnya
• Hasil pemeriksaan tidak hilang — tersimpan aman di sistem
• Setiap akses tercatat (audit log) — siapa membuka data Anda, dan kapan""",

    "9.2": """Layanan yang membuat berobat lebih praktis.

E-Resep Digital:
• Resep dengan QR — tinggal tunjukkan, tidak khawatir kertas hilang
• Apotek langsung menyiapkan, termasuk obat racikan

Surat Medis:
• Surat keterangan sakit, sehat, atau keterangan medis diterbitkan digital
• Lengkap kop faskes, tanda tangan & stempel dokter — sah & rapi
• Data Anda terisi otomatis — cepat dan minim salah ketik

Reservasi Online Tanpa Antri:
• Booking jadwal layanan dari rumah — bahkan tanpa perlu login
• Pilih dokter & jam, dapat nomor antrian, datang tepat waktu
• Bayar uang muka (DP) online bila tersedia""",

    "9.3": """Privasi & keamanan data kesehatan Anda:
• Data kesehatan bersifat rahasia — hanya nakes berwenang yang dapat mengakses
• Sistem dilindungi keamanan modern, termasuk anti-penyalinan oleh bot/AI
• Setiap pembukaan rekam medis tercatat dalam audit log

Satu riwayat, banyak faskes:
• Riwayat kesehatan Anda dapat berlanjut antar faskes Nakesmart
• Memudahkan rujukan — faskes tujuan melihat data yang relevan
• Anda tetap pemilik data; faskes mengelola sesuai izin & regulasi

Gratis untuk pasien: memakai layanan ini di sisi pasien tidak dikenakan biaya langganan — biaya layanan medis mengikuti tarif faskes masing-masing.""",

    "1.1": """Nakesmart adalah Platform Ekosistem Kesehatan Digital Indonesia yang menghubungkan pasien dengan nakes (tenaga kesehatan), fasilitas kesehatan (faskes), dan layanan kesehatan terintegrasi. Untuk Pasien, Nakesmart adalah cara paling praktis untuk: konsultasi dengan dokter tanpa antri, akses ke ribuan nakes terverifikasi di seluruh Indonesia, catat riwayat kesehatan keluarga, dan dapatkan e-resep digital tanpa repot.

Berbeda dengan aplikasi kesehatan konvensional yang hanya menawarkan satu fitur (booking saja, atau chat dengan dokter saja), Nakesmart memberikan akses ke 10+ layanan kesehatan terintegrasi dalam satu platform: telemedicine 3-tier, booking faskes, e-resep, health diary, family hub, AI symptom checker, edukasi kesehatan, dan komunitas.

Nakesmart untuk Pasien = Telemedicine + Cari Faskes + E-Resep + Health Diary + Family Hub + AI Symptom Checker — semua dalam satu aplikasi terintegrasi dengan keamanan data tingkat enterprise.

Apa yang Nakesmart Tawarkan untuk Pasien?
• Akses ke ribuan nakes terverifikasi (dokter, bidan, perawat, apoteker, psikolog)
• Telemedicine 3-tier: Reguler (chat 30 menit Rp45rb), Premium (telepon 15 menit Rp75rb), Exclusive (video 15 menit Rp150rb)
• Cari faskes terdekat berdasarkan layanan, lokasi, BPJS/asuransi
• Booking appointment online — tidak perlu antri di klinik
• E-Resep digital — dapat resep dari telemedicine langsung di HP
• Health Diary — catat mood, tekanan darah, gula darah, gejala harian
• Family Hub (Premium) — kelola kesehatan hingga 4 anggota keluarga dalam satu akun
• AI Symptom Checker gratis — cek gejala awal sebelum konsultasi
• Health Articles bilingual (ID/EN) — edukasi dari dokter dan ahli
• Wallet sistem — saldo terjamin escrow, top-up via Midtrans/Xendit/Faspay/manual
• Voucher & promo — diskon konsultasi dan layanan
• Referral program — ajak teman, dapat poin untuk diskon
• Komunitas — tanya jawab dengan dokter dan sesama pasien
• Multi-channel (web responsive + Android APK + PWA iOS)
• Anti-scraping AI security — data Anda terlindungi dari bot crawler""",

    "1.2": """Visi
Menjadi ekosistem kesehatan digital #1 di Indonesia — memberdayakan setiap warga Indonesia untuk akses ke layanan kesehatan berkualitas, terjangkau, dan terpercaya tanpa batasan lokasi.

Misi (Patient-Focused)
1. Universal Health Access — Memberikan akses ke nakes berkualitas untuk pasien di mana pun di Indonesia, dari Sabang hingga Merauke.
2. Affordable Healthcare — Telemedicine mulai dari Rp45.000 (vs konsultasi offline Rp150.000-300.000+).
3. Continuity of Care — Health Diary + e-Resep + riwayat konsultasi tersimpan permanent, mendukung penanganan penyakit kronis.
4. Family-First — Family Hub khusus untuk kelola kesehatan seluruh keluarga (maks 4 anggota) dalam satu akun.
5. Data Security First — Multi-layer security (anti-AI scraping, HMAC, JWT, end-to-end enkripsi data sensitif).

Brand Identity Nakesmart
Warna brand Nakesmart mencerminkan kepercayaan dan kesehatan:
Warna · Hex Code · Penggunaan
Forest Green · #0F5132 / #1B4D3E · Brand primary, header, button CTA
Electric Lime · #C8FF00 · Tombol install, highlight
White · #FFFFFF · Background utama, cards
Charcoal · #1F2937 · Text utama
Sky Blue · #0EA5E9 · Info states, link, doctor avatar
Coral · #EF4444 · Alert, gejala darurat""",

    "1.3": """Sebagai Pasien, Anda berinteraksi dengan 4 role lain. Memahami siapa siapa membantu Anda navigasi platform dengan lebih efektif.

Role 1: PASIEN (Anda)
Pengguna utama yang mencari layanan kesehatan.
• Akun personal dengan profil + riwayat kesehatan
• Akses semua layanan telemedicine, booking, e-resep
• Health Diary untuk track kondisi harian
• Wallet untuk pembayaran (terlindungi escrow)
• Family Hub (Premium) untuk kelola keluarga

Role 2: NAKES (Tenaga Kesehatan)
Dokter umum, dokter spesialis, perawat, bidan, apoteker, psikolog, ahli gizi yang menyediakan layanan profesional.
• Setiap nakes WAJIB terverifikasi (NIK, STR, SIP)
• Punya tier telemedicine: Reguler/Premium/Exclusive dengan tarif berbeda
• Anda bisa lihat rating, ulasan, jam praktik, spesialisasi sebelum book

Role 3: FASKES (Fasilitas Kesehatan)
Klinik, rumah sakit, apotek, laboratorium yang menyediakan layanan offline.
• Anda bisa book appointment ke faskes melalui Nakesmart
• Faskes premium punya SIMRS terintegrasi (Anda dapat e-Resep digital)
• Cari berdasarkan lokasi GPS, layanan, BPJS/asuransi

Role 4: EO (Event Organizer)
Penyelenggara event kesehatan: webinar, workshop, talkshow.
• Anda bisa beli tiket event edukasi kesehatan via Nakesmart
• Event organizer juga bisa nakes yang adakan webinar bayar

Role 5: ADMIN
Tim platform Nakesmart yang verifikasi nakes, moderasi konten, resolve dispute.
• Anda tidak interaksi langsung kecuali butuh bantuan customer service""",

    "1.4": """Problem yang Pasien Indonesia Hadapi
1. Lokasi Jauh dari Faskes Berkualitas — Banyak daerah 3T (Tertinggal, Terdepan, Terluar) tidak punya spesialis terdekat
2. Antrian Klinik/RS — Bisa 2-4 jam menunggu untuk konsultasi 10 menit
3. Biaya Konsultasi Mahal — Spesialis Rp200rb-500rb, sekali kunjungan
4. Resep Hilang/Lupa — Resep kertas mudah robek atau lupa
5. Tidak Ada Riwayat Terstruktur — Tiap dokter mulai dari nol karena tidak ada continuity
6. Khawatir Penipuan Online — Banyak situs jual obat ilegal atau dokter palsu
7. Sulit Cari Nakes Spesialis Tertentu — Kebanyakan platform hanya umum
8. Tidak Ada Reminder Obat — Lupa minum obat → penyakit memburuk
9. Tidak Bisa Konsultasi Anggota Keluarga di Satu Akun — Repot bikin akun terpisah untuk anak/orangtua
10. Khawatir Data Pribadi Tersebar — Health data sangat sensitif

Solusi yang Nakesmart Berikan untuk Pasien
Problem · Solusi Nakesmart
Lokasi jauh · Telemedicine 24/7 (chat/voice/video)
Antrian lama · Booking online, dapat slot pasti
Biaya mahal · Telemedicine mulai Rp45rb (5x lebih murah)
Resep hilang · E-Resep digital permanen di akun
Tidak ada riwayat · Health Diary + riwayat konsultasi otomatis
Khawatir penipuan · Semua nakes WAJIB verified STR+SIP
Sulit cari spesialis · Filter spesialisasi, lokasi, BPJS, harga
Tidak ada reminder · Notification cerdas untuk obat & follow-up
Repot akun keluarga · Family Hub (1 akun, 4 anggota)
Data tersebar · Multi-layer security (anti-AI, HMAC, JWT)

Potensi Penghematan Pasien dengan Nakesmart
Skenario Konvensional · Konsultasi spesialis offline 4x/bulan = Rp1.000.000-2.000.000
Skenario Nakesmart · 2x telemedicine Premium + 2x AI symptom checker (gratis) = Rp150.000 → hemat Rp850K-1.85juta/bulan""",

    "2.1": """Pasien Indonesia memiliki banyak opsi platform kesehatan digital, tapi setiap opsi punya limitasi:

• Halodoc — Marketplace dokter besar, tapi fokus apotek + ojek obat
• Alodokter — Forum tanya jawab + telemedicine, tapi tidak ada SIMRS
• KlikDokter — Konten edukasi + chat dokter, terbatas booking offline
• SehatQ (sekarang Alodokter) — Penggabungan, fokus konten
• Good Doctor — Telemedicine dengan jaringan dokter besar
• Grab Health, Gojek HealthQu — Channel layanan kesehatan dari aplikasi super-app
• Klinik Pintar — Booking offline, terbatas teleconsult
• ProSehat — Healthcheck panel + lab
• Direct WhatsApp ke dokter — Manual, tidak ada protection
• Asuransi-based (Sequis, Allianz) — Akses terbatas pemegang polis

Kebanyakan pasien combine 2-3 platform ini, dengan banyak admin work dan riwayat yang tersebar.""",

    "2.2": """Kompetitor #1: Halodoc
• Fokus: Marketplace obat + ojek apotek + chat dokter
• Pros: Established, jaringan apotek besar, fast delivery obat
• Cons: Telemedicine basic (hanya chat), tidak ada Health Diary, tidak ada Family Hub, tidak ada e-Resep terintegrasi dengan faskes

Kompetitor #2: Alodokter
• Fokus: Forum + konten edukasi + telemedicine
• Pros: Konten medis berkualitas, banyak dokter
• Cons: Telemedicine 1-tier saja, tidak ada SIMRS integration, tidak punya wallet system

Kompetitor #3: Good Doctor
• Fokus: Telemedicine + sembako obat
• Pros: Jaringan dokter besar (kerja sama dengan Grab)
• Cons: Terbatas di kota besar, harga relatif mahal, tidak ada Family Hub

Kompetitor #4: KlikDokter
• Fokus: Konten edukasi + tanya jawab + booking
• Pros: Konten medis lengkap
• Cons: Fitur transaksi minim, tidak punya wallet, tidak ada Health Diary terstruktur

Kompetitor #5: Direct ke Faskes (offline)
• Fokus: Konsultasi langsung
• Pros: Bisa pemeriksaan fisik lengkap
• Cons: Lama antri, mahal, tidak fleksibel jam""",

    "2.3": """Keunggulan #1: Telemedicine 3-Tier dengan Harga Fleksibel
Nakesmart adalah satu-satunya yang punya 3 tier dengan harga jelas:
- Reguler (Chat) — Rp45.000/30 menit (cocok untuk konsultasi ringan)
- Premium (Telepon) — Rp75.000/15 menit (telepon real-time, lebih cepat dari chat)
- Exclusive (Video Zoom) — Rp150.000/15 menit (untuk konsultasi yang butuh visual)

Kompetitor biasanya 1 tier flat atau hidden pricing.

Keunggulan #2: Health Diary Lengkap
Nakesmart memiliki Health Diary dengan track:
- Mood (5-emoji)
- Tekanan darah, gula darah, berat badan, suhu
- Gejala harian dengan severity
- Voice transcription (bisa input via voice note)
- Trends analytics (grafik 30 hari)
- Coaching premium (rencana 8 minggu)

Kompetitor tidak punya health diary terstruktur seperti ini.

Keunggulan #3: Family Hub (4 Anggota per Akun)
Nakesmart Premium memungkinkan kelola kesehatan keluarga (suami/istri, anak, orangtua) dalam satu akun. Tidak perlu bikin akun terpisah.

Keunggulan #4: E-Resep Digital Terintegrasi
Setelah telemedicine, dokter bisa kirim e-Resep langsung ke akun Anda. Bisa tunjukkan ke apotek manapun atau order online.

Keunggulan #5: AI Symptom Checker Gratis
Cek gejala awal sebelum putuskan konsultasi. Body part picker + symptom list + duration. AI saran apakah perlu konsultasi atau cukup home care.

Keunggulan #6: Komunitas Aktif
Forum tanya jawab dengan verified doctor badge. Diskusi mingguan, topic hub, weekly topics.

Keunggulan #7: Wallet + Multi-Payment
Wallet sendiri dengan top-up via Midtrans, Xendit, Faspay, manual transfer. Pembayaran dilindungi escrow.

Keunggulan #8: Voucher & Referral
Voucher promo + referral program untuk hemat biaya.

Keunggulan #9: SIMRS Integration
Nakesmart kerja sama dengan ribuan faskes yang punya SIMRS terintegrasi — Anda dapatkan e-Resep langsung dari kunjungan offline juga.

Keunggulan #10: Multi-Layer Security
Anti-AI scraping (Layer 1-5), HMAC signed requests, JWT hardening, OTP fallback removed, semua untuk lindungi data kesehatan Anda.""",

    "2.4": """Matriks Komparasi Layanan untuk Pasien

Fitur · Nakesmart · Halodoc · Alodokter · Good Doctor
Chat dokter · ✅ 3 tier · ✅ 1 tier · ✅ 1 tier · ✅ 1 tier
Video call dokter · ✅ Exclusive · ⚠️ Limited · ❌ · ⚠️ Premium
E-Resep digital · ✅ · ✅ · ⚠️ · ⚠️
SIMRS integration · ✅ · ❌ · ❌ · ❌
Health Diary · ✅ Full · ❌ · ❌ · ❌
Family Hub · ✅ 4 anggota · ❌ · ❌ · ❌
AI Symptom Checker · ✅ Gratis · ⚠️ Basic · ⚠️ · ❌
Komunitas/Forum · ✅ Active · ❌ · ✅ · ❌
Booking faskes offline · ✅ · ⚠️ Klinik partner · ⚠️ · ⚠️
Wallet system · ✅ Escrow · ⚠️ Limited · ❌ · ❌
Voucher & Promo · ✅ Active · ✅ · ⚠️ · ⚠️
Referral program · ✅ Poin · ⚠️ · ❌ · ❌
Multi-language (ID/EN) · ✅ · ⚠️ Indonesian only · ⚠️ · ⚠️
Anti-AI security · ✅ 5 layers · ❌ · ❌ · ❌

Kesimpulan: Nakesmart unggul di fitur Health Diary, Family Hub, SIMRS integration, dan keamanan multi-layer.""",

    "3.1": """Cari Faskes adalah fitur untuk menemukan klinik, rumah sakit, apotek, atau laboratorium terdekat berdasarkan kebutuhan Anda.

Cara Menggunakan
1. Buka tab "Cari Faskes" dari beranda
2. Aktifkan lokasi GPS atau ketik kota/kecamatan
3. Filter:
   - Jenis faskes (Klinik, RS, Apotek, Lab)
   - Layanan (Umum, Gigi, Anak, Mata, Lab, Radiologi, Persalinan)
   - BPJS / Asuransi yang diterima
   - Jam buka (24 jam, weekend, dll)
   - Rating minimal
4. Lihat daftar dengan jarak (km), rating, status (buka/tutup)
5. Klik faskes untuk lihat detail: alamat, telepon, jam, layanan, dokter, fasilitas, foto

Detail Faskes Menampilkan
• Profil lengkap dengan logo & foto
• Daftar nakes yang praktik (dengan rating)
• Daftar layanan + harga
• Peta lokasi dengan tombol navigasi (Google Maps)
• Tombol "Book Appointment" untuk reservasi
• Tombol "Lihat Dokter" untuk pilih nakes spesifik
• Riwayat ulasan pasien sebelumnya

Tips Mencari Faskes
- Aktifkan GPS untuk akurasi lokasi
- Pasien Premium bisa lihat info tambahan (kelas kamar, harga rinci, jam dokter)
- Gunakan filter BPJS jika ingin pakai BPJS Kesehatan
- Cek rating dan ulasan sebelum book""",

    "3.2": """Telemedicine adalah layanan konsultasi online dengan nakes terverifikasi. Nakesmart memiliki 3 tier sesuai kebutuhan.

Tier 1: REGULER (Chat — Rp45.000/30 menit)
Cocok untuk:
- Konsultasi gejala ringan (batuk, demam, sakit kepala)
- Pertanyaan tentang obat
- Follow-up kondisi yang sudah didiagnosis
Fitur:
- Chat text + foto/file attachment
- Riwayat percakapan tersimpan
- E-Resep jika dibutuhkan
- Bisa lanjut ke tier lebih tinggi jika perlu

Tier 2: PREMIUM (Telepon — Rp75.000/15 menit)
Cocok untuk:
- Konsultasi kondisi kronis
- Penjelasan hasil lab
- Konseling kesehatan mental
Fitur:
- Telepon real-time (voice call) 15 menit
- Lebih cepat & privat dibanding chat
- E-Resep prioritas
- Akses ke spesialis tertentu

Tier 3: EXCLUSIVE (Video Zoom — Rp150.000/15 menit)
Cocok untuk:
- Konsultasi yang butuh visual (kulit, mata, gigi)
- Second opinion dengan spesialis
- Konseling psikologi
Fitur:
- Video call HD via Zoom
- Recording (opsional, dengan izin)
- E-Resep dengan stempel digital
- Bisa share screen untuk lihat hasil lab

Cara Booking
1. Buka tab "Telemedicine" atau "Cari Nakes"
2. Pilih spesialisasi (Umum, Anak, Kulit, dll)
3. Lihat list nakes dengan tier, rating, jadwal
4. Pilih nakes → pilih tier → pilih slot waktu
5. Bayar via wallet, Midtrans, Xendit, Faspay, atau bank transfer
6. Tunggu konfirmasi nakes (max 24 jam)
7. Sesi dimulai sesuai jadwal

Selama Sesi
- Reguler: chat di Nakesmart Chat
- Premium: tombol "Mulai Telepon" / "Join" muncul 5 menit sebelum jadwal
- Exclusive: tombol "Join Zoom" muncul 5 menit sebelum mulai
- E-Resep otomatis muncul di akun jika dokter resepkan""",

    "3.3": """Booking Appointment untuk konsultasi offline di faskes pilihan.

Cara Booking
1. Pilih faskes dari "Cari Faskes"
2. Klik "Book Appointment"
3. Pilih:
   - Jenis layanan (Umum, Gigi, Anak, dll)
   - Nakes spesifik atau "Any available"
   - Tanggal & jam dari slot tersedia
   - Pasien (diri sendiri atau anggota Family Hub)
4. Isi keluhan utama
5. Pilih metode bayar (wallet, gateway, manual transfer, atau bayar di faskes)
6. Konfirmasi → dapat QR code & invoice

Hari H Kunjungan
- Datang 15 menit sebelum jadwal
- Tunjukkan QR code di reception
- Konsultasi dilakukan
- Jika resep diberikan, otomatis masuk e-Resep di Nakesmart

Membatalkan/Reschedule
- Maks 6 jam sebelum jadwal: full refund ke wallet
- 3-6 jam sebelum: 50% refund
- <3 jam: no refund
- Reschedule gratis 1x (tergantung kebijakan faskes)

Pasien Premium Mendapat
- Priority queue di faskes partner
- Konfirmasi lebih cepat
- Reschedule unlimited tanpa biaya""",

    "3.4": """E-Resep adalah resep digital yang Anda terima setelah konsultasi (telemedicine atau offline). Tersimpan permanen di akun.

Cara Mendapatkan E-Resep
- Otomatis setelah telemedicine jika dokter resepkan
- Otomatis dari faskes partner setelah kunjungan offline
- Bisa dipanggil ulang dari "E-Resep Saya"

Isi E-Resep
• Nama dokter + nomor STR/SIP
• Tanggal resep + masa berlaku
• Daftar obat dengan:
  - Nama generic + dagang
  - Dosis (mg)
  - Frekuensi (3x sehari, dll)
  - Durasi (5 hari, dll)
  - Catatan khusus (sebelum makan, dll)
• Tanda tangan digital dokter
• QR code verifikasi

Cara Tebus E-Resep
Opsi 1 — Apotek Offline
- Tunjukkan QR code ke apotek manapun
- Apoteker scan untuk verifikasi
- Beli obat seperti biasa

Opsi 2 — Apotek Online Partner
- Klik "Tebus Online"
- Pilih apotek partner (jika ada)
- Bayar via wallet/gateway
- Obat dikirim 1-3 jam

Reminder Obat
- Notifikasi otomatis sesuai dosis
- Toggle on/off per obat
- Riwayat kepatuhan minum obat""",

    "3.5": """Health Diary adalah jurnal kesehatan harian yang Anda catat sendiri. Membantu nakes dengan data riil saat konsultasi.

Yang Bisa Dicatat
• Mood (5-emoji: sangat baik, baik, biasa, kurang baik, buruk)
• Tekanan darah (sistolik/diastolik)
• Gula darah (puasa, sewaktu, 2 jam PP)
• Berat badan & tinggi badan (BMI auto-calculate)
• Suhu tubuh
• Gejala harian (pilih dari list + severity 1-10)
• Pola tidur (jam mulai, jam bangun, kualitas)
• Aktivitas fisik (jenis, durasi)
• Asupan air & makanan utama
• Catatan bebas (voice note → auto-transcribe)

Trends & Analytics
• Grafik mingguan/bulanan untuk semua metric
• Warning otomatis (tekanan darah > 140/90 → alert)
• Korelasi: mood vs tidur, gula darah vs aktivitas

Coaching (Premium)
• 8-week plan untuk hipertensi, diabetes, kolesterol, mental health
• Tugas harian + edukasi
• Progress tracking

Share dengan Dokter
• Saat telemedicine, dokter bisa lihat data 30 hari terakhir
• Berikan akses spesifik (toggle: bagikan ke Dr. X selama konsultasi)
• Auto-share saat booking telemedicine""",

    "3.6": """Family Hub adalah fitur Premium untuk Pasien Premium (Rp150.000/tahun) yang memungkinkan kelola kesehatan keluarga hingga 4 anggota dalam satu akun.

Anggota yang Bisa Ditambahkan
• Pasangan (suami/istri)
• Anak (kandung/angkat)
• Orang tua (ayah/ibu)
• Saudara kandung
• Anggota keluarga lain (mertua, paman, dll)

Cara Setup
1. Upgrade ke Pasien Premium di Berkala
2. Tab "Family Hub" muncul di Akun
3. Tambah anggota dengan:
   - Nama lengkap, NIK, tanggal lahir
   - Foto profil, jenis kelamin, alamat
   - Riwayat kesehatan (opsional)
4. Masing-masing anggota dapat Health Diary terpisah
5. Pilih anggota mana saat booking konsultasi

Fitur Family Hub
• Pilih siapa yang konsultasi (saya/anggota)
• E-Resep terpisah per anggota
• Health Diary independen
• Reminder obat untuk setiap anggota
• Vaksinasi calendar (BCG, polio, dll untuk anak)
• Family Health Score (aggregate semua anggota)

Privasi
- Riwayat kesehatan terenkripsi
- Hanya pemegang akun yang bisa akses
- Tidak share otomatis ke anggota lain""",

    "3.7": """AI Symptom Checker adalah alat AI gratis untuk cek gejala awal sebelum putuskan konsultasi.

Cara Pakai
1. Buka tab "AI Symptom Checker"
2. Pilih body part di gambar tubuh interaktif (kepala, dada, perut, dll)
3. Pilih gejala dari daftar (sesuai body part)
4. Tambah info: durasi, severity, faktor pemicu
5. AI proses → keluar rekomendasi

Output AI
• Probable conditions (3-5 kemungkinan dengan persentase)
• Severity assessment (ringan / sedang / darurat)
• Recommended action:
  - Home care (saran resep mandiri)
  - Konsultasi telemedicine (saran tier)
  - Datang ke klinik
  - IGD darurat
• Saran nakes spesialis yang relevan

Limitasi (Penting!)
⚠️ AI Symptom Checker BUKAN diagnosis medis. Hanya saran awal. Selalu konsultasi nakes untuk diagnosis pasti.""",

    "3.8": """Health Articles adalah konten edukasi kesehatan ditulis oleh nakes terverifikasi.

Kategori Artikel
• Penyakit umum (flu, demam, batuk)
• Penyakit kronis (hipertensi, diabetes, kolesterol)
• Kesehatan mental
• Gizi & nutrisi
• Ibu & anak (kehamilan, ASI, MPASI)
• Lansia
• Kesehatan seksual
• Vaksinasi
• Pertolongan pertama

Fitur Artikel
• Bilingual (Indonesia + English)
• Audio narration (text-to-speech)
• Bookmark untuk baca nanti
• Share via WA / link
• Komentar + diskusi
• Author verified (nakes dengan STR)
• Related articles
• Search berdasarkan keyword

Daily Tip
- Setiap hari muncul tip kesehatan di beranda
- Bisa save ke bookmark
- Bisa share ke keluarga""",

    "3.9": """Komunitas Nakesmart adalah forum tanya jawab dengan moderasi nakes.

Section
• Q&A: pertanyaan kesehatan dengan jawaban dari dokter verified
• Discussion: topik mingguan tertentu (e.g. minggu ini: Diabetes)
• Topic Hub: kumpulan diskusi per topik (Diet, Kesehatan Mental, dll)
• Expert AMA (Ask Me Anything): sesi live dengan dokter spesialis

Rules
- Tidak boleh ask emergency (gunakan IGD)
- Tidak boleh promosi obat ilegal
- Tidak boleh share data pribadi orang lain
- Moderator akan hapus konten melanggar

Reward
- Jawaban dipilih sebagai "Best Answer" → poin
- Like dari user → poin
- Pertanyaan banyak engagement → featured""",

    "3.10": """My Health Journey adalah timeline visual riwayat kesehatan Anda di Nakesmart.

Timeline Menampilkan
• Setiap telemedicine session
• Setiap booking offline ke faskes
• E-Resep yang pernah diterima
• Catatan Health Diary (highlight)
• Vaksinasi (jika dicatat)
• Hasil lab (jika upload)
• Diagnosis dari dokter

Fungsi
• Bagikan ke dokter baru untuk continuity of care
• Export PDF untuk asuransi atau dokter offline
• Filter by tanggal, dokter, jenis layanan
• Search keyword

Privacy
- Hanya Anda yang lihat
- Bisa berikan akses spesifik per dokter""",

    "4.1": """Nakesmart Wallet adalah saldo digital untuk pembayaran di Nakesmart.

Cara Top Up
• Midtrans (Snap): transfer bank, e-wallet (OVO, DANA, GoPay, ShopeePay), QRIS, kartu kredit
• Xendit: virtual account BCA/BNI/BRI/Mandiri/Permata/BJB/BSI/CIMB
• Faspay: VA bank + retail (Alfamart, Indomaret)
• Manual Transfer: ke rekening admin (perlu approval admin, 1-2 jam)

Saldo Wallet Digunakan Untuk
• Telemedicine session
• Booking faskes
• Voucher purchase
• Course/event (jika ada)
• Tebus obat online

Fitur Wallet
• Saldo real-time
• Riwayat transaksi lengkap (filter, search)
• Convert poin → saldo (1000 poin = Rp10.000)
• Refund otomatis ke wallet jika booking dibatalkan
• Withdraw (untuk nakes/EO, bukan pasien biasa)

Keamanan Wallet
- Multi-layer security (HMAC signed)
- Distributed lock di server (Redis)
- Idempotency key untuk prevent double-charge
- Escrow protection
- Limit per transaksi (default Rp10jt)""",

    "4.2": """Voucher & Promo adalah diskon yang bisa Anda klaim untuk hemat biaya.

Jenis Voucher
• Welcome (untuk user baru): -50% telemedicine pertama
• Referral: diskon dari ajak teman
• Event Sale: promo musiman (HUT RI, Tahun Baru, Hari Kesehatan)
• Loyalty: dari aktivitas tertentu (10 konsultasi → voucher 20%)
• Faskes Partner: voucher dari klinik partner

Cara Klaim
1. Buka "Voucher Saya" di Akun
2. Lihat list voucher available
3. Klik "Klaim" → masuk ke saldo voucher
4. Saat checkout, pilih voucher → otomatis diskon

Voucher Catalog
- Tab voucher catalog menampilkan promo aktif
- Filter: jenis, minimum belanja, expiry
- Beberapa voucher butuh kode promo

Aturan
- 1 voucher per transaksi (kecuali stackable)
- Tidak bisa di-cash out
- Expiry biasanya 30 hari setelah klaim""",

    "4.3": """Referral Program adalah cara hemat dengan ajak teman.

Cara Kerja
1. Buka "Referral" di Akun
2. Copy kode referral unik Anda (e.g. PASIEN-ABC123)
3. Share ke teman via WhatsApp, IG, email
4. Saat teman daftar pakai kode Anda → keduanya dapat reward

Reward Pasien
• Anda: 500 poin (= Rp5.000) saat teman daftar
• Anda: 1.000 poin (= Rp10.000) saat teman first transaction
• Teman: Voucher diskon Rp10.000 untuk transaksi pertama

Leaderboard Referral
- Ranking referral terbanyak per bulan
- Top 3 dapat hadiah eksklusif

Anti-Fraud
- Tidak boleh refer akun sendiri (cek dengan device fingerprint)
- Verifikasi by phone + email
- Sistem fraud detection otomatis""",

    "4.4": """Poin & Gamification — sistem reward untuk aktivitas di Nakesmart.

Cara Dapat Poin
• Daftar akun: +100 poin
• Lengkapi profil: +50 poin
• Konsultasi pertama: +200 poin
• Konsultasi tiap bulan: +50 poin/bulan
• Catat Health Diary konsisten 7 hari: +100 poin
• Refer teman: +500-1000 poin
• Beli tiket event: +50-100 poin
• Tulis review berkualitas: +20 poin
• Best answer di komunitas: +50 poin
• Selesaikan tugas dari Care Path: +30 poin

Tukar Poin
• 100 poin = Rp1.000 saldo wallet
• 1000 poin = Rp10.000 saldo wallet
• Tukar di tab "Wallet" → "Konversi Poin"

Badges
• Healthy Starter (catat diary 7 hari)
• Consistent Reporter (catat diary 30 hari)
• Family Caretaker (Family Hub aktif)
• Referral Pro (refer 5+ teman)
• Health Advocate (10+ review)
• Lifelong Learner (baca 50+ artikel)

Leaderboard
- Ranking poin per bulan
- Hadiah top 10 (voucher, merchandise)""",

    "4.5": """Notification Center — pusat notifikasi pintar.

Jenis Notifikasi
• Konfirmasi telemedicine (1 jam sebelum)
• Reminder obat (sesuai jadwal)
• Reminder follow-up
• Reminder vaksinasi
• Voucher baru
• Promo terbatas
• Update Health Diary streak
• Aktivitas komunitas (jawaban Q&A Anda)
• Update artikel dari dokter favorit

Preferensi
• Pilih kanal: push, email, WA, SMS
• Pilih jenis: enable/disable per kategori
• Quiet hours: silent dari jam X-Y
• Bahasa: ID/EN

Smart Filter
- AI prioritasikan notif penting
- Bundle notifikasi yang serupa
- Auto-mute jika tidak engage""",

    "4.6": """Bookmarks — simpan konten favorit untuk dibuka lagi.

Yang Bisa Di-Bookmark
• Artikel kesehatan
• Nakes (untuk konsultasi lagi nanti)
• Faskes (untuk visit kembali)
• Diskusi komunitas
• Q&A jawaban
• Voucher yang ingin klaim nanti

Manajemen
• Kategorisasi: kesehatan, dokter, makanan, dll
• Search bookmark
• Notifikasi: artikel di-update, dokter tambah jadwal""",

    "4.7": """Smart App Banner — banner ajakan install aplikasi yang muncul di nakesmart.com.

Untuk Android User
• Buka nakesmart.com di Chrome
• Banner hijau muncul di atas (3 detik setelah load)
• Klik "Install" → ke halaman download APK
• Klik "Tutup" → banner hilang 2 hari

Untuk iPhone User
• Buka nakesmart.com di Safari
• Otomatis redirect ke PWA di nakesmart.com/m/
• Tutup banner → bisa pakai versi web

Auto-Redirect iOS
• User iOS yang buka nakesmart.com root path → otomatis ke /m/ (PWA)
• Bypass: tambah ?web=1 di URL atau klik "Buka Versi Web" di Akun PWA

Halaman Install (nakesmart.com/install.html)
- Auto-detect OS:
  - Android → tombol Download APK (~50 MB)
  - iOS → instruksi Add to Home Screen
  - Desktop → QR code untuk scan dari HP

PWA (Progressive Web App) di nakesmart.com/m/
• Bisa di-Add to Home Screen Safari
• Offline support (service worker)
• Splash screen
• Push notification (iOS 16.4+)
• Hampir setara aplikasi native""",
}


# =====================================================================
# Bab 5+ content
# =====================================================================

CONTENT.update({
    "5.1": """Flow Pasien menggunakan Nakesmart dari awal hingga selesai konsultasi:

Phase 1: REGISTRASI & VERIFIKASI (5-10 menit)
- Daftar pakai email, no HP, atau Google
- Verifikasi via OTP
- Lengkapi profil dasar (nama, NIK, tanggal lahir)

Phase 2: SETUP PROFIL & HEALTH DIARY (5-15 menit)
- Upload foto, info kesehatan dasar
- Setup Health Diary preference
- Tambah anggota Family Hub (jika Premium)

Phase 3: PILIH LAYANAN (1-3 menit)
- Telemedicine, Cari Faskes, atau AI Symptom Checker
- Filter, pilih nakes/faskes

Phase 4: PEMBAYARAN (1-2 menit)
- Pilih metode (wallet/gateway/transfer)
- Aplikasi voucher jika ada
- Konfirmasi

Phase 5: KONSULTASI (15-60 menit)
- Chat (Reguler/Premium) atau video (Exclusive)
- Tunjukkan Health Diary jika relevan

Phase 6: E-RESEP & FOLLOW-UP (langsung-1 jam)
- Dapat e-Resep digital
- Setup reminder obat
- Schedule follow-up jika perlu

Phase 7: REVIEW & RATING (opsional, 1-2 menit)
- Rate nakes (1-5 star)
- Tulis review
- Dapat poin reward""",

    "5.2": """Phase 1: REGISTRASI

Step 1.1: Buka nakesmart.com atau install aplikasi
- Web: nakesmart.com
- Android: nakesmart.com/install.html → Download APK
- iPhone: nakesmart.com → otomatis ke PWA → Add to Home Screen

Step 1.2: Pilih "Daftar"
- Email + password, atau
- Login Google (paling cepat), atau
- No HP + OTP WhatsApp

Step 1.3: Verifikasi
- Cek email/WA untuk OTP 6-digit
- Masukkan OTP (valid 5 menit)
- Akun aktif

Step 1.4: Setup Profil Dasar
- Nama lengkap (sesuai KTP)
- NIK (opsional, tapi recommended untuk health record)
- Tanggal lahir
- Jenis kelamin
- Foto profil

Tips
- Gunakan email aktif (untuk notifikasi penting)
- Pastikan no HP benar (untuk OTP & reminder)
- Profil lengkap = +50 poin bonus""",

    "5.3": """Phase 2: SETUP PROFIL & HEALTH DIARY

Step 2.1: Lengkapi Health Profile
- Tinggi & berat badan (BMI auto-calculate)
- Golongan darah
- Alergi (obat, makanan)
- Riwayat penyakit (hipertensi, diabetes, dll)
- Obat rutin yang dikonsumsi
- Riwayat operasi
- Riwayat keluarga (jika ada penyakit keturunan)

Step 2.2: Setup Health Diary Preference
- Pilih metric yang ingin track:
  ✓ Mood (recommended untuk semua)
  ✓ Tekanan darah (untuk hipertensi)
  ✓ Gula darah (untuk diabetes)
  ✓ Berat badan (untuk diet)
  ✓ Gejala umum
- Pilih frekuensi reminder (harian/mingguan)

Step 2.3: Family Hub (jika Premium)
- Upgrade ke Premium di tab "Berkala"
- Tambah anggota: pasangan, anak, orangtua
- Setup profil masing-masing

Step 2.4: Notification Preference
- Enable channel: push, email, WA
- Pilih jenis notifikasi yang ingin diterima""",

    "5.4": """Phase 3: PILIH LAYANAN

Opsi A: TELEMEDICINE (Konsultasi Online)
1. Tab "Telemedicine"
2. Pilih spesialisasi atau lihat list nakes online
3. Filter: tier, rating, harga, jam tersedia
4. Pilih nakes & tier:
   - Reguler (Chat 30 menit Rp45rb)
   - Premium (Telepon 15 menit Rp75rb)
   - Exclusive (Video 15 menit Rp150rb)
5. Pilih slot waktu
6. Lanjut ke Phase 4 (Pembayaran)

Opsi B: BOOKING FASKES (Konsultasi Offline)
1. Tab "Cari Faskes"
2. Aktifkan GPS atau pilih kota
3. Filter: layanan, BPJS, jam buka
4. Pilih faskes → lihat detail
5. Klik "Book Appointment"
6. Pilih layanan, dokter, tanggal, jam
7. Lanjut ke Phase 4

Opsi C: AI SYMPTOM CHECKER (Gratis)
1. Tab "AI Symptom Checker"
2. Pilih body part di gambar interaktif
3. Pilih gejala + durasi + severity
4. AI proses → keluar rekomendasi
5. Jika perlu konsultasi → langsung ke telemedicine

Opsi D: KOMUNITAS (Gratis)
1. Tab "Komunitas"
2. Pilih topic atau tanya pertanyaan
3. Dokter verified akan jawab dalam 24 jam""",

    "5.5": """Phase 4: PEMBAYARAN

Metode Pembayaran Tersedia
1. Saldo Wallet (paling cepat — 1 klik)
2. Midtrans Snap (semua bank, e-wallet, QRIS, CC)
3. Xendit (Virtual Account bank)
4. Faspay (VA + retail Alfamart/Indomaret)
5. Manual Transfer (perlu approval admin)
6. Bayar di Faskes (untuk booking offline)

Apply Voucher
- Klik "Punya Voucher?"
- Pilih voucher dari saldo voucher Anda
- Atau masukkan kode promo
- Diskon otomatis applied

Apply Poin
- Toggle "Pakai Poin"
- Maksimal 50% dari total transaksi
- 1 poin = Rp10 (di tab konversi: 100 poin = Rp1.000)

Konfirmasi
- Review total bayar
- Klik "Bayar"
- Untuk Midtrans/Xendit/Faspay: popup gateway
- Setelah sukses: invoice masuk email + di akun

Keamanan
- HMAC signed request (anti-tampering)
- Distributed lock (no double-charge)
- Escrow: dana ditahan sampai konsultasi selesai
- Idempotency key (retry tidak duplikat)""",

    "5.6": """Phase 5: SESI KONSULTASI

Untuk Telemedicine Reguler (Chat)
1. 5 menit sebelum mulai, tombol "Mulai Chat" aktif
2. Klik untuk masuk ke ruang chat
3. Chat dengan nakes:
   - Text + emoji
   - Foto (luka, ruam, hasil lab)
   - File attachment (PDF, dokumen)
   - Voice note
4. Nakes balas, diskusi diagnosis
5. Sesi berakhir saat timer 0 atau klik "Selesai"
6. E-Resep auto-generated jika ada resep

Untuk Telemedicine Premium (Telepon)
1. 5 menit sebelum jadwal, tombol "Mulai Telepon" aktif
2. Klik untuk masuk ke panggilan suara (voice call) 15 menit
3. Bicara langsung dengan nakes; bisa kirim foto/file lewat panel chat
4. Sesi berakhir saat timer 0 atau klik "Selesai"
5. E-Resep auto-generated jika ada resep

Untuk Telemedicine Exclusive (Video)
1. 5 menit sebelum mulai, tombol "Join Zoom" aktif
2. Klik → buka Zoom (di-embed di Nakesmart)
3. Tunggu nakes masuk
4. Video call 15 menit:
   - Kamera & mic on
   - Bisa share screen
   - Chat panel untuk catatan
5. Setelah selesai, e-Resep langsung muncul

Untuk Booking Offline
1. Datang ke faskes 15 menit sebelum jadwal
2. Tunjukkan QR code di reception
3. Antri (jika ada)
4. Konsultasi dengan dokter
5. Resep otomatis masuk e-Resep di akun

Tips Konsultasi Efektif
- Siapkan list pertanyaan
- Buka Health Diary untuk share data
- Catat saran dokter
- Tanya apa boleh dilakukan/dihindari""",

    "5.7": """Phase 6: E-RESEP & FOLLOW-UP

Setelah Konsultasi
1. Notifikasi: "E-Resep Baru dari Dr. X"
2. Buka tab "E-Resep Saya"
3. Lihat detail:
   - Daftar obat
   - Dosis & jadwal
   - Catatan khusus (sebelum/sesudah makan)
   - Masa berlaku resep (umumnya 7 hari)

Cara Tebus Obat
Opsi A: Apotek Offline
- Tunjukkan QR code di apotek
- Beli obat seperti biasa

Opsi B: Apotek Online Partner
- Klik "Tebus Online"
- Pilih apotek partner
- Bayar via wallet
- Obat dikirim 1-3 jam

Setup Reminder Obat
- Untuk setiap obat, set jam minum
- Notifikasi 10 menit sebelum
- Track kepatuhan harian

Follow-Up
- Jika dokter saran follow-up, tombol "Book Follow-Up" aktif
- Auto-isi keluhan dari konsultasi sebelumnya
- Diskon 20% untuk follow-up dalam 7 hari

Catatan di Health Diary
- Auto-create entry "Konsultasi dengan Dr. X"
- Tambah catatan harian: kondisi setelah minum obat
- Track perbaikan/perburukan""",

    "5.8": """Phase 7: REVIEW & RATING

Setelah 1 Jam Sesi Selesai
- Notifikasi: "Bagaimana sesi dengan Dr. X?"
- Klik untuk masuk ke form review

Komponen Review
• Rating 1-5 star
• Sub-rating:
  - Profesionalitas dokter
  - Komunikasi
  - Kecepatan respon
  - Kemudahan dipahami
• Review tertulis (opsional, minimal 20 karakter untuk +20 poin)
• Tag: "Akan konsultasi lagi", "Recommended", "Tepat waktu"

Manfaat Review
- Bantu pasien lain pilih dokter
- Dokter dapat feedback untuk improve
- Anda dapat poin (+20 untuk review berkualitas)
- Bisa di-edit dalam 7 hari

Anonymous Option
- Bisa review tanpa nama (opsional)
- Tetap dapat poin

Aturan Review
- Tidak boleh insulting/kasar
- Tidak boleh share data sensitif
- Tidak boleh promosi kompetitor
- Admin akan moderasi""",
})

# =====================================================================
# Bab 6+ content
# =====================================================================

CONTENT.update({
    "6.1": """Pasien Premium adalah upgrade berbayar yang memberikan akses ke fitur eksklusif.

Harga
- Rp150.000/tahun
- Atau Rp25.000/bulan (langganan)

Yang Dapat Anda
• Family Hub (kelola 4 anggota keluarga)
• Diskon 15% untuk semua telemedicine
• Diskon 20% untuk Course/event berbayar
• Priority queue di faskes partner
• Reschedule unlimited tanpa biaya
• Coaching 8-minggu untuk penyakit kronis
• Health Diary Analytics lengkap (forecast, korelasi)
• Akses webinar premium

ROI Premium (Contoh)
- Pasien biasa: 4 telemedicine Premium/bulan × Rp75rb = Rp300rb/bulan = Rp3.6jt/tahun
- Premium: diskon 15% × Rp3.6jt = hemat Rp540rb/tahun
- Setelah dikurangi Premium Rp150rb → net hemat Rp390rb/tahun + Family Hub""",

    "6.2": """Health Diary konsisten = data akurat untuk dokter = diagnosis lebih tepat.

Tips Konsisten
1. Set reminder harian (pagi & malam)
2. Mulai kecil: 1 metric dulu (e.g. mood saja)
3. Pakai voice note kalau malas ketik
4. Streak counter: target 30 hari berturut → badge

Untuk Penyakit Kronis
- Hipertensi: ukur TD 2x sehari (pagi & sebelum tidur)
- Diabetes: gula darah puasa + 2 jam PP
- Asma: catat gejala + pemicu
- Mental health: mood 3x sehari

Bagikan dengan Dokter
- Saat telemedicine, dokter request akses
- Grant 30 hari terakhir saja
- Dokter pakai untuk diagnosis trend""",

    "6.3": """Telemedicine adalah cara tercepat & termurah untuk konsultasi.

Kapan Pakai Telemedicine
- Gejala ringan (batuk, demam, sakit kepala)
- Follow-up kondisi yang sudah didiagnosis
- Pertanyaan tentang obat
- Konsultasi second opinion
- Konsultasi kesehatan mental

Kapan Jangan Pakai Telemedicine
- Gejala darurat (sesak nafas berat, dada terasa berat, pingsan)
- Cedera fisik (luka, patah tulang)
- Konsultasi yang butuh pemeriksaan fisik
- Vaksinasi

Pilih Tier yang Tepat
- Reguler: keluhan jelas, butuh resep simple
- Premium: kondisi kronis, butuh diskusi lengkap
- Exclusive: butuh visual (kulit, mata, gigi)

Hemat Biaya
- Premium subscriber: diskon 15%
- Voucher welcome user baru: 50% telemedicine pertama
- Refer teman: diskon dari poin reward""",

    "6.4": """Referral = ajak teman = hemat biaya.

Strategi Referral
1. Share ke grup keluarga WhatsApp
2. Share ke kolega kantor (ajak konsultasi kerja)
3. Posting di sosial media dengan testimoni Anda
4. Share saat ada acara komunitas

Cara Maksimal Reward
- Jika teman aktif transaksi → Anda dapat poin terus
- Top referrer per bulan dapat hadiah eksklusif
- Group referral: 5 teman daftar → bonus 500 poin

Tukar Poin
- 1.000 poin = Rp10.000
- Tukar di Wallet → Konversi Poin
- Saldo wallet bisa pakai untuk telemedicine, obat, dll""",

    "6.5": """Poin Nakesmart bisa ditukar ke saldo wallet kapan saja.

Rate Konversi
- 100 poin = Rp1.000
- 1.000 poin = Rp10.000
- 10.000 poin = Rp100.000

Strategi Maksimal Poin
1. Daftar + lengkapi profil (+150)
2. Konsultasi rutin (+50/bulan)
3. Health Diary 7 hari berturut (+100)
4. Referral teman (+500-1000 per referral)
5. Review berkualitas (+20 per review)
6. Best answer di komunitas (+50)

Kapan Tukar?
- Saat butuh wallet untuk transaksi
- Atau saat saldo poin > 5.000 (untuk hindari capped)""",

    "7.1": """Tips Memilih Nakes yang Tepat:

1. Cek Verifikasi
- Hanya nakes ber-status "Terverifikasi" (badge ✅)
- Verifikasi berarti STR + SIP + ID sudah dicek admin

2. Cek Spesialisasi
- Untuk masalah spesifik, pilih spesialis
- Untuk masalah umum, dokter umum sudah cukup

3. Cek Rating & Ulasan
- Rating 4.5+ adalah indikator baik
- Baca minimal 5 ulasan terbaru
- Cek tag "Recommended" dan "Akan konsultasi lagi"

4. Cek Jadwal & Response Time
- Pilih nakes dengan response time < 5 menit
- Cek jadwal yang cocok dengan Anda

5. Cek Tarif vs Tier
- Reguler vs Premium vs Exclusive
- Bandingkan harga dengan dokter lain spesialisasi sama

6. Cek Bahasa
- Beberapa nakes bisa Indonesia + English
- Atau bahasa daerah tertentu

7. Lihat Profil Lengkap
- Education background, pengalaman, fokus area
- Foto profesional (bukan selfie)""",

    "7.2": """Persiapan Sebelum Konsultasi Telemedicine:

1. Setting Tempat
- Cari ruangan tenang
- Lighting bagus (untuk video call)
- WiFi/data stabil
- Headphone untuk privasi

2. Siapkan Informasi
- Keluhan utama (kapan mulai, severity)
- Riwayat obat yang sedang diminum
- Hasil lab terbaru (foto/upload)
- Alergi
- Riwayat penyakit relevan

3. Pertanyaan
- Tulis list pertanyaan sebelum konsultasi
- Prioritaskan yang paling penting
- Tanya satu per satu agar tidak terlewat

4. Dokumentasi
- Buka Health Diary, siapkan share
- Foto area sakit (jika visual)
- Siapkan obat-obatan untuk perlihatkan

5. Saat Sesi
- Mulai dengan keluhan utama
- Jujur tentang gaya hidup (alkohol, rokok, olahraga)
- Catat saran dokter
- Tanya pantangan & yang boleh dilakukan""",

    "7.3": """Tips Mengelola E-Resep & Reminder Obat:

Setelah Dapat E-Resep
1. Baca semua dengan teliti
2. Konfirm dosage & frekuensi
3. Catat di Health Diary
4. Setup reminder di setiap jam minum

Mengatur Reminder Obat
- Open e-Resep → klik obat → "Set Reminder"
- Atur jam minum (e.g. 7 pagi, 1 siang, 7 malam)
- Notifikasi 10 menit sebelum
- Ucapkan "diminum" untuk track kepatuhan

Tips Patuh Minum Obat
- Letakkan obat di tempat yang terlihat (meja makan)
- Gabungkan dengan rutinitas (e.g. setelah gosok gigi)
- Pillbox 7 hari untuk obat banyak
- Family Hub: anggota lain juga reminder

Lupa Minum Obat
- Cek panduan obat: bisa diminum saat ingat, atau skip
- Jangan double dose untuk catch up
- Konsultasi nakes jika sering lupa""",

    "7.4": """Health Diary untuk Penyakit Kronis:

Untuk Hipertensi
- Ukur tekanan darah 2x sehari (pagi sebelum makan, malam sebelum tidur)
- Catat: sistolik/diastolik
- Catatan tambahan: olahraga, garam intake, stress
- Target normal: < 140/90 (atau sesuai saran dokter)

Untuk Diabetes
- Ukur gula darah:
  - Puasa (pagi sebelum makan): target 70-130
  - 2 jam setelah makan: target < 180
  - Sewaktu (random): target < 200
- Catat: makanan, dosis insulin, olahraga

Untuk Kolesterol
- Tidak diukur harian, tapi catat:
  - Makanan tinggi lemak
  - Olahraga
  - Berat badan
- Lab 3-6 bulan sekali

Untuk Asma
- Catat gejala: sesak, mengi, batuk
- Catat pemicu: cuaca, debu, exercise, stress
- Catat penggunaan inhaler

Bagikan Trend dengan Dokter
- Saat konsultasi rutin (3-6 bulan sekali)
- Grafik 30 hari otomatis dibuat
- Dokter assess kontrol penyakit""",

    "7.5": """Tips Aman Bertransaksi di Nakesmart:

1. Verifikasi Akun
- Selalu pakai akun terverifikasi (email + phone)
- Jangan share password
- Aktifkan 2FA (jika tersedia)

2. Pembayaran
- Pakai metode resmi (wallet, gateway, manual transfer)
- Cek invoice sebelum bayar
- Jangan transfer ke rekening pribadi (selalu via Nakesmart)
- Simpan bukti pembayaran

3. Komunikasi
- Komunikasi hanya di Nakesmart Chat (jangan WA pribadi)
- Jangan share OTP atau password ke siapapun
- Jangan klik link mencurigakan

4. Data Pribadi
- Nakesmart pakai enkripsi end-to-end
- Anti-AI scraping protection
- Data hanya share ke dokter yang Anda pilih

5. Tanda Penipuan
- Dokter minta transfer pribadi → SCAM, laporkan
- Email/SMS minta password/OTP → SCAM, jangan klik
- Voucher dari sumber tidak resmi → SCAM, jangan klaim

6. Laporkan Masalah
- Tab "Bantuan" → "Laporkan Masalah"
- Tim support respon 24 jam
- Emergency: 119 (Ambulan Indonesia)""",
})

# =====================================================================
# Bab 8 — Fitur baru, mobile app, roadmap
# =====================================================================

CONTENT.update({
    "8.1": """Aplikasi mobile Nakesmart tersedia di Android (APK) dan iOS (PWA).

Android APK
- Size: ~50 MB (setelah optimisasi)
- Versi terkini: 1.0.0
- Download: nakesmart.com/install.html → tombol Download APK
- Compatibility: Android 7+ (Nougat ke atas)
- Update otomatis via in-app prompt

Fitur Mobile App (80 layar)
• Semua fitur web (Telemedicine, Health Diary, Booking, dll)
• Push notification native
• Camera untuk upload foto/dokumen
• GPS untuk cari faskes terdekat
• Offline support (cache data)
• Biometric login (fingerprint, FaceID untuk iOS)
• Voice transcription untuk Health Diary

iOS PWA (Progressive Web App)
- Bukan native app, tapi powerful
- Bisa Add to Home Screen via Safari
- Splash screen + ikon di Home Screen
- Full-screen (tidak ada Safari URL bar)
- Push notification (iOS 16.4+)
- Service worker untuk offline support
- Tidak perlu Apple Developer account = gratis

Mengapa Tidak APK untuk iOS?
- Apple melarang side-load APK
- TestFlight perlu akun Developer $99/tahun
- PWA solusi gratis & efektif untuk 99% kebutuhan

Cara Install PWA di iPhone
1. Buka nakesmart.com di Safari (BUKAN Chrome)
2. Tap ikon Share (kotak dengan panah ke atas)
3. Scroll bawah → "Add to Home Screen"
4. Tap "Add"
5. Ikon Nakesmart muncul di Home Screen

Universal Web (Desktop & laptop)
- Buka nakesmart.com
- Responsive design
- Semua fitur tersedia""",

    "8.2": """Smart App Banner adalah banner yang muncul di top web nakesmart.com untuk ajak install aplikasi mobile.

Cara Kerja
• Detect OS user (Android / iOS / Desktop)
• Muncul 3 detik setelah load (tidak intrusive)
• Tombol "Install" + tombol "Tutup"
• Cooldown 2 hari setelah dismiss

Tampilan Android
- Background hijau gradient (#0F5132 → #1B4D3E)
- Logo Nakesmart + nama
- Subtitle: "Lebih cepat & notifikasi konsultasi langsung"
- Tombol "Install" lime → ke install.html

Tampilan iOS
- Sama style, tapi subtitle: "Tambahkan ke Home Screen via Safari"
- Tombol "Buka" → ke install.html

Auto-Redirect iOS (Eksklusif)
• User iOS yang buka nakesmart.com (root path) → otomatis pindah ke nakesmart.com/m/
• Ini PWA Nakesmart yang lebih optimal untuk iOS
• Bypass:
  - URL ?web=1 → tetap di web nakesmart.com
  - Klik "Buka Versi Web" di Akun PWA → set flag tidak redirect lagi

Mengapa Auto-Redirect?
- iOS Safari tidak support semua fitur mobile web
- PWA di /m/ optimasi untuk iOS (offline, push notif, dll)
- User experience lebih bagus
- Tidak bisa untuk Android (Chrome lebih powerful)""",

    "8.3": """Halaman Install (nakesmart.com/install.html) adalah landing page dengan auto-detect OS.

Tampilan Berbeda per OS

Untuk Android Visitor
- Card: "📱 Android"
- Heading: "Download APK"
- Subtitle: "Ukuran sekitar 50 MB. Pastikan izinkan install dari 'Unknown Sources'"
- Tombol lime: "Download APK Sekarang"
- Step-by-step instruksi 4 langkah

Untuk iPhone Visitor
- Card: "🍎 iPhone / iPad"
- Heading: "Tambahkan ke Home Screen"
- Subtitle: "Aplikasi versi web (PWA) bisa dipasang langsung dari Safari tanpa App Store"
- Tombol: "Buka di Safari" → nakesmart.com/m/
- Step-by-step 4 langkah dengan ikon Share

Untuk Desktop Visitor
- Card: "💻 Desktop"
- Heading: "Scan QR di HP"
- QR code untuk scan dari kamera HP
- Subtitle: "Atau buka nakesmart.com/install di browser HP"

Web Fallback (Semua Visitor)
- Card "🌐 Tetap pakai versi Web"
- Tombol untuk langsung ke nakesmart.com

URL Permanent
- Web utama: nakesmart.com
- Halaman install: nakesmart.com/install.html
- APK direct: nakesmart.com/downloads/nakesmart.apk (~50 MB universal)
- PWA: nakesmart.com/m/
- Bypass auto-redirect iOS: nakesmart.com/?web=1""",

    "8.4": """Nakesmart memiliki sistem keamanan multi-layer untuk lindungi data Anda dari scraping AI bot.

Latar Belakang
Beberapa AI tools (ChatGPT, Claude, Bard) bisa browse dan scrape konten website. Mereka bisa:
- Salin artikel kesehatan untuk training AI mereka
- Akses data pasien jika berhasil bypass login
- Crawl seluruh website secara otomatis

Nakesmart Sistem 5-Layer Anti-AI Scraping

Layer 1: Frontend Bot Detection
- Detect navigator.webdriver (true di automated browsers)
- Detect headless Chrome via User Agent
- Detect Selenium, Playwright, Puppeteer signatures
- Behavioral: mouse movement entropy, click timing

Layer 2: Content Protection
- Disable right-click di halaman sensitif
- Watermark per user (invisible fingerprint di setiap page)
- DevTools detection (raise bot score jika terbuka)
- CSS-rendered text untuk konten ultra-sensitif

Layer 3: API HMAC Signing
- Setiap request ke /api/wallet, /api/admin, /api/payment perlu signature HMAC-SHA256
- Token TTL pendek (5 menit)
- Replay protection

Layer 4: Server-Side Behavioral
- Redis-based rate limiting (30 request/10 detik burst, 1000/jam)
- UA blacklist: GPTBot, ClaudeBot, Bytespider, scrapy, curl, Selenium, Playwright langsung diblock dengan 403
- Anomaly scoring (missing headers, UA churn)
- CAPTCHA challenge untuk suspicious sessions

Layer 5: Anti-Claude-in-Chrome
- Detect Claude Chrome Extension signatures
- Detect synthetic mouse events (isTrusted=false)
- Detect chrome.runtime.sendMessage dari page context
- Block jika extension terdeteksi

Hasil
✅ GPTBot, ClaudeBot crawler tidak bisa scrape Nakesmart
✅ AI tools tidak bisa baca konten lengkap kalau login dari extension
✅ Bot scraping dideteksi & diblok otomatis
✅ Real user tidak terganggu — sistem invisible

Untuk Pasien
Tidak perlu lakukan apa-apa. Sistem otomatis melindungi:
- Profil kesehatan
- Riwayat konsultasi
- E-Resep
- Health Diary
- Family Hub data""",

    "8.5": """Update Security Nakesmart 2026 (8-Round Audit + Fix):

Round 1-3: Authentication & Money Path
✅ JWT secret hardening (no fallback)
✅ Midtrans webhook signature validation
✅ Wallet IDOR fixes
✅ Referral/use-code authentication

Round 4: Unauth Endpoint Hardening
✅ Bank accounts CRUD: admin auth required
✅ Cart verify-payment: admin auth required
✅ Admin users dump: protected
✅ EO event_tickets: ownership check

Round 5: OTP Leak + Race Conditions
✅ OTP code tidak di-return di response
✅ Distributed lock untuk wallet, voucher, payouts
✅ Idempotency keys untuk prevent double-charge

Round 6: Global Admin Guard
✅ Middleware untuk semua /api/admin/* endpoints
✅ X-Admin-User-Id header + JWT match

Round 7-8: Misc + Defense in Depth
✅ Telemedicine slot conflict check
✅ Phone normalization E.164
✅ CORS hardening (no wildcard with credentials)
✅ JWT blacklist fail-CLOSED
✅ Email template XSS protection
✅ File upload extension validation
✅ Healthcare booking auto-refund
✅ Webhook state transition enforcement

Untuk Pasien
Semua update ini meningkatkan keamanan data Anda:
- Akun lebih sulit di-hack
- Transaksi lebih aman (no double-charge)
- Refund otomatis ke wallet jika cancel
- Data pribadi terlindungi dengan multi-layer encryption""",

    "8.6": """Roadmap Nakesmart 2026-2028:

Q3 2026 (Juli-September)
• Integration dengan BPJS Kesehatan untuk klaim otomatis
• Asuransi partnership (Allianz, Manulife, AXA)
• Lab test integrasi (Prodia, Kimia Farma)
• Pharmacy delivery partnership (Apotek K-24, Century)

Q4 2026 (Oktober-Desember)
• AI Health Coach (chatbot 24/7 untuk pertanyaan kesehatan)
• Mental Health Center (modul khusus psikolog & psikiater)
• Telemedicine multi-bahasa daerah (Jawa, Sunda, Batak, dll)
• Apple Health & Google Fit sync

Q1 2027 (Januari-Maret)
• Wearable device integration (smartwatch sync)
• AI imaging assistant (kulit, mata via foto)
• Genomic & DNA test integration
• International telemedicine (dokter dari Malaysia, Singapura)

Q2 2027 (April-Juni)
• Submit ke Google Play Store + Apple App Store resmi
• Multi-region expansion (Filipina, Vietnam, Thailand)
• Blockchain medical record (opt-in)
• Vaccine passport digital

Q3-Q4 2027
• AR/VR for medical education
• AI surgical planning assistance
• Direct integration RSUD/Puskesmas pemerintah
• Government tender for KIP Kesehatan integration

2028
• Full Indonesian Healthcare ID system
• Cross-platform with SatuSehat MoH
• Telemedicine for surgical follow-up
• AI second-opinion assistance

Beta Features (Pasien Premium first)
• Voice biomarker untuk depresi/anxiety detection
• Skin AI untuk dermatologi
• Posture analysis via camera
• Sleep tracking dengan smartwatch""",
})

# =====================================================================
# Lampiran
# =====================================================================

CONTENT.update({
    "A": """Glossarium Pasien

BPJS Kesehatan — Program jaminan kesehatan nasional Indonesia
E-Resep — Resep digital yang ditulis nakes setelah konsultasi
Faskes — Fasilitas Kesehatan (klinik, RS, apotek, lab)
Family Hub — Fitur Premium untuk kelola 4 anggota keluarga
HMAC — Hash-based Message Authentication Code, sistem signing request
JWT — JSON Web Token, format auth token modern
KTP — Kartu Tanda Penduduk
Nakes — Tenaga Kesehatan (dokter, bidan, perawat, apoteker, psikolog, ahli gizi)
NIK — Nomor Induk Kependudukan
OTP — One-Time Password, kode verifikasi 6-digit
PWA — Progressive Web App, aplikasi web yang bisa di-install seperti aplikasi native
Reguler — Tier telemedicine paling basic (chat 30 menit)
SIMRS — Sistem Informasi Manajemen Rumah Sakit
SIP — Surat Izin Praktek dokter/nakes
STR — Surat Tanda Registrasi nakes
Telemedicine — Konsultasi kesehatan online via chat/voice/video
Voucher — Diskon yang bisa diklaim untuk transaksi""",

    "B": """FAQ Khusus Pasien

Q: Apakah Nakesmart gratis?
A: Daftar dan beberapa fitur gratis (AI Symptom Checker, Health Articles, Komunitas, Health Diary basic). Telemedicine, booking, dan fitur Premium berbayar.

Q: Bagaimana cara konsultasi yang gratis?
A: AI Symptom Checker untuk cek gejala awal. Komunitas untuk tanya jawab dengan dokter (dijawab dalam 24 jam).

Q: Apakah saya bisa pakai BPJS Kesehatan?
A: Untuk booking offline ke faskes partner yang terima BPJS — ya. Untuk telemedicine online — saat ini belum, tapi sedang dalam pengembangan (Q3 2026).

Q: Bagaimana keamanan data kesehatan saya?
A: Multi-layer security: enkripsi data, HMAC signed request, anti-AI scraping, JWT hardening, GDPR-compliant. Data hanya share ke dokter yang Anda pilih.

Q: Bisa kah saya pakai akun untuk anggota keluarga?
A: Bisa, dengan upgrade Pasien Premium (Family Hub 4 anggota). Untuk Pasien Basic, satu akun per orang.

Q: Bagaimana refund jika konsultasi tidak dimulai?
A: Otomatis full refund ke wallet jika nakes tidak respond dalam slot waktu. Refund 50% jika cancel 3-6 jam sebelum. No refund jika cancel < 3 jam.

Q: Apakah dokter di Nakesmart benar-benar terverifikasi?
A: Ya. Semua nakes wajib upload STR + SIP + KTP. Tim admin verifikasi dengan database resmi (KKI untuk dokter, MTKI untuk perawat/bidan).

Q: Bagaimana jika saya emergency?
A: Nakesmart bukan untuk emergency. Hubungi 119 (Ambulan), 118 (PMI), atau langsung ke IGD terdekat.

Q: Apakah ada batas usia?
A: 13+ dengan persetujuan orangtua. Untuk anak < 13, gunakan Family Hub di akun orangtua.

Q: Bagaimana cara cancel langganan Premium?
A: Akun → Berkala → "Batalkan Langganan". Akan aktif sampai akhir periode bayar.""",

    "C": """Daftar Tarif Telemedicine

Tier Reguler (Chat)
- Durasi: 30 menit
- Harga: Rp45.000
- Spesialisasi: dokter umum
- Premium subscriber: Rp38.250 (diskon 15%)

Tier Premium (Telepon / Voice Call)
- Durasi: 15 menit
- Harga: Rp75.000
- Spesialisasi: dokter umum, beberapa spesialis
- Premium subscriber: Rp63.750 (diskon 15%)

Tier Exclusive (Video Zoom)
- Durasi: 15 menit
- Harga: Rp150.000
- Spesialisasi: spesialis (kulit, mata, gigi, anak, kandungan, jiwa, dll)
- Premium subscriber: Rp127.500 (diskon 15%)

Catatan
- Tarif final ditentukan nakes (bisa lebih tinggi sesuai pengalaman)
- Pasien Premium mendapat diskon 15% untuk semua tier
- Refund otomatis jika nakes tidak respond
- Tarif bisa berubah, cek di profil nakes terbaru

Biaya Tambahan (Opsional)
- Voucher purchase: gratis
- Tebus e-Resep online: ongkir apotek partner
- Booking offline: tarif faskes (bervariasi)""",

    "D": """Kontak Customer Service & Emergency

Customer Service Nakesmart
• Tab "Bantuan" di aplikasi
• Email: support@nakesmart.com
• WhatsApp: +62 851-XXXX-XXXX
• Response time: 24 jam (urgent: 2 jam)

Bantuan Teknis
• Email: tech@nakesmart.com
• Subject: "[TEKNIS] - deskripsi masalah"

Pelaporan Penipuan/Abuse
• Email: report@nakesmart.com
• Atau via tab "Laporkan Masalah" di aplikasi
• Anonim diperbolehkan

EMERGENCY (Bukan via Nakesmart)
🚑 Ambulan Indonesia: 119
🆘 PMI (Palang Merah): 118
🚒 Damkar: 113
👮 Kepolisian: 110
☎️ Rumah Sakit Terdekat: cek di "Cari Faskes" → filter "24 jam"

Pengaduan Konsumen
• YLKI: yayasanlembagakonsumen.id
• Dirjen Yankes Kemenkes: yankes.kemkes.go.id

Tentang PT Nakesmart
PT GIANNA MEDICAL CENTER
Alamat: Jakarta
Website: nakesmart.com
Email: info@nakesmart.com""",
})
