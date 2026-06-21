# Checklist Screenshot - Dokumen Midtrans (PT GIANNA MEDICAL CENTER)

Total 11 screenshot. Centang [x] tiap selesai.

## CARA TERMUDAH (auto-embed ke PDF)

1. Login ke nakesmart.com pakai akun pasien Anda.
2. Tekan `Windows + Shift + S` -> pilih area layar -> screenshot ke clipboard.
3. Tempel & simpan sebagai file di folder INI (`screenshots\`) dengan nama PERSIS:
   `step1.png` , `step2.png` , ... , `step9.png` , dan `zoom.png`
   (boleh `.jpg`; nama harus sama persis, huruf kecil)
4. Bilang ke Claude **"rebuild PDF"** -> file otomatis masuk ke `Dokumen_Midtrans_Nakesmart.pdf`.

> Alternatif: tempel langsung ke kotak placeholder di `Dokumen_Midtrans_Nakesmart.docx` (klik kotak, Delete, `Ctrl + V`).
> Ukuran browser disarankan: 1280x720 atau 1366x768 (window biasa, bukan fullscreen).

---

## A. Customer Journey (9 screenshot - Bab 2)

- [ ] **Step 1 - Landing Page**  ->  simpan: `step1.png`
  URL: `https://nakesmart.com`
  Tampilkan: hero + menu layanan (Telemedicine, Cek Gejala AI, dll) + tombol Sign In / Sign Up.

- [ ] **Step 2 - Katalog Telemedicine**  ->  simpan: `step2.png`
  URL: `https://nakesmart.com/telemedicine`
  Tampilkan: kartu nakes dengan 3 tier (Chat / Voice / Video) + rating + tombol View & Book.

- [ ] **Step 3 - Pilih Jadwal + Keranjang**  ->  simpan: `step3.png`
  URL: `https://nakesmart.com/cart` (setelah pilih nakes & slot)
  Tampilkan: slot waktu terpilih + ringkasan keranjang + total harga.

- [ ] **Step 4 - Halaman Checkout**  ->  simpan: `step4.png`
  URL: `https://nakesmart.com/checkout`
  Tampilkan: daftar metode pembayaran + logo/label Midtrans + tombol "Bayar Sekarang".

- [ ] **Step 5 - Popup Midtrans Snap**  ->  simpan: `step5.png`
  Muncul setelah klik "Bayar Sekarang" (perlu keys Midtrans Sandbox/Production).
  Tampilkan: popup Snap resmi Midtrans (Order ID + nominal + VA/GoPay/QRIS/CC).
  > Bukti paling penting buat Midtrans. TANPA keys, popup ini tak muncul -> lewati, dokumen pakai mockup.

- [ ] **Step 6 - Konfirmasi Pembayaran**  ->  simpan: `step6.png`
  Contoh: layar GoPay / instruksi Virtual Account / tampilan QRIS.
  Tampilkan: nominal + tujuan "PT GIANNA MEDICAL CENTER" + via Midtrans.

- [ ] **Step 7 - (opsional) Bukti Webhook**  ->  simpan: `step7.png`
  Midtrans Dashboard > Transactions status "settlement", ATAU log server `/api/midtrans/notification` 200 OK.

- [ ] **Step 8 - Pembayaran Sukses**  ->  simpan: `step8.png`
  URL: `https://nakesmart.com/payment/success`
  Tampilkan: status sukses + Order ID + detail layanan + total dibayar.

- [ ] **Step 9 - Ruang Konsultasi / Layanan Diterima**  ->  simpan: `step9.png`
  URL: `https://nakesmart.com/telemedicine/session/...`
  Tampilkan: ruang chat konsultasi ATAU e-Resep yang diterima.

---

## B. Bukti Zoom Partner (1 screenshot - Bab 4.2)

- [ ] **Video Konsultasi (Tier Exclusive)**  ->  simpan: `zoom.png`
  URL: `https://nakesmart.com/telemedicine/zoom/...` (saat sesi Exclusive berlangsung)
  Tampilkan: video meeting Zoom ter-embed di Nakesmart.

---

## C. Lampiran Zoom (KIRIM TERPISAH ke Midtrans, jangan di dokumen publik)

- [ ] **Zoom Marketplace Dashboard** - `marketplace.zoom.us` > Manage > Built Apps
  Tampilkan App "Nakesmart Telemedicine Video" (Server-to-Server OAuth). Sensor Client Secret.
- [ ] **(opsional) Hasil API call** `GET https://api.zoom.us/v2/users/me` (sensor token).

---

## D. Dokumen Legal Pendukung (lampiran terpisah bila diminta Midtrans)

- [ ] NIB (Nomor Induk Berusaha)
- [ ] NPWP perusahaan (PT GIANNA MEDICAL CENTER)
- [ ] Akta pendirian PT
- [ ] Rekening bank perusahaan (untuk settlement)
- [ ] KTP + NPWP direktur / PIC

---

## Catatan Sandbox vs Production

Belum production? Jalankan flow di Sandbox dulu (keys GRATIS di `dashboard.sandbox.midtrans.com`):
- Step 5-6 menampilkan popup Snap Sandbox (ada label "SANDBOX") - ini tetap valid sebagai bukti integrasi.
- Kartu test Midtrans: `4811 1111 1111 1114` (CC), atau simulator VA/e-wallet di dashboard sandbox.

Setelah Midtrans approve production, alur yang sama berjalan dengan uang asli.
