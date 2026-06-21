# -*- coding: utf-8 -*-
"""
Build dokumentasi Midtrans:
- End-to-end flow customer order -> payment
- Mockup screenshots (rectangle-based representations)
- Zoom partner integration proof

Output: Dokumen_Midtrans_Nakesmart.pdf
"""
import os
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, black, white, lightgrey
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Image, Flowable,
)
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Polygon, Circle
from reportlab.graphics import renderPDF

# Brand colors
FOREST_GREEN = "#0F5132"
DEEP_FOREST = "#1B4D3E"
LIME = "#C8FF00"
CHARCOAL = "#1F2937"
LIGHT_BG = "#F8FAFC"
WHITE = "#FFFFFF"
MIDTRANS_BLUE = "#1F60E3"
GRAY = "#94A3B8"
LIGHTGRAY = "#E2E8F0"

YEAR = "2026"
COMPANY = "PT GIANNA MEDICAL CENTER"
WEBSITE = "nakesmart.com"

# Folder screenshot asli. Taruh file bernama step1.png .. step9.png + zoom.png
# (boleh .jpg) di sini → otomatis dipakai menggantikan mockup saat rebuild.
SCREENSHOT_DIR = Path(__file__).parent / "screenshots"


def screen_or_mockup(step_key, mockup, width=15.5 * cm, max_height=17 * cm):
    """Kembalikan Image (jika screenshots/{step_key}.{png,jpg} ada), else mockup."""
    from reportlab.lib.utils import ImageReader
    for ext in ('.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'):
        img_path = SCREENSHOT_DIR / f"{step_key}{ext}"
        if img_path.exists():
            try:
                ir = ImageReader(str(img_path))
                iw, ih = ir.getSize()
                w = width
                h = w * ih / iw
                if h > max_height:
                    h = max_height
                    w = h * iw / ih
                return Image(str(img_path), width=w, height=h)
            except Exception as e:
                print(f"  [warn] gagal load {img_path.name}: {e}")
    return mockup


# =====================================================================
# Mockup screen flowable
# =====================================================================

class MockupScreen(Flowable):
    """Draws a phone-shaped mockup of a screen with header + content boxes."""
    def __init__(self, title="Screen", url="", elements=None, width=11*cm, height=14*cm):
        Flowable.__init__(self)
        self.title = title
        self.url = url
        self.elements = elements or []
        self.width = width
        self.height = height

    def wrap(self, *args):
        return self.width, self.height

    def draw(self):
        c = self.canv
        # Phone frame outline
        c.setStrokeColor(HexColor(CHARCOAL))
        c.setFillColor(HexColor(WHITE))
        c.setLineWidth(1.2)
        c.roundRect(0, 0, self.width, self.height, 0.4*cm, fill=1, stroke=1)

        # URL bar (top)
        c.setFillColor(HexColor(LIGHTGRAY))
        c.rect(0, self.height - 0.7*cm, self.width, 0.7*cm, fill=1, stroke=0)
        c.setFillColor(HexColor(CHARCOAL))
        c.setFont("Helvetica", 7)
        c.drawString(0.25*cm, self.height - 0.5*cm, "[URL] " + self.url)

        # Title bar (Nakesmart green)
        c.setFillColor(HexColor(FOREST_GREEN))
        c.rect(0, self.height - 1.7*cm, self.width, 1.0*cm, fill=1, stroke=0)
        c.setFillColor(HexColor(WHITE))
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0.4*cm, self.height - 1.3*cm, "NAKESMART  -  " + self.title)

        # Content area
        y = self.height - 2.2*cm
        for el in self.elements:
            etype = el.get('type', 'text')
            label = el.get('label', '')
            if etype == 'text':
                c.setFillColor(HexColor(CHARCOAL))
                c.setFont("Helvetica", 9)
                c.drawString(0.4*cm, y, label)
                y -= 0.4*cm
            elif etype == 'header':
                c.setFillColor(HexColor(DEEP_FOREST))
                c.setFont("Helvetica-Bold", 11)
                c.drawString(0.4*cm, y, label)
                y -= 0.55*cm
            elif etype == 'card':
                # box with label
                bx = 0.4*cm
                bw = self.width - 0.8*cm
                bh = el.get('h', 1.4*cm)
                c.setFillColor(HexColor(LIGHT_BG))
                c.setStrokeColor(HexColor(LIGHTGRAY))
                c.setLineWidth(0.5)
                c.roundRect(bx, y - bh, bw, bh, 0.15*cm, fill=1, stroke=1)
                # Card text lines
                c.setFillColor(HexColor(CHARCOAL))
                lines = label.split('|')
                ty = y - 0.4*cm
                c.setFont("Helvetica-Bold", 9)
                if lines:
                    c.drawString(bx + 0.25*cm, ty, lines[0])
                    ty -= 0.35*cm
                c.setFont("Helvetica", 8)
                for ln in lines[1:]:
                    c.drawString(bx + 0.25*cm, ty, ln)
                    ty -= 0.3*cm
                y -= bh + 0.2*cm
            elif etype == 'button':
                # CTA button (lime green)
                bx = 0.5*cm
                bw = self.width - 1.0*cm
                bh = 0.7*cm
                c.setFillColor(HexColor(LIME))
                c.roundRect(bx, y - bh, bw, bh, 0.15*cm, fill=1, stroke=0)
                c.setFillColor(HexColor(FOREST_GREEN))
                c.setFont("Helvetica-Bold", 10)
                tw = c.stringWidth(label, "Helvetica-Bold", 10)
                c.drawString(bx + (bw - tw)/2, y - bh + 0.22*cm, label)
                y -= bh + 0.2*cm
            elif etype == 'button_outline':
                bx = 0.5*cm
                bw = self.width - 1.0*cm
                bh = 0.6*cm
                c.setFillColor(HexColor(WHITE))
                c.setStrokeColor(HexColor(FOREST_GREEN))
                c.setLineWidth(1)
                c.roundRect(bx, y - bh, bw, bh, 0.15*cm, fill=1, stroke=1)
                c.setFillColor(HexColor(FOREST_GREEN))
                c.setFont("Helvetica-Bold", 9)
                tw = c.stringWidth(label, "Helvetica-Bold", 9)
                c.drawString(bx + (bw - tw)/2, y - bh + 0.2*cm, label)
                y -= bh + 0.15*cm
            elif etype == 'midtrans_logo':
                # Midtrans branded box
                bx = 0.4*cm
                bw = self.width - 0.8*cm
                bh = 1.0*cm
                c.setFillColor(HexColor(MIDTRANS_BLUE))
                c.roundRect(bx, y - bh, bw, bh, 0.1*cm, fill=1, stroke=0)
                c.setFillColor(HexColor(WHITE))
                c.setFont("Helvetica-Bold", 11)
                c.drawString(bx + 0.3*cm, y - 0.4*cm, "MIDTRANS")
                c.setFont("Helvetica", 8)
                c.drawString(bx + 0.3*cm, y - 0.75*cm, label)
                y -= bh + 0.2*cm
            elif etype == 'divider':
                c.setStrokeColor(HexColor(LIGHTGRAY))
                c.setLineWidth(0.5)
                c.line(0.4*cm, y, self.width - 0.4*cm, y)
                y -= 0.3*cm
            elif etype == 'price':
                c.setFillColor(HexColor(FOREST_GREEN))
                c.setFont("Helvetica-Bold", 14)
                c.drawString(0.4*cm, y - 0.1*cm, label)
                y -= 0.55*cm
            elif etype == 'status_success':
                bx = 0.4*cm
                bw = self.width - 0.8*cm
                bh = 1.5*cm
                c.setFillColor(HexColor("#DCFCE7"))
                c.setStrokeColor(HexColor("#22C55E"))
                c.roundRect(bx, y - bh, bw, bh, 0.15*cm, fill=1, stroke=1)
                c.setFillColor(HexColor("#15803D"))
                c.setFont("Helvetica-Bold", 11)
                c.drawString(bx + 0.3*cm, y - 0.5*cm, "[OK] PEMBAYARAN SUKSES")
                c.setFont("Helvetica", 9)
                c.setFillColor(HexColor(CHARCOAL))
                c.drawString(bx + 0.3*cm, y - 0.95*cm, label)
                y -= bh + 0.2*cm


