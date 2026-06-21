# -*- coding: utf-8 -*-
"""Render CHECKLIST_Screenshot_Midtrans.md -> CHECKLIST_Screenshot_Midtrans.pdf
Renderer markdown ringan (header / checkbox / bullet / quote / hr / bold / code).
"""
import re
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
                                Table, TableStyle)

HERE = Path(__file__).parent
SRC = HERE / "CHECKLIST_Screenshot_Midtrans.md"
OUT = HERE / "CHECKLIST_Screenshot_Midtrans.pdf"

BLUE = colors.HexColor("#1565C0")
DARK = colors.HexColor("#1A2530")
GREY = colors.HexColor("#5A6B7B")
LBOX = colors.HexColor("#EEF3F8")

# map karakter non-latin1 -> ascii agar Helvetica tak render kotak
_MAP = {"×": "x", "→": "->", "—": "-", "–": "-",
        "‘": "'", "’": "'", "“": '"', "”": '"',
        "•": "-", "…": "...", " ": " "}


def sanitize(t: str) -> str:
    for k, v in _MAP.items():
        t = t.replace(k, v)
    # buang sisa codepoint tinggi (emoji dll)
    return "".join(ch if ord(ch) < 0x250 else "" for ch in t)


def inline(t: str) -> str:
    t = sanitize(t)
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"`(.+?)`", r'<font face="Courier" size="8.5">\1</font>', t)
    return t


def build():
    ss = getSampleStyleSheet()
    h1 = ParagraphStyle("h1", parent=ss["Title"], fontSize=17, textColor=BLUE,
                        spaceAfter=4, leading=21)
    h2 = ParagraphStyle("h2", parent=ss["Heading2"], fontSize=12.5, textColor=DARK,
                        spaceBefore=10, spaceAfter=4, leading=15)
    body = ParagraphStyle("body", parent=ss["BodyText"], fontSize=9.5, textColor=DARK,
                          leading=13, spaceAfter=2)
    sub = ParagraphStyle("sub", parent=body, fontSize=8.7, textColor=GREY,
                         leftIndent=16, leading=11.5)
    quote = ParagraphStyle("quote", parent=body, fontSize=8.7, textColor=BLUE,
                           leftIndent=10, leading=12, fontName="Helvetica-Oblique")
    chk = ParagraphStyle("chk", parent=body, fontSize=9.8, textColor=DARK,
                         leading=13, spaceBefore=4)

    lines = SRC.read_text(encoding="utf-8").splitlines()
    story = []
    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        indented = len(line) - len(line.lstrip())

        if not stripped:
            story.append(Spacer(1, 3))
        elif stripped == "---":
            story.append(Spacer(1, 2))
            story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#C9D6E2")))
            story.append(Spacer(1, 2))
        elif stripped.startswith("# "):
            story.append(Paragraph(inline(stripped[2:]), h1))
            story.append(HRFlowable(width="100%", thickness=1.4, color=BLUE, spaceAfter=6))
        elif stripped.startswith("## "):
            story.append(Paragraph(inline(stripped[3:]), h2))
        elif re.match(r"- \[[ xX]\] ", stripped):
            txt = stripped[5:].lstrip()  # buang "- [ ] "
            box = "[v]" if stripped[3] in "xX" else "[  ]"
            story.append(Paragraph(f'<font face="Courier"><b>{box}</b></font>  {inline(txt)}', chk))
        elif stripped.startswith("- "):
            story.append(Paragraph("&bull;  " + inline(stripped[2:]), body))
        elif stripped.startswith("> "):
            story.append(Paragraph(inline(stripped[2:]), quote))
        elif indented >= 2:
            story.append(Paragraph(inline(stripped), sub))
        else:
            story.append(Paragraph(inline(stripped), body))

    doc = SimpleDocTemplate(str(OUT), pagesize=A4,
                            leftMargin=1.8*cm, rightMargin=1.8*cm,
                            topMargin=1.6*cm, bottomMargin=1.6*cm,
                            title="Checklist Screenshot Midtrans - PT GIANNA MEDICAL CENTER")
    doc.build(story)
    print(f"[OK] {OUT}  ({OUT.stat().st_size//1024} KB)")


if __name__ == "__main__":
    build()
