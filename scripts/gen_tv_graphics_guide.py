"""PDF 4: F1 2026 TV Graphics Guide -- Timing, sectors, tires, telemetry, flags, weather."""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from f1_pdf_style import F1PDF, F1_DARK, DARK_GRAY, F1_RED
import f1_graphics


def color_swatch_row(pdf, swatches):
    """Draw a row of colored circles with labels.
    swatches = [((R,G,B), "Label"), ...]
    """
    n = len(swatches)
    usable = pdf.w - 20
    col_w = usable / n
    y = pdf.get_y()

    for i, (color, label) in enumerate(swatches):
        cx = 10 + i * col_w + 8
        cy = y + 4
        pdf.set_fill_color(*color)
        pdf.circle(cx, cy, 3.5, style="F")
        pdf.set_xy(cx + 5, y + 1)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(*F1_DARK)
        pdf.cell(col_w - 15, 7, label)

    pdf.set_y(y + 12)


def generate():
    pdf = F1PDF(
        title="2026 TV Graphics Guide",
        subtitle="Understanding the Broadcast Graphics"
    )
    pdf.add_cover_page()
    pdf.add_page()

    # -- Introduction ------------------------------------------------------
    pdf.section_header("Introduction")
    pdf.body_text(
        "Formula 1's live broadcast uses a rich set of on-screen graphics "
        "to convey race information in real time. Understanding these "
        "graphics transforms the viewing experience from passive watching "
        "to informed analysis. This guide covers every major graphic element "
        "you'll see during a 2026 broadcast."
    )
    pdf.info_box(
        "2026 Broadcast Note",
        "Apple TV+ becomes a major broadcast partner for F1 starting in "
        "2026, bringing updated graphics packages and presentation styles. "
        "Core information elements remain consistent, though visual design "
        "may evolve throughout the season."
    )

    # -- Timing Tower ------------------------------------------------------
    pdf.section_header("The Timing Tower")
    pdf.body_text(
        "The timing tower is the vertical leaderboard displayed on the left "
        "side of the screen. It is the single most important graphic for "
        "following the race."
    )

    pdf.subsection_header("Information Displayed")
    pdf.styled_table(
        headers=["Element", "Description", "Example"],
        data=[
            ["Position", "Current race position (P1, P2, etc.)", "1"],
            ["Driver Code", "Three-letter abbreviation", "VER, HAM, NOR"],
            ["Team Color", "Colored bar showing team identity", "Red Bull = dark blue"],
            ["Interval", "Gap to car directly ahead", "+1.234"],
            ["Gap to Leader", "Total gap to the race leader", "+12.567"],
            ["Pit Indicator", "Shows when a driver is in the pits", "PIT / OUT"],
            ["Tire Compound", "Current tire compound and age", "M (Lap 12)"],
            ["Position Change", "Arrow showing gained/lost positions", "Up/Down arrow"],
        ],
        col_widths=[32, 85, 50],
    )

    pdf.subsection_header("Timing Tower Modes")
    pdf.body_text(
        "The timing tower can display different information depending on the "
        "session and broadcast director's choice:"
    )
    pdf.bullet_list([
        "Interval mode: Shows gap to car ahead (most common during races)",
        "Leader mode: Shows gap to the race leader for all drivers",
        "Practice/Qualifying: Shows best lap times and sector splits",
        "Pit stop mode: Highlights pit stop duration and positions gained/lost",
    ])

    tower_img = f1_graphics.mock_timing_tower()
    pdf.add_diagram(tower_img, w=90, caption="Example timing tower display")

    # -- Sector Colors -----------------------------------------------------
    pdf.section_header("Sector Colors")
    pdf.body_text(
        "Each circuit is divided into three sectors (S1, S2, S3). As a driver "
        "completes each sector, the time is color-coded to show performance."
    )

    # Color swatches for sector colors
    color_swatch_row(pdf, [
        ((160, 32, 240), "Purple - Session Fastest"),
        ((0, 180, 0), "Green - Personal Best"),
        ((220, 200, 0), "Yellow - Not Improved"),
    ])

    pdf.styled_table(
        headers=["Color", "Meaning", "Detail"],
        data=[
            ["Purple", "Overall fastest", "Fastest sector time by ANY driver in the session"],
            ["Green", "Personal best", "Driver's own best sector time in the session"],
            ["Yellow", "Not a personal best", "Slower than the driver's previous best"],
            ["White", "First timed lap", "No comparison available yet"],
        ],
        col_widths=[25, 40, 105],
    )

    pdf.info_box(
        "Reading Sectors During Qualifying",
        "In qualifying, watch the sector colors to predict lap times before "
        "the driver crosses the line. Three purple sectors = potential pole "
        "lap. A yellow sector means the driver has lost time and the lap may "
        "not improve their position."
    )

    pdf.subsection_header("Mini Sectors")
    pdf.body_text(
        "Each sector is further divided into mini sectors (approximately "
        "every 200-300 meters). These provide even more granular speed "
        "comparisons and are shown on detailed telemetry overlays."
    )

    # -- Tire Information --------------------------------------------------
    pdf.section_header("Tire Information")
    pdf.body_text(
        "Tire graphics are critical for understanding race strategy. Pirelli "
        "supplies all tires with standardized color coding."
    )

    pdf.subsection_header("Dry Compounds")
    # Color swatches for tire colors
    color_swatch_row(pdf, [
        ((225, 6, 0), "Red - Soft"),
        ((220, 200, 0), "Yellow - Medium"),
        ((255, 255, 255), "White - Hard"),
    ])

    pdf.styled_table(
        headers=["Compound", "Color", "Range", "Characteristics"],
        data=[
            ["Hard", "White", "C1-C2", "Most durable, least grip, longest stints"],
            ["Medium", "Yellow", "C2-C4", "Balanced durability and performance"],
            ["Soft", "Red", "C3-C5", "Maximum grip, fastest degradation, qualifying"],
        ],
        col_widths=[25, 20, 22, 100],
    )

    pdf.subsection_header("Wet Compounds")
    color_swatch_row(pdf, [
        ((0, 180, 0), "Green - Intermediate"),
        ((0, 100, 220), "Blue - Full Wet"),
    ])

    pdf.styled_table(
        headers=["Compound", "Color", "Usage"],
        data=[
            ["Intermediate", "Green", "Damp/drying track; light rain or drying conditions"],
            ["Full Wet", "Blue", "Heavy rain; standing water on track"],
        ],
        col_widths=[30, 20, 117],
    )

    pdf.subsection_header("On-Screen Tire Information")
    pdf.bullet_list([
        "Tire compound icon (colored circle) next to driver name on timing tower",
        "Tire age in laps (e.g., 'Lap 15' means 15 laps since fitting)",
        "Tire performance curves shown during strategy analysis graphics",
        "Pit stop window predictions overlaid on race progression charts",
        "Used vs. new tire indicator (some broadcasts show this distinction)",
    ])

    pdf.info_box(
        "Compound Selection",
        "Pirelli selects three of the five dry compounds (C1-C5) for each "
        "Grand Prix. These are labeled Hard, Medium, and Soft regardless "
        "of which C-numbers they actually are. A C3 tire might be the 'Hard' "
        "at one race and the 'Soft' at another."
    )

    # -- Telemetry Overlays ------------------------------------------------
    pdf.section_header("Telemetry & Data Overlays")
    pdf.body_text(
        "Modern F1 broadcasts include detailed telemetry graphics that show "
        "real-time car data. These are especially prominent during onboard "
        "camera views."
    )

    pdf.subsection_header("Speed & Gear")
    pdf.bullet_list([
        "Speed (km/h or mph): Displayed as a large number on onboard views",
        "Gear indicator: Shows current gear (1-8), often with RPM bar",
        "Speed trace: Line graph comparing speeds of two drivers through a lap",
        "Speed trap: Maximum speed recorded at a specific point on the straight",
    ])

    pdf.subsection_header("Throttle & Brake")
    pdf.bullet_list([
        "Throttle application: Bar showing 0-100% throttle input",
        "Brake pressure: Bar showing braking force (often red-colored)",
        "Combined view shows both inputs simultaneously during onboard laps",
        "Useful for comparing driving styles into braking zones",
    ])

    pdf.subsection_header("ERS & Battery (New for 2026)")
    pdf.body_text(
        "With the dramatically increased electric power in 2026, battery and "
        "ERS graphics become much more important:"
    )

    # Stat callout for ERS numbers
    pdf.stat_callout([
        ("~50%", "Electric Power"),
        ("350", "kW MGU-K"),
        ("0", "MGU-H (Removed)"),
    ])

    pdf.bullet_list([
        "Battery state of charge: Percentage or bar showing remaining energy",
        "ERS deployment: Visual indicator of when electric power is being used",
        "ERS harvesting: Shows when the MGU-K is recovering energy under braking",
        "X-Mode indicator: Shows when active aero is in low-drag configuration",
        "Power split graphic: Pie chart or bar showing ICE vs. electric power",
        "Energy management is now a key strategic element visible on broadcasts",
    ])

    pdf.info_box(
        "Why ERS Matters More in 2026",
        "With ~50% of power from electric sources, battery management becomes "
        "as important as tire strategy. Drivers who manage energy better on "
        "high-demand circuits will have a significant advantage. Watch the "
        "battery graphic to see who is deploying and harvesting efficiently."
    )

    # -- Flags -------------------------------------------------------------
    pdf.section_header("Flags & Their Meanings")
    pdf.body_text(
        "Flags are the primary means of communication between race control "
        "and drivers. They are shown on-screen and at marshalling posts "
        "around the circuit."
    )

    pdf.styled_table(
        headers=["Flag", "Color/Pattern", "Meaning"],
        data=[
            ["Green", "Solid green", "Track clear, racing conditions, session start"],
            ["Yellow", "Solid yellow", "Danger ahead - slow down, no overtaking in zone"],
            ["Double Yellow", "Two yellow flags", "Great danger - be prepared to stop"],
            ["Red", "Solid red", "Session stopped - return to pit lane immediately"],
            ["Blue", "Solid blue", "Let faster car through (lapped traffic)"],
            ["White", "Solid white", "Slow-moving vehicle ahead (recovery, medical)"],
            ["Black", "Solid black", "Driver disqualified (shown with car number)"],
            ["Black/Orange", "Black + orange circle", "Car has mechanical issue - must pit"],
            ["Black/White", "Diagonal halves", "Unsportsmanlike behavior warning"],
            ["Yellow/Red", "Red + yellow stripes", "Slippery surface (oil, water, debris)"],
            ["Checkered", "Black/white checks", "Session or race finished"],
        ],
        col_widths=[30, 40, 97],
        font_size=8,
    )

    pdf.subsection_header("Safety Car & VSC Graphics")
    pdf.bullet_list([
        "SC (Safety Car): Yellow 'SC' banner across timing tower; field bunches up",
        "VSC (Virtual Safety Car): 'VSC' indicator; cars maintain delta time",
        "SC ending: 'SC IN THIS LAP' message before green flag restart",
        "Red flag: Red banner replaces all other graphics",
    ])

    # -- Weather Graphics --------------------------------------------------
    pdf.section_header("Weather Graphics")
    pdf.body_text(
        "Weather information is crucial in F1, as conditions directly affect "
        "tire choice, strategy, and car setup."
    )

    pdf.subsection_header("On-Screen Weather Data")
    pdf.styled_table(
        headers=["Metric", "What It Shows", "Why It Matters"],
        data=[
            ["Air Temp", "Ambient air temperature (C/F)", "Affects engine cooling and aero"],
            ["Track Temp", "Road surface temperature", "Major impact on tire grip/degradation"],
            ["Humidity", "Moisture in the air (%)", "Affects engine performance"],
            ["Wind Speed", "Wind velocity and direction", "Impacts aero balance, especially on straights"],
            ["Rain Probability", "Chance of rain (%)", "Triggers strategy decisions"],
            ["Radar", "Rain radar overlay of circuit", "Shows approaching weather systems"],
        ],
        col_widths=[30, 55, 82],
    )

    pdf.info_box(
        "Weather Strategy",
        "A rain probability increase during a race creates massive strategic "
        "decisions: pit now for intermediates or gamble on staying out? Watch "
        "the radar graphic to see if rain is actually hitting the circuit. "
        "Different sectors can have different conditions simultaneously."
    )

    # -- Additional Broadcast Elements -------------------------------------
    pdf.section_header("Additional Broadcast Elements")

    pdf.subsection_header("Battle Graphics")
    pdf.bullet_list([
        "Head-to-head comparison between two close drivers",
        "Gap timer showing live interval between battling cars",
        "Overtake probability (experimental AI-driven graphic)",
        "Historical comparison of laps between two drivers",
    ])

    pdf.subsection_header("Strategy Graphics")
    pdf.bullet_list([
        "Pit stop window: Predicted optimal pit window for each driver",
        "Undercut/overcut analysis: Shows if an early or late stop is beneficial",
        "Tire life remaining: Estimated laps left on current compound",
        "Race progression chart: Lap-by-lap position chart for all drivers",
    ])

    pdf.subsection_header("Driver Communications")
    pdf.bullet_list([
        "Team radio transcripts displayed on screen",
        "Driver-of-the-Day voting graphics",
        "Penalty notifications with explanation",
        "Track limit warnings and violations",
    ])

    # -- Quick Reference Card (Enhanced) -----------------------------------
    pdf.section_header("Quick Reference Card")
    pdf.body_text(
        "Print this page as a single-sheet cheat sheet for race day."
    )

    pdf.subsection_header("Sector Colors at a Glance")
    color_swatch_row(pdf, [
        ((160, 32, 240), "Purple = Session Fastest"),
        ((0, 180, 0), "Green = Personal Best"),
        ((220, 200, 0), "Yellow = Not Improved"),
    ])

    pdf.subsection_header("Tire Colors at a Glance")
    color_swatch_row(pdf, [
        ((225, 6, 0), "Soft (Red)"),
        ((220, 200, 0), "Medium (Yellow)"),
        ((200, 200, 200), "Hard (White)"),
        ((0, 180, 0), "Inter (Green)"),
        ((0, 100, 220), "Wet (Blue)"),
    ])

    pdf.subsection_header("Common Flag Summary")
    pdf.styled_table(
        headers=["Green", "Yellow", "Red", "Blue", "Checkered"],
        data=[["Clear", "Danger", "Stopped", "Move over", "Finished"]],
        col_widths=[33.6] * 5,
    )

    pdf.subsection_header("Points (Race / Sprint)")
    pdf.styled_table(
        headers=["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"],
        data=[
            ["25/8", "18/7", "15/6", "12/5", "10/4", "8/3", "6/2", "4/1", "2/-", "1/-"],
        ],
        col_widths=[19.2] * 10,
        font_size=8,
    )
    pdf.body_text("No bonus point for fastest lap (abolished from 2025 onwards).")

    pdf.save("2026-TV-Graphics-Guide.pdf")


if __name__ == "__main__":
    generate()
