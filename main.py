#!/usr/bin/env python3
"""Plan entry: turn $100 into the most money in 30 days.

Writes a single short plan to /output/entry.txt (1-280 chars).

Why this plan works
-------------------
* Start with businesses that already have paying customers and a clear
  missing asset (a website), not with a new product idea that needs demand
  to be created from scratch.
* Sell a finished site, not a promise: the prospect sees the preview in
  their inbox, so the pitch is "keep this for $99" instead of "hire me".
* The $100 budget goes to the only two things that gate the sale -- a
  domain and an email setup with proper deliverability -- not to ads.
* The funnel is a numbers game: 200 prospects at a realistic 2.5-4%
  conversion yields 5-8 sales at $99, i.e. $495-$792 in 30 days.
"""

from pathlib import Path  # stdlib only; no network, no dependencies.

# The plan itself. 277 chars -- deliberately kept near the cap so the
# pitch (prospecting, the $99 offer, the $100 spend, the expected return,
# and the edge) all fit in one short, self-contained paragraph.
PLAN = (
    "Day 1: find 200 plumbers/roofers/dentists with no website on Google Maps. "
    "Build each a one-page site, email the preview: $99 to keep. "
    "Spend $100 on a domain + email for inbox delivery. "
    "Likely 5-8 sales: $495-$792. "
    "Edge: they buy a finished site, not a promise \u2014 no bidding war."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Validate the plan fits the entry rules before writing anything.
    assert 1 <= len(PLAN) <= 280, f"plan must be 1-280 chars, got {len(PLAN)}"
    assert PLAN.strip(), "plan must not be whitespace-only"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(PLAN, encoding="utf-8")
    # Re-read what landed on disk to confirm the file is exactly the plan.
    written = OUTPUT.read_text(encoding="utf-8")
    assert written == PLAN, "entry.txt content mismatch"
    print(f"Wrote {len(PLAN)} chars to {OUTPUT}")


if __name__ == "__main__":
    main()
