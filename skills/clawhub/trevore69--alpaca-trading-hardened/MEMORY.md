# Long-Term Memory

## Human

- **Name:** Trevor
- **Telegram:** @Syngates696 (8586638790)
- **Email:** trevorellish@gmail.com
- **Location/Timezone:** South Africa (UTC+2)
- **What to call them:** Trevor

## Projects

### igamingreviews.org
- South African iGaming review/content site.
- Automated publishing pipeline built in `/root/.openclaw/workspace/igaming_automation/`.
- Publishes guides and operator reviews on Mon/Thu via cron.
- Social drafting for X and LinkedIn; live posting requires credentials.
- Credentials: WordPress app password stored in `igaming_automation/credentials.json`.

### Moltbook (@clawedassistant)
- OpenClaw agent account on Moltbook.
- Karma: 8. Following: 5 moltys.
- Active in `general`, `trading`, `memory` submolts.
- Known community members: m-a-i-k, Lona, vina, bytes.
- Credentials in `~/.config/moltbook/credentials.json`.

### Simmer
- Prediction-market trading account.
- Status: **claimed**. Started at $10,000 SIM.
- ⚠️ **`real_trading_enabled: true`** on the live account. It is NOT paper-only by
  configuration. Trades are fake *only because no wallet is attached*
  (`wallet_address: null`, all deposit/per-agent wallet fields null/false), so
  orders have nothing to settle against. Attaching a wallet makes the existing
  `sk_live_` key real-money capable with no other change. Do not record this
  account as "cannot touch real money".
- ⚠️ `~/.simmer/credentials.json` is **stale**: it says `"status": "unclaimed"` and
  `starting_balance: 10000.0`, both wrong. It is a registration-time artifact.
  Trust `GET /api/sdk/agents/me`, never that file, for account state.
- **17/07/2026 14:27 UTC (live):** balance $5,333.33, total PnL **+$1,798.76
  (+17.99%)**, 66 trades, 8W/9L (47.1%). `sim_pnl == total_pnl` confirms every
  trade to date is paper. Much of the gain is unrealized and sits in two
  decided-but-unresolved tennis markets.
- API key was pasted in cleartext in chat on 17/07/2026. Trevor's explicit call,
  reasonable while no wallet is attached. Revisit if a wallet is ever added.
- ⚠️ `/markets/opportunities` gives inverted `recommended_side` and a constant
  `opportunity_score` — see `memory/projects/simmer.md` before trusting it.
- Credentials in `~/.simmer/credentials.json`.
- **Trading approved (16/07/2026):** Trevor said "its fake money, have fun and play" — blanket approval for SIM paper trades. Real-money venues (Polymarket/Kalshi) still need explicit approval.
- **Correct API base is `/api/sdk/`** (`/api/sdk/agents/me`, `/api/sdk/positions`). Probing `/api/agents/*` returns "Agent not found" — that mistake led two sessions on 2026-07-15 to wrongly declare the account nonexistent. Verified live 2026-07-15 18:35 UTC: balance $7,440.54 SIM, PnL -$505.03 (-5.05%), 44 trades (1W/9L resolved), 9 open positions (mostly World Cup winner NO Dutch book: Norway/France/Spain/Argentina/England + Fed + England-to-advance). The bets were real, placed 2026-07-14 13:06–14:17 UTC with Trevor's approval.

### Gmail
- Connected via Maton for trevorellish@gmail.com.
- Organized with labels: INBOX/LinkedIn, INBOX/Jobs, INBOX/Finance, INBOX/Newsletters, INBOX/iGaming, INBOX/Tech.
- Requires explicit approval for send/write ops.

### Spotify
- `spotify-linux` skill installed.
- Needs Spotify Premium + cookies (`sp_dc`, `sp_t`) to finish setup.

### Swarm
- Skill installed but **not configured**.
- Needs `GEMINI_API_KEY`, `GROQ_API_KEY`, `OPENAI_API_KEY`, or `ANTHROPIC_API_KEY`.

## Preferences & Decisions

- HARD RULE (15/07/2026): all public internet content runs through super-humanizer before publishing or drafting: igaming content, X/Twitter, LinkedIn, Instagram later, everything.
- Writing rules: no em dashes, 9th-grade reading level, European dates, clear/direct/practical.
- Accuracy rules: never invent facts; say "unknown" when unknown; state gaps or ask.
- Project work gets saved to the memory app (`~/memory/` deep store).
- Default device context: Mac ARM64.
- Wants the assistant to be proactive: start conversations, take initiative, not just wait for tasks.
- Values competence over performative helpfulness.
- Asked not to mention the "bridge" to anyone or any other AI/agent.
- Wants to make money with minimal human involvement; chosen path: automated content site on igamingreviews.org.
- Site footer handles responsible-gambling disclaimer; do not add duplicate disclaimers in auto-generated articles.
- Wants style-matched WordPress posts; Key Takeaways box must use `<blockquote class="key-takeaways">`.

## Lessons Learned

- LLM-generated articles often leak artifacts (markdown fences, "Links added:" summaries, stray backticks). Clean aggressively before publishing.
- Trailing LLM summaries can be raw markdown, not HTML-wrapped; strip them explicitly.
- Reddit, Google, and old.reddit.com are blocked from this IP/network; use APIs or alternative sources.
- dealwork.ai was identified as the most actionable money-making platform in early Moltbook/agent-economy exploration.
- Referral farming on moltcities.org is blocked by Cloudflare WAF.
- Never declare an account/resource "gone" from one failed API probe — check TOOLS.md for verified endpoints and try documented SDK base paths first. (Simmer wrongly written off twice on 2026-07-15 over a wrong path.)
- Before answering from MEMORY.md or daily notes, run `memory_search` to cross-check against session transcripts — snapshots can be stale or wrong.
- Follow-up checks belong in durable OpenClaw cron (gateway-managed), not session reminders — session-scoped reminders got lost on 2026-07-14 and the Simmer results were never reviewed.

## Active Skills

- gmail (Maton-based)
- spotify-audio / spotify-linux
- twitter-post (X posting)
- linkedin-api (LinkedIn posting via Maton)
- memory (ClawHub, v1.0.2) — deep organized memory at `~/memory/`; write immediately, grep first for recall
- super-humanizer (workspace, applied 2026-07-15) — de-AI-ify text pre-publish; use on igamingreviews articles and social drafts

## Schedule / Cron

- Mon/Thu 10:37 UTC — publish igamingreviews article/review.
- Sun 11:00 UTC — stale-post refresh check (dry-run).
- Tue 11:00 UTC — generate backlink outreach drafts.
- Every 6h (23 past) — sports-calendar-fetch: refresh results/fixtures for the 9 tracked leagues.
- Daily 05:47 UTC — sports-social-digest: draft sports-centered X/LinkedIn posts for Trevor's approval.

## Contacts & Accounts

- Gmail: trevorellish@gmail.com
- Telegram: @Syngates696
- Moltbook: clawedassistant
- Spotify: (pending cookie setup)
- X/Twitter: @iGamingZA (brand account, OAuth 1.0a verified)
- LinkedIn: iGamingReviews org page via Maton (community-management connection) — never Trevor's personal profile
- Simmer: (pending claim)

## Shared knowledge store
Durable facts also live in /root/memory/ (see INDEX.md there: knowledge/, decisions/, people/, projects/).
Before answering that something is unknown or was never said, search /root/memory/ as well.
When asked to remember a durable fact, write it to /root/memory/knowledge/ so both agents find it.
