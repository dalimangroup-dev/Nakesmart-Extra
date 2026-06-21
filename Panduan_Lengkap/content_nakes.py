# -*- coding: utf-8 -*-
"""Panduan Nakesmart untuk Nakes — content module."""

ROLE = "Nakes"
TAGLINE = "Platform Praktek Digital untuk Tenaga Kesehatan Indonesia"

TOC = [
    ("Bab 1 — Mengenal Nakesmart dari Sisi Nakes", [
        "1.1 Apa Itu Nakesmart untuk Nakes?",
        "1.2 Visi & Misi Nakesmart",
        "1.3 Jenis User di Nakesmart (5 Role)",
        "1.4 Mengapa Nakes Indonesia Membutuhkan Nakesmart",
    ]),
    ("Bab 2 — Kompetitor & Keunggulan Nakesmart untuk Nakes", [
        "2.1 Landscape Praktek Digital Nakes di Indonesia",
        "2.2 Kompetitor Nakesmart (dari Sisi Nakes)",
        "2.3 Keunggulan Nakesmart untuk Nakes",
        "2.4 Matriks Komparasi Earnings & Tools",
    ]),
    ("Bab 3 — Fitur Utama untuk Nakes", [
        "3.1 Profile & Verification — Bagaimana Pasien Menemukan Anda",
        "3.2 Tier Telemedicine — Setup 3 Tier (Reguler, Premium, Exclusive)",
        "3.3 Telemedicine Inbox — Manage Konsultasi",
        "3.4 E-Resep Digital — Tulis Resep dari HP",
        "3.5 Nakes Payouts — Withdrawal ke Rekening",
        "3.6 Nakes Recruitment — Cari Lowongan di Faskes",
        "3.7 Faskes Affiliations — Praktek di Multi-Klinik",
        "3.8 Article Authoring — Tulis Artikel Kesehatan",
        "3.9 Komunitas — Jawab Q&A & Earn Reputation",
        "3.10 SKP & Sertifikat — Kelola Pengembangan Diri",
    ]),
    ("Bab 4 — Fitur Pelengkap untuk Nakes", [
        "4.1 Nakes Wallet — Earnings Multi-Sumber",
        "4.2 Nakes Availability — Atur Jadwal Otomatis",
        "4.3 Referral Program — Earn dengan Refer Faskes & Pasien",
        "4.4 Affiliate Earnings — Komisi Layanan",
        "4.5 Gamification — Badges & Poin",
        "4.6 Notification Preferences — Atur Notif Pintar",
        "4.7 Health Diary Doctor Report — Lihat Trend Pasien",
    ]),
    ("Bab 5 — Flow Nakes Menerima & Mengelola Konsultasi", [
        "5.1 Overview Flow Nakes",
        "5.2 Phase 1: Registrasi & Verifikasi",
        "5.3 Phase 2: Setup Profil & Tier",
        "5.4 Phase 3: Atur Jadwal & Availability",
        "5.5 Phase 4: Terima Booking dari Pasien",
        "5.6 Phase 5: Konsultasi & Diagnosis",
        "5.7 Phase 6: E-Resep & Follow-up Plan",
        "5.8 Phase 7: Payout & Rating",
    ]),
    ("Bab 6 — Maksimalkan Income (Multi-Revenue Streams)", [
        "6.1 Telemedicine Income (Main Revenue)",
        "6.2 Faskes Affiliations Income",
        "6.3 Article Authoring Income",
        "6.4 Webinar/Event Speaker Fee",
        "6.5 Referral Fee dari Faskes",
        "6.6 Course Authoring (Phase 3 Feature)",
        "6.7 Tipping dari Pasien (Phase 3 Feature)",
        "6.8 Course/Pelatihan Self-Promotion",
    ]),
    ("Bab 7 — Tools & Strategi Growth", [
        "7.1 Optimize Profile untuk Discovery",
        "7.2 Setup Tier yang Kompetitif",
        "7.3 Best Practices Telemedicine",
        "7.4 Manajemen E-Resep Efisien",
        "7.5 Founding Nakes Program (Limited Slot)",
    ]),
    ("Bab 8 — Fitur Baru, Mobile App & Roadmap", [
        "8.1 Aplikasi Mobile Nakes (Android + PWA iOS)",
        "8.2 Native SIMRS untuk Tablet/iPad (Faskes Internal)",
        "8.3 Multi-Layer Security & Anti-AI Protection",
        "8.4 Audit Security 2026 (Round 1-8)",
        "8.5 Roadmap 2026-2028",
    ]),
    ("Bab 9 — SIMRS EMR-CMS-HMS untuk Nakes", [
        "9.1 Apa Itu EMR-CMS-HMS & Manfaatnya bagi Nakes",
        "9.2 Rekam Medis Digital, E-Resep & Surat Medis",
        "9.3 Praktik Lintas Faskes & Jadwal/Absensi Digital",
    ]),
    ("Lampiran", [
        "A. Glossarium Nakes",
        "B. FAQ Khusus Nakes",
        "C. Rate Guide Tier (Benchmark per Spesialisasi)",
        "D. Payout Schedule & Kontak",
    ]),
]