def make_flow_arrow(width=2*cm, height=1.5*cm, label="STEP"):
    """Returns a Drawing flowable of an arrow with label."""
    d = Drawing(width, height)
    poly = Polygon(
        points=[0, height/2 + 0.3*cm,
                width - 0.5*cm, height/2 + 0.3*cm,
                width - 0.5*cm, height/2 + 0.6*cm,
                width, height/2,
                width - 0.5*cm, height/2 - 0.6*cm,
                width - 0.5*cm, height/2 - 0.3*cm,
                0, height/2 - 0.3*cm],
        fillColor=HexColor(LIME), strokeColor=HexColor(FOREST_GREEN), strokeWidth=1,
    )
    d.add(poly)
    d.add(String(width/2 - 0.4*cm, height/2 - 0.15*cm, label,
                 fontName="Helvetica-Bold", fontSize=9, fillColor=HexColor(FOREST_GREEN)))
    return d


# =====================================================================
# PDF builder
# =====================================================================

def get_styles():
    base = getSampleStyleSheet()
    return {
        'cover_brand': ParagraphStyle('cover_brand', parent=base['Title'],
            fontName='Helvetica-Bold', fontSize=40, textColor=HexColor(FOREST_GREEN),
            alignment=TA_CENTER, leading=46, spaceAfter=8),
        'cover_title': ParagraphStyle('cover_title', parent=base['Title'],
            fontName='Helvetica-Bold', fontSize=24, textColor=HexColor(CHARCOAL),
            alignment=TA_CENTER, leading=30, spaceAfter=10),
        'cover_sub': ParagraphStyle('cover_sub', parent=base['Title'],
            fontName='Helvetica', fontSize=14, textColor=HexColor(DEEP_FOREST),
            alignment=TA_CENTER, leading=18, spaceAfter=8),
        'cover_meta': ParagraphStyle('cover_meta', parent=base['Normal'],
            fontName='Helvetica-Bold', fontSize=11, textColor=HexColor(FOREST_GREEN),
            alignment=TA_CENTER, spaceAfter=4),
        'cover_company': ParagraphStyle('cover_company', parent=base['Normal'],
            fontName='Helvetica', fontSize=10, textColor=HexColor(CHARCOAL),
            alignment=TA_CENTER, spaceAfter=2),
        'h1': ParagraphStyle('h1', parent=base['Heading1'],
            fontName='Helvetica-Bold', fontSize=20, textColor=HexColor(FOREST_GREEN),
            spaceBefore=10, spaceAfter=12, leading=24),
        'h2': ParagraphStyle('h2', parent=base['Heading2'],
            fontName='Helvetica-Bold', fontSize=14, textColor=HexColor(DEEP_FOREST),
            spaceBefore=12, spaceAfter=6, leading=18),
        'h3': ParagraphStyle('h3', parent=base['Heading3'],
            fontName='Helvetica-Bold', fontSize=11, textColor=HexColor(FOREST_GREEN),
            spaceBefore=8, spaceAfter=4, leading=14),
        'body': ParagraphStyle('body', parent=base['Normal'],
            fontName='Helvetica', fontSize=10, textColor=HexColor(CHARCOAL),
            alignment=TA_JUSTIFY, leading=13.5, spaceAfter=5),
        'bullet': ParagraphStyle('bullet', parent=base['Normal'],
            fontName='Helvetica', fontSize=9.5, textColor=HexColor(CHARCOAL),
            leftIndent=14, spaceAfter=2, leading=12.5, bulletIndent=4),
        'step_label': ParagraphStyle('step_label', parent=base['Normal'],
            fontName='Helvetica-Bold', fontSize=12, textColor=HexColor(WHITE),
            alignment=TA_CENTER),
        'caption': ParagraphStyle('caption', parent=base['Normal'],
            fontName='Helvetica-Oblique', fontSize=9, textColor=HexColor(GRAY),
            alignment=TA_CENTER, spaceAfter=8),
        'note_box': ParagraphStyle('note_box', parent=base['Normal'],
            fontName='Helvetica', fontSize=9.5, textColor=HexColor(CHARCOAL),
            leftIndent=10, rightIndent=10, leading=13, spaceAfter=4),
    }


