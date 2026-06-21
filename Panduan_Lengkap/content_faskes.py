# -*- coding: utf-8 -*-
"""Panduan Nakesmart untuk Faskes — content module."""

ROLE = "Faskes"
TAGLINE = "Platform Digital untuk Fasilitas Kesehatan Indonesia · SIMRS Terintegrasi"

TOC = [
    ("Bab 1 — Mengenal Nakesmart dari Sisi Faskes", [
        "1.1 Apa Itu Nakesmart untuk Faskes?",
        "1.2 Visi & Misi Nakesmart",
        "1.3 Jenis User di Nakesmart (5 Role)",
        "1.4 Mengapa Faskes Indonesia Membutuhkan Nakesmart",
    ]),
    ("Bab 2 — Kompetitor & Keunggulan Nakesmart untuk Faskes", [
        "2.1 Landscape SIMRS & Manajemen Klinik di Indonesia",
        "2.2 Kompetitor Nakesmart (dari Sisi Faskes)",
        "2.3 Keunggulan Nakesmart untuk Faskes",
        "2.4 Matriks Komparasi SIMRS & Subscription",
    ]),
    ("Bab 3 — Fitur Utama untuk Faskes", [
        "3.1 Faskes Onboarding & Verification",
        "3.2 Faskes Subscription Tiers — Pilih Paket Sesuai Skala",
        "3.3 SIMRS Lengkap — EMR/CMS/HMS",
        "3.4 Nakes Affiliations — Onboard & Manage Nakes",
        "3.5 Service Catalog — Layanan & Tarif",
        "3.6 Booking & Reservasi Management",
        "3.7 Faskes Analytics — Insights & Reports",
        "3.8 Faskes Cost Management",
        "3.9 Faskes Doctors Page — Public Profile",
        "3.10 Multi-Klinik Management (Untuk Group)",
    ]),
    ("Bab 4 — Fitur Pelengkap untuk Faskes", [
        "4.1 Faskes Wallet & Revenue Management",
        "4.2 Subscription Comparison & Upgrade",
        "4.3 Faskes Referral Leaderboard",
        "4.4 Voucher System untuk Promo",
        "4.5 Payment Methods per Faskes",
        "4.6 Investment & Partnership Page",
        "4.7 Staff & Payroll Management (CMS)",
    ]),
    ("Bab 5 — Flow Faskes Operasional", [
        "5.1 Overview Flow Faskes",
        "5.2 Phase 1: Registrasi & Subscription",
        "5.3 Phase 2: Setup Profil & Service Catalog",
        "5.4 Phase 3: Onboard Nakes",
        "5.5 Phase 4: Setup SIMRS Module",
        "5.6 Phase 5: Operasional Harian (Booking → Konsultasi → Billing)",
        "5.7 Phase 6: Monthly Reporting & Analytics",
        "5.8 Phase 7: Renewal & Upgrade Subscription",
    ]),
    ("Bab 6 — Maksimalkan ROI Subscription", [
        "6.1 Pilih Tier yang Tepat (Solo/CMS_RJ/CMS_RI/HMS)",
        "6.2 Aktivasi Multi-Klinik untuk Group",
        "6.3 Nakes Recruitment untuk Faskes Growth",
        "6.4 Service Catalog Optimization",
        "6.5 Voucher untuk Customer Retention",
    ]),
    ("Bab 7 — Tools & Strategi Growth", [
        "7.1 Faskes Profile Optimization untuk Discovery",
        "7.2 Manage Booking Backlog Efisien",
        "7.3 Multi-Channel Patient Acquisition",
        "7.4 SOP untuk Nakes Affiliated",
        "7.5 Premium Service Marketing",
    ]),
    ("Bab 8 — Fitur Baru, Mobile App & Roadmap", [
        "8.1 Native SIMRS App (Tablet/iPad)",
        "8.2 Desktop SIMRS (Electron)",
        "8.3 Multi-Layer Security & Compliance",
        "8.4 Audit Security 2026 (Round 1-8)",
        "8.5 Roadmap 2026-2028",
    ]),
    ("Bab 9 — EMR-CMS-HMS: SIMRS Terpadu Nakesmart", [
        "9.1 Arsitektur EMR-CMS-HMS — Satu Data, Tiga Lapisan",
        "9.2 Modul EMR — Rekam Medis Elektronik",
        "9.3 Modul CMS — Manajemen Klinik (Operasional)",
        "9.4 Modul HMS — Penunjang & Unit Rumah Sakit",
        "9.5 Tingkatan Tier & Capability (Solo - CMS - HMS)",
        "9.6 Keunggulan EMR-CMS-HMS Nakesmart vs Kompetitor",
        "9.7 Ringkasan — Mengapa Memilih EMR-CMS-HMS Nakesmart",
        "9.8 Matriks Komparasi EMR-CMS-HMS vs Kompetitor",
    ]),
    ("Lampiran", [
        "A. Glossarium Faskes",
        "B. FAQ Khusus Faskes",
        "C. Daftar Tarif Subscription per Tier",
        "D. Kontak Sales & Support",
    ]),
]

