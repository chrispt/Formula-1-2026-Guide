"""PDF 7: F1 2026 Circuit Guide -- Notable circuits on the 2026 calendar."""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from f1_pdf_style import F1PDF
import f1_graphics


def circuit_profile(pdf, name, location, length, turns, lap_record,
                    special, famous_corners, overtaking):
    """Render a circuit profile using team_card-style layout."""
    x = 10
    card_w = pdf.w - 20

    # Build the description text with line breaks between sections
    desc_parts = []
    if special:
        desc_parts.append(special)
    if famous_corners:
        desc_parts.append(f"Famous sections: {famous_corners}")
    if overtaking:
        desc_parts.append(f"Overtaking: {overtaking}")
    desc_text = "\n".join(desc_parts)

    # Calculate height
    pdf.set_font("Helvetica", "", 9)
    text_h = pdf.multi_cell(card_w - 12, 4.5, desc_text, dry_run=True, output="HEIGHT")
    card_h = max(44, 3 + 7 + 6 + 6 + 3 + text_h + 4)

    if pdf.get_y() + card_h > pdf.h - 20:
        pdf.add_page()

    y = pdf.get_y()

    # White card with gray border
    from f1_pdf_style import SEPARATOR_GRAY, WHITE, F1_RED, F1_DARK, DARK_GRAY
    pdf.set_draw_color(*SEPARATOR_GRAY)
    pdf.set_line_width(0.3)
    pdf.set_fill_color(*WHITE)
    pdf.rect(x, y, card_w, card_h, "DF")

    # Red top accent bar
    pdf.set_fill_color(*F1_RED)
    pdf.rect(x, y, card_w, 3, "F")

    # Circuit name
    pdf.set_xy(x + 5, y + 5)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(*F1_DARK)
    pdf.cell(0, 6, name)

    # Location and stats
    pdf.set_xy(x + 5, y + 12)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*DARK_GRAY)
    pdf.cell(0, 5, f"{location}  |  {length}  |  {turns} turns  |  Lap record: {lap_record}")

    # Type label
    pdf.set_xy(x + 5, y + 19)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*F1_RED)
    circuit_type = "Street Circuit" if "street" in special.lower() or "street" in name.lower() else "Permanent Circuit"
    pdf.cell(0, 5, circuit_type)

    # Description
    pdf.set_xy(x + 5, y + 26)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*F1_DARK)
    pdf.multi_cell(card_w - 12, 4.5, desc_text)

    pdf.set_y(y + card_h + 5)


