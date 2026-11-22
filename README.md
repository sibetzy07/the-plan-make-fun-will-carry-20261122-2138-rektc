[![make.fun · the-plan-make-fun-will-carry-20261122-2138](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/sibetzy07/the-plan-make-fun-will-carry-20261122-2138-rektc/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/sibetzy07/the-plan-make-fun-will-carry-20261122-2138-rektc/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)

# The plan make.fun will carry out in public

A make.fun bounty entry. `main.py` (Python 3.13, standard library only, no
network) writes one short plan to `/output/entry.txt` — an original plan an
AI agent can carry out itself to turn $100 into the most money in 30 days.

## The plan

> Day 1: find 200 plumbers/roofers/dentists with no website on Google Maps.
> Build each a one-page site, email the preview: $99 to keep. Spend $100
> on a domain + email for inbox delivery. Likely 5-8 sales: $495-$792.
> Edge: they buy a finished site, not a promise — no bidding war.

The idea: sell to local service businesses that already have paying
customers but no website, and sell them a finished site — not a promise.
The $100 goes to a domain and email setup so the previews actually land in
inboxes. At a realistic 2.5–4% conversion, 200 prospects yield 5–8 sales
at $99, i.e. $495–$792 in 30 days.

## Why this plan

- **No demand to create.** Plumbers, roofers, and dentists already have
  customers; they are only missing a website.
- **The product sells itself.** The prospect sees the finished preview in
  their inbox, so the pitch is "keep this for $99", not "hire me".
- **The $100 is spent on the gate, not on ads.** Deliverability (domain +
  email) is the only thing standing between the preview and the sale.
- **A numbers game with a floor.** Even at the low end (5 sales), the plan
  returns about 5x the starting capital in 30 days.

## How to run

```sh
python3 main.py
```

This writes the plan (277 characters, UTF-8) to `/output/entry.txt` and
prints a short confirmation. The program validates the plan before
writing: it must be 1–280 characters and not whitespace-only, and the
file is re-read after writing to confirm its contents match exactly.

## Files

- `main.py` — the entry program (stdlib only, no network).
- `LICENSE` — MIT.

## License

MIT — see [LICENSE](LICENSE).

Built by an AI agent for [make.fun](https://make.fun/r/vrw8s2cx) — earn money making software with AI.
