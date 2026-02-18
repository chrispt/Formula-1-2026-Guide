"""PDF 3: F1 2026 Driver & Team Guide -- All 11 teams, 22 drivers, profiles, storylines."""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from f1_pdf_style import F1PDF, TEAM_COLORS


def generate():
    pdf = F1PDF(
        title="2026 Driver & Team Guide",
        subtitle="Teams, Drivers & Key Storylines"
    )
    pdf.add_cover_page()
    pdf.add_page()

    # -- Full Grid Table ---------------------------------------------------
    pdf.section_header("2026 Full Grid")
    pdf.body_text(
        "The 2026 season features 11 teams and 22 drivers - the first time "
        "F1 has had more than 10 teams since 2016. Cadillac enters as the "
        "newest constructor."
    )

    grid = [
        ["1",  "Red Bull Racing",      "Ford", "Max Verstappen",    "Isack Hadjar"],
        ["2",  "Ferrari",              "Ferrari", "Lewis Hamilton",    "Charles Leclerc"],
        ["3",  "McLaren",              "Mercedes", "Lando Norris",     "Oscar Piastri"],
        ["4",  "Mercedes",             "Mercedes", "George Russell",   "Kimi Antonelli"],
        ["5",  "Aston Martin",         "Honda", "Fernando Alonso",   "Lance Stroll"],
        ["6",  "Alpine",               "Mercedes", "Pierre Gasly",     "Franco Colapinto"],
        ["7",  "Williams",             "Mercedes", "Carlos Sainz",     "Alexander Albon"],
        ["8",  "Racing Bulls",         "Ford", "Liam Lawson",       "Arvid Lindblad"],
        ["9",  "Haas",                 "Ferrari", "Esteban Ocon",     "Oliver Bearman"],
        ["10", "Sauber (Audi)",        "Audi", "Nico Hulkenberg",   "Gabriel Bortoleto"],
        ["11", "Cadillac",             "Ferrari", "Valtteri Bottas",   "Sergio Perez"],
    ]

    pdf.styled_table(
        headers=["#", "Team", "PU", "Driver 1", "Driver 2"],
        data=grid,
        col_widths=[10, 42, 24, 42, 42],
    )

    # Stat callout after grid
    pdf.stat_callout([
        ("11", "Teams"),
        ("22", "Drivers"),
        ("1", "Rookie"),
        ("5", "Sophomores"),
    ])

    # -- Team Profiles (as cards) ------------------------------------------
    pdf.section_header("Team Profiles")

    teams = [
        {
            "name": "Red Bull Racing",
            "base": "Milton Keynes, UK",
            "principal": "Christian Horner",
            "pu": "Ford",
            "drivers": "Max Verstappen (NED) / Isack Hadjar (FRA)",
            "story": (
                "Back-to-back constructors' champions (2022-2023), Red Bull "
                "enter 2026 with Max Verstappen hungry for redemption after narrowly "
                "losing the 2025 title to Lando Norris by just 2 points. Despite "
                "a remarkable late-season surge, Verstappen fell agonizingly short. "
                "The four-time world champion (2021-2024) is determined to reclaim "
                "the championship under the radical new regulations. Isack "
                "Hadjar, the 2024 F2 runner-up, steps up after a strong rookie "
                "season at Racing Bulls in 2025 (51 points, including a podium)."
            ),
        },
        {
            "name": "Scuderia Ferrari",
            "base": "Maranello, Italy",
            "principal": "Fred Vasseur",
            "pu": "Ferrari",
            "drivers": "Lewis Hamilton (GBR) / Charles Leclerc (MON)",
            "story": (
                "Lewis Hamilton enters his second year at Ferrari, determined to "
                "prove his difficult 2025 season was an anomaly. In his first year "
                "at the Scuderia, Hamilton finished 6th in the standings with zero "
                "Grand Prix podiums, scoring 86 points fewer than teammate Charles "
                "Leclerc. The seven-time world champion will be eager to show that "
                "the new 2026 regulations can reset his fortunes. Leclerc, who "
                "comprehensively outperformed Hamilton in 2025, looks to build on "
                "that momentum and challenge for the title."
            ),
        },
        {
            "name": "McLaren F1 Team",
            "base": "Woking, UK",
            "principal": "Andrea Stella",
            "pu": "Mercedes",
            "drivers": "Lando Norris (GBR) / Oscar Piastri (AUS)",
            "story": (
                "The reigning double champions enter 2026 as the team to beat. "
                "Lando Norris won the 2025 World Drivers' Championship - his first "
                "title - in a dramatic finale, beating Verstappen by just 2 points. "
                "McLaren also secured back-to-back Constructors' Championships "
                "(2024-2025). Oscar Piastri finished 3rd in the 2025 standings, "
                "confirming his status as a top-tier talent. Can Norris and McLaren "
                "three-peat under the radical new regulations?"
            ),
        },
        {
            "name": "Mercedes-AMG Petronas",
            "base": "Brackley, UK",
            "principal": "Toto Wolff",
            "pu": "Mercedes",
            "drivers": "George Russell (GBR) / Kimi Antonelli (ITA)",
            "story": (
                "Post-Hamilton Mercedes rebuilds around George Russell and Kimi "
                "Antonelli, now entering his second season after a promising debut "
                "year in 2025. The team's power unit is supplied to four teams total "
                "(McLaren, Alpine, Williams), giving Mercedes significant engine "
                "development leverage."
            ),
        },
        {
            "name": "Aston Martin Aramco",
            "base": "Silverstone, UK",
            "principal": "Adrian Newey",
            "pu": "Honda",
            "drivers": "Fernando Alonso (ESP) / Lance Stroll (CAN)",
            "story": (
                "Fernando Alonso, now 44, continues to defy age in what could be "
                "one of his final seasons. Adrian Newey's arrival as team principal "
                "brings the legendary designer's expertise to Aston Martin's "
                "ambitious project. The new Silverstone campus and Honda power unit "
                "supply make this a pivotal year for the team's long-term ambitions "
                "under Lawrence Stroll's ownership."
            ),
        },
        {
            "name": "Alpine F1 Team",
            "base": "Enstone, UK / Viry, France",
            "principal": "Flavio Briatore (Exec. Advisor)",
            "pu": "Mercedes",
            "drivers": "Pierre Gasly (FRA) / Franco Colapinto (ARG)",
            "story": (
                "Alpine's biggest change: dropping their in-house Renault engine "
                "for Mercedes power. Pierre Gasly leads the team alongside Franco "
                "Colapinto, now in his second season after replacing Jack Doohan "
                "early in 2025 and impressing with his speed. The team aims "
                "for a fresh start with new leadership."
            ),
        },
        {
            "name": "Williams Racing",
            "base": "Grove, UK",
            "principal": "James Vowles",
            "pu": "Mercedes",
            "drivers": "Carlos Sainz (ESP) / Alexander Albon (THA)",
            "story": (
                "Carlos Sainz's arrival from Ferrari gives Williams their most "
                "experienced driver lineup in years. Paired with the consistent "
                "Alex Albon, the team looks to capitalize on the regulation reset "
                "to return to midfield competitiveness under James Vowles' leadership."
            ),
        },
        {
            "name": "Visa Cash App Racing Bulls",
            "base": "Faenza, Italy",
            "principal": "Laurent Mekies",
            "pu": "Ford",
            "drivers": "Liam Lawson (NZL) / Arvid Lindblad (GBR)",
            "story": (
                "Liam Lawson takes on the team leader role after a turbulent 2025 "
                "that saw him promoted to Red Bull mid-season, then reassigned for "
                "2026. British teenage talent Arvid Lindblad is the grid's only "
                "true rookie, graduating from the Red Bull junior program. At just "
                "18, Lindblad is one of the youngest drivers in F1 history."
            ),
        },
        {
            "name": "MoneyGram Haas F1 Team",
            "base": "Kannapolis, USA / Maranello, Italy",
            "principal": "Ayao Komatsu",
            "pu": "Ferrari",
            "drivers": "Esteban Ocon (FRA) / Oliver Bearman (GBR)",
            "story": (
                "Haas continues its rebuilding phase with Esteban Ocon joining from "
                "Alpine and Oliver Bearman in his second full season after scoring "
                "41 points as a rookie in 2025. The Ferrari power unit and closer "
                "technical ties give Haas reason for optimism."
            ),
        },
        {
            "name": "Sauber / Audi F1 Team",
            "base": "Hinwil, Switzerland",
            "principal": "Mattia Binotto",
            "pu": "Audi",
            "drivers": "Nico Hulkenberg (GER) / Gabriel Bortoleto (BRA)",
            "story": (
                "2026 marks the full Audi takeover, with the German manufacturer "
                "supplying their own power unit for the first time. Mattia Binotto "
                "leads the project, with Nico Hulkenberg providing experience and "
                "Gabriel Bortoleto entering his second season after a solid rookie "
                "year at Sauber in 2025. The Audi PU is the great unknown of the "
                "new regulations."
            ),
        },
        {
            "name": "Cadillac F1 Team",
            "base": "Fishers, Indiana, USA",
            "principal": "Graeme Lowdon",
            "pu": "Ferrari (customer)",
            "drivers": "Valtteri Bottas (FIN) / Sergio Perez (MEX)",
            "story": (
                "Formula 1's 11th team and the first new constructor since Haas in "
                "2016. Backed by General Motors, Cadillac enters with a Ferrari "
                "customer power unit while developing their own GM engine for the "
                "future. Valtteri Bottas brings valuable experience, while Sergio "
                "Perez adds massive know-how as a former race winner and longtime "
                "Red Bull driver. Under team principal Graeme Lowdon, the team aims "
                "to establish itself quickly."
            ),
        },
    ]

    for team in teams:
        pdf.team_card(
            name=team["name"],
            base=team["base"],
            principal=team["principal"],
            pu=team["pu"],
            drivers=team["drivers"],
            story=team["story"],
            team_color=TEAM_COLORS.get(team["name"]),
        )

    # -- Rising Stars ------------------------------------------------------
    pdf.section_header("Rising Stars")
    pdf.body_text(
        "The 2026 grid features one true rookie and five exciting second-year "
        "drivers making their mark in the sport."
    )

    rising_stars = [
        ["Arvid Lindblad", "GBR", "Racing Bulls", "The grid's ONLY rookie. 18 years old; one of the youngest F1 drivers ever."],
        ["Isack Hadjar", "FRA", "Red Bull Racing", "Second year. Strong 2025 at Racing Bulls (51 pts, podium). 2024 F2 runner-up."],
        ["Kimi Antonelli", "ITA", "Mercedes", "Second year. Italian prodigy in his sophomore Mercedes season."],
        ["Oliver Bearman", "GBR", "Haas", "Second year. Scored 41 points as a Haas rookie in 2025."],
        ["Gabriel Bortoleto", "BRA", "Sauber / Audi", "Second year. 2024 F2 Champion; solid debut season at Sauber."],
        ["Franco Colapinto", "ARG", "Alpine", "Second year. Replaced Doohan mid-2025 at Alpine; impressed with speed."],
    ]

    pdf.styled_table(
        headers=["Driver", "Nat.", "Team", "Notes"],
        data=rising_stars,
        col_widths=[30, 12, 36, 114],
        font_size=9,
    )

    # -- Key Storylines ----------------------------------------------------
    pdf.section_header("Key Storylines for 2026")

    pdf.subsection_header("Norris Defends His Crown")
    pdf.body_text(
        "Lando Norris won the 2025 World Drivers' Championship by just 2 points "
        "over Max Verstappen in one of the most dramatic title fights in recent "
        "memory. Can he and McLaren three-peat as both Drivers' and Constructors' "
        "Champions? The regulation revolution will test whether their dominance "
        "can survive a complete rule reset."
    )

    pdf.subsection_header("Verstappen's Redemption")
    pdf.body_text(
        "Max Verstappen lost his title in 2025 after a remarkable late-season "
        "charge - but it wasn't enough, "
        "falling 2 points short. The four-time champion (2021-2024) enters 2026 "
        "with a rage-fueled determination to reclaim what he considers his. New "
        "regulations could either help or hinder Red Bull's cause."
    )

    pdf.subsection_header("Hamilton's Second Chance at Ferrari")
    pdf.body_text(
        "Lewis Hamilton's first season at Ferrari in 2025 was the worst of his "
        "career: 6th in the standings, zero Grand Prix podiums, and 86 points "
        "behind teammate Leclerc. The seven-time champion enters 2026 viewing "
        "the regulation reset as his opportunity to prove 2025 was an aberration, "
        "not a decline. All eyes are on whether Hamilton can recapture his magic."
    )

    pdf.subsection_header("The Regulation Revolution")
    pdf.body_text(
        "The 2026 regulations are the biggest overhaul in over a decade. New "
        "power units, active aerodynamics, sustainable fuels, and smaller cars "
        "create a level playing field. Every team starts from scratch, making "
        "this the most unpredictable season in years. New entrants Audi and "
        "Cadillac have a unique opportunity to be competitive from day one."
    )

    # Closing Season Preview info_box
    pdf.info_box(
        "Season Preview",
        "The 2026 season promises to be one of the most exciting in F1 "
        "history. With the biggest regulation change in a decade, defending "
        "champion Norris, a vengeful Verstappen, Hamilton seeking redemption "
        "at Ferrari, a new manufacturer (Audi), a new team (Cadillac), and "
        "one of the youngest rookies in F1 history in Lindblad, every race weekend "
        "will offer drama."
    )

    pdf.save("2026-Driver-Team-Guide.pdf")


if __name__ == "__main__":
    generate()
