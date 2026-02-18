"""
Shared F1 PDF styling module.
Provides the F1PDF subclass with consistent branding, headers, footers,
cover pages, section helpers, styled tables, info boxes, and visual helpers.
"""

from fpdf import FPDF
import os

# Unicode-to-ASCII mapping for built-in fonts (Helvetica doesn't support Unicode)
_UNICODE_MAP = {
    "\u2013": "-",    # en-dash
    "\u2014": " - ",  # em-dash
    "\u2018": "'",    # left single quote
    "\u2019": "'",    # right single quote
    "\u201c": '"',    # left double quote
    "\u201d": '"',    # right double quote
    "\u2022": "-",    # bullet
    "\u2026": "...",  # ellipsis
    "\u2192": "->",   # right arrow
    "\u00b0": "deg",  # degree sign
    "\u2248": "~",    # approximately
}


def _sanitize(text):
    """Replace non-Latin-1 Unicode characters with ASCII equivalents."""
    if not isinstance(text, str):
        return text
    for uc, ascii_eq in _UNICODE_MAP.items():
        text = text.replace(uc, ascii_eq)
    return text

# ── Accent Colors (distinct from official F1 brand) ─────────────────────────
F1_RED = (195, 15, 30)         # Racing red (not F1 brand #E10600)
F1_DARK = (28, 30, 42)         # Dark charcoal
LIGHT_GRAY = (240, 240, 240)   # #F0F0F0
WHITE = (255, 255, 255)
MEDIUM_GRAY = (180, 180, 180)
DARK_GRAY = (100, 100, 100)
F1_RED_LIGHT = (255, 230, 230) # subtle red tint for highlight cells
CARD_BG = (247, 247, 250)      # warm gray for card backgrounds
SEPARATOR_GRAY = (210, 210, 210)  # thin divider lines

# ── F1 Team Colors ───────────────────────────────────────────────────────────
TEAM_COLORS = {
    "Red Bull Racing":      (30, 65, 255),    # dark blue
    "Scuderia Ferrari":     (220, 0, 0),      # Ferrari red
    "McLaren F1 Team":      (255, 135, 0),    # papaya orange
    "Mercedes-AMG Petronas": (39, 244, 210),  # teal/silver-green
    "Aston Martin Aramco":  (0, 111, 98),     # British racing green
    "Alpine F1 Team":       (0, 144, 255),    # Alpine blue
    "Williams Racing":      (0, 55, 190),     # Williams blue
    "Visa Cash App Racing Bulls": (102, 146, 255),  # RB light blue
    "MoneyGram Haas F1 Team": (180, 180, 180), # gray/white
    "Sauber / Audi F1 Team": (0, 0, 0),       # Audi black
    "Cadillac F1 Team":     (30, 30, 30),     # Cadillac dark
}

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "output")


