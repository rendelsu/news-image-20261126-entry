#!/usr/bin/env python3
"""Render the 26 November 2026 world-news newspaper image (1024x1024 PNG).

Local build step only: the shipped program (main.ts) is stdlib-only and just
copies the committed entry.png to the output directory.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 234)
INK = (24, 24, 24)
RED = (178, 24, 24)
BLUE = (24, 66, 128)
TEAL = (12, 110, 110)
PURPLE = (88, 44, 128)
GREEN = (28, 110, 52)
ORANGE = (196, 96, 10)
GREY = (70, 70, 70)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def center(draw, cx, y, text, fnt, fill):
    draw.text((cx, y), text, font=fnt, fill=fill, anchor="ma")


def fit(draw, text, path, size, max_w):
    fnt = font(path, size)
    while draw.textlength(text, font=fnt) > max_w and size > 10:
        size -= 2
        fnt = font(path, size)
    return fnt


def panel(draw, x, y, w, h, color, kicker, headline_lines, body_lines, icon):
    draw.rectangle([x, y, x + w, y + h], outline=INK, width=3, fill=(255, 255, 255))
    draw.rectangle([x, y, x + w, y + 34], fill=color)
    draw.text((x + 14, y + 5), kicker, font=font(SANS_B, 22), fill=(255, 255, 255))
    ty = y + 48
    for line in headline_lines:
        fnt = fit(draw, line, SERIF_B, 40, w - 28)
        draw.text((x + 14, ty), line, font=fnt, fill=INK)
        ty += 46
    ty += 2
    for line in body_lines:
        fnt = fit(draw, line, SANS, 25, w - 124)
        draw.text((x + 14, ty), line, font=fnt, fill=GREY)
        ty += 32
    icon(draw, x + w - 92, y + h - 84, color)


def icon_ship(d, x, y, c):
    d.rectangle([x + 6, y + 44, x + 74, y + 58], fill=c)
    d.polygon([(x + 6, y + 44), (x + 74, y + 44), (x + 66, y + 58), (x + 14, y + 58)], fill=c)
    for i, col in enumerate([RED, BLUE, ORANGE]):
        d.rectangle([x + 10 + i * 20, y + 26, x + 28 + i * 20, y + 43], fill=col)
    d.rectangle([x + 62, y + 14, x + 72, y + 26], fill=c)


def icon_drone(d, x, y, c):
    d.ellipse([x + 28, y + 26, x + 52, y + 44], fill=c)
    for dx, dy in [(8, 10), (62, 10), (8, 52), (62, 52)]:
        d.ellipse([x + dx, y + dy, x + dx + 16, y + dy + 8], outline=c, width=3)
        d.line([x + 40, y + 35, x + dx + 8, y + dy + 4], fill=c, width=3)


def icon_tanker(d, x, y, c):
    d.polygon([(x + 2, y + 46), (x + 78, y + 46), (x + 70, y + 60), (x + 10, y + 60)], fill=c)
    d.rectangle([x + 14, y + 36, x + 58, y + 46], fill=c)
    d.rectangle([x + 58, y + 24, x + 70, y + 46], fill=c)
    d.line([x + 4, y + 66, x + 76, y + 66], fill=BLUE, width=3)


def icon_satellite(d, x, y, c):
    d.rectangle([x + 32, y + 26, x + 48, y + 44], fill=c)
    d.rectangle([x + 2, y + 28, x + 30, y + 42], fill=BLUE)
    d.rectangle([x + 50, y + 28, x + 78, y + 42], fill=BLUE)
    d.line([x + 40, y + 44, x + 40, y + 56], fill=c, width=3)
    d.arc([x + 26, y + 50, x + 54, y + 70], 20, 160, fill=c, width=3)


def icon_flask(d, x, y, c):
    d.polygon([(x + 34, y + 8), (x + 46, y + 8), (x + 46, y + 28), (x + 64, y + 62),
               (x + 16, y + 62), (x + 34, y + 28)], outline=c, width=4)
    d.polygon([(x + 26, y + 48), (x + 54, y + 48), (x + 60, y + 60), (x + 20, y + 60)], fill=c)
    d.ellipse([x + 36, y + 36, x + 42, y + 42], fill=c)


def icon_balloon(d, x, y, c):
    d.ellipse([x + 14, y + 4, x + 66, y + 48], fill=c)
    d.line([x + 24, y + 44, x + 36, y + 60], fill=INK, width=2)
    d.line([x + 56, y + 44, x + 44, y + 60], fill=INK, width=2)
    d.rectangle([x + 34, y + 60, x + 46, y + 68], fill=INK)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([10, 10, W - 10, H - 10], outline=INK, width=4)

    # Masthead
    center(d, W // 2, 24, "THE WORLD TODAY", font(SERIF_B, 64), INK)
    d.rectangle([30, 104, W - 30, 152], fill=INK)
    center(d, W // 2, 112, "THURSDAY 26 NOVEMBER 2026", font(SANS_B, 32), (255, 255, 255))

    # Lead story
    lx, ly, lw, lh = 30, 168, W - 60, 262
    d.rectangle([lx, ly, lx + lw, ly + lh], outline=INK, width=3, fill=(255, 255, 255))
    d.rectangle([lx, ly, lx + lw, ly + 40], fill=RED)
    d.text((lx + 16, ly + 7), "LEAD STORY  ·  EGYPT", font=font(SANS_B, 25), fill=(255, 255, 255))
    d.text((lx + 16, ly + 56), "CAIRO TANKER FIRE", font=fit(d, "CAIRO TANKER FIRE", SERIF_B, 72, 620), fill=INK)
    d.text((lx + 16, ly + 136), "31 DEAD, 21 HURT", font=font(SERIF_B, 56), fill=RED)
    d.text((lx + 16, ly + 196), "Fuel tanker overturns on the Ring Road;", font=font(SANS, 27), fill=GREY)
    d.text((lx + 16, ly + 226), "blaze kills at least 31.", font=font(SANS, 27), fill=GREY)
    # Tanker + flame illustration
    ix, iy = lx + lw - 250, ly + 70
    d.polygon([(ix, iy + 120), (ix + 220, iy + 120), (ix + 200, iy + 152), (ix + 20, iy + 152)], fill=INK)
    d.rectangle([ix + 30, iy + 84, ix + 150, iy + 120], fill=RED)
    d.rectangle([ix + 160, iy + 66, ix + 196, iy + 120], fill=BLUE)
    d.polygon([(ix + 90, iy + 6), (ix + 122, iy + 66), (ix + 58, iy + 66)], fill=RED)
    d.polygon([(ix + 90, iy + 24), (ix + 112, iy + 66), (ix + 68, iy + 66)], fill=ORANGE)
    d.polygon([(ix + 90, iy + 42), (ix + 104, iy + 66), (ix + 76, iy + 66)], fill=(250, 200, 40))

    # Six panels, 2 columns x 3 rows
    px, py, pw, ph, gap = 30, 446, (W - 60 - 16) // 2, 176, 16
    panels = [
        (BLUE, "TRADE", ["US TARIFFS ON 14"],
         ["Proposed — not yet in effect.", "China · EU · Japan · India"], icon_ship),
        (PURPLE, "UKRAINE", ["KYIV: AIRFIELD HIT"],
         ["5 warplanes damaged, Kyiv says.", "2 Samara refineries struck."], icon_drone),
        (TEAL, "HORMUZ", ["HORMUZ ON EDGE"],
         ["Iran claims mines hit tankers.", "Houthis threaten Saudi ports."], icon_tanker),
        (BLUE, "SPACE", ["1M SATELLITES OK'D"],
         ["FCC clears SpaceX Starmind.", "Authorized — not launched."], icon_satellite),
        (GREEN, "NIGERIA", ["METH LAB SEIZED"],
         ["1,512 kg · about $227M.", "5 suspects arrested."], icon_flask),
        (ORANGE, "NEW YORK", ["PARADE POSTPONED"],
         ["Macy's parade: Thu → Sat.", "Storm forces first delay."], icon_balloon),
    ]
    for i, (color, kicker, head, body, icon) in enumerate(panels):
        col, row = i % 2, i // 2
        panel(d, px + col * (pw + gap), py + row * (ph + gap), pw, ph,
              color, kicker, head, body, icon)

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
