"""Runner script: generates all 8 F1 2026 reference PDFs."""

import sys, os, time

# Ensure scripts directory is on the path
sys.path.insert(0, os.path.dirname(__file__))

import gen_race_schedule
import gen_weekend_format
import gen_glossary
import gen_driver_team_guide
import gen_regulations
import gen_tv_graphics_guide
import gen_circuit_guide
import gen_strategy_101

GENERATORS = [
    ("Race Schedule",       gen_race_schedule),
    ("Race Weekend Format", gen_weekend_format),
    ("Glossary",            gen_glossary),
    ("Driver & Team Guide", gen_driver_team_guide),
    ("Regulation Changes",  gen_regulations),
    ("TV Graphics Guide",   gen_tv_graphics_guide),
    ("Circuit Guide",       gen_circuit_guide),
    ("Strategy 101",        gen_strategy_101),
]


def main():
    print("=" * 55)
    print("  F1 2026 Reference PDF Generator")
    print("=" * 55)
    print()

    start = time.time()
    for name, module in GENERATORS:
        print(f"  Generating: {name}...")
        module.generate()

    elapsed = time.time() - start
    print()
    print(f"  All 8 PDFs generated in {elapsed:.1f}s")
    print(f"  Output directory: {os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output')}")
    print()


if __name__ == "__main__":
    main()