class F1PDF(FPDF):
    """Custom FPDF subclass with F1 2026 branding."""

    def __init__(self, title="2026 Season Reference", subtitle=""):
        super().__init__(orientation="P", unit="mm", format="Letter")
        self.doc_title = title
        self.doc_subtitle = subtitle
        self.set_auto_page_break(auto=True, margin=20)

    def normalize_text(self, text):
        """Override to sanitize Unicode before fpdf's Latin-1 encoding."""
        return super().normalize_text(_sanitize(text))

    # ── Header ────────────────────────────────────────────────────────────
    def header(self):
        if self.page_no() == 1:
            return  # Cover page has its own layout
        # Red accent bar (4mm thick)
        self.set_fill_color(*F1_RED)
        self.rect(10, 5, self.w - 20, 4, "F")
        # Dark understrip (1mm) for depth
        self.set_fill_color(*F1_DARK)
        self.rect(10, 9, self.w - 20, 1, "F")
        # Document title (left)
        self.set_y(13)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*F1_DARK)
        self.cell(self.w - 20, 5, self.doc_title, align="L")
        # "2026 Season" label (right) - draw over same line
        self.set_xy(10, 13)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*DARK_GRAY)
        self.cell(self.w - 20, 5, "2026 Season", align="R")
        self.set_y(24)  # Adjusted top margin to accommodate thicker header

    # ── Footer ────────────────────────────────────────────────────────────
    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-15)
        # Separator line above footer
        self.set_draw_color(*SEPARATOR_GRAY)
        self.set_line_width(0.3)
        self.line(10, self.get_y(), self.w - 10, self.get_y())
        self.ln(2)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*DARK_GRAY)
        self.cell((self.w - 20) / 2, 8, "Unofficial 2026 Season Guide", align="L")
        self.cell((self.w - 20) / 2, 8, f"Page {self.page_no() - 1}", align="R")

    # ── Cover Page ────────────────────────────────────────────────────────
    def add_cover_page(self):
        self.add_page()
        # Dark background
        self.set_fill_color(*F1_DARK)
        self.rect(0, 0, self.w, self.h, "F")

        # Geometric decorations - diagonal stripe
        with self.local_context(fill_opacity=0.07):
            self.set_fill_color(*F1_RED)
            self.polygon([
                (self.w * 0.55, 0),
                (self.w * 0.75, 0),
                (self.w, self.h * 0.25),
                (self.w, self.h * 0.45),
            ], style="F")

        # Ghost circles
        with self.local_context(fill_opacity=0.04):
            self.set_fill_color(*F1_RED)
            self.circle(self.w * 0.82, self.h * 0.25, 35, style="F")
            self.circle(self.w * 0.15, self.h * 0.72, 22, style="F")

        # "UNOFFICIAL FAN GUIDE" badge at top
        self.set_y(self.h / 2 - 65)
        badge_w = 70
        badge_x = (self.w - badge_w) / 2
        self.set_draw_color(*F1_RED)
        self.set_line_width(0.8)
        self.set_fill_color(*F1_RED)
        self.rect(badge_x, self.get_y(), badge_w, 8, "DF")
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*WHITE)
        self.cell(0, 8, "UNOFFICIAL FAN GUIDE", align="C")
        self.ln(18)

        # Main title: "2026 SEASON GUIDE"
        self.set_font("Helvetica", "B", 32)
        self.set_text_color(*WHITE)
        self.cell(0, 14, "2026 SEASON GUIDE", align="C")
        self.ln(18)

        # Red accent bar
        line_w = 100
        x_start = (self.w - line_w) / 2
        self.set_fill_color(*F1_RED)
        self.rect(x_start, self.get_y(), line_w, 4, "F")
        self.ln(12)

        # Document subtitle (e.g., "Race Schedule", "Driver & Team Guide")
        self.set_font("Helvetica", "", 20)
        self.set_text_color(*MEDIUM_GRAY)
        self.cell(0, 10, self.doc_subtitle, align="C")
        self.ln(30)

        # Tagline
        self.set_font("Helvetica", "", 11)
        self.set_text_color(*DARK_GRAY)
        self.cell(0, 6, "A Beginner's Guide to the Formula 1 Season", align="C")
        self.ln(8)

        # Bottom accent line
        bot_w = 60
        x_bot = (self.w - bot_w) / 2
        self.set_fill_color(*F1_RED)
        self.rect(x_bot, self.get_y(), bot_w, 1.5, "F")

        # Disclaimer at bottom of cover
        self.set_y(self.h - 30)
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*DARK_GRAY)
        disclaimer = (
            "This is an unofficial fan-made guide. Not associated with Formula 1, "
            "FIA, or any F1 team. Formula 1, F1, and Grand Prix are trademarks "
            "of Formula One Licensing BV. All trademarks are property of their "
            "respective owners."
        )
        self.multi_cell(0, 3.5, disclaimer, align="C")

    # ── Section Header (dynamic underline) ────────────────────────────────
    def section_header(self, title, size=16):
        self.ln(6)
        if self.get_y() > self.h - 40:
            self.add_page()
        self.set_font("Helvetica", "B", size)
        self.set_text_color(*F1_DARK)
        title_w = self.get_string_width(title)
        self.cell(0, 10, title)
        self.ln(10)
        # Red underline proportional to title width
        red_w = min(title_w + 5, self.w - 20)
        self.set_fill_color(*F1_RED)
        self.rect(10, self.get_y(), red_w, 1.5, "F")
        # Gray extension line to right margin
        gray_start = 10 + red_w
        gray_w = self.w - 10 - gray_start
        if gray_w > 2:
            self.set_fill_color(*SEPARATOR_GRAY)
            self.rect(gray_start, self.get_y() + 0.5, gray_w, 0.3, "F")
        self.ln(6)

    # ── Subsection Header ─────────────────────────────────────────────────
    def subsection_header(self, title, size=12):
        self.ln(3)
        if self.get_y() > self.h - 35:
            self.add_page()
        self.set_font("Helvetica", "B", size)
        self.set_text_color(*F1_RED)
        self.cell(0, 8, title)
        self.ln(8)
        self.set_text_color(*F1_DARK)

    # ── Body Text ─────────────────────────────────────────────────────────
    def body_text(self, text, size=10):
        self.set_font("Helvetica", "", size)
        self.set_text_color(*F1_DARK)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    # ── Bold Body Text ────────────────────────────────────────────────────
    def body_bold(self, text, size=10):
        self.set_font("Helvetica", "B", size)
        self.set_text_color(*F1_DARK)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    # ── Bullet List (Red Circle Markers) ─────────────────────────────────
    def bullet_list(self, items, indent=15, size=10):
        self.set_font("Helvetica", "", size)
        self.set_text_color(*F1_DARK)
        for item in items:
            y = self.get_y()
            if y > self.h - 20:
                self.add_page()
                y = self.get_y()
            # Red circle bullet
            self.set_fill_color(*F1_RED)
            self.circle(10 + indent - 5, y + 2.5, 1.2, style="F")
            # Text
            self.set_x(10 + indent)
            self.set_font("Helvetica", "", size)
            self.set_text_color(*F1_DARK)
            self.multi_cell(self.w - 20 - indent, 5.5, item)
            self.ln(1)
        self.ln(2)

    # ── Styled Table ──────────────────────────────────────────────────────
    def styled_table(self, headers, data, col_widths=None, font_size=9):
        """Draw a table with F1 red header, alternating rows, column separators."""
        usable = self.w - 20  # 10mm margins each side
        n_cols = len(headers)
        if col_widths is None:
            col_widths = [usable / n_cols] * n_cols

        header_h = 8   # taller header row
        row_h = 7
        table_w = sum(col_widths)

        def draw_header():
            hy = self.get_y()
            self.set_fill_color(*F1_RED)
            self.set_text_color(*WHITE)
            self.set_font("Helvetica", "B", font_size)
            for i, h in enumerate(headers):
                self.cell(col_widths[i], header_h, f" {h}", border=0, fill=True)
            self.ln(header_h)
            # Dark line below header
            self.set_draw_color(*F1_DARK)
            self.set_line_width(0.5)
            self.line(10, self.get_y(), 10 + table_w, self.get_y())
            # White vertical separators in header
            x_pos = 10
            for i in range(n_cols - 1):
                x_pos += col_widths[i]
                with self.local_context(stroke_opacity=0.3):
                    self.set_draw_color(*WHITE)
                    self.set_line_width(0.15)
                    self.line(x_pos, hy, x_pos, hy + header_h)

        draw_header()

        # Data rows
        self.set_font("Helvetica", "", font_size)
        self.set_text_color(*F1_DARK)
        for row_idx, row in enumerate(data):
            if self.get_y() + row_h > self.h - 20:
                self.add_page()
                draw_header()
                self.set_font("Helvetica", "", font_size)
                self.set_text_color(*F1_DARK)

            row_y = self.get_y()
            if row_idx % 2 == 0:
                self.set_fill_color(*LIGHT_GRAY)
            else:
                self.set_fill_color(*WHITE)

            for i, val in enumerate(row):
                self.cell(col_widths[i], row_h, f" {val}", border=0, fill=True)
            self.ln(row_h)

            # Subtle vertical column separators
            x_pos = 10
            for i in range(n_cols - 1):
                x_pos += col_widths[i]
                self.set_draw_color(*SEPARATOR_GRAY)
                self.set_line_width(0.15)
                self.line(x_pos, row_y, x_pos, row_y + row_h)

        # Bottom border line
        self.set_draw_color(*SEPARATOR_GRAY)
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 10 + table_w, self.get_y())
        self.ln(4)

    # ── Info Box (accurate height via dry_run) ────────────────────────────
    def info_box(self, title, text):
        x = 10
        box_w = self.w - 20

        # Calculate accurate height using dry_run
        self.set_font("Helvetica", "", 9)
        text_h = self.multi_cell(box_w - 16, 4.5, text, dry_run=True, output="HEIGHT")
        box_h = max(18, 10 + text_h + 2)

        # Page break check with accurate height
        if self.get_y() + box_h > self.h - 20:
            self.add_page()

        y = self.get_y()

        # Box background
        self.set_fill_color(*LIGHT_GRAY)
        self.rect(x, y, box_w, box_h, "F")

        # Red left border
        self.set_fill_color(*F1_RED)
        self.rect(x, y, 3, box_h, "F")

        # Title
        self.set_xy(x + 6, y + 2)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*F1_RED)
        self.cell(0, 5, title)

        # Body
        self.set_xy(x + 6, y + 8)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*F1_DARK)
        self.multi_cell(box_w - 16, 4.5, text)
        self.set_y(y + box_h + 4)

    # ── Comparison Row ────────────────────────────────────────────────────
    def comparison_row(self, label, old_val, new_val, col_widths=None):
        usable = self.w - 20
        if col_widths is None:
            col_widths = [usable * 0.35, usable * 0.325, usable * 0.325]
        row_h = 7
        self.set_font("Helvetica", "B", 9)
        self.cell(col_widths[0], row_h, f" {label}", border=0, fill=True)
        self.set_font("Helvetica", "", 9)
        self.cell(col_widths[1], row_h, f" {old_val}", border=0, fill=True)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*F1_RED)
        self.cell(col_widths[2], row_h, f" {new_val}", border=0, fill=True)
        self.set_text_color(*F1_DARK)
        self.ln(row_h)

    # ── Glossary Entry (card-style) ───────────────────────────────────────
    def glossary_entry(self, term, definition):
        """Render a glossary term as a card with red left accent."""
        x = 10
        card_w = self.w - 20

        # Accurate height via dry_run
        self.set_font("Helvetica", "", 9)
        text_h = self.multi_cell(card_w - 16, 4.5, definition, dry_run=True, output="HEIGHT")
        card_h = max(16, 9 + text_h + 2)

        if self.get_y() + card_h > self.h - 20:
            self.add_page()

        y = self.get_y()

        # Card background
        self.set_fill_color(*CARD_BG)
        self.rect(x, y, card_w, card_h, "F")

        # Red left accent
        self.set_fill_color(*F1_RED)
        self.rect(x, y, 2.5, card_h, "F")

        # Term
        self.set_xy(x + 6, y + 2)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*F1_DARK)
        self.cell(0, 5, term)

        # Definition
        self.set_xy(x + 6, y + 8)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*F1_DARK)
        self.multi_cell(card_w - 16, 4.5, definition)

        self.set_y(y + card_h + 3)

    # ── Team Card ─────────────────────────────────────────────────────────
    def team_card(self, name, base, principal, pu, drivers, story, team_color=None):
        """Render a team profile as a bordered card with colored left accent."""
        x = 10
        card_w = self.w - 20

        # Calculate story height
        self.set_font("Helvetica", "", 9)
        story_h = self.multi_cell(card_w - 12, 4.5, story, dry_run=True, output="HEIGHT")
        card_h = max(40, 3 + 7 + 6 + 6 + 3 + story_h + 4)

        if self.get_y() + card_h > self.h - 20:
            self.add_page()

        y = self.get_y()

        # White card with gray border
        self.set_draw_color(*SEPARATOR_GRAY)
        self.set_line_width(0.3)
        self.set_fill_color(*WHITE)
        self.rect(x, y, card_w, card_h, "DF")

        # Top accent bar: use team color if provided, else F1 red
        color = team_color if team_color else F1_RED
        self.set_fill_color(*color)
        self.rect(x, y, card_w, 3, "F")

        # Left border in team color
        if team_color:
            self.set_fill_color(*team_color)
            self.rect(x, y, 3, card_h, "F")

        # Team name
        self.set_xy(x + 5, y + 5)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(*F1_DARK)
        self.cell(0, 6, name)

        # Metadata
        self.set_xy(x + 5, y + 12)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*DARK_GRAY)
        self.cell(0, 5, f"Base: {base}  |  Principal: {principal}  |  PU: {pu}")

        # Drivers (in red)
        self.set_xy(x + 5, y + 19)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*F1_RED)
        self.cell(0, 5, drivers)

        # Story
        self.set_xy(x + 5, y + 26)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*F1_DARK)
        self.multi_cell(card_w - 12, 4.5, story)

        self.set_y(y + card_h + 5)

    # ── Stat Callout ──────────────────────────────────────────────────────
    def stat_callout(self, stats):
        """Row of big red numbers with gray labels.
        stats = [("24", "Grands Prix"), ("11", "Teams"), ...]
        """
        if self.get_y() > self.h - 30:
            self.add_page()

        n = len(stats)
        usable = self.w - 20
        col_w = usable / n
        y = self.get_y()
        x = 10

        # Background
        self.set_fill_color(*CARD_BG)
        self.rect(x, y, usable, 22, "F")

        for i, (number, label) in enumerate(stats):
            # Big red number
            self.set_font("Helvetica", "B", 22)
            self.set_text_color(*F1_RED)
            self.set_xy(x + i * col_w, y + 1)
            self.cell(col_w, 12, str(number), align="C")
            # Gray label below
            self.set_font("Helvetica", "", 8)
            self.set_text_color(*DARK_GRAY)
            self.set_xy(x + i * col_w, y + 13)
            self.cell(col_w, 6, label, align="C")

        self.set_y(y + 26)

    # ── Colored Divider ───────────────────────────────────────────────────
    def colored_divider(self):
        """Thin gray lines with red center accent segment."""
        y = self.get_y() + 3
        center = self.w / 2
        # Gray line (left)
        self.set_draw_color(*SEPARATOR_GRAY)
        self.set_line_width(0.3)
        self.line(10, y, center - 15, y)
        # Gray line (right)
        self.line(center + 15, y, self.w - 10, y)
        # Red center accent
        self.set_draw_color(*F1_RED)
        self.set_line_width(0.7)
        self.line(center - 15, y, center + 15, y)
        self.set_line_width(0.2)
        self.set_y(y + 5)

    # ── Diagram Embed ────────────────────────────────────────────────────
    def add_diagram(self, img_bytes, w=None, h=None, caption=None):
        """Embed a BytesIO PNG image, optionally centered with a caption."""
        import tempfile, io
        from PIL import Image as PILImage
        if isinstance(img_bytes, io.BytesIO):
            img_bytes.seek(0)
        # Read image to get dimensions
        pil_img = PILImage.open(img_bytes)
        img_w_px, img_h_px = pil_img.size
        # Write to a temp file so fpdf can read it
        img_bytes.seek(0)
        tmp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        tmp.write(img_bytes.read() if hasattr(img_bytes, 'read') else img_bytes)
        tmp.close()
        # Calculate sizing — ensure both w and h are set
        if w is None and h is None:
            w = self.w - 20
        if w and not h:
            h = w * (img_h_px / img_w_px)
        elif h and not w:
            w = h * (img_w_px / img_h_px)
        # Center horizontally
        x = (self.w - w) / 2
        # Page break check
        if self.get_y() + h + 10 > self.h - 20:
            self.add_page()
        self.image(tmp.name, x=x, w=w, h=h)
        os.unlink(tmp.name)
        if caption:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(*DARK_GRAY)
            self.cell(0, 5, caption, align="C")
            self.ln(6)
        self.ln(4)

    # ── Save Helper ───────────────────────────────────────────────────────
    def save(self, filename):
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        path = os.path.join(OUTPUT_DIR, filename)
        self.output(path)
        print(f"  Created: {path}")
        return path
