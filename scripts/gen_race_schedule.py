"""PDF 1: F1 2026 Race Schedule -- Full 24-race calendar with sprint weekends."""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from f1_pdf_style import F1PDF
import f1_graphics


def generate():
    pdf = F1PDF(
        title="2026 Race Schedule",
        subtitle="Race Calendar & Key Dates"
    )
    pdf.add_cover_page()
    pdf.add_page()

    # -- Pre-Season Testing ------------------------------------------------
    pdf.section_header("Pre-Season Testing")
    pdf.body_text(
        "Three rounds of official pre-season testing take place before the "
        "first Grand Prix, giving teams their first chance to run the "
        "revolutionary 2026 cars on track."
    )
    pdf.styled_table(
        headers=["Test", "Circuit", "Location", "Dates"],
        data=[
            ["Test 1", "Circuit de Barcelona-Catalunya", "Barcelona, Spain", "Jan 26 - 30"],
            ["Test 2", "Bahrain International Circuit", "Sakhir, Bahrain", "Feb 11 - 13"],
            ["Test 3", "Bahrain International Circuit", "Sakhir, Bahrain", "Feb 18 - 20"],
        ],
        col_widths=[25, 65, 55, 45],
    )
    pdf.info_box(
        "Testing Format",
        "Each test day runs two 4-hour sessions (morning and afternoon). "
        "All 11 teams participate simultaneously. Tire testing for Pirelli "
        "is integrated into the schedule."
    )

    # -- Full Race Calendar ------------------------------------------------
    pdf.section_header("2026 Race Calendar")
    pdf.body_text(
        "The 2026 season features 24 Grands Prix across five continents. "
        "Six weekends feature the Sprint format (marked with * below)."
    )

    # Stat callout: headline numbers
    pdf.stat_callout([
        ("24", "Grands Prix"),
        ("6", "Sprints"),
        ("21", "Countries"),
        ("5", "Continents"),
    ])

    timeline_img = f1_graphics.season_timeline()
    pdf.add_diagram(timeline_img, w=180, caption="2026 Season Overview: 24 races from March to December")

    races = [
        ["1",  "Australian Grand Prix",     "Albert Park",                  "Melbourne, Australia",      "Mar 8",    ""],
        ["2",  "Chinese Grand Prix*",        "Shanghai Int'l Circuit",       "Shanghai, China",           "Mar 15",   "Sprint"],
        ["3",  "Japanese Grand Prix",        "Suzuka Circuit",               "Suzuka, Japan",             "Mar 29",   ""],
        ["4",  "Bahrain Grand Prix",         "Bahrain Int'l Circuit",        "Sakhir, Bahrain",           "Apr 12",   ""],
        ["5",  "Saudi Arabian Grand Prix",   "Jeddah Corniche Circuit",      "Jeddah, Saudi Arabia",      "Apr 19",   ""],
        ["6",  "Miami Grand Prix*",          "Miami Int'l Autodrome",        "Miami, USA",                "May 3",    "Sprint"],
        ["7",  "Canadian Grand Prix*",       "Circuit Gilles Villeneuve",    "Montreal, Canada",          "May 24",   "Sprint"],
        ["8",  "Monaco Grand Prix",          "Circuit de Monaco",            "Monte Carlo, Monaco",       "Jun 7",    ""],
        ["9",  "Spanish Grand Prix",         "Circuit de Barcelona-Catalunya","Barcelona, Spain",          "Jun 14",   ""],
        ["10", "Austrian Grand Prix",        "Red Bull Ring",                "Spielberg, Austria",        "Jun 28",   ""],
        ["11", "British Grand Prix*",        "Silverstone Circuit",          "Silverstone, UK",           "Jul 5",    "Sprint"],
        ["12", "Belgian Grand Prix",         "Spa-Francorchamps",            "Stavelot, Belgium",         "Jul 19",   ""],
        ["13", "Hungarian Grand Prix",       "Hungaroring",                  "Budapest, Hungary",         "Jul 26",   ""],
        ["--", "SUMMER BREAK",               "",                             "",                          "Aug 3-22", ""],
        ["14", "Dutch Grand Prix*",          "Circuit Zandvoort",            "Zandvoort, Netherlands",    "Aug 23",   "Sprint"],
        ["15", "Italian Grand Prix",         "Autodromo di Monza",           "Monza, Italy",              "Sep 6",    ""],
        ["16", "Madrid Grand Prix",          "Madrid Circuit",               "Madrid, Spain",             "Sep 13",   ""],
        ["17", "Azerbaijan Grand Prix",      "Baku City Circuit",            "Baku, Azerbaijan",          "Sep 26",   ""],
        ["18", "Singapore Grand Prix*",      "Marina Bay Street Circuit",    "Singapore",                 "Oct 11",   "Sprint"],
        ["19", "United States Grand Prix",   "Circuit of the Americas",      "Austin, USA",               "Oct 25",   ""],
        ["20", "Mexican Grand Prix",         "Autodromo H. Rodriguez",       "Mexico City, Mexico",       "Nov 1",    ""],
        ["21", "Brazilian Grand Prix",       "Interlagos",                   "Sao Paulo, Brazil",         "Nov 8",    ""],
        ["22", "Las Vegas Grand Prix",       "Las Vegas Street Circuit",     "Las Vegas, USA",            "Nov 22",   ""],
        ["23", "Qatar Grand Prix",           "Lusail Int'l Circuit",         "Lusail, Qatar",             "Nov 29",   ""],
        ["24", "Abu Dhabi Grand Prix",       "Yas Marina Circuit",           "Abu Dhabi, UAE",            "Dec 6",    ""],
    ]

    pdf.styled_table(
        headers=["Rd", "Grand Prix", "Circuit", "Location", "Date", "Format"],
        data=races,
        col_widths=[12, 52, 48, 42, 22, 16],
        font_size=8,
    )

    # Newcomer tip
    pdf.info_box(
        "How to Read the Calendar",
        "Each Grand Prix takes place over a full weekend (Friday-Sunday). "
        "Rounds marked with * use the Sprint format, which features a "
        "shorter Sprint race on Saturday in addition to the main Grand Prix "
        "on Sunday. See the Race Weekend Format guide for full details."
    )

    # -- Sprint Weekends ---------------------------------------------------
    pdf.section_header("Sprint Weekends")
    pdf.body_text(
        "Six Grands Prix feature the Sprint format, which replaces FP2 and "
        "FP3 with Sprint Qualifying and a shorter Sprint Race on Saturday."
    )
    sprint_rounds = [
        ["2",  "Chinese Grand Prix",   "Shanghai",   "Mar 15"],
        ["6",  "Miami Grand Prix",     "Miami",      "May 3"],
        ["7",  "Canadian Grand Prix",  "Montreal",   "May 24"],
        ["11", "British Grand Prix",   "Silverstone", "Jul 5"],
        ["14", "Dutch Grand Prix",     "Zandvoort",  "Aug 23"],
        ["18", "Singapore Grand Prix", "Singapore",  "Oct 11"],
    ]
    pdf.styled_table(
        headers=["Rd", "Grand Prix", "Location", "Date"],
        data=sprint_rounds,
        col_widths=[15, 60, 55, 40],
    )

    # Colored divider between sections
    pdf.colored_divider()

    # -- Key Dates & Notes -------------------------------------------------
    pdf.section_header("Key Dates & Notes")
    pdf.info_box(
        "Madrid GP Debut",
        "Round 16 marks the inaugural Madrid Grand Prix, held on a new "
        "purpose-built circuit in the Spanish capital. Madrid joins the "
        "calendar as an addition alongside Barcelona, giving Spain two "
        "Grands Prix."
    )
    pdf.info_box(
        "Zandvoort Final Year",
        "2026 is the final season for the Dutch Grand Prix at Zandvoort. "
        "The race has been on the calendar since its return in 2021."
    )
    pdf.info_box(
        "Summer Break",
        "The mandatory summer shutdown runs August 3-22. All team factories "
        "must close for a consecutive 14-day period within this window."
    )
    pdf.info_box(
        "Season Span",
        "The 2026 season runs from March 8 to December 6 - a 39-week season "
        "covering 24 races across 21 countries on 5 continents."
    )

    pdf.save("2026-Race-Schedule.pdf")


if __name__ == "__main__":
    generate()