def add_step_header(story, styles, step_num, title):
    """Add a styled step header."""
    table = Table(
        [[f"STEP {step_num}", title]],
        colWidths=[3*cm, 13*cm],
    )
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), HexColor(FOREST_GREEN)),
        ('BACKGROUND', (1, 0), (1, 0), HexColor(LIGHT_BG)),
        ('TEXTCOLOR', (0, 0), (0, 0), HexColor(WHITE)),
        ('TEXTCOLOR', (1, 0), (1, 0), HexColor(FOREST_GREEN)),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ('ALIGN', (1, 0), (1, 0), 'LEFT'),
        ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
        ('LEFTPADDING', (1, 0), (1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ]))
    story.append(table)
    story.append(Spacer(1, 0.3*cm))


def build_doc():
    out_path = Path(__file__).parent / "Dokumen_Midtrans_Nakesmart.pdf"
    styles = get_styles()
    doc = SimpleDocTemplate(
        str(out_path), pagesize=A4,
        topMargin=1.8*cm, bottomMargin=1.8*cm,
        leftMargin=2*cm, rightMargin=2*cm,
    )

    story = []

    # ==================== COVER ====================
    story.append(Spacer(1, 3*cm))
    story.append(Paragraph("NAKESMART", styles['cover_brand']))
    story.append(Paragraph("* * *", ParagraphStyle('cm', parent=styles['cover_meta'], fontSize=18, textColor=HexColor(LIME))))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("DOKUMEN UNTUK MIDTRANS", styles['cover_title']))
    story.append(Paragraph("End-to-End Customer Journey + Payment Flow", styles['cover_sub']))
    story.append(Paragraph("+ Bukti Integrasi Zoom Partner", styles['cover_sub']))
    story.append(Spacer(1, 3*cm))
    story.append(Paragraph(f"DIAJUKAN UNTUK: PT MIDTRANS (Veritrans Indonesia)", styles['cover_meta']))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(f"EDISI {YEAR} - VERSION 1.0", styles['cover_meta']))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(COMPANY, styles['cover_company']))
    story.append(Paragraph(WEBSITE, styles['cover_company']))
    story.append(PageBreak())

    # ==================== SECTION 1: PROFIL BISNIS ====================
    story.append(Paragraph("1. PROFIL BISNIS NAKESMART", styles['h1']))
    story.append(Paragraph("1.1 Tentang Nakesmart", styles['h2']))
    story.append(Paragraph(
        "Nakesmart adalah Platform Ekosistem Kesehatan Digital Indonesia yang menghubungkan "
        "pasien dengan tenaga kesehatan (nakes), fasilitas kesehatan (faskes), dan event organizer "
        "kesehatan. Platform ini dioperasikan oleh PT GIANNA MEDICAL CENTER dengan domain "
        "resmi <b>nakesmart.com</b> dan beroperasi 24/7 untuk melayani masyarakat Indonesia.",
        styles['body']
    ))

    story.append(Paragraph("1.2 Jenis Layanan yang Dijual", styles['h2']))

    services_data = [
        ["Kategori Layanan", "Deskripsi", "Rentang Harga"],
        ["Telemedicine Reguler",
         "Konsultasi chat 30 menit dengan nakes terverifikasi",
         "Rp 45.000 - Rp 100.000"],
        ["Telemedicine Premium",
         "Konsultasi chat lengkap 45 menit (chat + voice + file)",
         "Rp 75.000 - Rp 200.000"],
        ["Telemedicine Exclusive",
         "Konsultasi video 15 menit via Zoom (partner Nakesmart)",
         "Rp 150.000 - Rp 500.000"],
        ["Booking Layanan Faskes",
         "Reservasi online layanan klinik / rumah sakit / lab",
         "Rp 50.000 - Rp 5.000.000"],
        ["Tiket Event Kesehatan",
         "Webinar, workshop, conference dari Event Organizer",
         "Rp 50.000 - Rp 5.000.000"],
        ["Top-up Wallet",
         "Pengisian saldo wallet untuk transaksi berikutnya",
         "Rp 10.000 - Rp 10.000.000"],
        ["Subscription Faskes",
         "Berlangganan SIMRS untuk fasilitas kesehatan",
         "Rp 499.000 - Rp 9.900.000 / bulan"],
        ["Voucher & Paket",
         "Voucher diskon, bundle layanan, paket MCU",
         "Rp 50.000 - Rp 2.500.000"],
    ]
    tbl = Table(services_data, colWidths=[4*cm, 8*cm, 5*cm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor(FOREST_GREEN)),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor(WHITE)),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 8.5),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('TEXTCOLOR', (0, 1), (-1, -1), HexColor(CHARCOAL)),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor(LIGHTGRAY)),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor(WHITE), HexColor(LIGHT_BG)]),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("1.3 Customer Segments", styles['h2']))
    for s in [
        "<b>Pasien (B2C)</b> - individu yang membutuhkan layanan kesehatan",
        "<b>Nakes (B2B)</b> - tenaga kesehatan yang berpraktik di Nakesmart",
        "<b>Faskes (B2B)</b> - klinik, rumah sakit, apotek, laboratorium",
        "<b>EO (B2B)</b> - event organizer untuk event kesehatan",
    ]:
        story.append(Paragraph("&bull;&nbsp;&nbsp;" + s, styles['bullet']))

    story.append(PageBreak())

    # ==================== SECTION 2: END-TO-END FLOW ====================
    story.append(Paragraph("2. END-TO-END CUSTOMER JOURNEY", styles['h1']))
    story.append(Paragraph(
        "Berikut adalah alur lengkap perjalanan customer dari saat mengakses website hingga "
        "menerima layanan, dengan tampilan layar pada setiap tahap. Contoh kasus: <b>Pasien "
        "membeli sesi Telemedicine Premium dengan dokter spesialis.</b>",
        styles['body']
    ))
    story.append(Spacer(1, 0.3*cm))

    # =========== STEP 1: Landing Page ===========
    add_step_header(story, styles, 1, "CUSTOMER MEMBUKA WEBSITE NAKESMART")
    story.append(Paragraph(
        "Customer membuka <b>nakesmart.com</b> di browser (desktop / mobile). Halaman landing "
        "menampilkan layanan utama: Cari Faskes, Telemedicine, Health Diary, AI Symptom Checker, "
        "dan Komunitas. Customer login menggunakan email/Google OAuth.",
        styles['body']
    ))
    mockup1 = MockupScreen(
        title="Landing Page",
        url="https://nakesmart.com",
        elements=[
            {'type': 'text', 'label': 'NAKESMART    Home   CPD Credits   Services   Health   Pricing   Community   About Us     [Sign In]  [Sign Up]'},
            {'type': 'divider'},
            {'type': 'header', 'label': 'Aplikasi Kesehatan Terintegrasi'},
            {'type': 'text', 'label': 'Pendidikan - Pengabdian - Pelayanan Kesehatan'},
            {'type': 'button', 'label': 'Cek Gejala AI Gratis    /    Konsul Dokter Online'},
            {'type': 'card', 'label': 'Layanan Utama|Telemedicine . Cek Gejala AI . MedPing Chat . Health Diary|SKP & Webinar . Sewa Zoom . Lowongan Kerja', 'h': 1.9*cm},
            {'type': 'text', 'label': 'Customer login via email / Google OAuth untuk mulai transaksi'},
        ],
    )
    story.append(screen_or_mockup('step1', mockup1))
    story.append(Paragraph("Tampilan halaman utama nakesmart.com (responsive untuk desktop & mobile)", styles['caption']))
    story.append(PageBreak())

    # =========== STEP 2: Pilih Layanan Telemedicine ===========
    add_step_header(story, styles, 2, "CUSTOMER MEMILIH LAYANAN TELEMEDICINE")
    story.append(Paragraph(
        "Customer menelusuri katalog telemedicine. Dapat memfilter berdasarkan spesialisasi "
        "(Dokter Umum, Anak, Penyakit Dalam, Kulit, dll), tier layanan (Reguler / Premium / "
        "Exclusive), rating, dan harga.",
        styles['body']
    ))
    mockup2 = MockupScreen(
        title="Katalog Telemedicine",
        url="nakesmart.com/telemedicine",
        elements=[
            {'type': 'text', 'label': 'Online Consultations with Verified Healthcare Workers (STR/diploma/SIP)'},
            {'type': 'text', 'label': 'Cari nama nakes...    [ Semua kategori nakes v ]    Maks. biaya (Rp)'},
            {'type': 'divider'},
            {'type': 'card', 'label': 'dr. Andini Pratama, Sp.PD  -  Umum  -  Rating 4.8|Konsultasi umum, follow-up, dan edukasi kesehatan|Chat . Rp 45.000     Voice . Rp 75.000     Video . Rp 150.000', 'h': 2.1*cm},
            {'type': 'text', 'label': 'Tier: Reguler/Chat 30 mnt Rp 45.000  .  Premium/Voice 15 mnt Rp 75.000  .  Exclusive/Video 15 mnt Rp 150.000'},
            {'type': 'button', 'label': 'View & Book'},
        ],
    )
    story.append(screen_or_mockup('step2', mockup2))
    story.append(Paragraph("Katalog telemedicine live: kartu nakes dengan 3 tier (Chat/Voice/Video) + tombol View & Book", styles['caption']))
    story.append(PageBreak())

    # =========== STEP 3: Pilih Jadwal & Add to Cart ===========
    add_step_header(story, styles, 3, "MEMILIH JADWAL & MASUK KE KERANJANG")
    story.append(Paragraph(
        "Customer memilih slot waktu yang tersedia. Setelah memilih jadwal, layanan otomatis "
        "masuk ke keranjang belanja. Customer dapat menambahkan layanan lain atau langsung "
        "checkout.",
        styles['body']
    ))
    mockup3 = MockupScreen(
        title="Pilih Jadwal & Keranjang",
        url="nakesmart.com/cart",
        elements=[
            {'type': 'header', 'label': 'Jadwal Konsultasi'},
            {'type': 'text', 'label': 'Tanggal: 12 Juni 2026'},
            {'type': 'text', 'label': 'Waktu  : 14:00 - 14:45 WIB'},
            {'type': 'divider'},
            {'type': 'header', 'label': 'Keranjang'},
            {'type': 'card', 'label': 'Telemedicine Premium|dr. Aulia, Sp.PD - 45 menit|Rp 75.000', 'h': 1.5*cm},
            {'type': 'divider'},
            {'type': 'text', 'label': 'Subtotal           : Rp 75.000'},
            {'type': 'text', 'label': 'Biaya Layanan      : Rp  2.500'},
            {'type': 'price', 'label': 'Total: Rp 77.500'},
            {'type': 'button', 'label': 'LANJUT KE CHECKOUT'},
        ],
    )
    story.append(screen_or_mockup('step3', mockup3))
    story.append(Paragraph("Sistem menghitung biaya layanan otomatis (PPN 0% untuk konsultasi kesehatan)", styles['caption']))
    story.append(PageBreak())

    # =========== STEP 4: Checkout - Pilih Metode Pembayaran ===========
    add_step_header(story, styles, 4, "CHECKOUT - PILIH METODE PEMBAYARAN MIDTRANS")
    story.append(Paragraph(
        "Pada halaman checkout, customer memilih metode pembayaran. Nakesmart mengintegrasikan "
        "<b>Midtrans Snap</b> sebagai payment gateway utama, yang menyediakan multiple opsi "
        "pembayaran dalam satu tampilan (Virtual Account, E-Wallet, QRIS, Kartu Kredit, dll).",
        styles['body']
    ))
    mockup4 = MockupScreen(
        title="Checkout",
        url="nakesmart.com/checkout",
        elements=[
            {'type': 'header', 'label': 'Pilih Metode Pembayaran'},
            {'type': 'midtrans_logo', 'label': 'Payment Gateway Resmi - 20+ metode pembayaran'},
            {'type': 'button_outline', 'label': 'Saldo Wallet (Rp 25.000)'},
            {'type': 'button_outline', 'label': 'Transfer Bank (Virtual Account)'},
            {'type': 'button_outline', 'label': 'GoPay / OVO / DANA / ShopeePay'},
            {'type': 'button_outline', 'label': 'QRIS'},
            {'type': 'button_outline', 'label': 'Kartu Kredit / Debit'},
            {'type': 'divider'},
            {'type': 'price', 'label': 'Total: Rp 77.500'},
            {'type': 'button', 'label': 'BAYAR SEKARANG'},
        ],
    )
    story.append(screen_or_mockup('step4', mockup4))
    story.append(Paragraph("Customer memilih metode pembayaran lewat Midtrans Snap (popup)", styles['caption']))
    story.append(PageBreak())

    # =========== STEP 5: Midtrans Snap Popup ===========
    add_step_header(story, styles, 5, "MIDTRANS SNAP - PROSES PEMBAYARAN")
    story.append(Paragraph(
        "Setelah klik 'BAYAR SEKARANG', sistem Nakesmart memanggil API <b>Midtrans Snap "
        "/snap/v1/transactions</b> untuk generate snap token. Popup Midtrans Snap muncul "
        "dengan UI resmi Midtrans, menampilkan semua opsi pembayaran. Customer memilih metode, "
        "lalu menyelesaikan pembayaran sesuai instruksi (transfer ke VA, scan QRIS, dll).",
        styles['body']
    ))
    mockup5 = MockupScreen(
        title="Midtrans Snap Popup",
        url="snap.midtrans.com/snap/v3/redirection/.../",
        elements=[
            {'type': 'midtrans_logo', 'label': 'Order ID: NM-TELEMED-1734598123'},
            {'type': 'text', 'label': 'PT GIANNA MEDICAL CENTER'},
            {'type': 'price', 'label': 'Rp 77.500'},
            {'type': 'divider'},
            {'type': 'header', 'label': 'Pilih Pembayaran'},
            {'type': 'button_outline', 'label': 'BCA Virtual Account'},
            {'type': 'button_outline', 'label': 'BNI Virtual Account'},
            {'type': 'button_outline', 'label': 'GoPay'},
            {'type': 'button_outline', 'label': 'QRIS - All E-Wallet'},
            {'type': 'button_outline', 'label': 'Kartu Kredit'},
            {'type': 'text', 'label': 'Powered by Midtrans (terdaftar di OJK)'},
        ],
    )
    story.append(screen_or_mockup('step5', mockup5))
    story.append(Paragraph("Popup Midtrans Snap - dikelola sepenuhnya oleh Midtrans (PCI-DSS compliant)", styles['caption']))
    story.append(PageBreak())

    # =========== STEP 6: Customer Bayar (contoh GoPay) ===========
    add_step_header(story, styles, 6, "CUSTOMER MENYELESAIKAN PEMBAYARAN")
    story.append(Paragraph(
        "Customer menyelesaikan pembayaran via metode yang dipilih. Contoh: GoPay - "
        "customer membuka aplikasi GoPay di HP, scan QR / konfirmasi push notification, "
        "lalu memasukkan PIN. Pembayaran diproses oleh Midtrans (real-time).",
        styles['body']
    ))
    mockup6 = MockupScreen(
        title="Konfirmasi GoPay (contoh)",
        url="gopay.co.id/pay",
        elements=[
            {'type': 'header', 'label': 'Konfirmasi Pembayaran'},
            {'type': 'text', 'label': 'Untuk: PT Gianna Medical Center'},
            {'type': 'text', 'label': 'Via: Midtrans Payment Gateway'},
            {'type': 'divider'},
            {'type': 'price', 'label': 'Rp 77.500'},
            {'type': 'text', 'label': 'Saldo GoPay tersedia: Rp 350.000'},
            {'type': 'divider'},
            {'type': 'text', 'label': 'Masukkan PIN GoPay Anda:'},
            {'type': 'text', 'label': '* * * * * *'},
            {'type': 'button', 'label': 'KONFIRMASI BAYAR'},
        ],
    )
    story.append(screen_or_mockup('step6', mockup6))
    story.append(Paragraph("Alternatif: Transfer ke Virtual Account, scan QRIS, atau input kartu kredit", styles['caption']))
    story.append(PageBreak())

    # =========== STEP 7: Webhook Midtrans ke Backend Nakesmart ===========
    add_step_header(story, styles, 7, "MIDTRANS MENGIRIM WEBHOOK NOTIFIKASI")
    story.append(Paragraph(
        "Setelah pembayaran sukses, server Midtrans mengirim <b>HTTP POST notification</b> ke "
        "webhook endpoint Nakesmart di <b>https://nakesmart.com/api/midtrans/notification</b>. "
        "Server Nakesmart memverifikasi:",
        styles['body']
    ))
    for v in [
        "Signature HMAC-SHA512 (signature_key) dari payload Midtrans untuk memastikan asli dari Midtrans",
        "Gross_amount cocok dengan grand_total order di database",
        "transaction_status = 'settlement' atau 'capture' dengan fraud_status = 'accept'",
        "Idempotency check - menolak notifikasi duplikat untuk order yang sudah 'paid'",
    ]:
        story.append(Paragraph("&bull;&nbsp;&nbsp;" + v, styles['bullet']))

    # Webhook flow diagram
    story.append(Spacer(1, 0.3*cm))
    flow_data = [
        ["CUSTOMER", "MIDTRANS", "NAKESMART BACKEND"],
        ["Konfirmasi PIN/OTP", "Process payment", "Wait for webhook"],
        ["", "POST webhook ke\nnakesmart.com/api/\nmidtrans/notification", "Verify HMAC signature\nValidate amount\nUpdate status -> paid"],
        ["", "HTTP 200 OK", "Trigger fulfillment\n(book konsultasi)"],
    ]
    tbl = Table(flow_data, colWidths=[5*cm, 5.5*cm, 6*cm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor(FOREST_GREEN)),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor(WHITE)),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor(LIGHTGRAY)),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(tbl)
    story.append(PageBreak())

    # =========== STEP 8: Konfirmasi Sukses ke Customer ===========
    add_step_header(story, styles, 8, "KONFIRMASI PEMBAYARAN SUKSES KE CUSTOMER")
    story.append(Paragraph(
        "Setelah backend Nakesmart memverifikasi pembayaran, customer otomatis di-redirect "
        "ke halaman sukses. Email konfirmasi dikirim ke alamat email customer. Konsultasi "
        "dengan dr. Aulia otomatis dijadwalkan untuk 12 Juni 2026 jam 14:00 WIB.",
        styles['body']
    ))
    mockup8 = MockupScreen(
        title="Pembayaran Sukses",
        url="nakesmart.com/payment/success",
        elements=[
            {'type': 'status_success', 'label': 'Order ID: NM-TELEMED-1734598123'},
            {'type': 'header', 'label': 'Detail Konsultasi'},
            {'type': 'text', 'label': 'Dokter : dr. Aulia Rahmawati, Sp.PD'},
            {'type': 'text', 'label': 'Tier   : Telemedicine Premium'},
            {'type': 'text', 'label': 'Jadwal : 12 Juni 2026, 14:00 WIB'},
            {'type': 'text', 'label': 'Durasi : 45 menit (Chat + Voice)'},
            {'type': 'divider'},
            {'type': 'price', 'label': 'Total Dibayar: Rp 77.500'},
            {'type': 'text', 'label': 'Metode: GoPay via Midtrans'},
            {'type': 'button', 'label': 'BUKA RUANG KONSULTASI'},
        ],
    )
    story.append(screen_or_mockup('step8', mockup8))
    story.append(Paragraph("Email + push notification dikirim, konsultasi siap dijadwalkan", styles['caption']))
    story.append(PageBreak())

    # =========== STEP 9: Customer Menerima Layanan ===========
    add_step_header(story, styles, 9, "CUSTOMER MENERIMA LAYANAN (FULFILLMENT)")
    story.append(Paragraph(
        "Pada jadwal yang ditentukan (12 Juni 2026 14:00 WIB), customer membuka ruang "
        "konsultasi. Konsultasi berlangsung 45 menit dengan format chat + voice note. "
        "Setelah selesai, dokter dapat menerbitkan <b>e-Resep digital</b> yang otomatis "
        "tersimpan di akun customer.",
        styles['body']
    ))
    mockup9 = MockupScreen(
        title="Ruang Konsultasi",
        url="nakesmart.com/telemedicine/session/...",
        elements=[
            {'type': 'header', 'label': 'Konsultasi dengan dr. Aulia'},
            {'type': 'text', 'label': 'Sisa waktu: 38 menit | Premium - Chat+Voice'},
            {'type': 'divider'},
            {'type': 'card', 'label': 'dr. Aulia: Selamat sore Bapak/Ibu|Apa yang dapat saya bantu?', 'h': 1.4*cm},
            {'type': 'card', 'label': 'Anda: Saya mengalami...|(deskripsi gejala)', 'h': 1.4*cm},
            {'type': 'card', 'label': 'dr. Aulia: Saya akan meresepkan...|Silakan cek tab E-Resep', 'h': 1.4*cm},
            {'type': 'divider'},
            {'type': 'button_outline', 'label': 'Lihat E-Resep'},
            {'type': 'button', 'label': 'SELESAIKAN SESI'},
        ],
    )
    story.append(screen_or_mockup('step9', mockup9))
    story.append(Paragraph("Setelah sesi selesai, dana di-release ke wallet dokter (escrow protection)", styles['caption']))
    story.append(PageBreak())

    # ==================== SECTION 3: TECHNICAL FLOW ====================
    story.append(Paragraph("3. TECHNICAL FLOW - INTEGRASI MIDTRANS", styles['h1']))
    story.append(Paragraph(
        "Berikut adalah arsitektur teknis integrasi Midtrans pada platform Nakesmart, "
        "dari sisi backend dan frontend.",
        styles['body']
    ))

    story.append(Paragraph("3.1 Arsitektur Tinggi", styles['h2']))
    arch_data = [
        ["Layer", "Komponen", "Fungsi"],
        ["Frontend", "Web App (React) + Mobile App (Expo)",
         "Trigger checkout, embed Snap.js, redirect ke status page"],
        ["Backend API", "FastAPI di nakesmart.com/api",
         "Generate snap token, handle webhook, update DB"],
        ["Database", "Supabase (PostgreSQL)",
         "Store orders, payments, escrow status"],
        ["Payment Gateway", "Midtrans Snap (snap.midtrans.com)",
         "Process payment dari customer, kirim webhook ke backend"],
        ["Notification", "Midtrans webhook -> Backend",
         "POST notification ke /api/midtrans/notification"],
    ]
    tbl = Table(arch_data, colWidths=[3.5*cm, 5*cm, 8.5*cm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor(FOREST_GREEN)),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor(WHITE)),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor(LIGHTGRAY)),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor(WHITE), HexColor(LIGHT_BG)]),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("3.2 Endpoint Webhook Midtrans di Nakesmart", styles['h2']))
    story.append(Paragraph(
        "<b>URL Notifikasi (Notification URL):</b> "
        "https://nakesmart.com/api/midtrans/notification",
        styles['body']
    ))
    story.append(Paragraph(
        "<b>Finish Redirect URL:</b> https://nakesmart.com/payment/success",
        styles['body']
    ))
    story.append(Paragraph(
        "<b>Unfinish URL:</b> https://nakesmart.com/payment/pending",
        styles['body']
    ))
    story.append(Paragraph(
        "<b>Error URL:</b> https://nakesmart.com/payment/failed",
        styles['body']
    ))

    story.append(Paragraph("3.3 Keamanan & Verifikasi", styles['h2']))
    for v in [
        "<b>HMAC-SHA512 Signature</b> - Setiap webhook diverifikasi signature_key sesuai dokumentasi Midtrans",
        "<b>Amount Validation</b> - gross_amount divalidasi sama dengan grand_total order",
        "<b>Idempotency</b> - Order yang sudah berstatus 'paid' tidak diproses ulang",
        "<b>HTTPS Only</b> - Semua komunikasi menggunakan TLS 1.2+",
        "<b>Anti-Replay</b> - Order ID unik, tidak bisa digunakan ulang",
        "<b>PCI-DSS Compliance</b> - Tidak ada data kartu kredit yang disimpan di server Nakesmart (semua handled oleh Midtrans)",
    ]:
        story.append(Paragraph("&bull;&nbsp;&nbsp;" + v, styles['bullet']))

    story.append(Paragraph("3.4 Refund Flow", styles['h2']))
    story.append(Paragraph(
        "Apabila customer cancel layanan atau dispute disetujui, Nakesmart memproses refund "
        "melalui salah satu jalur berikut: (1) Refund ke wallet internal customer untuk "
        "digunakan transaksi berikutnya, atau (2) Refund langsung ke rekening sumber pembayaran "
        "via Midtrans Refund API.",
        styles['body']
    ))

    story.append(PageBreak())

    # ==================== SECTION 4: ZOOM PARTNER ====================
    story.append(Paragraph("4. BUKTI INTEGRASI ZOOM PARTNER", styles['h1']))
    story.append(Paragraph(
        "Nakesmart adalah <b>partner resmi Zoom Video Communications, Inc.</b> melalui "
        "Zoom Marketplace App. Integrasi ini digunakan untuk layanan Telemedicine Tier "
        "Exclusive yang membutuhkan video konsultasi HD antara pasien dan nakes.",
        styles['body']
    ))

    story.append(Paragraph("4.1 Detail Integrasi", styles['h2']))
    zoom_data = [
        ["Item", "Detail"],
        ["Partner Type", "Zoom Marketplace - Server-to-Server OAuth App"],
        ["App Name", "Nakesmart Telemedicine Video"],
        ["Account ID", "[ZOOM_ACCOUNT_ID] (dikonfigurasi via env variable)"],
        ["Client ID", "[ZOOM_CLIENT_ID] (dikonfigurasi via env variable)"],
        ["Scopes",
         "meeting:write:admin, meeting:read:admin, recording:read:admin, user:read:admin"],
        ["Webhook URL", "https://nakesmart.com/api/zoom/webhook"],
        ["Use Case", "Auto-create video meeting untuk Telemedicine Tier Exclusive"],
        ["Pricing Tier", "Zoom Business / Pro (multi-host)"],
        ["Capacity", "500 meetings concurrent (upgradable)"],
        ["Recording", "Cloud recording enabled (with patient consent)"],
        ["Code Reference",
         "backend/services/zoom_api.py, backend/services/zoom_webinar_service.py"],
    ]
    tbl = Table(zoom_data, colWidths=[4*cm, 13*cm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor(FOREST_GREEN)),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor(WHITE)),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor(LIGHTGRAY)),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor(WHITE), HexColor(LIGHT_BG)]),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("4.2 Tampilan Video Meeting (Telemedicine Exclusive)", styles['h2']))
    mockup_zoom = MockupScreen(
        title="Video Konsultasi Zoom",
        url="nakesmart.com/telemedicine/zoom/...",
        elements=[
            {'type': 'header', 'label': 'Sesi Video Konsultasi'},
            {'type': 'text', 'label': 'Powered by Zoom Video SDK'},
            {'type': 'divider'},
            {'type': 'card', 'label': '[VIDEO FEED]|dr. Aulia Rahmawati, Sp.PD|HD Video aktif', 'h': 2.5*cm},
            {'type': 'card', 'label': '[VIDEO FEED ANDA]|Patient camera aktif|Mic: ON', 'h': 1.6*cm},
            {'type': 'divider'},
            {'type': 'button_outline', 'label': 'Mute Mic'},
            {'type': 'button_outline', 'label': 'Share Screen'},
            {'type': 'button', 'label': 'AKHIRI SESI'},
        ],
    )
    story.append(screen_or_mockup('zoom', mockup_zoom))
    story.append(Paragraph("Tampilan video meeting di Telemedicine Exclusive (powered by Zoom)", styles['caption']))

    story.append(PageBreak())

    story.append(Paragraph("4.3 Verifikasi Partnership Zoom", styles['h2']))
    story.append(Paragraph(
        "Untuk verifikasi keaslian integrasi, Midtrans dapat memeriksa hal berikut:",
        styles['body']
    ))
    for v in [
        "<b>Zoom Marketplace Listing</b> - https://marketplace.zoom.us (Search: 'Nakesmart Telemedicine')",
        "<b>Account Dashboard</b> - Login ke marketplace.zoom.us dengan akun terdaftar Nakesmart",
        "<b>App Type</b> - Server-to-Server OAuth (untuk auto-create meetings tanpa user login)",
        "<b>Verifikasi via API</b> - Endpoint Zoom https://api.zoom.us/v2/users/me dapat dipanggil dengan credentials Nakesmart",
        "<b>Recording Storage</b> - Recording tersimpan di Zoom Cloud (sesuai retention policy)",
        "<b>HIPAA-Style Compliance</b> - Nakesmart menggunakan Zoom dengan setting privacy untuk konsultasi kesehatan (waiting room, password meeting, encrypted recording)",
    ]:
        story.append(Paragraph("&bull;&nbsp;&nbsp;" + v, styles['bullet']))

    story.append(Spacer(1, 0.3*cm))
    note_table = Table([[
        Paragraph(
            "<b>CATATAN UNTUK MIDTRANS:</b> Kredensial Zoom (Account ID, Client ID, Client Secret) "
            "tidak dilampirkan di dokumen ini demi keamanan. Apabila diperlukan, Nakesmart dapat "
            "memberikan screenshot dashboard Zoom Marketplace yang menampilkan App yang telah "
            "terinstal, melalui channel komunikasi yang aman (email terenkripsi atau in-person).",
            styles['note_box']
        )
    ]], colWidths=[17*cm])
    note_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor("#FEF3C7")),
        ('BOX', (0, 0), (-1, -1), 1, HexColor("#F59E0B")),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(note_table)
    story.append(PageBreak())

    # ==================== SECTION 5: COMPLIANCE & LEGAL ====================
    story.append(Paragraph("5. KEPATUHAN & LEGAL", styles['h1']))

    story.append(Paragraph("5.1 Pengembalian Dana (Refund Policy)", styles['h2']))
    story.append(Paragraph(
        "Nakesmart memiliki kebijakan pengembalian dana yang transparan dan terdokumentasi di "
        "<b>nakesmart.com/refund-policy</b>. Skenario refund yang umum:",
        styles['body']
    ))
    for v in [
        "<b>Nakes tidak hadir</b> - Refund 100% otomatis ke wallet (sistem auto-detect setelah 30 menit)",
        "<b>Customer cancel H-7</b> - Refund 100%",
        "<b>Customer cancel H-3 sampai H-1</b> - Refund 50%",
        "<b>Customer cancel < 3 jam</b> - Tidak ada refund",
        "<b>Dispute disetujui admin</b> - Refund 100% via Midtrans Refund API",
        "<b>Customer Service ticket</b> - Customer dapat mengajukan komplain via tab Bantuan",
    ]:
        story.append(Paragraph("&bull;&nbsp;&nbsp;" + v, styles['bullet']))

    story.append(Paragraph("5.2 Penyelesaian Sengketa (Dispute Resolution)", styles['h2']))
    story.append(Paragraph(
        "Customer yang ingin mengajukan komplain dapat menghubungi: "
        "(1) Customer Service via in-app chat (24/7), "
        "(2) Email: support@nakesmart.com (response < 24 jam), "
        "(3) WhatsApp business: +62 851-xxxx-xxxx. "
        "Admin Nakesmart memiliki kewenangan untuk approve refund maksimal Rp 5.000.000 per ticket. "
        "Apabila tidak ada penyelesaian, customer dapat mengeskalasi ke YLKI atau OJK.",
        styles['body']
    ))

    story.append(Paragraph("5.3 Data Privacy (UU PDP)", styles['h2']))
    story.append(Paragraph(
        "Nakesmart patuh pada UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP). "
        "Data customer (termasuk data kesehatan yang sensitif) disimpan di server Indonesia "
        "(Supabase ap-southeast region), dienkripsi at-rest dan in-transit. Detail privacy "
        "policy: nakesmart.com/privacy-policy.",
        styles['body']
    ))

    story.append(Paragraph("5.4 Kategori Bisnis (MCC)", styles['h2']))
    story.append(Paragraph(
        "<b>Merchant Category Code:</b> 8099 (Health Services - Other), 8062 (Hospitals), "
        "5912 (Drug Stores & Pharmacies). Nakesmart bertransaksi sebagai marketplace healthcare "
        "yang menghubungkan pasien, nakes, faskes, dan event organizer.",
        styles['body']
    ))

    story.append(PageBreak())

    # ==================== SECTION 6: SUMMARY & CONTACT ====================
    story.append(Paragraph("6. RINGKASAN & KONTAK", styles['h1']))

    story.append(Paragraph("6.1 Ringkasan Customer Journey", styles['h2']))
    summary_data = [
        ["Step", "Aksi", "Sistem", "Waktu"],
        ["1", "Buka nakesmart.com", "Web Nakesmart", "< 5 detik"],
        ["2", "Pilih layanan (telemedicine)", "Web Nakesmart", "1-3 menit"],
        ["3", "Pilih jadwal & add to cart", "Web Nakesmart", "< 1 menit"],
        ["4", "Checkout & pilih metode bayar", "Web + Midtrans", "< 1 menit"],
        ["5", "Buka Midtrans Snap popup", "Midtrans", "< 5 detik"],
        ["6", "Customer bayar via GoPay/VA/QRIS", "Midtrans + Bank/E-Wallet", "1-10 menit"],
        ["7", "Webhook Midtrans -> Backend Nakesmart", "Server-to-Server", "< 5 detik"],
        ["8", "Konfirmasi sukses ke customer", "Email + Push + Web", "Instant"],
        ["9", "Konsultasi pada jadwal yang dipesan", "Web/Mobile + Zoom (jika Exclusive)", "15-45 menit"],
    ]
    tbl = Table(summary_data, colWidths=[1.2*cm, 6.5*cm, 5.3*cm, 4*cm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor(FOREST_GREEN)),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor(WHITE)),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8.5),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor(LIGHTGRAY)),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor(WHITE), HexColor(LIGHT_BG)]),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("6.2 Kontak PIC Nakesmart untuk Midtrans", styles['h2']))
    for v in [
        "<b>PT GIANNA MEDICAL CENTER</b>",
        "<b>Domain Resmi:</b> nakesmart.com",
        "<b>Email Sales/Billing:</b> finance@nakesmart.com",
        "<b>Email Teknis/Integrasi:</b> tech@nakesmart.com",
        "<b>Customer Service:</b> support@nakesmart.com",
        "<b>WhatsApp Business:</b> +62 851-xxxx-xxxx",
        "<b>Alamat Kantor:</b> Jakarta, Indonesia",
    ]:
        story.append(Paragraph("&bull;&nbsp;&nbsp;" + v, styles['bullet']))

    story.append(Spacer(1, 0.5*cm))
    sign_table = Table([[
        Paragraph(
            "<b>Demikian dokumen end-to-end customer journey dan bukti integrasi Zoom partner "
            "Nakesmart kami sampaikan untuk keperluan onboarding Midtrans Production.</b><br/><br/>"
            "Apabila diperlukan dokumen pendukung tambahan (NIB, NPWP, akta pendirian, "
            "screenshot dashboard Zoom Marketplace, atau testing transaksi di sandbox), "
            "silakan menghubungi PIC kami via email tech@nakesmart.com.",
            styles['note_box']
        )
    ]], colWidths=[17*cm])
    sign_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor(LIGHT_BG)),
        ('BOX', (0, 0), (-1, -1), 1, HexColor(FOREST_GREEN)),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(sign_table)

    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(
        f"Jakarta, {YEAR}<br/><br/>"
        f"<b>{COMPANY}</b><br/>"
        f"{WEBSITE}",
        ParagraphStyle('sign', parent=styles['body'], alignment=TA_LEFT, fontSize=11)
    ))

    # ==================== BUILD ====================
    def canvas_maker(*args, **kwargs):
        return FooterCanvas(*args, **kwargs)

    doc.build(story, canvasmaker=canvas_maker)
    print(f"\n[OK] Dokumen Midtrans dibuat: {out_path}")
    print(f"     Ukuran: {out_path.stat().st_size // 1024} KB")


class FooterCanvas(pdfcanvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for idx, state in enumerate(self._saved_page_states, 1):
            self.__dict__.update(state)
            self.draw_footer(idx, num_pages)
            super().showPage()
        super().save()

    def draw_footer(self, page_num, total):
        if page_num == 1:
            return
        self.setFont("Helvetica", 8)
        self.setFillColor(HexColor(CHARCOAL))
        self.drawCentredString(
            A4[0] / 2, 1.0 * cm,
            f"Halaman {page_num} / {total}  -  © {YEAR} {COMPANY}  -  Dokumen Midtrans"
        )


if __name__ == '__main__':
    build_doc()
