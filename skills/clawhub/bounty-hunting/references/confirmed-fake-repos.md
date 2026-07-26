# Confirmed Fake/Bot Bounty Repos

## Confirmed Fake by User
- **UnsafeLabs/Bounty-Hunters** — Issues #768 ($350), #763 ($300) confirmed fake. SKIP ALL.
- **SecureBananaLabs/bug-bounty** — Issue #30 ($750) confirmed fake. SKIP ALL.
- **UnsafeLabs/RFC-5322** — $400 bounty, fake.

## Confirmed Bot/Farm
- **BAWES-Universe** (studenthub, plugn) — PHP, 10-30+ bot PRs
- **moorcheh-ai/memanto** — Python, 20+ bot PRs
- **ClankerNation/OpenAgents** — Mass-created issues, "Autonomous Agents Only", $2k-$9k claims
- **orchestration-agent/AgentOrchestration** — 4-day-old repo, 234★/246 forks, bot swarm
- **mergeos-bounties/mergeos** — Token rewards (MRG), not USD
- **waxeye7/screeps-bounty-arena** — Points only, no USD
- **HELPDESK.AI (ritesh-1918)** — GSSoC points, not USD
- **Scottcjn/rustchain-bounties** — RTC tokens, not USD
- **Scottcjn/Rustchain** — RTC tokens, not USD
- **promptpolish-ai/git-context** — Crypto rewards only ($2 crypto)
- **xevrion-v2/agent-playground** — Suspicious, low-value tasks

## $10 Opire Fork Farms (Confirmed 2026-06)
Pattern: usernames like `davontepowlowsk1i`, `rodrickparker11`, `juanitahagenes` create $10 opire bounties on forks of major repos. Fake — repos are forks with no real maintainers.
- **victorjones6awpg/Casbin** — $10 opire on Casbin fork
- **davontepowlowsk1i/gofiber-fiber** — $10 opire on gofiber fork
- **davontepowlowsk1i/Apache-Pulsar** — $10 opire on Pulsar fork
- **davontepowlowsk1i/CockroachDB** — $10 opire on CockroachDB fork
- **rodrickparker11/TiKV** — $10 opire on TiKV fork
- **juanitahagenes/ClickHouse** — $10 opire on ClickHouse fork

## Bounty Radar/Tracking (Not Real Payouts)
- **relayhop/sn-monetization-runtime** — Uses `[radar] SN open bounty` titles with "radar"/"sn"/"bounty" labels. These are automated bounty-listing issues, not real bounties with payouts.

## Real Bounty Platforms
- **Expensify/App** — $250 per issue, real USD, External label
- **claude-builders-bounty** — $50-$150, Opire-based, high competition (600+ comments)

## Detection Heuristics
- Repo age < 7 days with 10+ bounties = farm
- Star/Fork ratio inverted (more forks than stars) = bot-inflated
- PRs appearing within 2-5 minutes of issue creation = automated
- Labels combining "good first issue" + "$5k+" = suspicious
- GSSoC labels = points, not USD
- "Autonomous Agents Only" label = bot farm
- Token rewards (MRG, RTC) = not real USD

## Repos That Require Assignment Before PR
- **langchain-ai/langchain** — Auto-closes PRs if not assigned. Comment on issue first.
- **pydantic/pydantic-settings** — Needs maintainer review. Be patient.
