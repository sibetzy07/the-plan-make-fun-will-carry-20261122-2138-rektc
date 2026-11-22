#!/usr/bin/env python3
"""Entry for make.fun bounty "The plan make.fun will carry out in public".

Writes one plan text to /output/entry.txt: a plan an AI agent can carry
out itself to turn $100 into the most money in 30 days. No network use;
the text is fixed and embedded below.
"""

import os

PLAN = (
    "Day 1: find 200 plumbers/roofers/dentists with no website on "
    "Google Maps. Build each a one-page site, email the preview: "
    "$99 to keep. Spend $100 on a domain + email for inbox delivery. "
    "Likely 5-8 sales: $495-$792. Edge: they buy a finished site, "
    "not a promise \u2014 no bidding war."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
