"""
F1 2026 Graphics Module -- Generates diagrams and infographics as PNG BytesIO.
Uses Pillow for simple block graphics and matplotlib for charts.
"""

from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

# Try to get a reasonable font; fall back to default
def _get_font(size=14, bold=False):
    """Get a TrueType font, falling back to default if needed."""
    names = ["arialbd.ttf", "arial.ttf", "Arial Bold.ttf", "Arial.ttf",
             "DejaVuSans-Bold.ttf", "DejaVuSans.ttf"]
    if bold:
        names = [n for n in names if "bd" in n.lower() or "bold" in n.lower()] + names
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


# ── A. Weekend Format: Session Timeline ──────────────────────────────────────

def weekend_timeline():
    """Two horizontal timelines (Standard vs Sprint), color-coded blocks."""
    W, H = 1400, 500
    img = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    font_title = _get_font(22, bold=True)
    font_label = _get_font(16, bold=True)
    font_small = _get_font(13)

    # Colors
    GRAY = (160, 160, 160)
    BLUE = (0, 100, 220)
    RED = (225, 6, 0)
    ORANGE = (255, 140, 0)
    DARK = (30, 30, 40)
    LIGHT_BG = (245, 245, 248)

    # Title
    draw.text((W // 2, 20), "Race Weekend Formats", fill=DARK, font=font_title, anchor="mt")

    # Legend
    legend_y = 55
    legend_items = [("Practice", GRAY), ("Qualifying", BLUE), ("Race", RED), ("Sprint", ORANGE)]
    lx = 350
    for label, color in legend_items:
        draw.rectangle([lx, legend_y, lx + 20, legend_y + 16], fill=color)
        draw.text((lx + 26, legend_y - 1), label, fill=DARK, font=font_small)
        lx += 130

    def draw_timeline(y_top, title, days):
        draw.text((30, y_top), title, fill=DARK, font=font_label)
        bar_y = y_top + 30
        bar_h = 50
        x = 100
        total_w = W - 140

        # Draw background
        draw.rectangle([x, bar_y, x + total_w, bar_y + bar_h], fill=LIGHT_BG, outline=(200, 200, 200))

        # Calculate block widths proportionally
        all_sessions = []
        for day_name, sessions in days:
            for s in sessions:
                all_sessions.append((day_name, s))
        n = len(all_sessions)
        block_w = total_w / n
        bx = x

        prev_day = None
        for day_name, (session_name, color) in all_sessions:
            # Day divider
            if day_name != prev_day:
                if prev_day is not None:
                    draw.line([(bx, bar_y - 5), (bx, bar_y + bar_h + 5)], fill=DARK, width=2)
                draw.text((bx + block_w * 0.3, bar_y - 18), day_name, fill=DARK, font=font_small)
                prev_day = day_name

            # Session block
            draw.rectangle([bx + 2, bar_y + 2, bx + block_w - 2, bar_y + bar_h - 2], fill=color)
            # Session label
            draw.text((bx + block_w / 2, bar_y + bar_h / 2), session_name,
                       fill=(255, 255, 255), font=font_small, anchor="mm")
            bx += block_w

    # Standard weekend
    standard_days = [
        ("FRIDAY", [("FP1", GRAY), ("FP2", GRAY)]),
        ("SATURDAY", [("FP3", GRAY), ("Qualifying", BLUE)]),
        ("SUNDAY", [("Grand Prix", RED)]),
    ]
    draw_timeline(100, "Standard Weekend", standard_days)

    # Sprint weekend
    sprint_days = [
        ("FRIDAY", [("FP1", GRAY), ("Sprint Quali", BLUE)]),
        ("SATURDAY", [("Sprint", ORANGE), ("Qualifying", BLUE)]),
        ("SUNDAY", [("Grand Prix", RED)]),
    ]
    draw_timeline(290, "Sprint Weekend", sprint_days)

    buf = BytesIO()
    img.save(buf, format="PNG", dpi=(200, 200))
    buf.seek(0)
    return buf


# ── B. Regulations: Power Unit Split Donut Charts ────────────────────────────

def power_unit_split():
    """Side-by-side donut charts: 2025 (~80/20) vs 2026 (~50/50)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))

    colors = ["#444444", "#E10600"]
    labels_2025 = ["ICE (~80%)", "Electric (~20%)"]
    sizes_2025 = [80, 20]
    labels_2026 = ["ICE (~50%)", "Electric (~50%)"]
    sizes_2026 = [50, 50]

    for ax, sizes, labels, year in [
        (ax1, sizes_2025, labels_2025, "2025 Power Split"),
        (ax2, sizes_2026, labels_2026, "2026 Power Split"),
    ]:
        wedges, texts, autotexts = ax.pie(
            sizes, labels=labels, colors=colors, autopct="%1.0f%%",
            startangle=90, pctdistance=0.75,
            wedgeprops=dict(width=0.4, edgecolor="white"),
            textprops=dict(fontsize=11),
        )
        for at in autotexts:
            at.set_color("white")
            at.set_fontweight("bold")
            at.set_fontsize(13)
        ax.set_title(year, fontsize=14, fontweight="bold", pad=12)

    fig.suptitle("Power Unit Energy Distribution", fontsize=16, fontweight="bold", y=1.0)
    plt.tight_layout()

    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    buf.seek(0)
    return buf


# ── C. Strategy 101: Tire Degradation Chart ──────────────────────────────────

def tire_degradation_chart():
    """Line chart: lap time vs laps for three compounds."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots(figsize=(9, 5))

    laps = np.arange(1, 36)

    # Soft: fast start, steep degradation, cliff at ~lap 18
    soft_base = 91.0 + 0.12 * laps
    cliff_offset = np.maximum(laps - 18, 0).astype(float)
    soft_cliff = 0.4 * cliff_offset ** 1.3
    soft = soft_base + soft_cliff

    # Medium: moderate
    medium = 91.8 + 0.065 * laps

    # Hard: slow start, gentle
    hard = 92.6 + 0.04 * laps

    ax.plot(laps, soft, color="#E10600", linewidth=2.5, label="Soft")
    ax.plot(laps, medium, color="#D4C800", linewidth=2.5, label="Medium")
    ax.plot(laps, hard, color="#888888", linewidth=2.5, label="Hard")

    # Annotate cliff
    cliff_lap = 18
    ax.annotate("Tire 'cliff'", xy=(cliff_lap, soft[cliff_lap - 1]),
                xytext=(cliff_lap + 4, soft[cliff_lap - 1] + 2),
                arrowprops=dict(arrowstyle="->", color="#E10600", lw=1.5),
                fontsize=11, color="#E10600", fontweight="bold")

    ax.set_xlabel("Lap Number", fontsize=12)
    ax.set_ylabel("Lap Time (seconds)", fontsize=12)
    ax.set_title("Tire Degradation by Compound", fontsize=14, fontweight="bold")
    ax.legend(fontsize=11, loc="upper left")
    ax.grid(True, alpha=0.3)
    ax.invert_yaxis()  # faster times (lower) at top
    # Actually, convention is higher = slower, so DON'T invert for this chart
    # Let's keep normal orientation (slower laps = higher on y-axis = bad)
    ax.invert_yaxis()  # undo - we want slower at top (which is default)
    # Actually let me just not invert. Y-axis: higher = slower, which is natural.
    # Let me just remove both inversions - matplotlib default has higher values at top
    # which means slower laps at top = correct.

    plt.tight_layout()
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    buf.seek(0)
    return buf


# ── D. Strategy 101: Undercut Diagram ────────────────────────────────────────

def undercut_diagram():
    """Position-vs-lap chart showing undercut mechanics."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots(figsize=(9, 4.5))

    laps = np.arange(1, 30)

    # Driver A (undercuts): pits on lap 12, emerges ahead
    gap_a = np.zeros_like(laps, dtype=float)
    for i, lap in enumerate(laps):
        if lap <= 12:
            gap_a[i] = 2.0 - 0.05 * lap  # gradually closing
        elif lap == 13:
            gap_a[i] = -20.0  # in pits (big drop)
        elif lap <= 15:
            gap_a[i] = -20.0 + 10.5 * (lap - 13)  # recovering
        else:
            gap_a[i] = -0.5 - 0.08 * (lap - 15)  # now ahead (negative = ahead)

    # Driver B (overcut victim): pits on lap 15
    gap_b = np.zeros_like(laps, dtype=float)
    for i, lap in enumerate(laps):
        if lap <= 15:
            gap_b[i] = 0.0  # reference driver
        elif lap == 16:
            gap_b[i] = -21.0  # in pits
        elif lap <= 18:
            gap_b[i] = -21.0 + 10.0 * (lap - 16)
        else:
            gap_b[i] = 1.0 + 0.05 * (lap - 18)  # now behind

    ax.plot(laps, gap_a, color="#E10600", linewidth=2.5, label="Driver A (pits Lap 12)")
    ax.plot(laps, gap_b, color="#0064C8", linewidth=2.5, label="Driver B (pits Lap 15)")

    # Pit window shading
    ax.axvspan(12, 15, alpha=0.1, color="orange", label="Pit window")
    ax.axvline(x=12, color="#E10600", linestyle="--", alpha=0.5, linewidth=1)
    ax.axvline(x=15, color="#0064C8", linestyle="--", alpha=0.5, linewidth=1)

    # Annotations
    ax.annotate("A pits (fresh tires)", xy=(12, gap_a[11]),
                xytext=(5, -15), fontsize=10, color="#E10600",
                arrowprops=dict(arrowstyle="->", color="#E10600"))
    ax.annotate("B pits (too late)", xy=(15, gap_b[15]),
                xytext=(18, -15), fontsize=10, color="#0064C8",
                arrowprops=dict(arrowstyle="->", color="#0064C8"))
    ax.annotate("A emerges AHEAD", xy=(17, gap_a[16]),
                xytext=(20, gap_a[16] - 5), fontsize=10, color="#E10600", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#E10600"))

    ax.set_xlabel("Lap", fontsize=12)
    ax.set_ylabel("Gap to Virtual Reference (s)", fontsize=12)
    ax.set_title("The Undercut: How Pitting Early Gains Position", fontsize=14, fontweight="bold")
    ax.legend(fontsize=10, loc="lower left")
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-25, 10)

    plt.tight_layout()
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    buf.seek(0)
    return buf


# ── F. Race Schedule: Season Timeline Bar ────────────────────────────────────

def season_timeline():
    """Horizontal bar Mar-Dec with race blocks, sprints highlighted."""
    W, H = 1400, 280
    img = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    font_title = _get_font(20, bold=True)
    font_label = _get_font(12, bold=True)
    font_tiny = _get_font(10)

    DARK = (30, 30, 40)
    RED = (225, 6, 0)
    DGRAY = (80, 80, 90)
    LIGHT_BG = (245, 245, 248)
    BREAK_COLOR = (200, 200, 210)

    draw.text((W // 2, 15), "2026 Season at a Glance", fill=DARK, font=font_title, anchor="mt")

    # Month markers
    months = ["MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    bar_x = 60
    bar_w = W - 120
    bar_y = 70
    bar_h = 40

    draw.rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h], fill=LIGHT_BG, outline=(200, 200, 200))

    month_w = bar_w / len(months)
    for i, m in enumerate(months):
        mx = bar_x + i * month_w
        draw.text((mx + month_w / 2, bar_y - 12), m, fill=DARK, font=font_label, anchor="mm")
        if i > 0:
            draw.line([(mx, bar_y), (mx, bar_y + bar_h)], fill=(210, 210, 210), width=1)

    # Race blocks (approximate positions within months, 0=Mar start, 9=Dec end)
    races = [
        (0.0, "AUS", False), (0.2, "CHN", True), (0.6, "JPN", False),
        (1.3, "BHR", False), (1.5, "SAU", False),
        (2.0, "MIA", True), (2.7, "CAN", True),
        (3.0, "MON", False), (3.2, "ESP", False), (3.6, "AUT", False),
        (4.0, "GBR", True), (4.5, "BEL", False), (4.7, "HUN", False),
        # Summer break ~5.0-5.5
        (5.6, "NED", True),
        (6.0, "ITA", False), (6.2, "MAD", False), (6.6, "AZE", False),
        (7.3, "SIN", True), (7.7, "USA", False),
        (8.0, "MEX", False), (8.2, "BRA", False),
        (8.7, "LAS", False), (8.9, "QAT", False),
        (9.2, "ABU", False),
    ]

    # Summer break
    break_start = bar_x + (5.0 / 10) * bar_w
    break_end = bar_x + (5.5 / 10) * bar_w
    draw.rectangle([break_start, bar_y + 2, break_end, bar_y + bar_h - 2], fill=BREAK_COLOR)
    draw.text(((break_start + break_end) / 2, bar_y + bar_h / 2), "BREAK",
              fill=DARK, font=font_tiny, anchor="mm")

    block_w = bar_w / 50  # narrow blocks
    for pos, code, is_sprint in races:
        rx = bar_x + (pos / 10) * bar_w
        color = RED if is_sprint else DGRAY
        draw.rectangle([rx, bar_y + 3, rx + block_w, bar_y + bar_h - 3], fill=color)
        # Code below
        draw.text((rx + block_w / 2, bar_y + bar_h + 8), code, fill=DARK,
                  font=font_tiny, anchor="mt")

    # Legend
    ly = bar_y + bar_h + 35
    draw.rectangle([bar_x, ly, bar_x + 16, ly + 12], fill=DGRAY)
    draw.text((bar_x + 22, ly - 1), "Standard", fill=DARK, font=font_tiny)
    draw.rectangle([bar_x + 100, ly, bar_x + 116, ly + 12], fill=RED)
    draw.text((bar_x + 122, ly - 1), "Sprint", fill=DARK, font=font_tiny)
    draw.rectangle([bar_x + 200, ly, bar_x + 216, ly + 12], fill=BREAK_COLOR)
    draw.text((bar_x + 222, ly - 1), "Summer Break", fill=DARK, font=font_tiny)

    buf = BytesIO()
    img.save(buf, format="PNG", dpi=(200, 200))
    buf.seek(0)
    return buf


# ── G. TV Graphics: Mock Timing Tower ────────────────────────────────────────

def mock_timing_tower():
    """Simplified timing tower showing ~5 drivers."""
    W, H = 500, 360
    img = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    font_title = _get_font(16, bold=True)
    font_row = _get_font(14, bold=True)
    font_detail = _get_font(12)

    DARK = (21, 21, 30)
    WHITE = (255, 255, 255)

    draw.text((W // 2, 10), "Timing Tower (Example)", fill=DARK, font=font_title, anchor="mt")

    drivers = [
        (1, "VER", (30, 65, 255), "LEADER", "1:31.245"),
        (2, "NOR", (255, 135, 0), "+1.234", "1:31.489"),
        (3, "LEC", (220, 0, 0), "+3.567", "1:31.812"),
        (4, "HAM", (220, 0, 0), "+5.891", "1:32.001"),
        (5, "PIA", (255, 135, 0), "+7.123", "1:32.156"),
    ]

    row_h = 48
    start_y = 45
    pad = 8
    col_w = W - 2 * pad

    for i, (pos, code, team_color, gap, lap_time) in enumerate(drivers):
        y = start_y + i * (row_h + 4)
        # Row background
        bg = (240, 240, 245) if i % 2 == 0 else WHITE
        draw.rectangle([pad, y, pad + col_w, y + row_h], fill=bg)

        # Team color bar (left edge)
        draw.rectangle([pad, y, pad + 6, y + row_h], fill=team_color)

        # Position number
        draw.rectangle([pad + 8, y + 4, pad + 38, y + row_h - 4], fill=DARK)
        draw.text((pad + 23, y + row_h // 2), str(pos), fill=WHITE, font=font_row, anchor="mm")

        # Driver code
        draw.text((pad + 48, y + 8), code, fill=DARK, font=font_row)

        # Gap
        draw.text((pad + 48, y + 28), gap, fill=(100, 100, 100), font=font_detail)

        # Lap time (right side)
        draw.text((pad + col_w - 10, y + row_h // 2), lap_time,
                  fill=(100, 100, 100), font=font_detail, anchor="rm")

    buf = BytesIO()
    img.save(buf, format="PNG", dpi=(200, 200))
    buf.seek(0)
    return buf


# ── E. Circuit Guide: Track Outlines ────────────────────────────────────────

def _draw_track(draw, points, W, H, name, color=(225, 6, 0)):
    """Draw a simplified track outline from normalized points (0-1 range)."""
    DARK = (30, 30, 40)
    font = _get_font(12, bold=True)

    # Scale points to image dimensions with padding
    pad = 30
    scaled = []
    for px, py in points:
        sx = pad + px * (W - 2 * pad)
        sy = pad + 20 + py * (H - 2 * pad - 20)
        scaled.append((sx, sy))

    # Draw track outline
    draw.line(scaled + [scaled[0]], fill=color, width=4)

    # Track name
    draw.text((W // 2, 12), name, fill=DARK, font=font, anchor="mt")


def track_outlines():
    """Generate a grid of simplified track silhouettes."""
    tracks = {
        "Monaco": [(0.1, 0.3), (0.2, 0.1), (0.5, 0.1), (0.7, 0.2),
                    (0.8, 0.4), (0.7, 0.7), (0.5, 0.9), (0.3, 0.8),
                    (0.15, 0.6)],
        "Silverstone": [(0.1, 0.4), (0.2, 0.15), (0.4, 0.1), (0.55, 0.2),
                        (0.7, 0.1), (0.85, 0.25), (0.9, 0.5), (0.8, 0.7),
                        (0.6, 0.85), (0.35, 0.8), (0.15, 0.65)],
        "Spa": [(0.05, 0.5), (0.1, 0.3), (0.15, 0.15), (0.3, 0.1),
                (0.5, 0.2), (0.65, 0.15), (0.85, 0.3), (0.95, 0.5),
                (0.85, 0.7), (0.6, 0.85), (0.35, 0.9), (0.15, 0.75)],
        "Monza": [(0.2, 0.15), (0.5, 0.1), (0.8, 0.15), (0.85, 0.35),
                  (0.75, 0.55), (0.8, 0.7), (0.7, 0.85), (0.4, 0.9),
                  (0.2, 0.75), (0.15, 0.5)],
        "Suzuka": [(0.1, 0.5), (0.15, 0.25), (0.3, 0.1), (0.5, 0.15),
                   (0.6, 0.3), (0.5, 0.5), (0.6, 0.65), (0.8, 0.55),
                   (0.9, 0.7), (0.75, 0.9), (0.4, 0.85), (0.2, 0.7)],
        "COTA": [(0.15, 0.2), (0.3, 0.1), (0.5, 0.15), (0.65, 0.1),
                 (0.8, 0.2), (0.9, 0.4), (0.85, 0.65), (0.7, 0.8),
                 (0.5, 0.9), (0.3, 0.8), (0.15, 0.6), (0.1, 0.4)],
        "Singapore": [(0.15, 0.3), (0.3, 0.1), (0.6, 0.1), (0.8, 0.25),
                      (0.85, 0.5), (0.75, 0.75), (0.55, 0.9), (0.3, 0.85),
                      (0.15, 0.6)],
        "Jeddah": [(0.1, 0.9), (0.1, 0.6), (0.15, 0.3), (0.2, 0.1),
                   (0.4, 0.1), (0.6, 0.15), (0.8, 0.1), (0.9, 0.3),
                   (0.85, 0.6), (0.7, 0.8), (0.4, 0.9)],
        "Madrid": [(0.15, 0.3), (0.3, 0.1), (0.55, 0.1), (0.75, 0.2),
                   (0.85, 0.4), (0.8, 0.65), (0.65, 0.8), (0.45, 0.9),
                   (0.25, 0.8), (0.1, 0.55)],
    }

    cell_w, cell_h = 280, 220
    cols = 3
    rows = 3
    W = cols * cell_w + 20
    H = rows * cell_h + 50

    img = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    font_title = _get_font(20, bold=True)
    draw.text((W // 2, 12), "Featured Circuit Outlines", fill=(30, 30, 40), font=font_title, anchor="mt")

    for idx, (name, points) in enumerate(tracks.items()):
        row = idx // cols
        col = idx % cols
        x0 = col * cell_w + 10
        y0 = row * cell_h + 45

        # Create sub-image
        cell = Image.new("RGB", (cell_w - 10, cell_h - 10), (250, 250, 252))
        cdraw = ImageDraw.Draw(cell)

        # Draw outline
        DARK = (30, 30, 40)
        font = _get_font(12, bold=True)
        pad = 20
        scaled = []
        for px, py in points:
            sx = pad + px * (cell_w - 10 - 2 * pad)
            sy = pad + 18 + py * (cell_h - 10 - 2 * pad - 18)
            scaled.append((sx, sy))
        cdraw.line(scaled + [scaled[0]], fill=(225, 6, 0), width=3)
        cdraw.text(((cell_w - 10) // 2, 8), name, fill=DARK, font=font, anchor="mt")

        # Border
        cdraw.rectangle([0, 0, cell_w - 11, cell_h - 11], outline=(210, 210, 210), width=1)

        img.paste(cell, (x0, y0))

    buf = BytesIO()
    img.save(buf, format="PNG", dpi=(200, 200))
    buf.seek(0)
    return buf
