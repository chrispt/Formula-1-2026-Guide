# 2026 Formula 1 Season Guide - Unofficial Beginner's Reference

A set of 8 beginner-friendly reference PDFs covering the 2026 Formula 1 season. Designed to help new fans understand the sport, teams, drivers, rules, and strategy.

## PDFs Included

| Guide | Description |
|-------|-------------|
| Race Schedule | Full 24-race calendar with sprint weekends and key dates |
| Driver & Team Guide | All 11 teams, 22 drivers, profiles, and key storylines |
| Regulation Changes | 2026 technical and sporting regulation overhaul explained |
| Race Weekend Format | Standard and sprint formats, qualifying, points system |
| Circuit Guide | Notable circuits with history, famous corners, and overtaking info |
| Strategy 101 | Pit stops, tires, undercut/overcut, safety car, energy management |
| TV Graphics Guide | Understanding broadcast graphics, timing tower, flags, telemetry |
| Glossary | Technical, sporting, and slang terminology with abbreviations |

## Generating the PDFs

```bash
pip install fpdf2 pillow matplotlib
python scripts/gen_all.py
```

PDFs are output to the `output/` directory.

## Data Sources

- Race schedule, results, and statistical data sourced from publicly available information
- Technical regulation summaries are based on publicly published FIA regulations and are the author's interpretation for educational purposes
- Team and driver information is factual and sourced from public records
- Track outlines are simplified artistic representations, not based on official FIA circuit maps

## Disclaimer

**This is an unofficial fan-made educational guide.** It is not associated with, endorsed by, or affiliated with Formula 1, the FIA, Formula One Licensing BV, or any Formula 1 team or driver.

Formula 1, F1, Grand Prix, and related marks are trademarks of Formula One Licensing BV. All team names and trademarks are property of their respective owners. This guide is provided for informational and educational purposes only.

## License

Content is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). See [LICENSE](LICENSE) for details.
