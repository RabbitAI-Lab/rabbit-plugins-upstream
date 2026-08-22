# Freelance Rate Calculator

**Price freelance work so it actually pays — the hourly rate that survives taxes, unpaid hours, bench time, and self-funded benefits.**

## The Problem

Most freelancers set rates by dividing their old salary by 2,080 hours. Then
they discover: only ~60% of their hours are billable (sales, admin, and
learning are unpaid), self-employment tax takes both halves of FICA
(~14.1%), health insurance and retirement are now retail, and contracts end —
leaving unpaid "bench" months. The result is the classic freelancer failure
mode: **broke while busy**, usually discovered around month 14.

Meanwhile clients and recruiters ask "what's your rate?" tomorrow morning,
and fixed-bid projects quietly become charity when estimates slip 30% and
the quote doesn't.

## What It Does

`scripts/freelance_rate.py` (offline, Python stdlib only) runs the real
economics:

| Command | Question it answers |
|---|---|
| `rate` | "I need $70k take-home — what's my hourly rate?" (tax gross-up, overhead, benefits, billable ratio, bench) |
| `salary` | "I'm leaving a $95k job — what rate replaces it?" (spoiler: ~2.4× the naive `salary÷2080`) |
| `check` | "Client offers $60/h — what does that actually net me? Is it enough?" |
| `project` | "This project looks like 60 hours — what do I quote fixed-bid?" (risk buffer + rush premium) |
| `demo` | All three scenarios with sample data |

Every assumption is documented and overridable (`--billable-ratio`,
`--bench-months`, `--income-tax`, `--se-tax`, `--benefits`, `--overhead`).

## Quick Start

```bash
# Rate that nets $70k with honest costs
python3 scripts/freelance_rate.py rate --target-net 70000 --overhead 4000 --benefits 9600
# → ══ HOURLY RATE: $115.35/h ══

# Leaving a $95k job?
python3 scripts/freelance_rate.py salary --salary 95000 --benefits 9600
# → $107.88/h (naive would be $45.67 — the trap)

# Is the client's $60/h enough for your $80k minimum?
python3 scripts/freelance_rate.py check --rate 60 --min-net 80000

# Fixed-bid quote for ~80h of work
python3 scripts/freelance_rate.py project --hours 80 --rate 110 --buffer 0.20

# Tests
python3 scripts/test_freelance_rate.py   # → "29 passed, 0 failed"
```

## The Math in One Paragraph

Revenue must cover your take-home **grossed up for tax** (keep-ratio ≈ 0.68
after income + self-employment tax), **plus** overhead and self-funded
benefits. Only the billable share of your working year (46 weeks × 40 h ×
60% ≈ 1,100 h, minus bench) generates that revenue — so
`rate = required revenue ÷ billable hours`. Fixed bids add a 15% risk
buffer (+25% rush) because estimate risk is now yours.

Full economics, benchmarks, and negotiation scripts in
[`references/rate-theory.md`](references/rate-theory.md).

## Who Needs This

- Developers/designers/consultants going solo (the salary→rate trap)
- Existing freelancers who haven't raised rates since starting
- Anyone quoted "$X/h" by a client, recruiter, or platform who needs to
  know what it actually nets
- Side-project freelancers deciding if the contract beats a salary

US-tax defaults; override the rates for other jurisdictions. Planning aid,
not tax advice — a CPA does the filing.

## License

MIT © Denis Voronin
