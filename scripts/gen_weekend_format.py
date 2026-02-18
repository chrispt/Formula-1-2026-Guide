"""PDF 6: F1 2026 Race Weekend Format -- Standard & sprint formats, qualifying, points."""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from f1_pdf_style import F1PDF
import f1_graphics


def generate():
    pdf = F1PDF(
        title="2026 Race Weekend Format",
        subtitle="Weekend Schedules, Qualifying & Points"
    )
    pdf.add_cover_page()
    pdf.add_page()

    # -- Standard Weekend --------------------------------------------------
    pdf.section_header("Standard Race Weekend")
    pdf.body_text(
        "A standard Formula 1 weekend spans three days (Friday to Sunday) "
        "and follows a consistent format of practice, qualifying, and race."
    )

    # Stat callout: key numbers
    pdf.stat_callout([
        ("3", "Days"),
        ("5", "Sessions"),
        ("305", "Race km"),
    ])

    timeline_img = f1_graphics.weekend_timeline()
    pdf.add_diagram(timeline_img, w=180, caption="Standard vs Sprint weekend session schedules")

    pdf.subsection_header("Friday")
    pdf.styled_table(
        headers=["Session", "Duration", "Purpose"],
        data=[
            ["Free Practice 1 (FP1)", "60 minutes",
             "Initial setup, tire evaluation, system checks"],
            ["Free Practice 2 (FP2)", "60 minutes",
             "Long runs, race simulations, fine-tuning"],
        ],
        col_widths=[50, 30, 112],
        font_size=9,
    )
    pdf.body_text(
        "FP1 often features rookie or reserve driver outings, as teams "
        "are required to run a young driver in at least two FP1 sessions "
        "per season."
    )

    pdf.subsection_header("Saturday")
    pdf.styled_table(
        headers=["Session", "Duration", "Purpose"],
        data=[
            ["Free Practice 3 (FP3)", "60 minutes",
             "Final setup, qualifying preparation"],
            ["Qualifying", "~60 minutes",
             "Determines grid positions (Q1/Q2/Q3 format)"],
        ],
        col_widths=[50, 30, 112],
        font_size=9,
    )

    pdf.subsection_header("Sunday")
    pdf.styled_table(
        headers=["Session", "Details"],
        data=[
            ["Drivers' Parade", "Pre-race fan engagement (track tour)"],
            ["Formation Lap", "Grid forms, warm-up lap to grid positions"],
            ["Grand Prix Race", "Full race distance (typically 305 km / ~57-70 laps)"],
            ["Podium Ceremony", "Top 3 celebration, trophies, national anthems"],
        ],
        col_widths=[50, 142],
        font_size=9,
    )

    # -- Sprint Weekend ----------------------------------------------------
    pdf.section_header("Sprint Race Weekend")
    pdf.body_text(
        "Six weekends in 2026 use the Sprint format. This compressed "
        "schedule replaces FP2 and FP3 with Sprint Qualifying and a "
        "short Sprint Race, adding an extra competitive session on Saturday."
    )

    pdf.subsection_header("Friday")
    pdf.styled_table(
        headers=["Session", "Duration", "Purpose"],
        data=[
            ["Free Practice 1 (FP1)", "60 minutes",
             "Only practice session of the weekend"],
            ["Sprint Qualifying (SQ)", "~36 minutes",
             "SQ1/SQ2/SQ3 to set Sprint grid"],
        ],
        col_widths=[55, 30, 107],
        font_size=9,
    )

    pdf.subsection_header("Saturday")
    pdf.styled_table(
        headers=["Session", "Duration", "Purpose"],
        data=[
            ["Sprint Race", "~30 min (100 km)",
             "Short race, separate points awarded"],
            ["Qualifying", "~60 minutes",
             "Sets grid for Sunday's Grand Prix"],
        ],
        col_widths=[55, 30, 107],
        font_size=9,
    )

    pdf.subsection_header("Sunday")
    pdf.body_text(
        "Sunday is identical to a standard weekend: formation lap, "
        "Grand Prix, and podium ceremony."
    )

    pdf.info_box(
        "Sprint Weekend Note",
        "Parc ferme conditions apply from the start of Sprint Qualifying. "
        "Teams must balance setup for both the Sprint and the Grand Prix "
        "with very limited practice data from just one FP session."
    )

    # -- Qualifying Format -------------------------------------------------
    pdf.section_header("Qualifying Format (Q1 / Q2 / Q3)")
    pdf.body_text(
        "Qualifying uses a three-part knockout format to determine the "
        "starting grid for the Grand Prix."
    )

    pdf.styled_table(
        headers=["Phase", "Duration", "Drivers", "Eliminated", "Grid Positions Set"],
        data=[
            ["Q1", "18 minutes", "All 22", "Slowest 6", "P17 - P22"],
            ["Q2", "15 minutes", "Remaining 16", "Slowest 6", "P11 - P16"],
            ["Q3", "12 minutes", "Top 10", "None (ranked)", "P1 - P10"],
        ],
        col_widths=[18, 26, 34, 38, 50],
    )

    pdf.body_text(
        "With 22 drivers (11 teams), Q1 eliminates the bottom 6, Q2 the "
        "next 6, and Q3 determines the top 10 positions. The fastest "
        "driver in Q3 earns pole position."
    )

    pdf.info_box(
        "107% Rule",
        "Any driver who fails to set a Q1 time within 107% of the fastest "
        "Q1 lap may not be permitted to start the race, at the stewards' "
        "discretion."
    )

    # -- Sprint Qualifying Format ------------------------------------------
    pdf.subsection_header("Sprint Qualifying (SQ1 / SQ2 / SQ3)")
    pdf.body_text(
        "Sprint Qualifying mirrors the main qualifying format but with "
        "shorter sessions:"
    )
    pdf.styled_table(
        headers=["Phase", "Duration", "Eliminated"],
        data=[
            ["SQ1", "12 minutes", "Slowest 6"],
            ["SQ2", "10 minutes", "Slowest 6"],
            ["SQ3", "8 minutes", "None (top 10 ranked)"],
        ],
        col_widths=[30, 30, 60],
    )

    # -- Race Day Procedures -----------------------------------------------
    pdf.section_header("Race Day Procedures")

    pdf.subsection_header("Pre-Race")
    pdf.bullet_list([
        "Pit lane opens 30 minutes before race start",
        "Cars take positions on the grid",
        "All cars must be on the grid 10 minutes before the start",
        "Tire blankets removed, teams clear the grid",
    ])

    pdf.subsection_header("Race Start")
    pdf.bullet_list([
        "Formation lap: Cars follow the pole-sitter around the circuit "
        "to warm tires and brakes",
        "Cars return to grid positions for a standing start",
        "Five red lights illuminate sequentially, then all extinguish "
        "simultaneously to signal the start",
        "Jump start penalties are detected automatically via sensors",
    ])

    # Lights-out info box for newcomers
    pdf.info_box(
        "Lights Out! - The Iconic F1 Start",
        "The race start is one of F1's most thrilling moments. Five red "
        "lights come on one by one (about 1 second apart), then all go "
        "out at once. Drivers must react instantly - the best reaction "
        "times are under 0.2 seconds. A jump start (moving before lights "
        "out) results in a penalty."
    )

    pdf.subsection_header("During the Race")
    pdf.bullet_list([
        "Pit stops: Mandatory - at least one stop required, as drivers must "
        "use at least two different dry tire compounds during a dry race",
        "Active aero (X-mode) is available on designated straights, "
        "replacing the old DRS system",
        "Blue flags: Lapped cars must let leaders through within 3 flag points",
        "Track limits: Exceeding track boundaries leads to lap time deletion "
        "or time penalties",
    ])

    pdf.subsection_header("Race End & Classification")
    pdf.bullet_list([
        "Checkered flag shown to race leader after completing full race distance",
        "All cars must cross the finish line to be classified",
        "Race must complete at least 75% distance (2 laps behind safety car) "
        "for full points to be awarded",
        "If less than 75%, reduced points are awarded",
        "Post-race parc ferme and technical inspections follow",
    ])

    # -- Points System -----------------------------------------------------
    pdf.section_header("Points System")

    pdf.subsection_header("Grand Prix Points (Top 10)")
    pdf.styled_table(
        headers=["Pos", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"],
        data=[
            ["Pts", "25", "18", "15", "12", "10", "8", "6", "4", "2", "1"],
        ],
        col_widths=[17.4] * 11,
    )
    pdf.body_text(
        "Points are awarded to the top 10 finishers only. There is no "
        "bonus point for fastest lap (abolished from 2025 onwards)."
    )

    pdf.subsection_header("Sprint Points (Top 8)")
    pdf.styled_table(
        headers=["Pos", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"],
        data=[
            ["Pts", "8", "7", "6", "5", "4", "3", "2", "1"],
        ],
        col_widths=[21.3] * 9,
    )
    pdf.body_text(
        "No fastest lap point is awarded in Sprint races. Sprint results "
        "count toward both the Drivers' and Constructors' Championships."
    )

    pdf.info_box(
        "Maximum Points Per Weekend",
        "Standard weekend: 25 pts (race win). "
        "Sprint weekend: 33 pts (8 Sprint win + 25 race win)."
    )

    # Stat callout for points
    pdf.stat_callout([
        ("25", "Max Pts (Standard)"),
        ("33", "Max Pts (Sprint)"),
        ("25", "Race Win"),
        ("8", "Sprint Win"),
    ])

    pdf.save("2026-Race-Weekend-Format.pdf")


if __name__ == "__main__":
    generate()
