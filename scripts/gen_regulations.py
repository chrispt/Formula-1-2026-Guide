"""PDF 2: F1 2026 Regulation Changes -- Power unit, aero, car design, budget cap, fuels."""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from f1_pdf_style import F1PDF
import f1_graphics


def generate():
    pdf = F1PDF(
        title="F1 2026 Regulation Changes",
        subtitle="Technical & Sporting Regulations"
    )
    pdf.add_cover_page()
    pdf.add_page()

    # -- Overview ----------------------------------------------------------
    pdf.section_header("Overview")
    pdf.body_text(
        "The 2026 Formula 1 regulations represent the most significant "
        "overhaul in over a decade. Every major area of the car is affected: "
        "power units, aerodynamics, chassis dimensions, fuel, and the "
        "financial regulations. The goals are to improve racing, increase "
        "sustainability, reduce costs, and attract new manufacturers."
    )

    # Stat callout: headline regulation numbers
    pdf.stat_callout([
        ("350", "kW MGU-K"),
        ("768", "kg Min Weight"),
        ("100%", "Sustainable"),
        ("$215M", "Budget Cap"),
    ])

    pdf.info_box(
        "Why 2026?",
        "The current Concorde Agreement, power unit regulations, and "
        "aerodynamic rules all converge for a reset in 2026. This alignment "
        "created a natural opportunity for a comprehensive regulation change "
        "and attracted new entrants like Audi and Cadillac/GM."
    )

    # -- Power Unit --------------------------------------------------------
    pdf.section_header("Power Unit Overhaul")
    pdf.body_text(
        "The 2026 power unit is a radical departure from the current design. "
        "The electrical component of the powertrain is dramatically increased, "
        "targeting a roughly 50/50 split between electric and combustion power."
    )

    pu_img = f1_graphics.power_unit_split()
    pdf.add_diagram(pu_img, w=160, caption="Power unit energy split: 2025 vs 2026")

    pdf.subsection_header("Key Changes")
    pdf.bullet_list([
        "MGU-H (Motor Generator Unit - Heat) is eliminated entirely, "
        "simplifying the power unit and reducing costs",
        "MGU-K output increases from 120 kW to 350 kW (nearly triple), "
        "making electric power roughly equal to ICE output",
        "Battery (Energy Store) capacity significantly increased to support "
        "the higher MGU-K output",
        "Internal combustion engine (ICE) output decreases to approximately "
        "400 kW, down from ~550 kW",
        "Total system output remains similar to current cars (~750 kW / "
        "~1,000 bhp), but the power delivery changes dramatically",
        "Engine RPM limit remains at 15,000 but expected operating range "
        "may shift with the new power balance",
    ])

    pdf.subsection_header("Power Unit Suppliers")
    pdf.styled_table(
        headers=["Supplier", "Teams Supplied", "Status"],
        data=[
            ["Ferrari", "Ferrari, Haas, Cadillac", "Incumbent"],
            ["Mercedes", "Mercedes, McLaren, Alpine, Williams", "Incumbent"],
            ["Ford", "Red Bull Racing, Racing Bulls", "New partnership"],
            ["Honda", "Aston Martin", "Incumbent"],
            ["Audi", "Sauber/Audi", "New entrant"],
        ],
        col_widths=[35, 80, 30],
    )

    pdf.info_box(
        "Why Remove the MGU-H?",
        "The MGU-H was the most complex and expensive component of the "
        "current power unit, creating a barrier for new manufacturers. "
        "Its removal lowers costs, simplifies the architecture, and was "
        "a key condition for Audi's entry and GM/Cadillac's future engine "
        "plans."
    )

    # -- Sustainable Fuel --------------------------------------------------
    pdf.section_header("Sustainable Fuels")
    pdf.body_text(
        "For the first time, Formula 1 mandates 100% advanced sustainable "
        "fuel. This is a cornerstone of the sport's commitment to reaching "
        "net-zero carbon by 2030."
    )

    pdf.bullet_list([
        "Fuel must be 100% sustainable (non-fossil origin)",
        "Can be produced from municipal waste, agricultural waste, or "
        "captured carbon combined with green hydrogen (e-fuels)",
        "Must be a 'drop-in' fuel compatible with standard fuel "
        "infrastructure and similar energy density to current fuels",
        "Fuel flow rate adjusted to account for the shift in power balance "
        "toward electric energy",
        "All fuel suppliers must meet FIA sustainability certification "
        "standards",
    ])

    pdf.info_box(
        "Real-World Impact",
        "F1's sustainable fuel development is intended to accelerate "
        "technology that can eventually be used in road cars and other "
        "transportation. The goal is to prove that high-performance "
        "sustainable fuels are viable at the highest level of motorsport."
    )

    # -- Active Aerodynamics -----------------------------------------------
    pdf.section_header("Active Aerodynamics")
    pdf.body_text(
        "The 2026 cars introduce active aerodynamics as a replacement for "
        "the Drag Reduction System (DRS). Instead of a simple rear wing "
        "flap, both the front and rear wings can change their configuration "
        "in real time."
    )

    pdf.subsection_header("How It Works")
    pdf.bullet_list([
        "Both front and rear wing elements are adjustable, changing angle "
        "and configuration during the lap",
        "X-Mode (low drag): Wing elements open/flatten on straights to "
        "minimize drag and maximize top speed",
        "Z-Mode (high downforce): Wings in maximum downforce configuration "
        "for cornering and braking zones",
        "Unlike DRS, active aero is available to all cars, not just those "
        "within 1 second of the car ahead",
        "The system operates automatically based on speed, throttle position, "
        "and track zones, with some driver input",
    ])

    pdf.subsection_header("DRS vs. Active Aero Comparison")
    pdf.styled_table(
        headers=["Feature", "DRS (2011-2025)", "Active Aero (2026+)"],
        data=[
            ["Wings affected", "Rear only", "Front and rear"],
            ["Activation", "Within 1s of car ahead", "Available to all cars"],
            ["Detection zones", "Specific DRS zones", "Speed/zone-based"],
            ["Modes", "Open / Closed", "Multiple configurations"],
            ["Driver control", "Manual button", "Automatic + driver input"],
            ["Purpose", "Reduce rear drag for overtaking", "Full drag/downforce management"],
        ],
        col_widths=[35, 65, 65],
    )

    pdf.info_box(
        "Overtaking Impact",
        "The FIA projects that active aero, combined with reduced dirty air "
        "from the new regulations, will maintain or improve overtaking "
        "opportunities compared to DRS. The variable wing configurations "
        "add a new tactical dimension to racing."
    )

    # -- Car Design --------------------------------------------------------
    pdf.section_header("Car Design Changes")
    pdf.body_text(
        "The 2026 cars are significantly smaller, lighter, and designed to "
        "produce less disruptive wake for following cars."
    )

    pdf.subsection_header("Dimensions & Weight")
    pdf.bullet_list([
        "Minimum weight: 768 kg (down from 798 kg, a 30 kg reduction)",
        "Wheelbase: 200 mm shorter than current cars",
        "Overall width: 100 mm narrower",
        "Cars will be visually more compact and agile-looking",
        "Weight reduction achieved despite the larger, heavier battery",
    ])

    pdf.subsection_header("Floor & Downforce")
    pdf.bullet_list([
        "Venturi tunnels (the shaped floor channels used since 2022) are "
        "eliminated",
        "Replaced by a flat floor with a larger rear diffuser",
        "Ground effect downforce is still the primary source of grip, but "
        "generated differently",
        "The goal is to reduce the sensitivity of downforce to ride height "
        "and reduce porpoising",
        "Front wing is simpler with fewer elements, working with active "
        "aero system",
        "Rear wing designed around the active aero mechanism",
    ])

    pdf.subsection_header("Crash Structures & Safety")
    pdf.bullet_list([
        "Updated front and side impact structures",
        "Halo remains mandatory with updated integration requirements",
        "New rear impact structure specifications",
        "Roll hoop design updated following recent incidents",
        "Survival cell testing requirements increased",
    ])

    # -- 2025 vs 2026 Comparison -------------------------------------------
    pdf.section_header("2025 vs. 2026 Comparison")
    pdf.body_text(
        "A side-by-side look at the key differences between the outgoing "
        "2025 and incoming 2026 regulations."
    )

    comparison_data = [
        ["MGU-H", "Yes (120 kW harvest)", "Eliminated"],
        ["MGU-K Output", "120 kW", "350 kW"],
        ["ICE Output", "~550 kW", "~400 kW"],
        ["Total Power", "~750 kW", "~750 kW (different split)"],
        ["Electric Share", "~20%", "~50%"],
        ["Fuel", "10% sustainable blend", "100% sustainable"],
        ["Rear Wing", "DRS (passive)", "Active aero (multi-mode)"],
        ["Front Wing", "Fixed", "Active aero"],
        ["Floor", "Venturi tunnels", "Flat floor + diffuser"],
        ["Min. Weight", "798 kg", "768 kg"],
        ["Width", "2000 mm", "1900 mm"],
        ["Wheelbase", "~3,600 mm (typical)", "~3,400 mm"],
        ["Budget Cap", "~$140M", "$215M (expanded scope)"],
        ["Teams", "10", "11 (Cadillac joins)"],
        ["PU Suppliers", "4 (Ferrari, Merc, Honda, Renault)",
         "5 (Ferrari, Merc, Ford, Honda, Audi)"],
    ]

    pdf.styled_table(
        headers=["Category", "2025 Regulations", "2026 Regulations"],
        data=comparison_data,
        col_widths=[35, 65, 65],
        font_size=8,
    )

    # -- Budget Cap --------------------------------------------------------
    pdf.section_header("Budget Cap Changes")
    pdf.body_text(
        "The cost cap headline figure rises from approximately $140 million "
        "to $215 million, but this increase is largely due to expanding what "
        "is included rather than allowing more spending."
    )

    pdf.bullet_list([
        "Headline cap: $215 million (up from ~$140M)",
        "More items now fall under the cap, including previously excluded "
        "costs like power unit development allocations and marketing",
        "Power unit cost cap introduced separately to control engine "
        "development spending",
        "Sprint event bonuses and prize money adjustments factored in",
        "Penalty structure remains: minor overages (< 5%) result in fines "
        "and reduced wind tunnel time; major overages can result in points "
        "deductions or exclusion",
        "New team exemptions: Cadillac receives a temporary uplift in "
        "their first seasons to account for startup costs",
    ])

    pdf.info_box(
        "Why the Increase?",
        "The headline number looks much higher, but the real-terms spending "
        "limit has not increased dramatically. The broader scope brings more "
        "team spending under scrutiny, which should improve competitive "
        "balance and financial fairness across the grid."
    )

    # -- Sporting Regulation Changes ---------------------------------------
    pdf.section_header("Sporting Regulation Updates")

    pdf.subsection_header("Grid Expansion")
    pdf.body_text(
        "With 11 teams and 22 drivers, qualifying knockout thresholds are "
        "adjusted: Q1 eliminates 5 drivers (positions 18-22), Q2 eliminates "
        "5 more (positions 13-17), and Q3 features the top 12 drivers."
    )

    pdf.subsection_header("Sprint Format")
    pdf.body_text(
        "The Sprint format continues with 6 events in 2026. Points remain "
        "8-7-6-5-4-3-2-1 for the top 8 finishers. No fastest lap bonus in "
        "Sprints."
    )

    pdf.subsection_header("Power Unit Allocation")
    pdf.body_text(
        "Each driver is allowed a specific number of power unit components "
        "across the season before incurring grid penalties. With the simpler "
        "PU design (no MGU-H), allocation numbers are adjusted for 2026."
    )

    pdf.subsection_header("Testing & Development")
    pdf.bullet_list([
        "Pre-season testing expanded to three sessions (Barcelona + 2x Bahrain)",
        "In-season testing days slightly increased for the first year of "
        "new regulations",
        "Wind tunnel and CFD allocations continue to be based on inverse "
        "championship position (lower-placed teams get more development time)",
        "Aero testing period (ATR) reset for all teams at the start of 2026",
    ])

    # -- Summary -----------------------------------------------------------
    pdf.section_header("The Big Picture")
    pdf.body_text(
        "The 2026 regulations represent F1's vision for the future: cars that "
        "are lighter, more electric, powered by sustainable fuels, and designed "
        "to produce better racing. The elimination of the MGU-H and introduction "
        "of active aerodynamics are the two most visible changes, while the "
        "sustainable fuel mandate positions F1 as a leader in motorsport "
        "sustainability."
    )
    pdf.body_text(
        "For fans, the key impacts will be different-sounding cars (more "
        "electric whine, less turbocharged whoosh), new overtaking dynamics "
        "with active aero replacing DRS, and a larger, more diverse grid "
        "with new manufacturers and teams."
    )

    pdf.save("F1-2026-Regulation-Changes.pdf")


if __name__ == "__main__":
    generate()
