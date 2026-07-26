# Project: igamingreviews.org

**Status:** Active. South African iGaming review/content site — Trevor's chosen path for making money with minimal human involvement.
**Pipeline:** `/root/.openclaw/workspace/igaming_automation/` (credentials.json holds the WordPress app password).
**Schedule:** publishes guides/operator reviews Mon & Thu 10:37 UTC; Sun 11:00 UTC stale-post refresh (dry-run); Tue 11:00 UTC backlink outreach drafts.
**Social:** LinkedIn LIVE-capable — posts go ONLY to the **iGamingReviews org page** (`urn:li:organization:126833959`, vanity igamingreviews) via Maton community-management connection `6f11f239`. X/Twitter LIVE-capable as **@iGamingZA** (iGaming Reviews, id 2062578976334163968) — verified 2026-07-15 via OAuth 1.0a `/2/users/me`. Brand accounts only: Trevor's personal profiles must NEVER be posted to (his rule 2026-07-15). `linkedin_client.py` authors as the org URN only; person-posting path removed. X gotcha: consumer keys and access tokens must come from the SAME app — mixing dev/staging apps gives "Could not authenticate you" (code 32).

## State check (2026-07-15 19:20 UTC)
- Live: 3 published posts — poker-legal guide + "How to Withdraw…" published TWICE (slug `-2` duplicate). Drafts: horse racing, sports-apps (x2 duplicate), wagering requirements.
- **Bug:** generator duplicated topics (sports apps drafted 2x, withdrawal published 2x); `state.json` only tracks 1 of 3 published posts — state tracking drifts from reality.
- **Gap:** the Mon/Thu publish, Sun refresh, Tue backlink cron jobs are NOT registered in OpenClaw cron — the "schedule" in MEMORY.md was aspirational. Nothing runs unattended right now.
- Queue: 20 guide topics + seed keywords; 6 indices marked used.

## Social drafts pending approval (17/07/2026)

Picks from `sports_snapshot.md` for South African betting audience:
- F1 Belgian GP Practice 1 today at 13:30 SAST.
- UCL qualifying: Egnatia 6-1 Petrocub Hîncești on 15/07.

Drafts run through super-humanizer rules. Not posted.

**X post (218 chars):**
F1 weekend starts today. Belgian GP Practice 1 is at 13:30 SAST. In midweek UCL qualifying, Egnatia hit Petrocub 6-1. If you are betting this weekend, check the schedule and markets before you lock in. https://igamingreviews.org

**LinkedIn post:**
Formula 1 is back this weekend with the Belgian Grand Prix. Practice 1 starts at 13:30 SAST today.

Midweek also brought a big result in the UCL qualifiers. Egnatia beat Petrocub Hîncești 6-1 on 15/07.

For South African bettors, the weekend has a clear headline. F1 race weekends always pull a wide range of markets, from outright winner to podium and head-to-head. Check the schedule and compare odds before you place anything.

https://igamingreviews.org

## Conventions
- Style-matched WordPress posts; Key Takeaways box must use `<blockquote class="key-takeaways">`.
- No responsible-gambling disclaimers in articles — the site footer handles it.
- Clean LLM artifacts aggressively before publishing (markdown fences, "Links added:" summaries, trailing raw-markdown summaries).
