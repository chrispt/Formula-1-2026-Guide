"""PDF 8: F1 2026 Strategy 101 -- Pit stops, tires, undercut/overcut, safety car, weather, ERS."""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from f1_pdf_style import F1PDF
import f1_graphics


def generate():
    pdf = F1PDF(
        title="F1 2026 Strategy 101",
        subtitle="Understanding Race Strategy"
    )
    pdf.add_cover_page()
    pdf.add_page()

    # -- Introduction ------------------------------------------------------
    pdf.section_header("Why Strategy Matters")
    pdf.body_text(
        "Formula 1 is not just about the fastest car. Every race involves "
        "strategic decisions about when to pit, which tires to use, how to "
        "manage energy, and how to react to changing conditions. A brilliant "
        "strategy can turn a fourth-place car into a race winner. This guide "
        "explains the key strategic concepts that new fans hear commentators "
        "discuss every race weekend."
    )

    pdf.stat_callout([
        ("1-3", "Pit Stops"),
        ("~2.5s", "Stop Duration"),
        ("20+", "Crew Members"),
        ("3", "Tire Compounds"),
    ])

    # -- Tire Degradation --------------------------------------------------
    pdf.section_header("Tire Degradation")
    pdf.body_text(
        "Tires are the single biggest strategic variable in a race. Every "
        "tire loses grip over time as the rubber wears and the surface "
        "degrades. Understanding tire degradation is the key to understanding "
        "why pit stops happen."
    )

    pdf.subsection_header("How Tires Wear")
    pdf.bullet_list([
        "Every lap, tires lose a small amount of performance (typically "
        "0.05-0.15 seconds per lap, depending on the compound and circuit)",
        "Soft tires are fastest when new but degrade quickly (short stints)",
        "Hard tires start slower but maintain performance longer (long stints)",
        "Medium tires offer a balance between speed and durability",
        "Track temperature, driving style, and car setup all affect wear rate",
        "Each circuit wears tires differently - some are very harsh on tires "
        "(Barcelona, Bahrain), others are gentle (Monaco, Monza)",
    ])

    deg_img = f1_graphics.tire_degradation_chart()
    pdf.add_diagram(deg_img, w=160, caption="Tire degradation curves by compound (illustrative)")

    pdf.subsection_header("The 'Cliff'")
    pdf.body_text(
        "Tires don't degrade linearly. At some point, they 'fall off the "
        "cliff' - a sudden, dramatic loss of grip where lap times drop by "
        "several seconds. A key strategy skill is pitting just before the "
        "cliff. If you miss it, you lose huge amounts of time."
    )

    pdf.info_box(
        "Mandatory Tire Rule",
        "In dry conditions, drivers MUST use at least two different tire "
        "compounds during a race. This guarantees at least one pit stop in "
        "every race, creating strategic variety."
    )

    # -- Pit Stops ---------------------------------------------------------
    pdf.section_header("Pit Stop Mechanics")
    pdf.body_text(
        "A Formula 1 pit stop is one of the most impressive feats in sport. "
        "A crew of over 20 mechanics changes all four tires in under 3 seconds."
    )

    pdf.subsection_header("What Happens During a Stop")
    pdf.bullet_list([
        "The driver enters the pit lane at the speed limit (typically 80 km/h)",
        "The car stops on a precise mark in the team's pit box",
        "Three mechanics per wheel: one operates the wheel gun, one removes "
        "the old tire, one fits the new tire",
        "Front and rear jack operators lift the car simultaneously",
        "The 'lollipop' person or light system signals the driver to go",
        "The fastest stops take around 2.0 seconds for the stationary time",
        "Total pit lane time (entry, stop, exit) is typically 20-25 seconds",
    ])

    pdf.subsection_header("Pit Stop Penalties")
    pdf.styled_table(
        headers=["Violation", "Penalty"],
        data=[
            ["Speeding in pit lane", "5 or 10 second time penalty"],
            ["Unsafe release (into traffic)", "5 second penalty or fine"],
            ["Cross-threaded wheel nut", "Retirement (wheel not secure)"],
            ["Pit crew across pit lane line", "Fine to the team"],
        ],
        col_widths=[80, 110],
    )

    pdf.info_box(
        "The Time Cost of Pitting",
        "A pit stop typically costs about 22-25 seconds of track time. "
        "This means fresh tires need to make up that time deficit through "
        "faster lap times over the remainder of the stint. Strategists "
        "calculate exactly when the time gain from fresh tires outweighs "
        "the pit stop cost."
    )

    # -- Undercut and Overcut ----------------------------------------------
    pdf.section_header("Undercut vs. Overcut")
    pdf.body_text(
        "These are the two fundamental pit stop strategies used to gain "
        "track position over a rival. You'll hear these terms constantly "
        "during race broadcasts."
    )

    pdf.subsection_header("The Undercut")
    pdf.bullet_list([
        "Pitting EARLIER than your rival",
        "You get fresh tires while they're still on old, slower tires",
        "Your faster 'out lap' on new tires gains enough time to emerge "
        "ahead when your rival eventually pits",
        "Works best when tire degradation is high (fresh tires are much "
        "faster than worn ones)",
        'Example: You pit on lap 15, your rival pits on lap 18. Your 3 '
        'laps on fresh tires are fast enough to jump ahead',
    ])

    pdf.subsection_header("The Overcut")
    pdf.bullet_list([
        "Pitting LATER than your rival",
        "You stay out on old tires while they pit, inheriting the lead",
        "Works when the tires still have life and the pit stop time loss "
        "is greater than the pace difference",
        "Also effective when your rival hits traffic after their pit stop",
        "Less common than the undercut but can be powerful at certain tracks",
    ])

    undercut_img = f1_graphics.undercut_diagram()
    pdf.add_diagram(undercut_img, w=160, caption="How the undercut works: Driver A pits early to gain position")

    pdf.info_box(
        "Reading the Strategy Battle",
        "When commentators say 'they're trying the undercut,' watch the "
        "gap between the two drivers. If the driver on fresh tires is "
        "setting purple or green sectors, the undercut is working. If the "
        "gap isn't closing fast enough, the overcut may prevail."
    )

    # -- Safety Car Strategy -----------------------------------------------
    pdf.section_header("Safety Car & Red Flag Strategy")
    pdf.body_text(
        "Safety cars and red flags can completely transform a race. They "
        "create both opportunities and crises for strategists."
    )

    pdf.subsection_header("Safety Car (SC)")
    pdf.bullet_list([
        "When the safety car is deployed, the pit lane remains open",
        "Because the field is running slowly behind the safety car, the "
        "time cost of a pit stop is dramatically reduced",
        "Teams rush to pit under the safety car for a 'cheap' stop - you "
        "lose far less time than pitting under green flag conditions",
        "Drivers who have already pitted gain an advantage (they don't "
        "need to stop again), while those who haven't must decide quickly",
        "The field bunches up behind the safety car, erasing gaps that "
        "were built up over many laps",
    ])

    pdf.subsection_header("Virtual Safety Car (VSC)")
    pdf.bullet_list([
        "Drivers slow to a delta time (~40% slower) but don't bunch up",
        "Still a cheaper pit stop than under green flags, but the advantage "
        "is smaller than a full safety car",
        "Maintains the relative gaps between cars more than a full SC",
    ])

    pdf.subsection_header("Red Flag")
    pdf.bullet_list([
        "Race is stopped; all cars return to the pit lane",
        "Teams can change tires and make repairs during the stoppage for free",
        "This resets tire strategy entirely - everyone gets fresh tires",
        "The race restarts from a standing or rolling start",
        "Drivers who were on worn tires or about to pit benefit enormously",
    ])

    pdf.info_box(
        "Safety Car Luck",
        "Some of the most dramatic strategy swings happen when a safety car "
        "appears at exactly the wrong (or right) moment. A driver about to "
        "pit gets a free stop; a driver who just pitted under green conditions "
        "watches their advantage evaporate. This element of unpredictability "
        "is part of what makes F1 so exciting."
    )

    # -- Weather Strategy --------------------------------------------------
    pdf.section_header("Weather Strategy")
    pdf.body_text(
        "Rain transforms an F1 race. The switch between dry and wet tires "
        "(and vice versa) creates enormous strategic dilemmas."
    )

    pdf.subsection_header("Rain Decisions")
    pdf.bullet_list([
        "When rain starts: Pit now for intermediates, or gamble that it stops?",
        "Too early and you're slow on wet tires while the track is still dry",
        "Too late and you're aquaplaning on dry tires in standing water",
        "The intermediate tire is the most versatile - works on damp to "
        "moderately wet surfaces",
        "Full wet tires are only for heavy rain with standing water",
    ])

    pdf.subsection_header("Drying Track")
    pdf.bullet_list([
        "When a wet track starts drying, switching to slick tires early "
        "can gain huge time - but it's risky",
        "The first driver to switch to slicks on a drying track often "
        "gains a massive advantage if the timing is right",
        "Get it wrong and you'll slide off on a still-wet surface",
        "The racing line dries first; off-line is wetter for longer",
    ])

    pdf.info_box(
        "The 'Crossover Point'",
        "Strategists monitor lap times to find the 'crossover point' - the "
        "moment when slick tires become faster than intermediates on a drying "
        "track. The team that calls this correctly can win a race from an "
        "unlikely position."
    )

    # -- ERS / Energy Management (New for 2026) ----------------------------
    pdf.section_header("Energy Management (New for 2026)")
    pdf.body_text(
        "With the 2026 power units generating roughly 50% of their power "
        "from electric sources, energy management becomes a crucial strategic "
        "element - similar in importance to tire strategy."
    )

    pdf.stat_callout([
        ("~50%", "Electric Power"),
        ("350", "kW MGU-K"),
        ("0", "MGU-H (Gone)"),
    ])

    pdf.subsection_header("How Energy Strategy Works")
    pdf.bullet_list([
        "The MGU-K harvests energy under braking and stores it in the battery",
        "Drivers deploy stored energy for acceleration, especially on straights",
        "The battery has a limited capacity - use too much too soon and you "
        "run low in the critical final laps",
        "Without the MGU-H (removed for 2026), energy recovery is less "
        "efficient, making management even more important",
        "Different circuits demand different energy strategies based on the "
        "number and length of straights vs. braking zones",
    ])

    pdf.subsection_header("Strategic Implications")
    pdf.bullet_list([
        "Drivers may 'lift and coast' before braking zones to save energy - "
        "trading a small amount of time for more electric power later",
        "Energy deployment is critical for defense and attack: a driver "
        "with more stored energy can deploy it for overtaking or defense",
        "Teams must balance energy use across the entire race distance",
        "Look for the battery level graphic on TV - a driver with low "
        "charge may be vulnerable on the next straight",
    ])

    pdf.info_box(
        "Energy as a Weapon",
        "In 2026, watch for drivers strategically saving energy in sectors "
        "where they can't overtake, then deploying it all on a straight "
        "where they can. Battery management adds a chess-like dimension "
        "to the racing that didn't exist before."
    )

    # -- Common Strategy Phrases -------------------------------------------
    pdf.section_header("Strategy Phrases You'll Hear")
    pdf.body_text(
        "Commentators and team radio use specific terminology. Here's what "
        "the most common phrases mean:"
    )

    phrases = [
        ('"Box, box, box"',
         "Team radio instruction telling the driver to pit this lap. 'Box' "
         'comes from the German "Boxenstopp" (pit stop).'),
        ('"Stay out, stay out"',
         "The team tells the driver NOT to pit. They may be trying the "
         "overcut or waiting for a safety car opportunity."),
        ('"Opposite to [driver name]"',
         "The team will do the opposite of whatever a rival does - if they "
         "pit, you stay out, and vice versa."),
        ('"Tires are gone"',
         "Driver reports severe tire degradation. May be genuine or tactical "
         "to force the team's hand on pit strategy."),
        ('"We\'re looking at Plan B / C"',
         "The team is switching from the original strategy. Plans are "
         "pre-agreed before the race for different scenarios."),
        ('"Push now, push now"',
         "Drive flat out - usually because the team is trying to create "
         "a gap for an undercut or respond to a rival's pit stop."),
        ('"Manage your tires"',
         "Drive more conservatively to extend the current stint and delay "
         "the pit stop."),
        ('"Pit window open"',
         "The optimal range of laps for the next pit stop has begun. "
         "The team is evaluating the best moment to stop."),
        ('"We need to cover [driver]"',
         "A rival has pitted, and the team needs to pit immediately to "
         "prevent losing position (covering the undercut)."),
        ('"Free air"',
         "The driver has clear track ahead with no slower cars to impede "
         "their pace. This is the ideal situation for fast lap times."),
    ]

    for phrase, meaning in phrases:
        pdf.glossary_entry(phrase, meaning)

    # -- Quick Strategy Reference ------------------------------------------
    pdf.section_header("Quick Strategy Reference")

    pdf.styled_table(
        headers=["Situation", "Common Response", "Why"],
        data=[
            ["Rival pits early", "Cover (pit next lap) or overcut", "Prevent undercut position loss"],
            ["Safety car deployed", "Pit immediately if due", "Cheap pit stop, lose less time"],
            ["Rain starting", "Pit for intermediates", "Dry tires lose all grip in rain"],
            ["Track drying", "Be first to switch to slicks", "Huge time gain if timed right"],
            ["Tire cliff approaching", "Pit before cliff hits", "Avoid massive time loss"],
            ["Low battery on straights", "Lift and coast earlier", "Save energy for key moments"],
            ["Red flag", "Free tire change in pit lane", "Fresh tires for the restart"],
        ],
        col_widths=[45, 55, 70],
        font_size=8,
    )

    pdf.info_box(
        "The Human Element",
        "Race strategy in F1 isn't purely mathematical. Drivers have instincts "
        "about tire condition, weather, and opponents that computers can't "
        "replicate. Some of the greatest strategic calls in F1 history came "
        "from drivers overriding their team's plan based on feel. In 2026, "
        "the added complexity of energy management makes this human element "
        "even more valuable."
    )

    pdf.save("F1-2026-Strategy-101.pdf")


if __name__ == "__main__":
    generate()