CONTENT = {
    "9.1": """EMR-CMS-HMS adalah SIMRS (Sistem Informasi Manajemen Rumah Sakit/Klinik) terpadu Nakesmart: satu basis data, tiga lapisan — EMR (rekam medis), CMS (operasional klinik), HMS (penunjang & unit RS). Saat Anda praktik di faskes yang berlangganan Nakesmart, seluruh pekerjaan klinis Anda berjalan digital dalam satu sistem.

Manfaat langsung bagi Nakes:
• Tanpa kertas — anamnesa, diagnosis (ICD-10), resep, hasil lab/radiologi dalam satu layar
• Hemat waktu administrasi — billing & antrian otomatis, fokus ke pasien
• Reputasi terbawa — rekam jejak praktik & rating tersimpan rapi
• Akses web, tablet, dan mobile (native)

Modul aktif tergantung tier langganan faskes tempat Anda praktik (6 tier, per bulan per faskes):
• Solo (Rp49rb/bln): EMR rawat jalan + e-resep + Dental
• CMS Rawat Jalan (Rp99rb/bln): + farmasi, lab, radiologi, antrian
• CMS Rawat Inap (Rp199rb/bln): + rawat inap, UGD, persalinan
• HMS RS Tipe C-D (Rp999rb/bln): + kamar operasi, ICU, bank darah (lengkap RS)
• HMS RS Tipe B (Rp2jt/bln): skala RS 200-400 bed + DICOM/PACS unlimited
• HMS RS Tipe A (Rp3jt/bln): skala RS >400 bed + custom branding + SLA 99.9%

Semua tier termasuk: BPJS (PCare/VClaim/Antrol), SATUSEHAT, migrasi data, training, dan DICOM/PACS. Add-on opsional (di luar paket): MedAI mulai Rp300rb/bln, Medping Telemedicine Kit Rp1jt/bln, WhatsApp Business Notif Rp750rb/bln. Free trial: 6 bulan GRATIS atau sampai 20 pasien/bulan (mana dulu).""",

    "9.2": """Alat klinis harian Anda di dalam EMR-CMS-HMS.

Rekam Medis Elektronik (EMR):
• Anamnesa + pemeriksaan fisik terstruktur (format SOAP)
• Diagnosis ICD-10, treatment plan, riwayat lengkap pasien
• Peringatan interaksi obat & alergi otomatis

E-Resep:
• Resep digital dengan QR verifikasi (anti-pemalsuan)
• Obat racikan (compounding): perhitungan bahan + jasa racik otomatis
• Terhubung langsung ke farmasi & stok (FEFO, kartu stok)

Surat Medis:
• Surat sakit, sehat, keterangan, kelahiran, kematian
• Kop surat faskes otomatis (logo, alamat, izin, kontak)
• Isi terisi otomatis dari data pasien (nama, umur, NIK, alamat)
• Blok nama + tanda tangan + stempel dokter & faskes
• Cetak A4 rapi, nomor surat otomatis per jenis""",

    "9.3": """Satu akun nakes, banyak faskes:
• Anda dapat praktik & terhubung dengan beberapa faskes Nakesmart
• Jadwal praktek & poliklinik dikelola digital (per dokter)
• Jadwal kontrol pasien terjadwal otomatis

Hak akses sesuai peran (RBAC):
• Faskes memiliki 25 peran (dokter spesialis/umum/gigi, perawat, apoteker, radiografer, analis lab, kasir, pendaftaran, keuangan, dll.)
• Setiap peran hanya melihat fitur yang relevan dengan tugasnya
• Perijinan Anda (STR, SIP, KTP, Ijazah) & jadwal tersimpan di registri staf faskes

Absensi digital (mobile app):
• Check-in/out dengan GPS geofence (wajib berada di lokasi faskes)
• Verifikasi biometrik perangkat (sidik jari / wajah) + foto selfie
• Catatan: pemindaian retina tidak didukung perangkat ponsel standar

Hasilnya: lebih sedikit kerja administratif, lebih banyak waktu untuk pasien — di web, tablet, maupun ponsel.""",

    "1.1": """Nakesmart untuk Nakes adalah platform praktek digital terintegrasi untuk tenaga kesehatan Indonesia. Anda bisa: praktek telemedicine 3-tier, kerjasama dengan multi-faskes, tulis artikel & dapat passive income, kelola SKP & sertifikat, dan bangun reputasi profesional dengan rating + ulasan transparan.

Berbeda dengan platform kompetitor yang hanya menawarkan telemedicine flat-rate, Nakesmart memberikan akses ke 8+ revenue streams sekaligus dalam satu ekosistem.

Nakesmart untuk Nakes = Telemedicine + Faskes Affiliations + Article Authoring + E-Resep + Wallet + SKP Tracker + Komunitas + Referral — semua dalam satu platform terintegrasi.

Apa yang Nakesmart Tawarkan untuk Nakes?
• Akses ke ribuan pasien aktif yang cari nakes
• Revenue share fair: 80% nakes, 20% platform (untuk telemedicine)
• Affiliate dengan multi-faskes (tidak terbatas 1 klinik)
• 3 Tier telemedicine: atur sendiri harga sesuai pengalaman
• Tarif fleksibel: Reguler Rp45rb/30m, Premium Rp75rb/45m, Exclusive Rp150rb/15m
• E-Resep digital dengan QR code verifikasi
• Wallet untuk terima earnings + withdraw ke rekening
• Article authoring — passive income dari artikel populer
• Komunitas — jawab Q&A dengan reputation reward
• SKP tracker untuk CME (Continuing Medical Education)
• Sertifikat dari event Nakesmart
• Multi-channel (web responsive + Android APK + PWA iOS)
• Anti-AI scraping protection — data pasien Anda terlindungi""",

    "1.2": """Visi
Memberdayakan setiap tenaga kesehatan Indonesia untuk praktek digital dengan tools profesional, multiple income streams, dan reach pasien tanpa batasan geografis.

Misi (Nakes-Focused)
1. Empower Indonesian Healthcare Workers — Tools profesional yang affordable untuk nakes bersaing global.
2. Fair Revenue Sharing — 80/20 untuk telemedicine (lebih tinggi dari Halodoc ~70/30, Alodokter variable).
3. Multi-Faskes Affiliations — Tidak tergantung 1 klinik, bisa praktek di banyak tempat sekaligus.
4. Continuity of Care — Riwayat pasien tersimpan, mendukung penanganan jangka panjang.
5. Professional Growth — SKP, sertifikat, networking, dan reputation building dalam satu platform.

Brand Identity Nakesmart
Forest Green (#0F5132) untuk professional trust
Electric Lime (#C8FF00) untuk action & CTAs
White (#FFFFFF) untuk clean medical theme""",

    "1.3": """Sebagai Nakes, Anda berinteraksi dengan 4 role lain di platform:

Role 1: NAKES (Anda)
Dokter, bidan, perawat, apoteker, psikolog, ahli gizi, fisioterapis.
• Profile public dengan portfolio + STR/SIP terverifikasi
• Akses ribuan pasien dengan AI matching
• Multiple income streams
• Wallet untuk earnings + withdrawal

Role 2: PASIEN
Pengguna yang cari layanan kesehatan. Klien utama Anda.
• Bisa booking telemedicine atau offline
• Pasien Premium (dengan Family Hub) bisa konsultasi untuk anggota keluarga

Role 3: FASKES (Fasilitas Kesehatan)
Klinik, RS, apotek tempat Anda berafiliasi.
• Anda bisa multi-affiliate (praktek di banyak klinik)
• Faskes dengan SIMRS bisa sync e-Resep otomatis
• Bisa diundang faskes untuk praktek part-time

Role 4: EO (Event Organizer)
Penyelenggara event kesehatan: webinar, workshop.
• Anda bisa jadi speaker untuk earning fee + sertifikat SKP
• EO juga bisa nakes sendiri yang adakan webinar

Role 5: ADMIN
Tim platform Nakesmart untuk verifikasi & moderasi.
• Verifikasi STR/SIP nakes (1-3 hari)
• Verifikasi artikel sebelum publish
• Resolve dispute pasien-nakes""",

    "1.4": """Problem yang Nakes Indonesia Hadapi
1. Income Terbatas — Gaji RS rendah, susah praktik mandiri tanpa modal
2. Susah Cari Pasien Tanpa Branding — Marketing personal mahal & susah
3. Geographic Limit — Hanya bisa praktek di lokasi fisik klinik
4. No Multi-Faskes Practice — Susah praktek di banyak klinik
5. Payment Risk — Pasien tidak bayar, bayar lambat
6. Tools Kerja Mahal — EMR, scheduling software, e-resep terpisah & mahal
7. No Passive Income — Income tergantung jam praktek
8. SKP Tracking Repot — Catat manual, hilang sertifikat
9. Komunitas Profesional Lemah — Susah connect dengan sejawat
10. Data Pasien Insecure — Riwayat di kertas, mudah hilang

Solusi Nakesmart untuk Nakes
Problem · Solusi Nakesmart
Income terbatas · 8+ revenue streams (telemedicine, article, affiliate, dll)
Susah cari pasien · 1000+ pasien aktif, AI matching by spesialisasi
Geographic limit · Telemedicine 24/7 ke seluruh Indonesia
No multi-faskes · Faskes Affiliations: praktek di banyak klinik
Payment risk · Escrow system, dana dijamin
Tools mahal · Semua terintegrasi gratis (telemedicine, e-resep, scheduling)
No passive income · Article authoring, course, tipping
SKP repot · SKP tracker otomatis + sertifikat digital
Komunitas lemah · Komunitas aktif dengan reputation system
Data insecure · Multi-layer security + anti-AI scraping

Potensi Earnings Nakes dengan Nakesmart (Realistic)
Tier Nakes · Telemedicine · Affiliate · Article · Total/bulan
Junior (< 5 thn) · Rp3-15jt · Rp1-5jt · Rp0-2jt · Rp4-22jt
Mid (5-10 thn) · Rp10-40jt · Rp3-15jt · Rp1-8jt · Rp14-63jt
Senior (10-20 thn) · Rp25-100jt · Rp5-30jt · Rp3-25jt · Rp33-155jt
Specialist · Rp50-200jt · Rp10-50jt · Rp5-50jt · Rp65-300jt

Estimasi ini realistic. Actual earnings tergantung consistency, spesialisasi, dan reputation building.""",

    "2.1": """Landscape praktek digital untuk nakes Indonesia:

Halodoc Doctor — Telemedicine dengan high volume
• Revenue share ~70/30 (nakes/platform)
• Banyak pasien tapi tarif rendah (Rp30-50rb)
• Tidak ada multi-tier system

Alodokter Doctor — Banyak konsultasi gratis (CSR)
• Sebagian besar gratis (tidak ada revenue)
• Tarif premium rendah
• Tidak ada Faskes Affiliations

Good Doctor — Premium telemedicine
• Tarif tinggi tapi pasien terbatas
• Geographic limit (mostly Jakarta)
• Tidak ada e-resep terintegrasi

Praktek Mandiri (Klinik/RS)
• Income besar tapi modal & risiko tinggi
• Marketing personal mahal
• No remote pasien

Direct WhatsApp/Phone
• Tidak ada protection
• Tidak ada e-resep
• Susah scale

Kebanyakan nakes combine 2-3 platform ini dengan income tidak stabil.""",

    "2.2": """Kompetitor #1: Halodoc Doctor
• Revenue share: ~70/30
• Pros: High volume pasien, established brand
• Cons: Tarif flat rendah (Rp30-50rb), tidak ada multi-tier, tidak ada Faskes Affiliations

Kompetitor #2: Alodokter Doctor
• Revenue share: variable
• Pros: Konten authority, banyak baca
• Cons: Banyak konsultasi gratis (CSR), tarif premium rendah

Kompetitor #3: KlikDokter
• Revenue share: ~75/25
• Pros: Quality patient base
• Cons: Limited slot, harus apply admin

Kompetitor #4: Independent (WhatsApp/Phone)
• Revenue share: 100% (no platform fee)
• Pros: Full control
• Cons: No protection, no marketing, susah scale, no e-resep, no scheduling""",

    "2.3": """Keunggulan #1: Revenue Share 80/20 — Tertinggi di Industri
Standar industri telemedicine Indonesia 70/30. Nakesmart 80/20 = 10% lebih banyak earnings.

Keunggulan #2: 3-Tier Pricing System
Anda bisa atur:
- Reguler (chat 30 menit): Rp45-100rb sesuai pengalaman
- Premium (chat 45 menit): Rp75-150rb
- Exclusive (video 15 menit): Rp150-500rb
Tidak ada kompetitor yang punya 3 tier seperti ini.

Keunggulan #3: Multi-Faskes Affiliations
Praktek di klinik A pagi, klinik B sore, telemedicine malam. Semua dalam 1 akun.

Keunggulan #4: E-Resep Digital Terintegrasi
Resep langsung masuk akun pasien. Tidak perlu print + tanda tangan. QR code verifikasi.

Keunggulan #5: Article Authoring Passive Income
Tulis artikel kesehatan → publish → dapat poin per view. Top artikel: Rp1-10jt/bulan passive.

Keunggulan #6: Komunitas dengan Reputation
Jawab Q&A → best answer dapat poin. Build reputasi → AI prioritize Anda di matching.

Keunggulan #7: SKP Tracker + Sertifikat Digital
Tracking otomatis SKP dari konsultasi, webinar, course. Tidak perlu manual catat.

Keunggulan #8: Wallet + Multi-Bank Withdrawal
Earnings masuk wallet. Withdraw ke bank mana saja (BCA, BNI, BRI, Mandiri, dll).

Keunggulan #9: Anti-AI Scraping Protection
Data konsultasi Anda dengan pasien terlindungi dari AI bot scraping.

Keunggulan #10: Free Education & Training
Course gratis untuk nakes (telemedicine ethics, e-prescribing, dll).""",

    "2.4": """Matriks Komparasi Nakes Platform

Fitur · Nakesmart · Halodoc · Alodokter · Good Doctor
Revenue Share · 80/20 · 70/30 · Variable · 70/30
Multi-Tier Pricing · ✅ 3 tier · ❌ Flat · ❌ Flat · ⚠️ 2 tier
Multi-Faskes Affiliations · ✅ Unlimited · ❌ · ❌ · ❌
E-Resep Digital · ✅ QR + verify · ✅ Basic · ⚠️ Limited · ✅ Basic
SIMRS Integration · ✅ Faskes partner · ❌ · ❌ · ❌
Article Authoring Income · ✅ Per view · ❌ Volunteer · ✅ Voluntary · ❌
SKP Tracker · ✅ Auto · ❌ · ❌ · ❌
Komunitas Reputation · ✅ Active · ❌ · ⚠️ · ❌
Health Diary Doctor Report · ✅ View patient trends · ❌ · ❌ · ❌
Family Hub Patient Support · ✅ · ❌ · ❌ · ❌
Wallet + Multi-Bank Payout · ✅ Auto · ⚠️ Limited · ⚠️ · ⚠️
Anti-AI Scraping · ✅ 5 layers · ❌ · ❌ · ❌
Geographic Reach · Indonesia · Indonesia · Indonesia · Kota besar

Kesimpulan: Nakesmart unggul di revenue share, multi-tier, multi-faskes, dan tools profesional.""",

    "3.1": """Profile & Verification — pintu masuk pasien menemukan Anda.

Components Profile Nakes
• Foto profesional (formal, latar netral)
• Nama lengkap + gelar (e.g. dr. Budi Santoso, Sp.PD)
• Spesialisasi (umum, spesialis penyakit dalam, dll)
• Bio singkat (200 karakter)
• Education background:
  - Pendidikan dokter (FK Universitas X, tahun)
  - Spesialisasi (PPDS Universitas Y, tahun)
  - Subspesialisasi
  - Fellowship
• Pengalaman kerja (RS A 2015-2018, dll)
• Bahasa (ID, EN, daerah)
• Fokus area (Hipertensi, Diabetes, Kesehatan Reproduksi, dll)
• Sertifikat terkini (link ke modul SKP)

Verifikasi (Wajib)
• Upload foto STR (Surat Tanda Registrasi)
• Upload foto SIP (Surat Izin Praktek)
• Upload foto KTP
• Verifikasi by admin (1-3 hari)
• Setelah verify: badge ✅ Verified

Tier Nakes (Internal Score)
• Junior (< 5 tahun): rating awal 4.0
• Mid (5-10 tahun): rating awal 4.3
• Senior (10-20 tahun): rating awal 4.5
• Specialist with subspecialty: rating awal 4.7

Discovery Algorithm
• AI matching berdasarkan:
  - Spesialisasi vs keluhan pasien
  - Rating + jumlah ulasan
  - Response time (cepat = priority)
  - Tier tarif vs budget pasien
  - Bahasa cocok
  - Lokasi (untuk offline booking)""",

    "3.2": """Setup Tier Telemedicine — atur 3 tier harga.

Cara Setup
1. Akun → "Tier Telemedicine"
2. Toggle setiap tier (Reguler / Premium / Exclusive)
3. Atur tarif per tier (dalam range yang disarankan)
4. Atur jam tersedia per tier
5. Atur tipe layanan (chat only / chat + voice / video)
6. Simpan

Reguler (Tier Wajib untuk Mulai)
• Chat text + foto/file
• Durasi 30 menit
• Tarif: Rp45-100rb (suggested)
• Anda dapat 80% = Rp36-80rb per sesi
• Pasien target: keluhan ringan, follow-up

Premium (Recommended)
• Chat + voice note + foto/video lebih banyak
• Durasi 45 menit
• Tarif: Rp75-200rb (suggested)
• Anda dapat 80% = Rp60-160rb per sesi
• Pasien target: konsultasi mendalam, kondisi kronis

Exclusive (Premium Earnings)
• Video Zoom HD 15 menit
• E-Resep dengan stempel digital
• Tarif: Rp150-500rb (suggested untuk spesialis)
• Anda dapat 80% = Rp120-400rb per sesi
• Pasien target: butuh visual examination, second opinion

Pricing Strategy
- Junior nakes: mulai dari range bawah, build review dulu
- Mid nakes: range tengah, fokus quality
- Senior/Specialist: range atas, eksklusivitas
- Update tarif setiap 3 bulan berdasarkan permintaan

Tier Verification
Admin verify bahwa Anda eligible untuk Exclusive tier (perlu spesialisasi).""",

    "3.3": """Telemedicine Inbox — pusat manajemen konsultasi.

Tampilan Inbox
• Tab "Pending" — booking yang perlu accept/reject
• Tab "Scheduled" — booking yang sudah dikonfirmasi
• Tab "In Progress" — konsultasi yang sedang berjalan
• Tab "Completed" — riwayat konsultasi selesai
• Tab "Cancelled" — yang dibatalkan

Booking Card Menampilkan
• Nama pasien + foto
• Spesialisasi keluhan
• Tier yang dipilih (Reguler/Premium/Exclusive)
• Jadwal slot
• Tarif yang akan diterima (setelah platform fee)
• Keluhan awal pasien

Aksi di Booking
• Accept → notify pasien
• Reject (dengan alasan)
• Reschedule (propose alternative time)
• Tambah catatan internal

Notifikasi
• Push notification saat ada booking baru
• Reminder 1 jam sebelum sesi
• Reminder 5 menit sebelum sesi
• Alert pasien sudah masuk chat room

Time Management
- Auto-decline jika tidak respond 30 menit
- Buffer otomatis antar slot (15 menit)
- Block specific dates (cuti, libur)""",

    "3.4": """E-Resep Digital — tulis resep dengan QR code verifikasi.

Cara Tulis E-Resep
1. Selama/setelah konsultasi
2. Klik "Tulis E-Resep"
3. Tambah obat satu per satu:
   - Cari obat dari database (generic + dagang)
   - Pilih dosis (mg)
   - Pilih frekuensi (1x sehari, 3x sehari, dll)
   - Pilih durasi (5 hari, 14 hari, dll)
   - Catatan khusus (sebelum/sesudah makan, dll)
4. Add as many obat as needed
5. Tanda tangan digital (auto-generate)
6. Simpan → kirim ke pasien

Hasil E-Resep
• PDF dengan format resep standar
• QR code untuk verifikasi apotek
• Nama nakes + nomor STR/SIP
• Tanggal + masa berlaku (default 7 hari)
• Stempel digital
• Otomatis masuk akun pasien

E-Resep Template
• Save template untuk obat yang sering diresep
• Quick-fill untuk efisiensi
• Bisa edit per pasien

Audit & Tracking
• Setiap e-Resep tercatat di profile Anda
• Tracking SKP otomatis (5 SKP per 50 e-Resep)
• Pasien bisa rate e-Resep (untuk improve)

Verifikasi Apotek
• Apotek scan QR → verifikasi keaslian
• Database obat terkontrol untuk obat keras
• Tidak bisa tulis obat narkotika tanpa SIP narkotika""",

    "3.5": """Nakes Payouts — withdrawal earnings ke rekening bank.

Saldo Wallet
• Setiap konsultasi selesai → 80% masuk wallet (setelah konfirmasi pasien)
• Wallet ditampilkan real-time di dashboard
• Riwayat transaksi lengkap

Withdrawable Status
• Earnings dari konsultasi yang sudah complete + lewat 24 jam
• Auto-release jika pasien tidak protest
• Status: pending → withdrawable → processing → completed

Cara Withdraw
1. Tab "Payouts" → "Withdraw"
2. Pilih jumlah (minimal Rp50.000)
3. Pilih rekening bank tujuan (tambah jika belum ada)
4. Confirm dengan OTP
5. Status: processing (1-2 hari kerja)
6. Setelah sukses: notifikasi + bukti transfer

Bank Tujuan
• BCA, BNI, BRI, Mandiri, CIMB, Permata, BSI, BJB, dan bank lainnya
• Bisa tambah multiple rekening
• Switch antar rekening

Fee Withdrawal
• Rp50.000 - 500.000: gratis 1x/bulan
• > 500.000: Rp2.500 per withdraw
• Premium nakes: gratis unlimited

Pajak (Penting!)
• Nakesmart auto-track earnings untuk laporan pajak
• Export annual statement
• PPh 21 (untuk nakes karyawan) sudah dihitung
• PPh 23 (untuk nakes freelance) auto-deduct""",

    "3.6": """Nakes Recruitment — cari lowongan part-time atau full-time di faskes.

Tab Recruitment Menampilkan
• Lowongan dari faskes partner
• Filter:
  - Lokasi (provinsi, kota)
  - Spesialisasi yang dicari
  - Jenis (part-time, full-time, on-call)
  - Tarif yang ditawarkan
  - Benefit (BPJS, insentif, dll)

Aplikasi Lowongan
1. Klik "Apply" di lowongan
2. Auto-attach CV dari profile Anda
3. Isi cover letter singkat
4. Submit
5. Faskes review → schedule interview

Setelah Diterima
• Auto-set up Faskes Affiliation
• Sync ke jadwal Anda
• Bisa terima booking dari pasien faskes tersebut

Insentif
• Nakes Recruitment fee untuk Nakesmart: gratis
• Negosiasi tarif & jadwal: langsung dengan faskes
• Nakesmart sebagai matchmaker only""",

    "3.7": """Faskes Affiliations — praktek di multi-faskes.

Cara Affiliate
• Diundang faskes via tab "Undangan Faskes"
• Atau apply lowongan di "Nakes Recruitment"
• Accept undangan/offer

Status Affiliation
• Active — sedang praktek
• Inactive — tidak aktif sementara
• Terminated — sudah berhenti

Per Faskes
• Atur jadwal praktek di faskes tersebut
• Atur tarif khusus (bisa berbeda dari tier telemedicine)
• Sync e-Resep dengan SIMRS faskes
• Akses pasien faskes yang assigned

Faskes-Specific Settings
• Bisa setting beda per faskes
• Hari Senin di Klinik A, Selasa di Klinik B
• Tarif beda per faskes (Klinik A premium, Klinik B mid)

Sync Pasien
• Riwayat pasien sync dengan SIMRS faskes
• E-Resep tertulis di sistem faskes & Nakesmart
• Health Diary pasien tetap independen""",

    "3.8": """Article Authoring — tulis artikel kesehatan dan dapat passive income.

Cara Tulis Artikel
1. Tab "Article Authoring"
2. Klik "Tulis Artikel Baru"
3. Editor lengkap dengan:
   - Format teks (heading, bold, list)
   - Insert gambar
   - Insert video (YouTube embed)
   - Insert kode markdown
   - Auto-save
4. Tambah:
   - Judul (max 100 karakter)
   - Excerpt (max 200 karakter)
   - Kategori
   - Tag
   - Featured image
5. Submit untuk review admin

Review Process
• Admin medical advisor review 1-3 hari
• Cek: akurasi medis, sumber, plagiarism
• Approve atau request revision
• Setelah approve: publish + notifikasi reader

Monetisasi Artikel
• Setiap view: +0.5 poin (= Rp5)
• Setiap like: +1 poin
• Setiap share: +2 poin
• Bookmark: +1 poin

Top Artikel Bisa Earn
• Viral artikel: 100K+ views/bulan
• Earning potential: Rp500K - 10jt/bulan per artikel
• Royalty selama artikel di-baca

Best Practices
• Topik current/seasonal (flu di musim hujan)
• Tulis untuk awam (jangan terlalu teknis)
• Sertakan referensi
• Add infographic
• Update secara berkala""",

    "3.9": """Komunitas — jawab Q&A pasien & sesama nakes.

Tab Q&A
• Pertanyaan dari pasien
• Filter by spesialisasi
• Sortir by terbaru / paling banyak engagement

Jawab Pertanyaan
• Klik pertanyaan → tulis jawaban
• Format teks lengkap
• Bisa attach gambar
• Submit

Reputation System
• Best Answer: +50 poin + badge
• Most helpful (vote): +20 poin
• Top contributor: featured profile

Aturan Komunitas
- Tidak boleh diagnosis spesifik (jawab umum)
- Tidak boleh ask DM untuk konsultasi (harus via Nakesmart)
- Tidak boleh promote obat ilegal
- Wajib disclaimer "konsultasikan dengan dokter"

Discussion Hub
• Topik mingguan (e.g. Diabetes Awareness)
• Anda jadi expert host
• Engagement = reputation""",

    "3.10": """SKP & Sertifikat — kelola pengembangan profesional.

SKP Tracker (Auto)
Tracking otomatis SKP dari:
• Konsultasi (5 SKP per 50 konsultasi)
• Article authoring (10 SKP per 5 artikel published)
• Webinar attendance (sesuai SKP webinar)
• Best Answer komunitas (1 SKP per 10 best answers)

Sertifikat Digital
Dari event di Nakesmart:
• Webinar (auto-issue setelah attend > 75%)
• Workshop (issue manual oleh organizer)
• Course completion
• Speaker fee at event

Download Sertifikat
• PDF dengan QR code verify
• Logo nakesmart + organizer + Kemenkes (jika partnered)
• Bisa dipakai untuk re-registrasi STR

CME Synchronization
• Untuk dokter: sync dengan KKI/IDI
• Untuk perawat: sync dengan PPNI
• Untuk bidan: sync dengan IBI

Reminder Re-Registrasi
• Notifikasi 6 bulan sebelum STR expired
• Total SKP yang harus dipenuhi
• Saran event/webinar untuk fulfill SKP""",

    "4.1": """Nakes Wallet — pusat earnings multi-sumber.

Sumber Income di Wallet
• Telemedicine sessions (80%)
• Article authoring royalty
• Faskes affiliation fee (sesuai kontrak)
• Webinar speaker fee
• Referral fee
• Affiliate commission
• Best Answer rewards
• Course earnings (Phase 3)

Wallet Status
• Available balance
• Pending balance (belum cleared)
• Withdrawable balance
• Total earnings (lifetime)
• Total payouts (lifetime)

Transaksi
• Riwayat detail dengan filter
• Search by tanggal, jenis, pasien
• Export CSV/PDF untuk pajak

Convert Poin
• Poin (dari reputation) → wallet
• 100 poin = Rp1.000

Auto-Reinvest Option
- Bisa setting % saldo auto-buy course/webinar untuk SKP
- Atau auto-donate ke charity partner""",

    "4.2": """Nakes Availability — atur jadwal otomatis.

Calendar View
• Lihat semua slot per minggu/bulan
• Color coding:
  - Hijau: available untuk booking
  - Kuning: tentative (bisa rejected)
  - Merah: blocked (cuti, libur)
  - Biru: sudah dibooking

Bulk Setting
• Set jam praktek default (e.g. Senin-Jumat 9-17)
• Set buffer antar slot (15-30 menit)
• Set max booking per hari (e.g. 10 telemedicine)

Block Specific Dates
• Cuti, libur nasional, agenda pribadi
• Recurring (setiap minggu di hari X)

Vacation Mode
• Set auto-decline semua booking
• Auto-reply ke pasien yang mau book
• Resume dengan toggle

Smart Suggestions
- AI saran slot popular (jam pasien sering book)
- Suggest harga adjustment berdasarkan demand
- Suggest expand availability jika overbook""",

    "4.3": """Referral Program untuk Nakes — earn dengan ajak faskes & pasien.

Refer Faskes
• Anda kenal klinik yang mau onboard?
• Share kode referral Anda ke faskes
• Setelah faskes subscribe → Anda dapat:
  - Rp500K-1jt onboarding fee per faskes
  - 5% recurring fee selama mereka aktif

Refer Pasien
• Bagikan kode ke pasien baru
• Setelah pasien daftar + transaksi pertama:
  - Anda: 1.000 poin (= Rp10K)
  - Pasien: voucher Rp10K

Refer Nakes Lain
• Ajak kolega nakes untuk join Nakesmart
• Setelah mereka verify + first earning:
  - Anda: Rp100K bonus
  - Nakes baru: priority verifikasi

Anti-Fraud
- Verifikasi by phone + email
- Device fingerprint
- AI fraud detection""",

    "4.4": """Affiliate Earnings — komisi dari layanan partner.

Affiliate Partners
• Apotek online (komisi 5-10% per resep tebusan)
• Lab partner (komisi per rujukan)
• Asuransi kesehatan (komisi per polis terjual)
• Kursus medical (komisi per registrasi)

Cara Earn
• Bagikan link affiliate Anda
• Track per click + conversion
• Komisi auto-credit ke wallet

Tracking
• Dashboard affiliate dengan analytics
• Conversion rate per partner
• Earnings per bulan
• Top performing campaigns""",

    "4.5": """Gamification — Badges & Poin untuk Nakes.

Badges yang Bisa Diperoleh
• First Consultation (1 sesi)
• Power Consultant (100 sesi)
• Top Rated (rating > 4.8, > 50 ulasan)
• Article Author (5 artikel published)
• Best Answer Champion (50+ best answers)
• SKP Master (200+ SKP earned)
• Veteran (1 tahun di Nakesmart)
• Specialist Pioneer (top performer di spesialisasi)
• Community Hero (top contributor)
• Featured Doctor (di profile public)

Leaderboards
• Top Earners per spesialisasi
• Top Rated per kota
• Top Article Authors
• Top Q&A Contributors

Featured Nakes
• Featured di homepage Nakesmart
• Banner di category page
• Hadiah eksklusif untuk top performer""",

    "4.6": """Notification Preferences — atur notif pintar untuk efisiensi.

Notifikasi yang Bisa Diatur
• Booking baru (push + email)
• Reminder konsultasi (1 jam, 5 menit)
• Pasien chat masuk (push)
• E-Resep di-tebus pasien
• Article approved/rejected
• Earnings masuk wallet
• Withdrawal status
• Q&A new question (filter by spesialisasi)
• Komunitas mention/reply
• SKP earned
• Sertifikat issued

Channels
• Push notification (mobile)
• Email
• WhatsApp (untuk urgent)
• SMS (only urgent)

Quiet Hours
• Set silent dari jam X-Y
• Tetap log, tapi tidak push""",

    "4.7": """Health Diary Doctor Report — lihat trend pasien Anda.

Saat Pasien Booking Anda
• Otomatis request akses ke Health Diary mereka
• Pasien grant akses 30 hari terakhir (default)
• Atau full history (jika pasien izinkan)

Trend Analytics
• Grafik tekanan darah pasien selama 30 hari
• Grafik gula darah
• Pola mood
• Gejala harian dengan severity
• Korelasi: mood vs tidur, BP vs aktivitas

Insights untuk Diagnosis
• Pasien BP tidak terkontrol meskipun obat? → cek pola medikasi
• Mood drop di akhir pekan? → mungkin work stress
• Gula darah spike di malam? → check dinner habits

Setelah Konsultasi
• Tambah catatan ke Health Diary pasien (dokter view only)
• Atau saran ke pasien untuk add catatan tertentu""",

    "5.1": """Flow Nakes dari onboarding hingga payout:

Phase 1: Registrasi & Verifikasi (1-3 hari)
- Daftar akun
- Upload STR, SIP, KTP
- Admin verifikasi
- Badge ✅ Verified

Phase 2: Setup Profil & Tier (30 menit)
- Lengkapi profil profesional
- Setup 3 tier telemedicine
- Setup jadwal availability

Phase 3: Marketing Profile (ongoing)
- Tulis bio menarik
- Upload foto profesional
- Setup spesialisasi & focus area
- Build reputation via Q&A

Phase 4: Terima Booking (real-time)
- Pasien book → notification masuk
- Accept/reject dalam 30 menit
- Sync ke calendar

Phase 5: Konsultasi (15-60 menit)
- Chat/voice/video session
- Diagnosis & saran
- Catat di EMR

Phase 6: E-Resep (10 menit)
- Tulis e-Resep digital
- Submit dengan tanda tangan digital
- Auto kirim ke pasien

Phase 7: Payout (1-2 hari)
- Earnings masuk wallet
- 24 jam protection period
- Withdrawable
- Withdraw ke bank""",

    "5.2": """Phase 1: REGISTRASI & VERIFIKASI

Step 1.1: Daftar Akun
- Buka nakesmart.com
- Klik "Daftar Sebagai Nakes"
- Pilih role: Dokter / Bidan / Perawat / Apoteker / Psikolog / Ahli Gizi / Fisioterapis
- Email + password atau Google login
- Verifikasi OTP

Step 1.2: Upload Dokumen Verifikasi
Wajib (semua role):
• Foto KTP (jelas, terbaca semua data)
• Foto STR depan + belakang
• Selfie pegang KTP

Tambahan per Role:
• Dokter: SIP, ijazah dokter, sertifikat spesialisasi (jika ada)
• Perawat: SIP perawat, ijazah keperawatan
• Bidan: SIP bidan, ijazah kebidanan
• Apoteker: SIPA, ijazah apoteker
• Psikolog: SIPP, ijazah psikologi + S2

Step 1.3: Tunggu Verifikasi
• Admin verifikasi 1-3 hari kerja
• Notifikasi via email + push
• Jika ada data kurang/salah → revision request
• Setelah approved → badge ✅ Verified

Step 1.4: Aktivasi Akun
• Akun aktif untuk terima booking
• Tampil di marketplace nakes
• Bisa mulai setup tier""",

    "5.3": """Phase 2: SETUP PROFIL & TIER

Step 2.1: Lengkapi Profil Profesional
- Foto profesional (formal, latar netral)
- Bio: 200 karakter, highlight pengalaman + spesialisasi
- Education:
  - Pendidikan dokter
  - PPDS (jika spesialis)
  - Fellowship/subspesialisasi
- Pengalaman kerja (RS, klinik, organisasi)
- Bahasa yang dikuasai
- Fokus area (3-5 topik utama)

Step 2.2: Setup 3 Tier Telemedicine
Tab "Tier Telemedicine":
- Reguler (Chat 30 menit): tarif
- Premium (Chat 45 menit): tarif
- Exclusive (Video 15 menit): tarif (hanya jika spesialis)

Rekomendasi Tarif (Junior Dokter Umum)
- Reguler: Rp45.000
- Premium: Rp75.000
- Exclusive: tidak diaktifkan dulu

Rekomendasi Tarif (Spesialis 5+ tahun)
- Reguler: Rp75.000
- Premium: Rp125.000
- Exclusive: Rp250.000

Step 2.3: Setup Tipe Layanan
- Chat only / Chat + Voice / Chat + Voice + Video
- Spesialisasi yang dilayani
- Jenis konsultasi (Konsultasi awal / Follow-up / Second opinion)""",

    "5.4": """Phase 3: ATUR JADWAL & AVAILABILITY

Step 3.1: Set Jam Praktek Default
Tab "Availability":
- Senin: 9-17 (telemedicine)
- Selasa: 9-17
- Rabu: 9-13 (off PM)
- Kamis: 9-17
- Jumat: 9-15
- Sabtu: 9-13
- Minggu: off

Step 3.2: Set Buffer & Limit
- Buffer antar sesi: 15 menit (recommended)
- Max booking per hari: 10 telemedicine
- Hari off: cuti tanggal X, Y, Z

Step 3.3: Sync dengan Faskes (Jika Affiliasi)
Jika praktek di klinik A:
- Senin AM: di klinik A (telemedicine off)
- Senin PM: telemedicine on
Sync dengan SIMRS faskes A.

Step 3.4: Vacation Mode (Saat Cuti)
- Set start - end date
- Auto-decline semua booking
- Auto-reply ke pasien""",

    "5.5": """Phase 4: TERIMA BOOKING

Booking Masuk
• Push notification + email
• Detail booking:
  - Nama pasien
  - Tier dipilih
  - Slot waktu
  - Keluhan awal pasien
  - Health Diary access (jika diberi)

Decision (Within 30 Minutes)
• Accept → notifikasi pasien
• Reject (dengan alasan: "Tidak available hari itu", "Bukan spesialisasi saya")
• Reschedule (propose 3 alternative slots)

Setelah Accept
• Slot terblock di calendar
• Pasien dapat konfirmasi & QR code
• Reminder otomatis 1 jam & 5 menit sebelum

Persiapan Pra-Konsultasi
- Buka Health Diary pasien (jika ada akses)
- Review riwayat konsultasi sebelumnya
- Siapkan kemungkinan diagnosis differential""",

    "5.6": """Phase 5: KONSULTASI & DIAGNOSIS

Untuk Reguler/Premium (Chat)
1. 5 menit sebelum mulai, tombol "Mulai Sesi" aktif
2. Klik → masuk ke chat room
3. Sapa pasien dengan profesional
4. Tanya keluhan utama (lalu detail)
5. Anamnesa lengkap:
   - Kapan mulai, lokasi, severity, faktor pemicu
   - Riwayat obat, alergi
   - Riwayat penyakit
   - Lifestyle (rokok, alkohol, olahraga)
6. Jika perlu, minta foto/video tambahan
7. Berikan diagnosis (atau diagnosis differential)
8. Edukasi pasien
9. Berikan saran/resep

Untuk Exclusive (Video)
1. 5 menit sebelum, tombol "Join Video" aktif
2. Klik → masuk Zoom (embed di Nakesmart)
3. Cek koneksi, intro
4. Anamnesa + pemeriksaan visual (lihat ruam, mata, mulut)
5. Diagnosis lebih confident
6. Edukasi + resep

Catatan Klinis
• Tulis di "Notes" panel
• Auto-saved
• Pasien tidak lihat (kecuali Anda share)
• Pakai SOAP format jika perlu:
  - Subjective: keluhan pasien
  - Objective: hasil pemeriksaan
  - Assessment: diagnosis
  - Plan: rencana terapi""",

    "5.7": """Phase 6: E-RESEP & FOLLOW-UP

Tulis E-Resep
1. Klik "Tulis E-Resep"
2. Add obat:
   - Search nama obat
   - Pilih kekuatan/dosis
   - Pilih frekuensi
   - Durasi
   - Catatan
3. Add as many as needed
4. Preview e-Resep PDF
5. Tanda tangan digital
6. Submit → kirim ke pasien

Follow-Up Plan
• Saran follow-up 7-14 hari
• Booking otomatis: "Book Follow-Up dengan Dr. X"
• Diskon 20% untuk follow-up dalam 7 hari (pasien)

Edukasi Lifestyle
- Catatan di Health Diary pasien
- Saran: "Catat tekanan darah pagi & malam selama 7 hari"
- Pantangan: makanan/aktivitas
- Tanda darurat: kapan harus ke IGD

Referral ke Spesialis
- Jika butuh rujukan, suggest via Nakesmart
- Pasien bisa book langsung ke spesialis tsb""",

    "5.8": """Phase 7: PAYOUT & RATING

24 Jam Setelah Konsultasi
• Earnings 80% masuk wallet dengan status "pending"
• Jika pasien tidak protest dalam 24 jam → status "withdrawable"

Withdraw ke Bank
1. Tab "Payouts"
2. Klik "Withdraw"
3. Jumlah (min Rp50K)
4. Pilih rekening
5. OTP verifikasi
6. Status: processing
7. 1-2 hari kerja masuk rekening

Rating dari Pasien
• Pasien dapat rate 1-5 star
• Pasien dapat tulis review
• Rating Anda update otomatis

Build Reputation
• Rating > 4.5 + 50 ulasan → badge "Top Rated"
• Top Rated → priority di marketplace search
• More booking → more earnings""",

    "6.1": """Maksimalkan Telemedicine Income — main revenue stream Anda.

Strategi 1: Optimize Pricing
- Junior: mulai dari range bawah, build review
- Mid: range tengah, fokus quality
- Senior: range atas, eksklusivitas
- Update tarif setiap 3 bulan berdasarkan demand

Strategi 2: Maximize Availability
- Buka jam yang banyak diminati (sore, malam, weekend)
- Pasien sering book malam 19-22, weekend pagi 9-12
- Junior nakes: mulai dengan 40 jam/minggu untuk volume

Strategi 3: Response Time
- Respond booking < 5 menit
- AI prioritize Anda di matching
- Pasien lebih likely book Anda

Strategi 4: Quality > Quantity
- Konsultasi tepat waktu (jangan ngaret)
- Tidak cancel last-minute
- Profesional + ramah
- Hasil rating tinggi → more booking

Strategi 5: Specialty Focus
- Fokus 1-2 spesialisasi untuk build reputation
- Daripada "all-rounder"
- Specialist earnings biasanya 2-3x lebih tinggi

Potensi Earnings
- Junior dokter umum: 30 konsultasi/minggu × Rp36K = Rp4.3jt/bulan
- Mid dokter umum: 50 konsultasi/minggu × Rp60K = Rp12jt/bulan
- Senior spesialis: 70 konsultasi/minggu × Rp200K = Rp56jt/bulan""",

    "6.2": """Maksimalkan Faskes Affiliations Income.

Strategi Affiliate Multi-Faskes
- Affiliate dengan 2-3 faskes
- Atur jadwal: Klinik A Senin AM, Klinik B Selasa PM
- Telemedicine di sisa waktu

Tarif Negotiasi
• Per session base (Rp200-500K tergantung jam)
• Atau gaji bulanan (Rp10-25jt untuk part-time)
• Atau revenue share (60-70% untuk nakes)

Faskes Premium
• Faskes dengan reputasi baik = lebih banyak pasien
• Klinik VVIP = tarif lebih tinggi
• RS swasta vs RSUD

Insentif Tambahan
• Bonus jika capai target pasien/bulan
• Bonus untuk rujukan pasien (referral fee)
• Akses pelatihan + sertifikat dari faskes""",

    "6.3": """Article Authoring Income — passive income dari konten.

Strategi Tulis Artikel Populer
1. Topik trending (cek Google Trends, social media)
2. Topik current (musim flu, vaksinasi anak)
3. SEO-friendly (gunakan keyword yang dicari)
4. Format mudah dibaca (subheading, list, infografis)

Topik dengan Engagement Tinggi
- "Cara Atasi Demam Anak"
- "Diet untuk Penderita Diabetes"
- "Tanda-Tanda Kanker Payudara"
- "Mental Health di Tempat Kerja"
- "Vaksinasi COVID-19: Update Terbaru"

Strategi Maintain
- Tulis 2-3 artikel per bulan
- Update artikel lama yang masih populer
- Reply komentar pembaca

Compound Effect
- Bulan 1: 1 artikel × 5K views × Rp5 = Rp25K
- Bulan 6: 6 artikel × 10K views avg × Rp5 = Rp300K/bulan
- Bulan 12: 12 artikel × 20K views avg × Rp5 = Rp1.2jt/bulan
- Bulan 24: 24 artikel × 30K views avg × Rp5 = Rp3.6jt/bulan""",

    "6.4": """Webinar/Event Speaker Fee — earning sebagai pembicara.

Cara Jadi Speaker
1. Daftar di "Speaker Catalog"
2. Setup profil speaker:
   - Topik yang dikuasai
   - Pengalaman public speaking
   - Sample video (jika ada)
3. EO/organizer mencari speaker
4. Mereka invite Anda untuk event

Fee Speaker
• Webinar 1 jam: Rp500K-2.5jt
• Workshop 4 jam: Rp2-7.5jt
• Seminar full day: Rp5-15jt
• Conference keynote: Rp10-50jt

Plus Insentif
• SKP credits (bisa di-claim Anda)
• Sertifikat speaker
• Recording untuk portofolio
• Networking dengan attendees

Tips
- Topik niche (specialist) = fee lebih tinggi
- Build authority via article + komunitas dulu
- Bisa repeat speaker (event series)""",

    "6.5": """Referral Fee dari Faskes — earn dengan rekomendasi.

Refer Faskes ke Nakesmart
- Anda kenal klinik/RS yang belum onboard?
- Bagikan kode referral
- Setelah faskes subscribe → Anda dapat:
  - Rp500K-1jt onboarding fee
  - 5% recurring fee (selama mereka aktif)

Refer Sesama Nakes
- Ajak kolega join Nakesmart
- Setelah mereka verify + first earning:
  - Rp100K bonus
  - Akses ke private channel networking

Refer Pasien Premium
- Bagikan kode ke pasien
- Setelah upgrade Pasien Premium:
  - Rp25K per pasien Premium baru

Track di Tab "Referral"
- Jumlah refer + status
- Total earnings dari referral
- Tier referral (Bronze/Silver/Gold)""",

    "6.6": """Course Authoring (Phase 3 Feature — Coming Soon)

Akan tersedia akhir 2026.

Apa yang Bisa Dibuat
• Online course untuk pasien (e.g. "Hidup Sehat dengan Diabetes")
• Course untuk nakes lain (e.g. "Update Hipertensi Guidelines 2026")
• Workshop terkurasi
• Diabetes self-management course

Revenue
• 70% creator, 30% platform
• Harga course Rp99K-2jt
• Top course earn Rp10-100jt/bulan

Tools
• Video upload + chapter
• Quiz + assessment
• Sertifikat completion
• Discussion forum""",

    "6.7": """Tipping dari Pasien (Phase 3 Feature)

Akan tersedia awal 2027.

Cara Kerja
- Pasien yang merasa puas bisa tip nakes
- Nominal: Rp10K-1jt (pasien tentukan)
- Revenue share: 95% nakes, 5% platform

Use Case
• Pasien lifesaver moment (gawat darurat handle baik)
• Konsultasi yang sangat membantu
• Apresiasi long-term care

Saat Tipping Aktif
• Tombol "Beri Tip" muncul setelah konsultasi
• Atau di profile public Anda
• Pasien bisa anonim atau dengan nama""",

    "6.8": """Self-Promotion untuk Earnings Maksimal

Sosial Media
• Share profil Nakesmart di Instagram bio
• Posting artikel Anda yang published
• Reels pendek edukasi (no diagnosis, only education)

LinkedIn
• Update profil sebagai "Telemedicine Doctor at Nakesmart"
• Share article + insights medis
• Connect dengan referral network

Networking Offline
• Tunjukkan QR card Nakesmart di praktik offline
• Pasien existing bisa book telemedicine di luar jam praktik
• Build long-term relationship

Cross-Promotion
- Speaker di event = exposure
- Article authoring = SEO traffic
- Komunitas Q&A = profile views""",

    "7.1": """Optimize Profile untuk Discovery.

Foto Profile
- Formal (jas dokter atau seragam)
- Latar putih atau biru muda
- Resolusi tinggi (min 800x800)
- Senyum profesional (tidak terlalu serius)

Bio Tips
- 200 karakter, padat informasi
- Format: "[Spesialisasi] dengan [X tahun pengalaman]. Fokus [topik utama]."
- Contoh: "dr. Budi Santoso, Sp.PD. 10 tahun pengalaman penyakit dalam. Fokus hipertensi, diabetes, dan geriatri."

Spesialisasi & Focus
- Pilih 1 spesialisasi utama
- Pilih 3-5 focus area
- AI akan match keluhan pasien ke focus Anda

Bahasa
- ID + EN = double opportunity
- Bahasa daerah = niche market

Education Lengkap
- Universitas + tahun lulus
- Sertifikat tambahan
- Fellowship

Pengalaman
- 3 RS/klinik terbaik
- Dengan tahun + posisi""",

    "7.2": """Setup Tier yang Kompetitif.

Riset Tarif Kompetitor
- Buka marketplace nakes
- Filter spesialisasi & tier
- Lihat tarif rata-rata + range

Pricing Strategy
Pilihan A: Underprice (Build Volume)
- Tarif 10-20% di bawah avg
- Targetkan high volume
- Bagus untuk junior

Pilihan B: Match Average
- Tarif sama dengan kompetitor
- Fokus quality + service
- Bagus untuk mid

Pilihan C: Premium Pricing
- Tarif 20-50% di atas avg
- Targetkan pasien spesifik
- Bagus untuk senior/specialist

A/B Testing
- Coba 1 bulan dengan tarif A
- Coba 1 bulan dengan tarif B
- Pilih yang ROI lebih baik

Tier Distribution
- Reguler: 60% pasien (volume)
- Premium: 30% pasien (fokus)
- Exclusive: 10% pasien (premium)""",

    "7.3": """Best Practices Telemedicine.

Persiapan
- Cek koneksi internet 30 menit sebelum
- Ruang tenang, lighting bagus
- Headphone untuk privasi
- Backup device (HP cadangan)

Communication
- Sapa dengan profesional ("Selamat pagi, saya Dr. X")
- Tanya identitas pasien (double-check)
- Tanya keluhan utama dulu
- Aktif listening (jangan ketik selama pasien curhat)
- Repeat-back untuk konfirmasi

Anamnesa Efisien
- SOAP framework
- 80% waktu untuk anamnesa
- 10% pemeriksaan visual (jika exclusive)
- 10% edukasi + plan

Diagnosis
- Pakai bahasa awam saat jelaskan
- Differential diagnosis untuk kompleks
- Be honest tentang limitations telemedicine

Tutup Sesi
- Summary diagnosis + plan
- Konfirm pasien paham
- Saran follow-up
- E-Resep dijelaskan
- Tutup dengan "Semoga lekas sembuh"

Setelah Sesi
- Catat di EMR/notes
- Update Health Diary pasien (opsional)
- Follow-up via reminder

Ethical Considerations
- Jangan diagnosis berat tanpa pemeriksaan fisik
- Rujuk ke offline jika perlu
- Hormati privacy pasien
- Tidak boleh resepkan obat narkotika via telemedicine""",

    "7.4": """Manajemen E-Resep Efisien.

Template E-Resep
- Save template untuk kondisi sering (hipertensi, ISPA, diare)
- Quick-fill dengan modifikasi sesuai pasien

Rasional Prescribing
- Hindari over-prescribing
- Jelaskan reason setiap obat
- Catatan: kapan boleh stop

Polifarmasi Safety
- Untuk lansia, max 5 obat sekaligus
- Cek drug interaction (auto-warning di Nakesmart)
- Konsultasi farmasi jika ragu

Obat Generic vs Branded
- Generic lebih murah, sama efektif
- Edukasi pasien: "Boleh ganti dengan generic"
- Branded jika ada specific indication

E-Resep Re-fillable
- Untuk kondisi kronis, e-Resep bisa di-refill
- Tanpa harus konsultasi tiap bulan
- Save time untuk pasien & Anda""",

    "7.5": """Founding Nakes Program — Limited Slot.

Eligibility
- 100 nakes pertama per spesialisasi
- Minimum 3 tahun pengalaman
- Verified rating > 4.5
- Active 30+ konsultasi/bulan

Benefits
• Revenue share 90/10 (vs standard 80/20)
• Featured placement di homepage
• Priority verifikasi untuk artikel
• Free access to advanced courses
• Personal account manager
• Beta access ke fitur baru
• Annual networking event

Apply
- Tab "Founding Nakes Program" di Akun
- Submit aplikasi dengan portfolio
- Tunggu review (1-2 minggu)
- Onboarding 1-on-1 session

Komitmen
- Minimum 6 bulan aktif
- Quality maintained (rating > 4.7)
- Provide feedback untuk product improvement""",

    "8.1": """Aplikasi Mobile Nakes Android + PWA iOS.

Android APK
- Khusus untuk nakes (versi terpisah dari pasien app)
- Size ~60 MB
- Download: nakesmart.com/nakes/install.html
- Compatible: Android 7+

Fitur Mobile Nakes
• Push notification real-time untuk booking
• Quick accept/reject booking
• Chat dengan pasien
• Tulis e-Resep di HP
• Capture foto untuk EMR
• Lihat schedule
• Track earnings + withdraw
• Offline support (cache)

iOS PWA
- nakesmart.com/nakes/m/
- Add to Home Screen via Safari
- Push notification (iOS 16.4+)
- Splash screen

Tablet/iPad Optimization
- UI responsive untuk tablet
- Side-by-side chat + EMR
- Multi-window support (iPad Air, Pro)
- Apple Pencil support untuk handwriting""",

    "8.2": """Native SIMRS untuk Tablet/iPad (Faskes Internal).

Untuk Nakes di Faskes dengan SIMRS Nakesmart
- 12 layar Expo native
- Tampilan optimasi tablet 10-13 inch
- Modul:
  - EMR (Electronic Medical Record)
  - CMS (Clinical Management System)
  - HMS (Hospital Management System)
  - Lab orders
  - Radiology orders
  - Pharmacy
  - Billing
  - Patient queue
  - Vital signs
  - Discharge summary

Workflow Faskes Internal
1. Pasien masuk → receptionist register
2. Nakes terima notifikasi
3. Pasien masuk ruang konsultasi
4. Nakes buka SIMRS di tablet
5. Tulis catatan, order lab/radiologi
6. Tulis e-Resep
7. Discharge pasien

Sync dengan Nakesmart
- Data sinc real-time
- E-Resep juga ada di akun pasien Nakesmart
- Bisa lihat riwayat dari semua faskes affiliated""",

    "8.3": """Multi-Layer Security untuk Nakes.

Sistem 5-Layer Anti-AI Scraping
- Frontend bot detection
- Content protection (right-click, watermark)
- HMAC signed API requests
- Server-side behavioral analysis
- Anti-Claude-in-Chrome detection

Mengapa Penting untuk Nakes
- Data konsultasi pasien sangat sensitif
- Pasien percaya Anda untuk jaga data mereka
- Bocornya data = pelanggaran sumpah Hippocrates

Yang Dilindungi
• Catatan konsultasi
• E-Resep yang Anda tulis
• Riwayat pasien
• Earnings & financial data
• SKP records

Yang Tidak Dilindungi (Tetap Publik)
• Profil profesional Anda (untuk discovery)
• Artikel yang Anda publish
• Q&A jawaban (community)
• Rating & ulasan

Kompliansi
• GDPR-equivalent (Indonesian UU PDP)
• ISO 27001 (planning)
• HIPAA-style untuk medical data""",

    "8.4": """Audit Security 2026 — Round 1-8 Update.

Round 1-3: Authentication
✅ JWT hardening (no fallback)
✅ Midtrans webhook validation
✅ Wallet IDOR fixes
✅ Auth on critical endpoints

Round 4: Unauth Endpoint Hardening
✅ Bank accounts admin auth
✅ Cart verify-payment protection
✅ Admin users dump blocked
✅ EO ticket ownership check

Round 5: OTP + Race Conditions
✅ OTP tidak di-return di response
✅ Distributed lock untuk financial ops
✅ Idempotency keys

Round 6: Global Admin Guard
✅ Middleware untuk semua /api/admin/*

Round 7-8: Defense in Depth
✅ Telemedicine slot conflict check
✅ Phone E.164 normalization
✅ CORS hardening
✅ Email XSS protection
✅ File upload validation
✅ Auto-refund logic
✅ JWT blacklist fail-CLOSED

Untuk Nakes
Semua update meningkatkan keamanan:
- Akun Anda lebih sulit di-hack
- Earnings aman dari double-withdraw
- Data konsultasi pasien lebih terlindungi
- E-Resep tidak bisa di-tampering""",

    "8.5": """Roadmap Nakes 2026-2028.

Q3 2026
• AI medical assistant (saran diagnosis berdasarkan symptoms)
• Drug interaction checker real-time
• Voice-to-text untuk EMR
• Integrasi dengan KKI/IDI/PPNI untuk SKP

Q4 2026
• Course Authoring platform launch
• Tipping system untuk nakes
• Virtual Hospital Tour (untuk pasien preview faskes)
• Multi-Faskes single dashboard

Q1 2027
• AI imaging assistance (read X-Ray, MRI)
• Genomic data interpretation
• International telemedicine (Singapore, Malaysia)
• Wearable device data integration

Q2-Q4 2027
• Submit Play Store + App Store official
• Surgical planning assistance
• AR/VR for medical education
• Cross-border collaboration platform

2028
• Full integration with SatuSehat
• AI second-opinion service
• Robotic surgery assistance (consultation)
• Telemedicine for surgical follow-up

Beta Features (Founding Nakes first)
• Voice biomarker analysis
• Skin AI diagnosis
• AI diagnostic decision tree
• Real-time research integration""",

    "A": """Glossarium Nakes

CME — Continuing Medical Education
EMR — Electronic Medical Record
Faskes — Fasilitas Kesehatan
IDI — Ikatan Dokter Indonesia
KKI — Konsil Kedokteran Indonesia
MTKI — Majelis Tenaga Kesehatan Indonesia
PPDS — Program Pendidikan Dokter Spesialis
PPNI — Persatuan Perawat Nasional Indonesia
SIP — Surat Izin Praktek
SIMRS — Sistem Informasi Manajemen Rumah Sakit
SKP — Satuan Kredit Profesi
SOAP — Subjective, Objective, Assessment, Plan
STR — Surat Tanda Registrasi
Telemedicine — Konsultasi online via chat/voice/video""",

    "B": """FAQ Khusus Nakes

Q: Berapa lama verifikasi nakes?
A: 1-3 hari kerja untuk dokumen lengkap. Jika incomplete, admin request revision.

Q: Apakah saya bisa praktek di multi-faskes?
A: Bisa, unlimited. Pakai Faskes Affiliations feature.

Q: Berapa minimal withdrawal?
A: Rp50.000. Gratis 1x/bulan, atau Rp2.500/withdraw setelahnya.

Q: Apakah ada limit jumlah konsultasi per hari?
A: Tidak ada limit dari Nakesmart. Tapi kami sarankan max 30-40 sesi/hari untuk quality.

Q: Bagaimana jika pasien protest e-Resep saya?
A: Admin akan investigate. Anda bisa defend dengan SOAP notes. Jika valid, no penalty.

Q: Apakah saya boleh resepkan obat narkotika?
A: Tidak via telemedicine. Wajib offline dengan SIP narkotika.

Q: Bagaimana SKP otomatis?
A: Sync dengan KKI/IDI/PPNI by API. Track real-time di tab "SKP".

Q: Bisakah artikel saya monetize?
A: Ya, per view. Top artikel earn Rp1-10jt/bulan.

Q: Apakah saya bisa cancel booking yang sudah accepted?
A: Bisa tapi penalty: rating drop + small fee. Sebaiknya reschedule.""",

    "C": """Rate Guide per Tier per Spesialisasi (Benchmark)

Dokter Umum Junior (< 5 tahun)
- Reguler: Rp45K-65K
- Premium: Rp75K-100K
- Exclusive: tidak aktifkan dulu

Dokter Umum Mid (5-10 tahun)
- Reguler: Rp60K-85K
- Premium: Rp100K-150K
- Exclusive: Rp150K-200K

Dokter Umum Senior (10+ tahun)
- Reguler: Rp75K-100K
- Premium: Rp125K-200K
- Exclusive: Rp200K-300K

Spesialis Penyakit Dalam
- Reguler: Rp100K-150K
- Premium: Rp150K-250K
- Exclusive: Rp300K-500K

Spesialis Anak
- Reguler: Rp100K-150K
- Premium: Rp150K-250K
- Exclusive: Rp250K-400K

Spesialis Kulit & Kelamin
- Reguler: Rp125K-175K
- Premium: Rp200K-300K
- Exclusive: Rp350K-600K (banyak butuh visual)

Spesialis Mata
- Reguler: Rp100K-150K
- Premium: Rp175K-275K
- Exclusive: Rp300K-500K

Psikolog/Psikiater
- Reguler: Rp100K-150K
- Premium: Rp200K-350K
- Exclusive: Rp350K-600K

Bidan
- Reguler: Rp35K-50K
- Premium: Rp60K-90K
- Exclusive: hanya untuk konseling ANC

Apoteker
- Reguler: Rp30K-50K
- Premium: Rp60K-100K

Update tarif berdasarkan pengalaman + demand pasien.""",

    "D": """Payout Schedule & Kontak

Payout Schedule
• Real-time: setiap konsultasi selesai → wallet
• Withdraw: 1-2 hari kerja masuk bank
• Hari libur nasional: +1 hari kerja

Min/Max Withdraw
- Minimum: Rp50.000
- Maximum: Rp50.000.000 per transaksi
- Daily limit: Rp100.000.000

Bank Partner
BCA, BNI, BRI, Mandiri, CIMB, Permata, BSI, BJB, BTN, dan semua bank Indonesia.

Pajak
- PPh 21 (karyawan): admin urus kalau ada NPWP
- PPh 23 (freelance): auto-deduct 2%
- Annual statement download di Akun → Pajak

Kontak Nakes Support
• Tab "Bantuan" di aplikasi
• Email: nakes@nakesmart.com
• WhatsApp: +62 851-XXXX-XXXX
• Response time: 12 jam (urgent 2 jam)

Tentang PT Nakesmart
PT GIANNA MEDICAL CENTER
Alamat: Jakarta
Website: nakesmart.com
Email: info@nakesmart.com""",
}