CONTENT = {
    "9.1": """EMR-CMS-HMS Nakesmart adalah SIMRS (Sistem Informasi Manajemen Rumah Sakit/Klinik) terpadu — bukan tiga aplikasi terpisah, melainkan tiga lapisan modul di atas SATU basis data pasien yang sama.

Tiga Lapisan:
• EMR (Electronic Medical Record) — lapisan rekam medis: data pasien, kunjungan, SOAP, diagnosa ICD-10, e-resep, dental, persalinan. Dipakai oleh SEMUA jenis faskes.
• CMS (Clinic Management System) — lapisan operasional klinik: kasir/billing, farmasi & stok, reservasi & antrian, SDM, keuangan, laporan.
• HMS (Hospital Management System) — lapisan penunjang rumah sakit: laboratorium, radiologi, bank darah, ICU, kamar operasi, LIS, akreditasi SNARS.

Prinsip Kunci:
• Satu data — pasien & kunjungan dipakai bersama lintas EMR/CMS/HMS. Tidak ada duplikasi, tidak ada input ulang antar modul.
• Bertingkat (nested) — tier yang lebih tinggi otomatis memuat SEMUA modul tier di bawahnya. Secara modul: HMS memuat CMS, CMS memuat EMR-dasar.
• Cloud-native — tanpa server on-premise, auto-update, auto-backup, akses dari web + mobile + desktop.""",

    "9.2": """EMR adalah jantung klinis Nakesmart — rekam medis elektronik sesuai standar Permenkes RME.

Fitur EMR:
• Master pasien lengkap — NIK, No. BPJS, ID SatuSehat, No. Rekam Medis, tempat/tanggal lahir, golongan darah, riwayat alergi, email, kategori pasien
• Kunjungan & catatan SOAP (Subjective-Objective-Assessment-Plan) per encounter
• Diagnosa ICD-10 (kode + nama) + ranking diagnosa
• E-Resep terintegrasi langsung ke modul farmasi
• Vital signs + grafik tren, allergy alert, drug-drug interaction checker
• Dental — odontogram & tindakan gigi (tersedia di SEMUA tier)
• Persalinan normal dengan partograph (tier rawat inap ke atas)
• Rawat Inap, UGD/IGD, Kamar Operasi (tier rumah sakit)
• Rujukan masuk/keluar, informed consent + tanda tangan digital, discharge summary otomatis
• Surat Medis: keterangan sakit/sehat/keterangan dokter/kelahiran/kematian — lengkap dengan kop surat (logo, izin, alamat, kontak faskes), isi terisi otomatis dari data pasien, serta tanda tangan & stempel dokter/faskes
• Audit trail penuh (syarat Permenkes RME) + integrasi SatuSehat (FHIR) siap-sambung""",

    "9.3": """CMS mengubah klinik menjadi bisnis digital yang rapi — dari pendaftaran hingga laporan keuangan.

Kasir & Billing (kedalaman setara klinik/apotek profesional):
• Diskon per-item + diskon tagihan + voucher + diskon kategori pasien + tukar poin loyalty
• PPN, biaya admin/layanan, biaya lain (embalase/tuslah/materai), pembulatan otomatis
• Multi-metode pembayaran per faskes (tunai/transfer/QRIS/kartu/e-wallet) — diatur sendiri
• Cetak nota termal POS (58/80mm) & A4, penomoran invoice urut/acak

Farmasi & Stok:
• Master obat — golongan obat (bebas s/d narkotika), HET/harga modal, barcode, kode KFA SatuSehat
• Stok berbasis batch + FEFO (First Expired First Out)
• Obat Racikan (compounding) — beberapa bahan menjadi 1 racikan + jasa racik & embalase; stok tiap bahan terpotong otomatis (anti partial)
• Kartu stok (in/out + saldo berjalan), konversi satuan (box-strip-tablet), transfer stok antar faskes
• Laporan stok kadaluarsa & defecta (daftar re-order)

Pelayanan & CRM:
• Reservasi & antrian, Booking Layanan + DP (uang muka), Reservasi Online publik (pasien booking tanpa login)
• Kategori pasien + diskon otomatis, Loyalty Point (earn/redeem), Jadwal Kontrol/recall, notifikasi ulang tahun pasien

SDM, Akses & Keuangan:
• Registri staf + RBAC: 25 peran (dokter spesialis/umum/gigi, perawat, bidan, apoteker, asisten apoteker, analis lab, radiografer, kasir, keuangan, dll.)
• Perijinan staf (STR/SIP/KTP/Ijazah + masa berlaku), jadwal kerja, serta matrix akses fitur per peran (super-admin faskes mengatur sendiri)
• Absensi mobile — geofence GPS + biometrik perangkat (sidik jari/wajah) + selfie
• Kas kecil, fee tindakan/dokter, perusahaan mitra, return penjualan, buku besar, hutang/piutang, pengadaan, aset

Laporan (12 jenis):
• 10 besar penyakit (ICD), pendapatan per dokter/metode/penjamin
• Produk terlaris, pembelian pasien tertinggi, margin produk
• Stok barang (valuasi), stok kadaluarsa, defecta, kartu stok
• Pasien baru, aktivitas staf""",

    "9.4": """HMS membuka kemampuan setingkat rumah sakit, di atas lapisan EMR + CMS.

Modul HMS (tier rumah sakit):
• Laboratorium — order pemeriksaan, input hasil, inbox LIS
• Radiologi — order, hasil, integrasi PACS
• Bank Darah
• Unit Klinis & ICU
• Kamar Operasi (OK)
• Akreditasi SNARS — dashboard quality indicators
• Middleware LIS/PACS (HL7/DICOM) siap-sambung alat

Catatan penting: faskes tier HMS otomatis JUGA memiliki seluruh modul EMR & CMS — HMS adalah superset, bukan produk terpisah.""",

    "9.5": """Bayar sesuai skala, upgrade mulus tanpa migrasi data. Tier bertingkat (nested superset) — tier atas memuat SEMUA modul tier bawah.

CATATAN HARGA: angka berikut adalah estimasi tarif saat panduan disusun; harga resmi & terbaru konfirmasi ke sales@nakesmart.com atau /simrs/pricing.

HARGA SEMUA SUBSCRIPTION (6 tier, per bulan):

Tier 1 — EMR SOLO: Rp49.000/bulan
• Untuk: praktik dokter/bidan/perawat mandiri, klinik kecil 1-2 dokter
• Modul: EMR rawat jalan + e-resep + kasir sederhana + Dental + booking
• Kuota: 500 pasien/bulan, 2 akun (1 dokter + 1 admin)

Tier 2 — EMR-CMS RAWAT JALAN: Rp99.000/bulan
• Untuk: klinik rawat jalan multi-dokter / klinik pratama
• Modul: semua Solo + CMS penuh (farmasi, SDM, keuangan, antrian) + Lab + Radiologi (DICOM URL viewer)
• Kuota: multi-user unlimited

Tier 3 — EMR-CMS RAWAT INAP: Rp199.000/bulan
• Untuk: klinik utama / klinik rawat inap / RS Tipe D
• Modul: semua CMS_RJ + Rawat Inap (bed/CPPT) + UGD + Persalinan + Lab/Radiologi
• Kuota: multi-user unlimited

Tier 4 — EMR-HMS RS TIPE C-D: Rp999.000/bulan
• Untuk: rumah sakit tipe C-D (<200 bed)
• Modul: semua CMS_RI + Kamar Operasi + ICU + Bank Darah + LIS + SNARS
• Kuota: unlimited user & pasien, training 5 sesi onsite/online

Tier 5 — EMR-HMS RS TIPE B: Rp2.000.000/bulan
• Untuk: rumah sakit tipe B (200-400 bed)
• Modul: semua HMS C-D + high-volume (>10rb encounter/bulan) + DICOM/PACS storage unlimited + audit chain RFC 3161 + custom report builder + API integration 3rd-party
• Kuota: unlimited, training tim unlimited

Tier 6 — EMR-HMS RS TIPE A: Rp3.000.000/bulan
• Untuk: rumah sakit tipe A (>400 bed, RSCM, BUMN besar)
• Modul: semua HMS Tipe B + custom branding + dedicated SLA 99.9% + onsite engineer quarterly + white-label mobile + dedicated infrastructure (single-tenant) + opsi on-premise/hybrid
• Kuota: full-service + priority support 24/7

Add-On Premium (opsional, di luar paket):
• MedAI (voice-to-SOAP + AI assist): mulai Rp300.000/bulan
• Medping Telemedicine Kit: Rp1.000.000/bulan
• WhatsApp Business Notif: Rp750.000/bulan
• Backup Encryption + Offsite: Rp1.500.000/bulan (Tipe A sudah termasuk)
• Compliance Bundle (SNARS+IKP): Rp3.000.000/bulan · API Premium: Rp2.000.000/bulan
• DICOM/PACS extra storage: Rp2.500.000/TB (Tipe B/A sudah unlimited)

Multi-Faskes & Diskon:
• Multi-Klinik/Multi-RS: akumulasi subscription per faskes sesuai tiernya (mis. 3 klinik Rawat Inap = 3 x Rp199rb = Rp597rb/bulan)
• Diskon multi-faskes: -10% (2-5 faskes) · -15% (6+ faskes)
• Annual prepay: -17% (bayar 12 bulan dapat 14 bulan) · 2-tahun: -25%
• Startup faskes (<2 thn): -30% tahun pertama · NGO/Yayasan: -20% · Pemerintah: custom (LKPP e-katalog)
• Affiliate referral: -5% bulan pertama

Semua paket sudah TERMASUK: BPJS (PCare/VClaim/Antrol), SATUSEHAT (FHIR), migrasi data (auto-wizard), training, DICOM/PACS. Karena bertingkat, faskes HMS memiliki SEMUA modul. Upgrade = membuka modul baru; data lama tetap utuh tanpa migrasi.""",

    "9.6": """Mengapa EMR-CMS-HMS Nakesmart unggul dibanding SIMRS/aplikasi klinik lain (mis. SIMRS on-premise vendor lokal, Klinik Pintar, Trustmedis, Assist.id, Medifirst, SIMRS Khanza, Practo/Halodoc Clinic):

Keunggulan #1 — All-in-One, bukan sekadar SIM:
Kompetitor umumnya HANYA sistem manajemen klinik. Nakesmart = SIMRS + Patient Marketplace + Telemedicine + Nakes Recruitment + Analytics dalam satu platform. Pasien datang dari marketplace, bukan hanya dikelola.

Keunggulan #2 — Harga 90-95% lebih hemat:
SIMRS on-premise butuh Rp50-500jt setup + server + tim IT. Nakesmart cloud mulai Rp49rb/bulan, tanpa server, auto-update & auto-backup.

Keunggulan #3 — Kedalaman fitur setara/melebihi SIM klinik papan atas:
Billing depth (diskon per-item, PPN, embalase/tuslah, pembulatan), obat racikan + FEFO + kartu stok, surat medis dengan kop/TTD/stempel, 12 laporan spesifik — sekelas SIM klinik terbaik, dalam satu langganan.

Keunggulan #4 — Satu data EMR-CMS-HMS:
Banyak kompetitor memisahkan RME, billing, dan apotek (atau menjual modul RS terpisah). Nakesmart satu basis data — tanpa input ulang, tanpa rekonsiliasi antar-sistem.

Keunggulan #5 — Tier bertingkat & upgrade mulus:
Dari praktik solo, naik ke klinik, sampai rumah sakit — TANPA ganti aplikasi atau migrasi data. Kompetitor sering memaksa pindah produk saat skala bertambah.

Keunggulan #6 — Mobile & Desktop native:
Native SIMRS app (tablet/iPad) untuk dokter, Desktop Electron untuk resepsionis/kasir, plus absensi mobile (GPS + biometrik + selfie). Banyak kompetitor masih web-only.

Keunggulan #7 — RBAC & Keamanan:
25 peran + perijinan staf (STR/SIP/Ijazah) + jadwal + matrix akses per fitur. Plus anti-AI-scraping, audit trail Permenkes, dan data tersimpan di Indonesia (region ap-southeast).

Keunggulan #8 — Compliance Indonesia:
SatuSehat (FHIR) + BPJS (VClaim/Antrol/PCare) siap-sambung, ICD-10, akreditasi KARS/SNARS — dibangun untuk regulasi Indonesia.""",

    "9.7": """EMR-CMS-HMS Nakesmart dalam satu kalimat: SIMRS yang tumbuh dari praktik dokter mandiri sampai rumah sakit — dalam satu langganan.

Ringkasan keunggulan:
• Satu platform — rekam medis + operasional klinik + penunjang RS + marketplace pasien
• Satu data — tanpa input ulang, tanpa rekonsiliasi antar sistem
• Hemat 90-95% vs SIMRS konvensional, mulai Rp49rb/bulan
• Tumbuh bersama Anda — solo to klinik to rumah sakit tanpa migrasi
• Kedalaman fitur sekelas SIM papan atas — billing depth, racikan, FEFO, surat medis, 12 laporan, absensi biometrik, RBAC 25 peran
• Web + tablet + desktop, cloud-native, aman & compliant Indonesia

Langkah berikutnya: pilih tier sesuai skala faskes Anda di /simrs/pricing, lalu aktifkan modul EMR-CMS-HMS dari dashboard faskes.""",

    "9.8": """Perbandingan langsung EMR-CMS-HMS Nakesmart dengan SIM klinik/RS populer. Legenda: ✅ tersedia penuh · ⚠️ terbatas/add-on · ❌ tidak ada.

CATATAN: kolom kompetitor adalah estimasi umum saat panduan disusun (fitur & harga pihak ketiga dapat berubah). Untuk EMR-CMS-HMS Nakesmart, semua tanda ✅ sudah live di sistem.

Aspek · Nakesmart · PicKlinik · Klinik Pintar · Trustmedis · SIMRS On-Premise
Model · Cloud SaaS bertingkat · Cloud · Cloud · Cloud · On-premise
Harga mulai · Rp49rb/bln · ~Rp300-500K/bln · Rp1-3jt/bln · Variatif · Rp50-500jt setup
EMR (rekam medis elektronik) · ✅ · ✅ · ✅ · ✅ · ✅
CMS Rawat Jalan · ✅ · ✅ · ✅ · ✅ · ⚠️
Rawat Inap (CPPT + bed) · ✅ · ⚠️ · ⚠️ · ✅ · ✅
HMS (Lab/Rad/Apotek/ICU/OK) · ✅ · ❌ · ⚠️ · ⚠️ · ✅
Obat Racikan (compounding + FEFO) · ✅ · ⚠️ · ⚠️ · ⚠️ · ⚠️
Kartu Stok (saldo berjalan) · ✅ · ✅ · ⚠️ · ⚠️ · ✅
Billing depth (diskon item/PPN/pembulatan) · ✅ · ⚠️ · ⚠️ · ✅ · ✅
Surat Medis (kop + TTD + stempel + auto-fill) · ✅ · ⚠️ · ⚠️ · ⚠️ · ⚠️
RBAC 25 peran + perijinan staf (STR/SIP) · ✅ · ⚠️ · ⚠️ · ⚠️ · ⚠️
Absensi GPS + biometrik + selfie · ✅ · ❌ · ❌ · ⚠️ · ⚠️
Laporan klinis + finansial (12+) · ✅ · ✅ · ✅ · ✅ · ✅
Patient Marketplace (booking online) · ✅ · ❌ · ⚠️ · ❌ · ❌
Reservasi online publik (tanpa login) · ✅ · ⚠️ · ⚠️ · ❌ · ❌
BPJS / SATUSEHAT · ✅ · ✅ · ✅ · ✅ · ⚠️
Mobile + Desktop app · ✅ Native + Electron · ⚠️ · ⚠️ · ⚠️ · ❌
Anti-AI scraping security · ✅ · ❌ · ❌ · ❌ · ❌
Upgrade tier tanpa migrasi data · ✅ · n/a · n/a · n/a · ❌

Kesimpulan: Nakesmart menyamai SIM RS papan atas pada kedalaman klinis (rawat inap, HMS, racikan, kartu stok, billing depth, RBAC, absensi biometrik) sekaligus unggul pada hal yang jarang dimiliki kompetitor — patient marketplace, reservasi publik, mobile+desktop native, anti-AI security, dan upgrade tier tanpa migrasi — dengan harga mulai Rp49rb/bulan.""",

    "1.1": """Nakesmart untuk Faskes adalah platform digital terintegrasi untuk fasilitas kesehatan Indonesia. Anda mendapat: SIMRS lengkap (EMR/CMS/HMS), patient marketplace (booking online), nakes recruitment, analytics dashboard, dan multi-revenue streams dalam satu subscription.

Berbeda dengan SIMRS konvensional yang mahal (Rp50-500jt/tahun on-premise), Nakesmart cloud-native dengan harga mulai Rp49rb/bulan untuk klinik solo.

Nakesmart untuk Faskes = SIMRS Cloud + Patient Marketplace + Telemedicine + Nakes Recruitment + Analytics + Multi-Klinik Manager — semua dalam satu platform.

Apa yang Nakesmart Tawarkan untuk Faskes?
• SIMRS lengkap (EMR/CMS/HMS) cloud-native
• Patient marketplace — ribuan pasien aktif cari faskes
• Online booking dengan slot management
• E-Resep terintegrasi (nakes tulis → pasien terima)
• Nakes Recruitment — cari + onboard nakes part-time/full-time
• Multi-Klinik management (untuk group)
• Faskes Analytics — insights real-time
• Cost management untuk operasional
• Faskes Wallet untuk receive payments
• Voucher system untuk promo
• Subscription tier fleksibel (6 tier: Solo/CMS RJ/CMS RI/HMS C-D/B/A)
• Native tablet app (iPad/Android tablet) untuk dokter
• Desktop Electron untuk receptionist
• Multi-channel patient acquisition
• Anti-AI scraping security untuk patient data""",

    "1.2": """Visi
Menjadi sistem operasi #1 untuk fasilitas kesehatan Indonesia — memberdayakan setiap klinik, RS, apotek, lab untuk transform digital dengan tools profesional & affordable.

Misi (Faskes-Focused)
1. Affordable Digital Transformation — SIMRS mulai Rp49rb/bulan (vs konvensional Rp500jt+ setup)
2. Cloud-Native — No server on-premise, no IT team needed, auto-update
3. Patient Marketplace — Direct pipeline pasien dari Nakesmart
4. Nakes Marketplace — Cari & onboard nakes terverifikasi dengan mudah
5. Continuity of Care — Patient data sync across visit dan telemedicine
6. Data Sovereignty — Data di Indonesia (Supabase ap-southeast region)
7. Compliance Ready — Standar Kemenkes, BPJS, akreditasi KARS/SNARS

Brand Identity Nakesmart
Forest Green (#0F5132) — profesional, medical trust
Electric Lime (#C8FF00) — action CTAs""",

    "1.3": """5 Role di Ekosistem Nakesmart:

Role 1: FASKES (Anda)
Klinik, RS, apotek, lab, puskesmas.
• Subscription tier (6 tier: EMR Solo / CMS Rawat Jalan / CMS Rawat Inap / HMS RS Tipe C-D / B / A)
• SIMRS terintegrasi
• Multi-klinik (untuk group)
• Receive patient bookings

Role 2: NAKES
Dokter, perawat, bidan, apoteker yang praktek di faskes Anda.
• Bisa multi-affiliated (praktek di banyak faskes)
• Sync e-Resep dengan SIMRS Anda
• Akses pasien yang booking ke faskes

Role 3: PASIEN
Klien akhir Anda.
• Book layanan online
• Bayar via wallet/gateway
• Riwayat tersimpan otomatis

Role 4: EO (Event Organizer)
Untuk faskes yang adakan event kesehatan publik.
• Faskes bisa jadi EO sendiri
• Atau invite EO partner

Role 5: ADMIN Nakesmart
Tim platform untuk:
• Verifikasi faskes (1-3 hari)
• Verifikasi subscription
• Support technical & operasional""",

    "1.4": """Problem Faskes Indonesia Hadapi:
1. SIMRS Mahal — Konvensional Rp100-500jt setup + maintenance Rp10-50jt/bulan
2. No Digital Marketing — Pasien online tidak menemukan klinik
3. Booking via Phone — Receptionist overload, antrian tidak teratur
4. Cash-Only / Manual Pay — Tidak ada gateway online
5. Manual Resep — Resep kertas, hilang, salah baca
6. No Patient Continuity — Riwayat tidak tersync antar visit
7. Susah Cari Nakes Pengganti — Saat dokter cuti susah cari pengganti cepat
8. No Analytics — Tidak tahu pasien favorit layanan, peak hour
9. Compliance Risk — Akreditasi KARS/SNARS butuh data lengkap
10. Data Risk — On-premise rawan hilang, hack, fire

Solusi Nakesmart untuk Faskes:
Problem · Solusi
SIMRS mahal · Subscription Rp49rb-3jt/bulan cloud (6 tier)
No digital marketing · Listed di patient marketplace
Booking via phone · Online slot booking + reminders
Cash-only · Wallet + Midtrans/Xendit/Faspay gateway
Manual resep · E-Resep otomatis sync ke pasien akun
No continuity · Patient history sinc across faskes affiliated
Susah cari pengganti · Nakes Recruitment marketplace
No analytics · Real-time dashboard + reports
Compliance risk · Auto-track akreditasi metrics
Data risk · Cloud backup, encryption, anti-AI scraping

Potensi Revenue Boost untuk Faskes
Klinik Konvensional (50 pasien/hari, no online)
- Revenue: Rp500jt/bulan
- Operating cost: Rp400jt
- Net: Rp100jt

Klinik + Nakesmart (80 pasien/hari, online + telemed referral)
- Revenue: Rp800jt/bulan (+60%)
- Subscription Nakesmart: Rp199rb
- Operating cost: Rp450jt
- Net: Rp345jt (+245%)""",

    "2.1": """Landscape SIMRS & Klinik Manager di Indonesia:

SIMRS Konvensional (Vendor Local)
• InfoMedika, MedTrack, Sismadak, ePatient
• Setup: Rp50-500jt (server, lisensi, training)
• Bulanan: Rp10-50jt (maintenance, support)
• On-premise — perlu IT team

SIMRS Cloud (Limited)
• Practo SIMRS, Klinikmu
• Subscription Rp5-20jt/bulan
• Limited customization

EHR International
• Cerner, Epic, Athena
• Sangat mahal (>$100K/year), kompleks
• Tidak cocok untuk klinik Indonesia

Klinik Manager Lokal
• Klinik Pintar (booking only, no SIMRS lengkap)
• Halodoc Apps (basic clinic CRM)

Kebanyakan klinik kecil/menengah pakai Excel + WhatsApp untuk manage (inefisien).""",

    "2.2": """Kompetitor #1: SIMRS Konvensional Vendor Lokal
• Pros: Customization tinggi, support local
• Cons: Mahal (Rp50-500jt setup), perlu IT, no marketplace

Kompetitor #2: Practo, Halodoc Clinic
• Pros: Cloud-based, established
• Cons: Subscription mahal (Rp5-20jt), tidak lengkap (no HMS), no patient marketplace di Indonesia

Kompetitor #3: Klinik Pintar
• Pros: Booking management bagus
• Cons: Tidak ada SIMRS lengkap (no EMR, no billing, no pharmacy)

Kompetitor #4: Excel + WhatsApp
• Pros: Gratis
• Cons: Tidak scale, error-prone, tidak ada compliance""",

    "2.3": """Keunggulan #1: Harga Terjangkau dengan Fitur Lengkap (6 tier)
- EMR Solo: Rp49rb/bulan (vs konvensional Rp50jt setup)
- EMR-CMS Rawat Jalan: Rp99rb/bulan
- EMR-CMS Rawat Inap: Rp199rb/bulan
- EMR-HMS RS Tipe C-D: Rp999rb/bulan
- EMR-HMS RS Tipe B: Rp2jt/bulan
- EMR-HMS RS Tipe A: Rp3jt/bulan
Hemat 90-95% vs SIMRS konvensional dengan fitur sama lengkap.

Keunggulan #2: Cloud-Native
- No server on-premise
- No IT team needed
- Auto-update, auto-backup
- Akses dari mana saja (web, mobile, tablet)

Keunggulan #3: Patient Marketplace Built-In
- Ribuan pasien aktif di Nakesmart
- Faskes Anda muncul di "Cari Faskes"
- Online booking + payment
- Zero marketing cost di awal

Keunggulan #4: SIMRS Lengkap (EMR/CMS/HMS)
- EMR (Electronic Medical Record)
- CMS (Clinical Management System): Rawat Jalan + Rawat Inap
- HMS (Hospital Management System): Lab, Radiologi, Apotek, Persalinan, Gigi
- Tergantung tier

Keunggulan #5: Nakes Recruitment Marketplace
- Post lowongan gratis
- Cari nakes part-time/full-time
- Verified nakes dengan rating

Keunggulan #6: Multi-Klinik Manager
- Untuk group, manage 2+ klinik dalam 1 dashboard
- Consolidated reporting
- Lines accumulation untuk inventory

Keunggulan #7: Analytics Dashboard
- Pasien per hari, peak hour, layanan terlaris
- Revenue trends
- Cost analysis
- Nakes performance

Keunggulan #8: E-Resep Native
- Nakes tulis di tablet → langsung di SIMRS + akun pasien
- QR verifikasi
- Drug interaction check

Keunggulan #9: Multi-Payment Gateway
- Midtrans Snap (bank + e-wallet + QRIS + CC)
- Xendit VA
- Faspay VA + retail
- Manual transfer
- Bayar di tempat
- Faskes atur sendiri metode bayar per layanan

Keunggulan #10: Anti-AI Scraping Security
- Data pasien Anda lindungi multi-layer
- Compliance KARS/SNARS friendly""",

    "2.4": """Matriks Komparasi SIMRS

Fitur · Nakesmart · Konvensional · Practo · Klinik Pintar
Setup Cost · Rp0 · Rp50-500jt · Rp5-20jt · Rp5jt
Monthly · Rp49rb-3jt · Rp10-50jt · Rp5-20jt · Rp1-3jt
Cloud-Native · ✅ · ❌ On-premise · ✅ · ✅
EMR · ✅ Full · ✅ Full · ✅ · ⚠️
CMS (RJ + RI) · ✅ · ✅ · ⚠️ RJ only · ❌
HMS (Lab/Rad/Apotek) · ✅ · ✅ · ❌ · ❌
Patient Marketplace · ✅ · ❌ · ⚠️ · ⚠️
Telemedicine Integration · ✅ · ❌ · ⚠️ · ❌
Nakes Recruitment · ✅ · ❌ · ❌ · ❌
Multi-Klinik · ✅ · ⚠️ Tambahan · ⚠️ · ❌
Mobile/Tablet App · ✅ Native · ⚠️ Limited · ⚠️ · ⚠️
Voucher System · ✅ · ❌ · ❌ · ❌
Multi-Payment Gateway · ✅ 5+ · ⚠️ · ⚠️ · ⚠️
Anti-AI Security · ✅ · ❌ · ❌ · ❌
Auto-Update · ✅ · ❌ · ✅ · ⚠️
Data Backup · ✅ Auto · ⚠️ Manual · ✅ · ⚠️

Kesimpulan: Nakesmart unggul di harga, fitur lengkap, marketplace, dan keamanan modern.""",

    "3.1": """Faskes Onboarding — daftar & verifikasi.

Cara Daftar
1. Buka /simrs/pricing (atau landing /emr) lalu daftar faskes via /healthcare/register
2. Isi data faskes:
   - Nama faskes
   - Jenis (Klinik / RS / Apotek / Lab / Puskesmas)
   - Alamat lengkap + koordinat GPS
   - No telepon + email
   - Logo (opsional)
3. Upload dokumen verifikasi:
   - SIUP (Surat Izin Usaha)
   - SIO (Surat Izin Operasional)
   - SIPA (untuk apotek)
   - Akte pendirian
   - NPWP
   - KTP pemilik/PIC
4. Submit → tunggu verifikasi admin

Verifikasi Process
• Admin verifikasi 1-3 hari kerja
• Cek legalitas dokumen
• Cek lokasi (mungkin site visit untuk RS besar)
• Setelah approved: badge "Faskes Terverifikasi"

Setelah Verifikasi
• Akun aktif
• Pilih subscription tier
• Mulai setup operasional""",

    "3.2": """Faskes Subscription Tiers — pilih sesuai skala.

CATATAN HARGA: Angka di bawah adalah estimasi/contoh tarif Subscription Nakesmart pada saat panduan ini disusun. Harga resmi dan terbaru dapat berbeda dan harus dikonfirmasi langsung ke tim sales Nakesmart (sales@nakesmart.com) atau cek di /simrs/pricing. Ada 6 tier aktif di sistem: EMR Solo, EMR-CMS Rawat Jalan, EMR-CMS Rawat Inap, EMR-HMS RS Tipe C-D, EMR-HMS RS Tipe B, EMR-HMS RS Tipe A.

Tier 1: EMR SOLO (estimasi Rp49.000/bulan)
Untuk: Praktek mandiri dokter/bidan/perawat, klinik kecil 1-2 dokter
Fitur:
• EMR rawat jalan (SOAP, ICD-10)
• Booking management
• Service catalog basic
• Patient marketplace (basic listing)
• Dental (odontogram + tindakan gigi)
• Mobile app
• Limit: 500 encounter/bulan
• 2 akun (1 dokter/bidan/perawat + 1 admin)

Tier 2: EMR-CMS RAWAT JALAN (estimasi Rp99.000/bulan)
Untuk: Klinik rawat jalan multi-dokter, klinik pratama/spesialis
Fitur Solo +:
• CMS Rawat Jalan lengkap
• Multi-user unlimited (dokter, perawat, admin, kasir)
• Antrian digital + reservasi online
• Multi-dokter scheduling
• E-Resep terintegrasi
• Farmasi + inventory FEFO
• SDM + payroll + absensi, Finance (GL, AR/AP)
• Lab + Radiologi (DICOM URL viewer)
• Billing & kasir multi-payment

Tier 3: EMR-CMS RAWAT INAP (estimasi Rp199.000/bulan)
Untuk: Klinik dengan layanan rawat inap, RS Tipe D
Fitur CMS_RJ +:
• CMS Rawat Inap (bed management, CPPT)
• UGD basic (triage, disposisi)
• Persalinan normal (partograph + APGAR)
• Pharmacy lengkap (batch tracking, expired alert)
• Multi-user unlimited
• Lab + Radiologi + Dental (dari paket RJ)
• Insurance integration (BPJS)
• Multi-Klinik (akumulasi subscription per klinik)

Tier 4: EMR-HMS RS TIPE C-D (estimasi Rp999.000/bulan)
Untuk: RS Tipe C-D (<200 bed)
Fitur CMS_RI +:
• HMS (Hospital Management System) lengkap
• Kamar Operasi (OK) + checklist WHO
• Lab + integrasi LIS, Radiologi + DICOM viewer
• ICU + NEWS2, Bank Darah
• Diet & farmasi rawat inap
• IKP SNARS + quality indicators (BOR, ALOS, BTO, NDR, GDR)
• Training tim 5 sesi onsite/online
• Multi-user unlimited, Unlimited pasien
• Premium support 24/7

Tier 5: EMR-HMS RS TIPE B (estimasi Rp2.000.000/bulan)
Untuk: RS Tipe B (200-400 bed)
Fitur HMS C-D +:
• High-volume optimization (>10rb encounter/bulan)
• Mutu klinis SNARS Paripurna
• DICOM/PACS storage unlimited
• Audit chain external anchor (RFC 3161)
• Compliance dashboard (BPK ready)
• Custom report builder + API integration 3rd-party
• Training tim unlimited

Tier 6: EMR-HMS RS TIPE A (estimasi Rp3.000.000/bulan)
Untuk: RS Tipe A (>400 bed, RSCM, BUMN besar)
Fitur HMS Tipe B +:
• Custom branding (logo + warna RS)
• Dedicated SLA 99.9% + 24/7 priority support
• Onsite engineer quarterly
• White-label mobile app
• BI integration (Tableau, PowerBI, Metabase)
• Dedicated infrastructure (single-tenant)
• Opsi on-premise / hybrid deployment
• Audit log forensik real-time

Tambahan Per Tier
- Multi-Klinik/Multi-RS: akumulasi subscription per faskes sesuai tiernya (diskon -10%/-15% multi-faskes)
- Tablet/iPad apps: included
- Desktop Electron: included
- Anti-AI security: included

Free Trial (semua tier)
- 6 bulan pertama GRATIS, atau sampai pemakaian 20 pasien/bulan - mana yang tercapai lebih dulu
- Tanpa kartu kredit, cancel kapan saja, semua fitur tier aktif selama trial
- Anti-fraud: dedupe by STR/SIP/NIK
- Voucher COMEBACK25 untuk reactivation""",

    "3.3": """SIMRS Lengkap — modul EMR/CMS/HMS sesuai tier. EMR-CMS-HMS adalah INTI Nakesmart untuk faskes: satu basis data, tiga lapisan modul (rekam medis -> operasional klinik -> penunjang RS), tumbuh dari praktik solo sampai rumah sakit tanpa migrasi. Deep-dive lengkap + harga semua tier + perbandingan vs kompetitor ada di Bab 9.

EMR (Electronic Medical Record)
- Patient record dengan riwayat lengkap
- Anamnesa + pemeriksaan fisik
- Diagnosis (ICD-10 coding)
- Treatment plan
- Lab orders & results
- Radiology orders
- E-Resep dengan QR verifikasi
- Audit log (siapa input apa)

CMS (Clinical Management System)
Rawat Jalan:
- Antrian digital
- Multi-dokter scheduling
- Quick check-in via QR
- Konsultasi cepat workflow
- Auto-billing

Rawat Inap:
- Bed management (kelas 3/2/1/VIP/VVIP)
- Admission/Discharge
- CPPT (Catatan Perkembangan Pasien Terintegrasi)
- Nursing notes
- Visite dokter tracking

HMS (Hospital Management System)
Lab:
- Order entry
- Sample tracking
- Results entry
- Auto-billing
- Quality control

Radiologi:
- Order entry
- PACS integration (link viewer eksternal)
- Reports

Apotek:
- Inventory dengan batch
- Expired alert
- POS sale
- Formularium
- Prescription fulfillment

Persalinan:
- Partograph
- Newborn record
- Postpartum care

Dental:
- Odontogram
- Treatment plan
- Dental imaging

ICU:
- Observation chart (1-jam interval)
- Ventilator settings
- Multi-monitor tracking

Bank Darah:
- Stock per golongan darah
- Permintaan & cross-match
- Distribusi tracking""",

    "3.4": """Nakes Affiliations — onboard & manage nakes.

Cara Onboard Nakes
1. Tab "Nakes Affiliations" → "Invite Nakes"
2. Pilih cara:
   - Search nakes terverifikasi di Nakesmart
   - Invite via email (nakes yang belum di Nakesmart)
   - Post lowongan di "Nakes Recruitment"
3. Set offer:
   - Spesialisasi yang dicari
   - Jenis (part-time / full-time / on-call)
   - Tarif/gaji
   - Jadwal yang available
4. Nakes terima offer → accept/negotiate
5. Setelah accept: affiliation aktif

Manage Affiliations
• Lihat list nakes affiliated
• Status: Active / Inactive / Terminated
• Per nakes:
  - Jadwal praktek
  - Tarif khusus
  - Revenue contribution
  - Rating dari pasien
  - Sync e-Resep

Multi-Faskes Reality
Nakes Anda bisa affiliate juga dengan faskes lain. Itu normal.
• Nakes Anda di Klinik X (Senin-Rabu)
• Juga di Klinik Y (Kamis-Sabtu)
• Telemedicine di sisa waktu
• Nakes pilih waktu yang available untuk Anda""",

    "3.5": """Service Catalog — manage layanan & tarif.

Setup Service Catalog
1. Tab "Service Catalog"
2. Add service:
   - Nama layanan (e.g. "Konsultasi Dokter Umum")
   - Kategori (Umum / Spesialis / Lab / Radiologi)
   - Tarif (atau range jika varies)
   - Durasi estimasi
   - Description
   - Image (opsional)
3. Toggle: aktif/inactive
4. Set requirements (BPJS, asuransi, no insurance)

Bundle Layanan
• Combo layanan dengan diskon
• Misal: "Paket MCU Lengkap" = 5 layanan + 15% diskon

Pricing Strategy
- Solo: harga single per service
- CMS+: bisa multi-tier (basic/premium/VIP)
- HMS: pricing per kelas kamar untuk inpatient

Layanan Marketplace
• Layanan Anda muncul di Nakesmart Marketplace
• Pasien filter by service, harga, lokasi
• Direct booking ke service spesifik""",

    "3.6": """Booking & Reservasi Management.

Dashboard Booking
• Tab "Reservations"
• View: Today, This Week, This Month
• Filter by status: pending, confirmed, in-progress, completed, cancelled
• Filter by service, dokter

Booking Card
- Pasien (nama, foto, kontak)
- Service yang dipilih
- Dokter (atau "Any available")
- Tanggal & jam
- Status pembayaran
- Notes pasien
- QR code

Manage Booking
• Confirm / Reschedule / Cancel
• Assign ke dokter spesifik (jika "Any")
• Send reminder ke pasien

Auto-Reminder
• Email + WA 24 jam sebelum
• Push notif 1 jam sebelum
• Reduce no-show rate

Check-in
• Pasien tunjukkan QR di reception
• Scan → auto check-in di SIMRS
• Antrian otomatis update""",

    "3.7": """Faskes Analytics — insights real-time.

Dashboard Utama
• Today's bookings count
• Today's revenue
• Active patients (currently in faskes)
• Pending payments

Trends
• Bookings per week/month (graph)
• Revenue trend (line chart)
• Peak hours (heatmap)
• Day-of-week distribution

Top Layanan
• Most booked services
• Highest revenue services
• Customer satisfaction per service

Nakes Performance
• Top performing nakes
• Rating average per nakes
• Revenue contribution per nakes

Patient Demographics
• Age distribution
• Gender split
• Repeat vs new patients
• Geographic origin (kota)

Customer Acquisition
• Channel: marketplace, direct, referral
• Conversion rate per channel
• Cost per acquisition (CPA)

Cost Analysis
• Revenue vs operating cost
• Profit margin per service
• Inventory turnover (untuk apotek)

Reports
• Daily, Weekly, Monthly, Yearly
• Custom date range
• Export CSV/PDF
• Auto-email schedule""",

    "3.8": """Faskes Cost Management — kelola biaya operasional.

Components
• Staff payroll (untuk CMS+ subscriber)
• Inventory cost (obat, alat medis)
• Operational (listrik, sewa, internet)
• Marketing budget
• Subscription Nakesmart
• Vendor payments

Setup
1. Tab "Cost Management"
2. Tambah kategori biaya
3. Input bulanan (atau auto-sync untuk staff payroll)
4. Set budget vs actual

Analytics
• Cost vs revenue
• Per service profitability
• Cost trends
• Variance analysis (budget vs actual)
• Forecast

Saran AI
- Inventory obat A overstock - turun order
- Cost listrik naik 20 persen vs bulan lalu - investigate
- Marketing ROI rendah - pivot strategy""",

    "3.9": """Faskes Doctors Page — public profile untuk patient acquisition.

Public Page Features
• URL: nakesmart.com/faskes/{slug}
• Hero: logo + nama + tagline + photo
• Info: alamat, telepon, jam buka, BPJS
• Layanan list dengan tarif
• Dokter list dengan rating
• Foto fasilitas (galeri)
• Reviews dari pasien
• Map dengan navigasi

Doctors Section
• Foto + nama + spesialisasi
• Jadwal praktek per minggu
• Rating + jumlah ulasan
• Tarif konsultasi
• Tombol "Book Now"

SEO Optimization
• Auto-generate meta tags
• Schema.org markup
• Open Graph untuk social
• Sitemap submission

Embed di Website Sendiri
- Embed widget Nakesmart di website faskes
- Iframe booking
- Bisa share QR code untuk booking""",

    "3.10": """Multi-Klinik Management (Untuk Group).

Untuk Owner Multi-Klinik
- 1 dashboard untuk semua klinik
- Switch antar klinik
- Consolidated view

Per Klinik
- Individual SIMRS + data
- Separate financials
- Separate staff
- Bisa share nakes (multi-affiliated)

Group Features
- Centralized inventory (multi-warehouse)
- Inter-klinik transfer (obat, alat)
- Group-wide analytics
- Group accounting
- Multi-tenant security

Subscription
- Akumulasi subscription per klinik sesuai tiernya (campur tier bebas)
- Contoh: 3 klinik Rawat Inap = 3 x Rp199rb = Rp597rb/bulan
- Diskon multi-faskes otomatis: -10% (2-5 faskes) / -15% (6+ faskes)
- Pemerintah/enterprise: custom procurement (LKPP e-katalog) - hubungi sales""",

    "4.1": """Faskes Wallet — receive payments dari pasien.

Sumber Income di Wallet
• Patient bookings (after consultation)
• Telemedicine fees (jika nakes affiliated)
• Service catalog sales
• Voucher purchases
• Asuransi/BPJS claims (after approval)

Wallet Status
• Available balance
• Pending balance (belum cleared by patients)
• Withdrawable balance

Withdrawal
- Withdraw ke rekening bank faskes
- Min Rp500K
- Max Rp1M per transaksi (bisa di-unlock dengan verified)
- 1-2 hari kerja

Multi-Bank
- Tambah multi rekening (untuk multi-klinik)
- Auto-split per klinik
- Tax reporting per rekening""",

    "4.2": """Subscription Comparison & Upgrade.

Tab "Subscription"
- Lihat tier saat ini
- Komparasi dengan tier lain
- Fitur yang aktif vs tidak aktif
- Pricing breakdown

Upgrade Path
- Klik "Upgrade ke Tier X"
- Prorating: bayar selisih sampai end of period
- Activation: instant setelah pembayaran
- Data migrasi otomatis

Downgrade
- Bisa downgrade di akhir period
- Data tetap dipertahankan
- Beberapa fitur readonly setelah downgrade

Renewal
- Auto-renewal default
- Notification 30 hari sebelum expiry
- Bisa pause / cancel
- Discount annual prepay: -17% (bayar 12 bulan dapat 14 bulan); 2-tahun: -25%""",

    "4.3": """Faskes Referral Leaderboard.

Cara Earn dari Referral
- Ajak faskes lain join Nakesmart
- Bagikan kode referral Anda
- Setelah faskes terverifikasi + subscribe:
  - Anda: Rp500K-1jt onboarding fee
  - 5% recurring fee (selama mereka aktif subscriber)

Leaderboard
- Ranking faskes referrer per bulan
- Top 3 dapat bonus + recognition

Cara Ajak
- Share di asosiasi faskes (PERSI, KKI)
- Network di event kesehatan
- Direct outreach""",

    "4.4": """Voucher System untuk Promo Faskes.

Setup Voucher
1. Tab "Vouchers"
2. Buat voucher baru:
   - Type: % discount / fixed amount
   - Scope: all services / specific service / category
   - Quota: max usage (overall, per user)
   - Validity: start - end date
   - Min purchase
   - Code (auto atau custom)
3. Publish

Promo Strategy
• Welcome voucher untuk new patient
• Birthday voucher
• Seasonal (Hari Kesehatan, HUT RI)
• Loyalty voucher (after 5 visits)
• Win-back (untuk pasien tidak return)

Track Performance
• Voucher claimed count
• Conversion rate
• Revenue from voucher
• ROI per campaign""",

    "4.5": """Payment Methods per Faskes.

Faskes Atur Sendiri Metode Bayar
1. Tab "Payment Methods"
2. Toggle method:
   ✅ Wallet Nakesmart
   ✅ Midtrans Snap (default semua bank+e-wallet+QRIS+CC)
   ✅ Xendit VA
   ✅ Faspay VA + retail
   ✅ Manual Transfer (perlu approval)
   ✅ Bayar di Faskes (cash/EDC)
3. Set order priority
4. Set min/max per method

Untuk Layanan Tertentu
- Bisa beda method per layanan
- E.g. konsultasi: wallet only
- Surgery: manual transfer atau bayar di faskes

Fee per Gateway
- Midtrans: 2-3% per transaksi
- Xendit: Rp4.000 per VA
- Faspay: Rp3.500 per VA
- Manual: gratis
- Faskes biasanya absorb fee atau pass-through ke pasien""",

    "4.6": """Investment & Partnership Page.

Untuk Faskes yang Cari Investor
- Buat profile investment
- Highlight: revenue, ROI, growth metrics
- Investment offer (% saham, debentures)
- Investor verified di Nakesmart bisa connect

Untuk Faskes yang Mau Partner
- Cari faskes lain untuk collaboration
- Joint marketing
- Referral partnership
- Equipment sharing
- Group purchasing

Marketplace Investment Opportunities
- Klinik baru cari modal
- Klinik expansion
- Equipment financing
- Working capital loan

Anti-Fraud
- Investor wajib verified KYC
- Faskes wajib verified
- Audit trail""",

    "4.7": """Staff & Payroll Management (CMS Subscriber +).

Staff Module
• Add staff (medical + non-medical)
• Setup roles & permissions
• Salary & benefit setup
• Attendance tracking
• Performance review

Payroll
- Monthly payroll automation
- Auto-calculate: gaji pokok, tunjangan, lembur, BPJS, PPh 21
- Payslip digital
- Bank transfer integration (untuk batch payment)

Compliance
- PPh 21 calculation (sesuai PTKP)
- BPJS Kesehatan + Ketenagakerjaan
- Annual SPT data
- 1721-A1 form auto-generate""",

    "5.1": """Flow Faskes Operasional:

Phase 1: Registrasi & Subscription (1-3 hari)
- Daftar akun + upload SIUP, SIO
- Pilih tier subscription
- Bayar subscription
- Verifikasi admin

Phase 2: Setup Profil & Service Catalog (1-3 hari)
- Lengkapi profil public
- Setup service catalog + tarif
- Upload foto fasilitas
- Setup payment methods

Phase 3: Onboard Nakes (1-2 minggu)
- Invite nakes existing atau post lowongan
- Setup affiliation + jadwal
- Sync dengan SIMRS

Phase 4: Setup SIMRS Modules (1 minggu)
- Aktivasi modul sesuai tier
- Setup workflow per departemen
- Training staff
- Migrasi data (jika ada SIMRS lama)

Phase 5: Operasional Harian
- Patient booking masuk
- Check-in via QR
- Konsultasi + EMR entry
- E-Resep generation
- Billing + payment
- Inventory update

Phase 6: Monthly Reporting (akhir bulan)
- Generate reports
- Analytics review
- Payroll processing
- Tax filing prep

Phase 7: Quarterly Review
- Subscription tier review
- Service catalog optimization
- Nakes performance review
- Strategy adjustment""",

    "5.2": """Phase 1: REGISTRASI & SUBSCRIPTION

Step 1.1: Daftar Akun
- Lihat /simrs/pricing lalu daftar via /healthcare/register
- Isi data dasar faskes

Step 1.2: Upload Dokumen
- SIUP, SIO, NPWP, KTP PIC
- Akte pendirian
- Sertifikat akreditasi (jika ada)

Step 1.3: Pilih Subscription Tier
- EMR Solo (Rp49rb) untuk klinik kecil
- EMR-CMS Rawat Jalan (Rp99rb) untuk klinik rawat jalan
- EMR-CMS Rawat Inap (Rp199rb) untuk dengan rawat inap
- EMR-HMS RS Tipe C-D (Rp999rb) untuk RS kecil-menengah
- EMR-HMS RS Tipe B (Rp2jt) untuk RS Tipe B
- EMR-HMS RS Tipe A (Rp3jt) untuk RS Tipe A

Step 1.4: Bayar Subscription
- Free trial 6 bulan gratis, atau sampai 20 pasien/bulan (mana dulu) - tier mana saja
- Atau langsung bayar untuk activate
- Method: Midtrans / Xendit / transfer

Step 1.5: Tunggu Verifikasi
- Admin verifikasi 1-3 hari
- Jika OK: akun aktif
- Jika perlu revisi: notifikasi ke email""",

    "5.3": """Phase 2: SETUP PROFIL & SERVICE CATALOG

Step 2.1: Public Profile
- Logo + tagline
- Foto utama fasilitas
- Galeri (max 10 foto)
- Deskripsi (max 500 karakter)
- Jam operasional
- Layanan BPJS / asuransi yang diterima

Step 2.2: Service Catalog
- Add layanan satu per satu
- Kategorisasi
- Tarif
- Description per layanan

Step 2.3: Payment Methods
- Aktifkan gateway yang diinginkan
- Setup rekening untuk receive

Step 2.4: Operational Hours
- Hari & jam buka
- Hari libur
- Emergency 24 jam (atau tidak)""",

    "5.4": """Phase 3: ONBOARD NAKES

Step 3.1: Identifikasi Kebutuhan Nakes
- Spesialisasi yang dibutuhkan
- Berapa orang per spesialisasi
- Part-time / full-time

Step 3.2: Recruitment
Opsi A: Search Existing Nakes
- Search di Nakesmart database
- Filter spesialisasi + lokasi
- Send invitation

Opsi B: Post Lowongan
- Tab "Nakes Recruitment"
- Buat job posting
- Tunggu apply

Opsi C: Existing Nakes (Manual Invite)
- Anda kenal nakes yang belum di Nakesmart?
- Send invite via email
- Mereka akan daftar dengan kode referral Anda

Step 3.3: Negosiasi & Affiliation
- Diskusi tarif, jadwal
- Setelah deal: setup affiliation di SIMRS
- Training onboarding

Step 3.4: Sync ke SIMRS
- Nakes punya akses SIMRS faskes Anda
- E-Resep otomatis sync""",

    "5.5": """Phase 4: SETUP SIMRS MODULES

Step 4.1: Aktivasi Module per Tier
EMR Solo: EMR rawat jalan + e-resep + Dental + kasir sederhana
EMR-CMS Rawat Jalan: + CMS Rawat Jalan, antrian, farmasi, Lab/Radiologi
EMR-CMS Rawat Inap: + Rawat Inap (bed/CPPT), UGD, Persalinan
EMR-HMS RS Tipe C-D: + Kamar Operasi (OK), ICU, Bank Darah, LIS, SNARS
EMR-HMS RS Tipe B: + high-volume, DICOM/PACS unlimited, audit RFC 3161, custom report, API
EMR-HMS RS Tipe A: + custom branding, dedicated SLA, single-tenant, white-label

Step 4.2: Setup Workflow per Departemen
- Antrian: nomor antrian auto-generate
- Triase: parameter ABC
- Konsultasi: SOAP template
- E-Resep: drug interaction warning
- Billing: auto-calculate
- Discharge: summary auto

Step 4.3: Training Staff
- Webinar onboarding gratis dari Nakesmart
- Documentation lengkap
- Video tutorial
- Support 24/7

Step 4.4: Migrasi Data (Jika Ada SIMRS Lama)
- Export data lama (CSV/Excel)
- Import ke Nakesmart
- Mapping field
- Verify data integrity""",

    "5.6": """Phase 5: OPERASIONAL HARIAN

Pagi (Pre-Open)
- Cek booking hari ini
- Cek staff attendance
- Cek inventory critical

Siang (Operating Hours)
- Pasien check-in via QR
- Antrian dipanggil
- Konsultasi dengan nakes
- EMR entry
- E-Resep generation
- Billing & payment
- Inventory update (obat keluar)

Sore (Closing)
- Cash recap
- Pasien rawat inap handover
- Inventory check
- Tomorrow preview

Malam (Maintenance)
- Auto-backup data (cloud)
- Generate daily report
- Send to email PIC

Throughout the Day
- Telemedicine (jika nakes available)
- Walk-in (selain booking)
- Emergency handling (jika UGD)""",

    "5.7": """Phase 6: MONTHLY REPORTING

Akhir Bulan
Tab "Reports":
1. Generate report:
   - Patient visits per service
   - Revenue per service
   - Top performing nakes
   - Inventory turnover
   - Cost analysis
2. Export PDF / CSV
3. Distribute ke stakeholder

Payroll Processing
- Auto-calculate gaji
- Generate payslip
- Bank transfer (batch)
- BPJS reporting

Tax Filing Prep
- Income data ready
- Expense data ready
- Auto 1721-A1 untuk staff
- VAT (PPN) calculation

Strategy Review
- Compare bulan vs bulan lalu
- Identify trends
- Action items untuk improve

Akreditasi (Jika Akan KARS/SNARS)
- Auto-track metric akreditasi
- Documentation export
- Gap analysis""",

    "5.8": """Phase 7: RENEWAL & UPGRADE

30 Hari Sebelum Expiry
- Notification email + WA
- Review tier saat ini vs kebutuhan
- Discount annual prepay: -17% (bayar 12 bulan dapat 14 bulan)

Renewal Options
- Same tier: auto-renew
- Upgrade ke tier lebih tinggi
- Downgrade (jika overshoot)

Annual Plan vs Monthly
- Monthly: fleksibel cancel
- Annual prepay: -17% (bayar 12 bulan dapat 14 bulan), lock harga
- 2-tahun prepay: -25%

Upgrade Trigger
- Sudah hit limit (e.g. 500 encounter/bulan di Solo)
- Butuh modul advanced (Rawat Inap)
- Multi-klinik expansion

Downgrade Trigger
- Aktivitas berkurang
- Beberapa fitur tidak terpakai
- Tetap save dengan tier lebih rendah""",

    "6.1": """Pilih Tier yang Tepat untuk ROI.

EMR Solo (Rp49rb/bulan)
- Cocok: praktek mandiri, klinik 1-2 dokter
- Breakeven: 1 pasien/bulan @ Rp100K
- ROI: 10x easily

EMR-CMS Rawat Jalan (Rp99rb/bulan)
- Cocok: klinik rawat jalan, multi-dokter
- Breakeven: 1 pasien/bulan @ Rp100K
- ROI: 10-30x typical

EMR-CMS Rawat Inap (Rp199rb/bulan)
- Cocok: klinik + rawat inap, RS Tipe D
- Breakeven: 2 pasien/bulan @ Rp100K
- ROI: 20-50x

EMR-HMS RS Tipe C-D (Rp999rb/bulan)
- Cocok: RS Tipe C-D (<200 bed), multi-spesialisasi
- Breakeven: 10 pasien/bulan @ Rp100K
- ROI: 50-200x

EMR-HMS RS Tipe B (Rp2jt/bulan)
- Cocok: RS Tipe B (200-400 bed), high-volume
- Breakeven: 20 pasien/bulan @ Rp100K
- ROI: 100-300x

EMR-HMS RS Tipe A (Rp3jt/bulan)
- Cocok: RS Tipe A (>400 bed), dedicated SLA + single-tenant
- Breakeven: 30 pasien/bulan @ Rp100K
- ROI: 200x+

Kapan Upgrade?
- 80% capacity utilized
- Butuh fitur module advanced
- Multi-klinik expansion

Kapan Downgrade?
- < 50% capacity
- Beberapa modul tidak dipakai""",

    "6.2": """Multi-Klinik Activation untuk Group.

Untuk Group Faskes
- Manage 2+ klinik dalam 1 dashboard
- Consolidated reporting
- Inter-klinik resource sharing

Cost
- Akumulasi subscription per klinik sesuai tiernya (campur tier bebas)
- Diskon multi-faskes otomatis: -10% (2-5 faskes) / -15% (6+ faskes)
- Pemerintah/enterprise: custom procurement (LKPP e-katalog)

Benefits
• Single login untuk owner
• Quick switch antar klinik
• Group analytics
• Shared staff database
• Inter-klinik referral

ROI Group
- 5 klinik Rawat Inap × @Rp100jt/bulan revenue = Rp500jt
- Subscription: 5 × Rp199rb = Rp995rb, diskon -10% multi-faskes = ~Rp896rb/bulan
- Cost = ~0.18% of revenue
- Operating savings 5-10% via consolidation""",

    "6.3": """Nakes Recruitment untuk Faskes Growth.

Strategi Recruitment
1. Post lowongan menarik
   - Tarif kompetitif
   - Benefit (BPJS, sertifikat, training)
   - Jadwal fleksibel
   - Career growth

2. Active search
   - Search nakes di Nakesmart
   - Filter by spesialisasi + lokasi
   - Direct invite

3. Network
   - Recommend dari nakes existing
   - Event kesehatan
   - Asosiasi nakes (IDI, PPNI, IBI)

Onboarding Cepat
- Welcome kit
- SIMRS training (1-2 hari)
- Shadow senior nakes (1 minggu)
- Independent practice

Retention
- Bonus performance
- Sertifikat profesional
- Networking event
- Mental health support""",

    "6.4": """Service Catalog Optimization.

Add High-Demand Services
- MCU (Medical Check-Up)
- Vaccination (anak, dewasa, COVID)
- Aesthetic (botox, filler — jika legal)
- Konsultasi mental health
- Telemedicine premium

Bundle Layanan
- Paket MCU lengkap (-15%)
- Family Health Package
- Pre-Marriage Check
- Annual Diabetes Care

Tier Pricing
- Basic / Premium / VIP
- Beda durasi, beda dokter, beda value-add

Niche Specialty
- Skin & Beauty Clinic
- Mental Health Center
- Geriatric Care
- Pediatric Specialist

Marketing Service Catalog
- Featured di Nakesmart Marketplace (CMS+ subscriber)
- Promo voucher
- Referral program""",

    "6.5": """Voucher untuk Customer Retention.

Strategi Voucher
• Welcome 10% (new patient)
• Birthday Rp50K
• Loyalty: 5x visit → free konsultasi
• Win-back: 6 bulan no visit → Rp100K voucher
• Family combo: 1 visit → 25% off untuk family member

Seasonal Campaigns
• Hari Kesehatan Nasional (12 November): -20%
• HUT RI (17 Agustus): paket merdeka sehat
• Tahun Baru: detox program
• Hari Ibu (22 Des): MCU ibu

ROI Voucher
- Voucher Rp50K → tarik pasien Rp200K visit
- Net Rp150K + lifetime value Rp1-5jt

Track Performance
- Voucher claim rate
- Conversion (claim → actual visit)
- Revenue from voucher
- Cost per acquisition""",

    "7.1": """Faskes Profile Optimization.

Hero Section
- Foto kualitas tinggi (banyak natural light)
- Headline jelas: "Klinik Umum 24 Jam di Depok"
- Tagline value prop: "Antrian Cepat, Dokter Verified, Harga Transparan"

Galeri Foto
- Eksterior (gedung, papan nama)
- Interior (ruang tunggu, ruang dokter)
- Fasilitas (lab, radiologi, apotek)
- Tim staff (group photo)
- Equipment

Layanan Detail
- Description lengkap per layanan
- Tarif transparan (tidak hidden cost)
- Persiapan pasien (puasa, bawa apa)

SEO Keywords
- Lokasi: "Klinik di Depok Timur"
- Layanan: "MCU lengkap Depok"
- Spesialis: "Dokter spesialis kulit Depok"

Reviews Management
- Reply review pasien (positive & negative)
- Profesional + apologetic untuk negative
- Thank you untuk positive

Update Berkala
- Jam buka khusus libur
- Promo voucher aktif
- Dokter baru bergabung""",

    "7.2": """Manage Booking Backlog Efisien.

Antrian Smart
- Slot 30 menit untuk konsultasi
- Buffer 5 menit antar slot
- Time block untuk emergency

Pre-Visit Preparation
- Pasien kirim keluhan via app
- Dokter review sebelum bertemu
- Save 5-10 menit per pasien

Walk-In Management
- Slot khusus walk-in (e.g. 20% kapasitas)
- Atau walk-in fee lebih tinggi
- Prioritize booking

No-Show Reduction
- Reminder H-1
- Konfirmasi 1 jam sebelum
- Penalty no-show (50% deposit hangus)

Overbook Strategy
- 10-15% overbook untuk anticipate no-show
- Risk: long wait jika semua datang
- Communication jelas ke pasien""",

    "7.3": """Multi-Channel Patient Acquisition.

Online
• Nakesmart Marketplace (free listing)
• Google My Business
• Instagram/Facebook ads
• TikTok organic
• SEO website faskes
• Influencer partnership

Offline
• Brochure di apotek partner
• Sponsorship event kesehatan
• Community health screening
• Mall booth
• Kerja sama corporate (perusahaan)

Referral
• Pasien existing refer keluarga
• Dokter umum refer ke spesialis (di group)
• Asuransi network

Affiliate
• Affiliate dengan apotek (cross-promo)
• Affiliate dengan lab (combined package)
• Affiliate dengan insurance brokers""",

    "7.4": """SOP untuk Nakes Affiliated.

Welcome SOP
- Greeting standar
- Self-introduction
- Cek identitas pasien (double-check)

Konsultasi SOP
- Anamnesa SOAP framework
- Time management (max 15 menit untuk umum)
- Document di EMR
- E-Resep generation

Dispute Handling
- Pasien complain → konsultasi senior dulu
- Jika tidak resolved → escalate to faskes manager
- Document semua

Profesionalisme
- Punctuality
- Empathy
- Patient education
- Compliance dengan standar medis

Quality Metrics
- Patient satisfaction > 4.5
- Average consultation time
- E-Resep accuracy
- Follow-up rate""",

    "7.5": """Premium Service Marketing.

Premium Services Worth Marketing
• VIP MCU (10 specialist examination)
• Concierge service
• Home visit
• Telemedicine 24/7
• Aesthetic premium
• Mental health package

Positioning
- Quality over price
- Personalized service
- Exclusive doctors
- Premium facilities

Channel
- High-net-worth area targeting (Pondok Indah, Menteng)
- Country club partnership
- Premium card holder discount

Pricing Strategy
- Anchor pricing (show normal + premium)
- Bundle (lebih murah jika pakai 3+ services)
- Subscription model (annual MCU)""",

    "8.1": """Native SIMRS App (Tablet/iPad).

12 Layar Expo Native
- Patient queue
- EMR entry
- Vital signs
- Lab orders
- Radiology orders
- E-Resep
- Discharge summary
- Inventory check
- Billing
- Cashier
- Staff schedule
- Reports

Untuk Tablet 10-13 inch
- Optimasi iPad Air/Pro
- Android tablet Samsung, Lenovo
- Side-by-side view
- Apple Pencil support
- Multi-window

Workflow Optimization
- Dokter pegang tablet selama konsultasi
- Quick EMR entry
- E-Resep tanpa pindah computer
- Lab order ke perawat real-time

Offline Support
- Cache data 24 jam
- Sync saat online
- Tidak terganggu koneksi""",

    "8.2": """Desktop SIMRS (Electron).

Untuk Receptionist & Manager
- Desktop app via Electron
- Wraps web SIMRS
- Multi-window
- Keyboard shortcut native
- Auto-update

Use Case
- Receptionist: check-in pasien, antrian, billing
- Manager: analytics, reports, staff
- Kasir: payment processing

Compatibility
- Windows 10+
- macOS 11+
- Linux Ubuntu/Debian""",

    "8.3": """Multi-Layer Security untuk Faskes.

Patient Data Protection
- Multi-layer security (5 layers anti-AI scraping)
- Encryption at rest (database)
- Encryption in transit (HTTPS)
- HMAC signed API requests
- JWT hardening
- Role-based access control

Compliance
- UU PDP (Indonesian Data Protection)
- GDPR-equivalent
- KARS/SNARS friendly
- HIPAA-style (untuk medical)

Audit Trail
- Setiap akses logged
- Modifikasi data tracked
- Export untuk audit
- Tamper-proof logs

Backup
- Daily auto-backup
- 30 hari retention
- Geo-redundant (multi-region)
- Quick restore (RTO < 4 jam)""",

    "8.4": """Audit Security 2026 — Round 1-8.

Round 1-3: Auth & Money
✅ JWT hardening
✅ Midtrans validation
✅ Wallet IDOR fixes

Round 4: Unauth Endpoints
✅ Bank accounts protection
✅ Cart verify-payment
✅ Admin users dump blocked

Round 5: OTP + Race
✅ Distributed lock
✅ Idempotency keys

Round 6: Global Admin Guard
✅ Middleware /api/admin/*

Round 7-8: Defense in Depth
✅ Slot conflict check
✅ E.164 phone normalize
✅ CORS hardening
✅ Email XSS fix
✅ Upload validation
✅ Auto-refund

Untuk Faskes
- Data pasien lebih aman
- Financial transactions secure
- Compliance ready
- Audit trail complete""",

    "8.5": """Roadmap Faskes 2026-2028.

Q3 2026
• BPJS Claims auto-integration
• SatuSehat sync (full)
• KARS/SNARS auto-audit
• Telemedicine bridge ke faskes (pasien dapat resep dari telemed → tebus di faskes)

Q4 2026
• Lab equipment integration (auto-input results)
• Radiology PACS full integration
• Pharmacy automation (auto-reorder)
• Multi-language (untuk faskes di Bali, dll)

Q1 2027
• AI-powered diagnosis assistance
• Predictive analytics (patient no-show)
• Inventory AI (auto-reorder based on demand)
• Staff scheduling AI

Q2-Q4 2027
• Faskes Marketplace (sell unused capacity)
• Insurance network expansion (AXA, Allianz)
• Equipment leasing
• Group purchasing power

2028
• Full clinical AI suite
• Robotic surgery scheduling
• Telemedicine satellite (untuk daerah 3T)
• Cross-border medical tourism""",

    "A": """Glossarium Faskes

BPJS — Badan Penyelenggara Jaminan Sosial
CMS — Clinical Management System
CPPT — Catatan Perkembangan Pasien Terintegrasi
EMR — Electronic Medical Record
HMS — Hospital Management System
KARS — Komisi Akreditasi Rumah Sakit
NICU — Neonatal Intensive Care Unit
PACS — Picture Archiving and Communication System
RIS — Radiology Information System
SatuSehat — Platform Kemenkes Indonesia
SIMRS — Sistem Informasi Manajemen Rumah Sakit
SIUP — Surat Izin Usaha Perdagangan
SIO — Surat Izin Operasional
SNARS — Standar Nasional Akreditasi Rumah Sakit
SOAP — Subjective, Objective, Assessment, Plan""",

    "B": """FAQ Khusus Faskes

Q: Bagaimana free trial-nya?
A: 6 bulan pertama gratis, atau sampai 20 pasien/bulan (mana dulu). Tier mana saja, semua fitur aktif, tanpa kartu kredit. Anti-fraud: dedupe by STR/SIP/NIK.

Q: Bisakah saya pindah tier kapan saja?
A: Upgrade kapan saja (prorating). Downgrade di akhir period.

Q: Apakah data saya bisa di-export jika cancel?
A: Ya, full data export (CSV/PDF/JSON) sebelum cancel.

Q: Bagaimana migrasi dari SIMRS lama?
A: Migrasi data sudah TERMASUK di semua tier - self-service via auto-wizard (upload CSV dari Excel/Google Sheet/SIM lama -> preview + mapping -> confirm dengan validation + rollback).

Q: Apakah staff bisa multi-role?
A: Ya, satu staff bisa multi-role (dokter + perawat + apoteker).

Q: Bagaimana jika offline (no internet)?
A: Tablet app cache 24 jam. Auto-sync saat online.

Q: Compliance KARS/SNARS?
A: Auto-track metrics akreditasi. Documentation export ready.

Q: Multi-klinik harga?
A: Akumulasi subscription per klinik sesuai tiernya (campur tier bebas). Diskon multi-faskes otomatis -10% (2-5 faskes) / -15% (6+ faskes). Pemerintah/enterprise: custom procurement.

Q: Berapa lama setup?
A: 1-2 minggu untuk full setup. Training termasuk.""",

    "C": """Daftar Tarif Subscription per Tier (Estimasi)

CATATAN: Tarif di bawah adalah estimasi pada saat panduan disusun. Harga resmi & terbaru: hubungi sales@nakesmart.com atau cek /simrs/pricing. Ada 6 tier.

EMR Solo (estimasi Rp49.000/bulan)
- EMR rawat jalan (SOAP, ICD-10)
- Booking management + Dental
- 500 encounter/bulan
- 2 akun (1 dokter + 1 admin)
- Patient marketplace

EMR-CMS Rawat Jalan (Rp99.000/bulan)
- Semua Solo +
- CMS Rawat Jalan + Billing multi-payment
- Multi-user unlimited
- Farmasi FEFO, SDM+payroll, Finance
- Lab + Radiologi (DICOM URL viewer)
- Analytics

EMR-CMS Rawat Inap (Rp199.000/bulan)
- Semua CMS_RJ +
- Rawat Inap module (bed, CPPT)
- UGD basic, Persalinan normal
- Multi-user unlimited
- BPJS integration

EMR-HMS RS Tipe C-D (Rp999.000/bulan)
- Semua CMS_RI +
- HMS lengkap, Kamar Operasi (OK)
- Lab+LIS, Radiologi+DICOM, ICU+NEWS2, Bank Darah
- IKP SNARS + quality indicators
- Unlimited users & pasien, support 24/7

EMR-HMS RS Tipe B (Rp2.000.000/bulan)
- Semua HMS C-D +
- High-volume (>10rb encounter/bulan)
- DICOM/PACS storage unlimited
- Audit chain RFC 3161, custom report builder, API integration
- Training tim unlimited

EMR-HMS RS Tipe A (Rp3.000.000/bulan)
- Semua HMS Tipe B +
- Custom branding, dedicated SLA 99.9%
- Onsite engineer quarterly, white-label mobile
- Dedicated infrastructure (single-tenant), opsi on-premise/hybrid

Multi-Faskes
- Akumulasi subscription per faskes sesuai tiernya (campur tier bebas)
- Diskon multi-faskes: -10% (2-5 faskes) / -15% (6+ faskes)
- Pemerintah/enterprise: custom procurement (LKPP e-katalog)

Diskon Prabayar
- Annual prepay: -17% (bayar 12 bulan dapat 14 bulan)
- 2-tahun prepay: -25%
- Startup faskes (<2 thn): -30% tahun pertama
- NGO/Yayasan: -20%

Add-On Premium (opsional)
- MedAI mulai Rp300rb/bln, Medping Rp1jt/bln, WA Business Rp750rb/bln
- Backup Encryption Rp1,5jt/bln, Compliance Bundle Rp3jt/bln, API Premium Rp2jt/bln
- DICOM/PACS extra storage Rp2,5jt/TB

Voucher Tersedia
- COMEBACK25 untuk reactivation (-25%)
- NEWFASKES untuk first month (-50%)""",

    "D": """Kontak Sales & Support

Sales
• Email: sales@nakesmart.com
• WhatsApp: +62 851-XXXX-XXXX (Sales)
• Demo gratis (online via Zoom)

Onboarding Support
• Setup helper assigned
• Training 2-3 sesi gratis
• Migration assist

Technical Support
• 24/7 untuk HMS subscriber
• Business hours untuk Solo/CMS
• Tab "Bantuan" di app
• Email: support@nakesmart.com

Account Manager (HMS Subscriber)
• Personal account manager
• Quarterly business review
• Strategic planning

Emergency Hotline
• Critical issue (SIMRS down)
• Response < 30 menit
• Resolution SLA < 2 jam

Tentang PT Nakesmart
PT GIANNA MEDICAL CENTER
Alamat: Jakarta
Website: nakesmart.com
Email: faskes@nakesmart.com""",
}
