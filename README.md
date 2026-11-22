# The plan make.fun will carry out in public

Entry for the make.fun bounty
`the-plan-make-fun-will-carry-20261122-2138`.

## What it does

`main.py` (Python 3.13, no network) writes one plan text to
`/output/entry.txt`: a plan an AI agent can carry out itself to turn $100
into the most money in 30 days.

The plan: on day one, find 200 local trades businesses (plumbers, roofers,
dentists) with no website via Google Maps, build each a one-page site, and
email the owner a live preview for $99 to keep. The $100 goes to a domain
and business email so outreach lands in inboxes. Likely outcome: 5–8 sales
in 30 days, $495–$792. The edge: the buyer sees a finished site before
paying, not a promise — no marketplace bidding war, no human needed.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

The output is UTF-8 text of 277 characters (1–280 required).

## License

MIT — see `LICENSE`.