def generate():
    pdf = F1PDF(
        title="2026 Circuit Guide",
        subtitle="The Tracks of Formula 1"
    )
    pdf.add_cover_page()
    pdf.add_page()

    # -- Introduction ------------------------------------------------------
    pdf.section_header("Circuit Guide")
    pdf.body_text(
        "Formula 1 races at some of the most famous circuits in the world. "
        "Each track has its own character, challenges, and history. This guide "
        "covers the most notable circuits on the 2026 calendar to help new "
        "fans understand what makes each venue special."
    )

    pdf.stat_callout([
        ("24", "Race Venues"),
        ("5", "Continents"),
        ("4", "Street Circuits"),
        ("9", "Featured Here"),
    ])

    track_img = f1_graphics.track_outlines()
    pdf.add_diagram(track_img, w=180, caption="Simplified outlines of the 9 featured circuits")

    # -- Monaco ------------------------------------------------------------
    circuit_profile(
        pdf,
        name="Circuit de Monaco",
        location="Monte Carlo, Monaco",
        length="3.337 km (shortest on calendar)",
        turns="19",
        lap_record="1:12.909 (Lewis Hamilton, 2021)",
        special=(
            "The crown jewel of F1. This tight street circuit winds through "
            "the streets of Monte Carlo, past the famous Casino and along the "
            "harbor. Overtaking is nearly impossible, making qualifying and "
            "strategy crucial. It's the most prestigious race on the calendar "
            "and has been held since 1929."
        ),
        famous_corners=(
            "Casino Square (sharp hairpin after uphill climb), the Tunnel "
            "(unique light-to-dark transition at high speed), the Swimming "
            "Pool chicane (ultra-tight at the harbor), Rascasse (penultimate "
            "corner, slow hairpin)"
        ),
        overtaking=(
            "Extremely limited. The Nouvelle Chicane after the tunnel is the "
            "only realistic overtaking spot. Active aero zones will be minimal. "
            "Track position is everything at Monaco."
        ),
    )

    # -- Silverstone -------------------------------------------------------
    circuit_profile(
        pdf,
        name="Silverstone Circuit",
        location="Silverstone, United Kingdom",
        length="5.891 km",
        turns="18",
        lap_record="1:27.097 (Max Verstappen, 2020)",
        special=(
            "The home of British motorsport and where the first-ever Formula 1 "
            "World Championship race was held in 1950. Silverstone is one of "
            "the fastest circuits on the calendar, known for its high-speed "
            "corners that test aerodynamic performance. The passionate British "
            "crowd creates an electric atmosphere."
        ),
        famous_corners=(
            "Maggotts-Becketts-Chapel (legendary high-speed S-curves that "
            "are the ultimate test of car balance and driver courage), Copse "
            "(fast right-hander), Stowe (high-speed braking zone)"
        ),
        overtaking=(
            "Good opportunities at the end of the Wellington Straight into "
            "Brooklands and at the end of the Hangar Straight into Stowe. "
            "Active aero will be especially effective on the long straights."
        ),
    )

    # -- Spa-Francorchamps -------------------------------------------------
    circuit_profile(
        pdf,
        name="Spa-Francorchamps",
        location="Stavelot, Belgium",
        length="7.004 km (longest on calendar)",
        turns="19",
        lap_record="1:44.701 (Sergio Perez, 2024)",
        special=(
            "The longest and one of the most dramatic circuits in F1. Set in "
            "the Ardennes forest, Spa features dramatic elevation changes and "
            "is famous for unpredictable weather - it can rain on one part of "
            "the circuit while the sun shines on another. A true driver's "
            "circuit that rewards bravery and skill."
        ),
        famous_corners=(
            "Eau Rouge / Raidillon (iconic uphill left-right-left sequence "
            "taken at over 300 km/h, one of the most famous corners in "
            "motorsport), La Source (tight hairpin at the start), Blanchimont "
            "(flat-out left kink at extreme speed), Bus Stop chicane"
        ),
        overtaking=(
            "Excellent opportunities. The long Kemmel Straight after Eau Rouge "
            "is one of the best overtaking spots in F1. Additional chances "
            "into La Source and at the Bus Stop chicane."
        ),
    )

    # -- Monza -------------------------------------------------------------
    circuit_profile(
        pdf,
        name="Autodromo Nazionale Monza",
        location="Monza, Italy",
        length="5.793 km",
        turns="11",
        lap_record="1:20.901 (Lando Norris, 2025)",
        special=(
            "The 'Temple of Speed' - the fastest circuit on the calendar with "
            "average speeds exceeding 260 km/h. Home of the Italian Grand Prix "
            "since 1950, Monza is Ferrari's home race and the Tifosi (Ferrari "
            "fans) create an unforgettable atmosphere. Low-downforce setups and "
            "top speed are critical here."
        ),
        famous_corners=(
            "Curva Grande (long, sweeping right-hander), the two Lesmo corners "
            "(medium-speed right-handers through parkland), Variante Ascari "
            "(fast chicane), Parabolica/Curva Alboreto (long right-hander "
            "leading onto the main straight)"
        ),
        overtaking=(
            "Plentiful. The three chicanes (Variante del Rettifilo, Variante "
            "della Roggia, Variante Ascari) all offer heavy braking zones. "
            "Slipstreaming on the long straights is a key tactic."
        ),
    )

    # -- Suzuka ------------------------------------------------------------
    circuit_profile(
        pdf,
        name="Suzuka Circuit",
        location="Suzuka, Japan",
        length="5.807 km",
        turns="18",
        lap_record="1:30.983 (Lewis Hamilton, 2019)",
        special=(
            "One of the most technically demanding circuits in F1 and the "
            "only figure-of-eight layout on the calendar (the track crosses "
            "over itself via an overpass). Suzuka is revered by drivers for "
            "its flowing, high-speed nature. The Japanese fans are known for "
            "their deep knowledge and respect for the sport."
        ),
        famous_corners=(
            "The Esses (S-curves from turns 3-7, a breathtaking high-speed "
            "sequence), Degner curves (fast right-handers), Spoon curve "
            "(double-apex left-hander), 130R (once flat-out, still one of "
            "the fastest corners in F1), the Casio Triangle chicane"
        ),
        overtaking=(
            "Moderate. Main opportunities at the end of the back straight "
            "into the Casio Triangle and at Turn 1. The flowing nature of "
            "the circuit makes following difficult through the Esses."
        ),
    )

    # -- COTA --------------------------------------------------------------
    circuit_profile(
        pdf,
        name="Circuit of the Americas (COTA)",
        location="Austin, Texas, USA",
        length="5.513 km",
        turns="20",
        lap_record="1:36.169 (Charles Leclerc, 2019)",
        special=(
            "Purpose-built for F1 and opened in 2012, COTA combines design "
            "elements from great circuits worldwide. The dramatic uphill run "
            "to Turn 1 is one of F1's most exciting starts. Located in Austin, "
            "Texas, it has become a cornerstone of F1's growing American fanbase."
        ),
        famous_corners=(
            "Turn 1 (steep uphill blind apex, crucial for race starts), "
            "the Esses at turns 3-6 (inspired by Silverstone's Maggotts-Becketts), "
            "Turn 11 (hairpin, key overtaking point), the stadium section "
            "(turns 16-18, amphitheater with massive spectator capacity)"
        ),
        overtaking=(
            "Good opportunities at Turn 1 (especially on lap 1), Turn 12 "
            "(end of back straight), and Turn 15. Active aero will enhance "
            "overtaking on the long DRS/straight zones."
        ),
    )

    # -- Jeddah ------------------------------------------------------------
    circuit_profile(
        pdf,
        name="Jeddah Corniche Circuit",
        location="Jeddah, Saudi Arabia",
        length="6.174 km",
        turns="27",
        lap_record="1:30.734 (Lewis Hamilton, 2021)",
        special=(
            "The fastest street circuit in F1 history, averaging over 250 km/h. "
            "Jeddah's layout runs along the Red Sea waterfront with walls "
            "on both sides at extreme speed. It's a high-risk, high-reward "
            "circuit with limited visibility through several blind corners. "
            "The combination of street circuit barriers and high speed makes "
            "it uniquely challenging."
        ),
        famous_corners=(
            "Turn 1 (fast entry into the circuit), the sweeping section from "
            "turns 4-12 (high-speed flowing sequence near the coast), Turn 22 "
            "(fast kink near the walls), the final sector (tight and technical "
            "approaching the main straight)"
        ),
        overtaking=(
            "Reasonable opportunities on the main straight and at the end of "
            "sector 2's long blast. The tight final sector can bunch cars up, "
            "creating chances into Turn 1."
        ),
    )

    # -- Singapore ---------------------------------------------------------
    circuit_profile(
        pdf,
        name="Marina Bay Street Circuit",
        location="Singapore",
        length="4.940 km",
        turns="19",
        lap_record="1:35.867 (Lewis Hamilton, 2023)",
        special=(
            "F1's original night race, held under floodlights in the heart of "
            "Singapore's financial district. The Marina Bay circuit is one of "
            "the most physically demanding races of the year - the combination "
            "of heat, humidity, bumpy surfaces, and nearly 2 hours of racing "
            "makes it an endurance test. The spectacular nighttime setting with "
            "the city skyline as a backdrop makes it a visual highlight."
        ),
        famous_corners=(
            "Turn 5 (tight left-hander by the Esplanade), the Anderson Bridge "
            "section (turns 7-8, around the historic bridge), Turn 14 (tight "
            "corner under the Singapore Flyer), Turn 16-17 (tight sequence by "
            "Marina Bay Sands)"
        ),
        overtaking=(
            "Limited but possible. The main straight into Turn 1 is the best "
            "chance. The Raffles Boulevard section and Turn 7 hairpin also "
            "offer some opportunity. Strategy and safety car timing are often "
            "decisive here."
        ),
    )

    # -- Madrid (NEW) ------------------------------------------------------
    circuit_profile(
        pdf,
        name="Madrid Street Circuit",
        location="Madrid, Spain",
        length="5.473 km (estimated)",
        turns="20 (estimated)",
        lap_record="N/A (inaugural race in 2026)",
        special=(
            "The newest addition to the F1 calendar for 2026. Madrid's "
            "purpose-built circuit runs through the "
            "IFEMA exhibition complex area near the airport. As a brand-new "
            "venue, details are still emerging, but it promises a modern street "
            "circuit designed with F1's current standards for overtaking and "
            "spectator access. With Barcelona also remaining on the calendar, Spain now boasts "
            "two Grands Prix, reflecting the country's deep F1 heritage."
        ),
        famous_corners=(
            "Details of corner names and character will emerge during the "
            "inaugural event. The circuit is designed to provide a mix of "
            "high-speed straights and technical sections."
        ),
        overtaking=(
            "As a purpose-designed modern venue, the Madrid circuit is expected "
            "to include good overtaking opportunities with long straights and "
            "heavy braking zones. Active aero zones should be prominent."
        ),
    )

    # -- What to Watch For -------------------------------------------------
    pdf.section_header("What to Watch For at Each Race")
    pdf.body_text(
        "Not all circuits are the same. Here's how to think about what "
        "makes each race different:"
    )
    pdf.bullet_list([
        "Street circuits (Monaco, Singapore, Jeddah, Madrid): Walls punish "
        "mistakes, qualifying position matters more, safety cars are common",
        "Power circuits (Monza, Jeddah, Spa): Top speed and low drag are key, "
        "active aero (X-mode) has maximum impact, slipstreaming is a tactic",
        "High-downforce circuits (Monaco, Singapore, Budapest): Cornering "
        "speed matters most, overtaking is harder, strategy is crucial",
        "Mixed circuits (Silverstone, COTA, Suzuka): Reward all-round car "
        "balance, good for close racing across the entire field",
        "Weather-sensitive venues (Spa, Silverstone, Suzuka, Singapore): "
        "Rain can appear quickly, creating dramatic strategy decisions",
    ])

    pdf.info_box(
        "Elevation and Altitude",
        "Some circuits have significant elevation changes (Spa, COTA) that "
        "test suspension and aero. High-altitude venues like Mexico City "
        "(2,240m) reduce engine power and aero effectiveness due to thinner "
        "air, making them unique engineering challenges."
    )

    pdf.save("2026-Circuit-Guide.pdf")


if __name__ == "__main__":
    generate()
