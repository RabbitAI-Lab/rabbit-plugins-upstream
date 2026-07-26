---
name: news-briefing
description: "Automated daily news briefing system that fetches Twitter/X posts, generates star-rated summaries, and delivers them via Feishu/Lark. Supports Scweet precise fetching with VPN and WebSearch fallback. Configurable sources, scheduling, and briefing format."
agent_created: true
read_when:
  - User wants to create a daily news briefing automation
  - User wants to fetch and summarize Twitter/X posts
  - User wants to set up a scheduled news digest via Feishu/Lark
  - User wants to modify briefing format or information sources
  - User wants to add new bloggers/accounts to track
---

# News Briefing Skill

## Overview

This skill encapsulates a complete Twitter/X news briefing automation system that:

- Fetches posts from configurable Twitter/X accounts across multiple categories
- Generates star-rated, mobile-friendly briefings (readable in 20 seconds)
- Delivers briefings via Feishu/Lark messaging
- Deduplicates seen content with 7-day auto-cleanup
- Runs on a schedule (e.g., every 2 hours from 10:00 to 20:00), sending only once per day

## System Architecture

```
News Briefing System
├── Data Layer: Fetch tweets from configured accounts (last 24h)
├── Dedup Layer: Skip already-seen content by tweet_id
├── Briefing Layer: AI generates star-rated summary (max 12 items)
├── Delivery Layer: Send via Feishu/Lark bot
├── Anti-repeat Layer: Daily sent_log prevents duplicate sends
└── Schedule Layer: Runs at intervals, exits early if already sent
```

## Project Structure

```
project-directory/
├── config/sources.yaml          # Information source config (blogger list)
├── scripts/fetch_tweets.py      # Scweet tweet fetching script
├── data/sent_log.json           # Send status tracking
├── data/seen_tweets.json        # Seen content dedup (by tweet_id)
├── data/tweets_raw.json         # Raw fetched tweet data
└── .workbuddy/memory/           # Project memory
```

## Setup Guide

### Step 1: Configure Information Sources

Create `config/sources.yaml` with your selected accounts organized by category:

```yaml
ICT Trading:
  - handle: example_trader1
    name: Example Trader 1
    followers: "100K"

US Stocks:
  - handle: example_trader2
    name: Example Trader 2
    followers: "200K"

AI:
  - handle: example_ai1
    name: Example AI Researcher
    followers: "150K"
```

### Step 2: Set Up Tweet Fetching

Install Scweet for precise Twitter/X data fetching:

```bash
pip install scweet
```

Create `scripts/fetch_tweets.py` (see `scripts/fetch_tweets.py` in this skill for the full template). Key configuration:

- `AUTH_TOKEN`: Your Twitter/X auth_token (get from browser: login to x.com, F12, Application, Cookies, auth_token)
- `ACCOUNTS`: Dictionary mapping categories to lists of handles
- Requires VPN/proxy if accessing from regions where x.com is restricted

### Step 3: Initialize State Files

Create `data/sent_log.json`:
```json
{
  "last_sent_date": "",
  "last_sent_time": "",
  "history": []
}
```

Create `data/seen_tweets.json`:
```json
{
  "items": [],
  "last_cleanup": ""
}
```

### Step 4: Connect Feishu/Lark

1. Open WorkBuddy connector management
2. Find Feishu/Lark and connect/authorize
3. Verify connection with: `lark-cli auth status --json --verify`
4. Get your user open_id from the auth status output

### Step 5: Create Automation

Create a recurring automation in WorkBuddy with:

- **Schedule**: e.g., `FREQ=DAILY;BYHOUR=10,12,14,16,18,20;BYMINUTE=0`
- **Connectors**: feishu
- **Working directory**: Your project path

The automation prompt should follow the six-step workflow below.

## Six-Step Workflow

### Step 1: Check Daily Send Status

Read `data/sent_log.json`. If `last_sent_date` equals today, output "Already sent today, exiting" and stop immediately.

### Step 2: Fetch Last 24h Tweets

**Option A: Scweet Precise Fetching (requires VPN/proxy)**

```bash
python3 scripts/fetch_tweets.py --hours 24 --limit 5 --output data/tweets_raw.json
```

- Success (non-empty array) -> Use ONLY Scweet data, add VPN emoji to title
- Failure/empty array -> Fall back to Option B

**Option B: WebSearch Fallback (VPN not connected)**

Search each category's accounts using WebSearch. Collect results from the last 24 hours.

**VPN Status Marker**: If Scweet succeeds, add a VPN emoji to the briefing title. If WebSearch fallback is used, do not add the emoji.

### Step 3: Deduplication

Read `data/seen_tweets.json`. Skip any tweets whose `tweet_id` matches existing entries.

### Step 4: Generate Briefing

#### Importance Scoring (two factors combined)

1. Social impact of the information
2. Impact on US stock trading

- Both high -> 3 stars
- One high + one medium, or both medium -> 2 stars
- Both low -> 1 star

#### Format Requirements

- Maximum 12 items, readable in 20 seconds on mobile
- Grouped by star rating: 3 stars first, then 2 stars, then 1 star
- Each item numbered with emoji: 1️⃣ 2️⃣ 3️⃣ ... 🔟
- Each item format (hyphen-separated, no brackets shown):
  `Category-@Blogger-CoreContent-TradingImpact-OtherSignificance`
- Categories: ICT Trading / US Stocks / AI / Politics / Finance / Tech
- Core content: One-sentence summary (20-40 chars)
- Trading impact: e.g., "Highly impacts XXX stock" / "Low impact on XXX" / "No direct impact"
- Other significance: One-sentence supplementary insight (industry trend / forward judgment / risk alert)
- Language: Mixed (names/terms/tickers in English, analysis in user's preferred language)
- One blank line between each item for readability

#### Title Format (includes push time)

- VPN connected (Scweet success): `📰 Daily Briefing | {date} {HH:MM} VPN`
- VPN not connected (WebSearch): `📰 Daily Briefing | {date} {HH:MM}`

#### Footer Format

- Scweet success: `— {N} items / Scweet / next update {time}`
- WebSearch fallback: `— {N} items / WebSearch / next update {time}`

**Important**: When Scweet succeeds, use ONLY Scweet data. Do not mix with WebSearch results.

#### Format Example

```
📰 Daily Briefing | 2026-07-16 10:00 VPN

⭐⭐⭐

1️⃣ Finance-@example-Market drops 5% on rate fears-Highly impacts SPY/QQQ-Risk-off sentiment rising

2️⃣ Tech-@example-New AI chip announced-Low impact on sector-Competitive landscape shifting

⭐⭐

3️⃣ US Stocks-@example-ES futures grind higher-Highly impacts long strategies-Maintain long positions

⭐

4️⃣ AI-@example-New research paper published-No direct impact-Watch for commercialization timeline

— 4 items / Scweet / next update 12:00
```

If no valuable new content across all categories, output "No significant updates today" and end without marking as sent.

### Step 5: Send via Feishu/Lark

```bash
lark-cli im +messages-send --user-id {YOUR_OPEN_ID} --as bot --text $'briefing content'
```

- Returns `ok: true` -> Success
- Failure -> Do not mark as sent, will retry next run

### Step 6: Update State

After confirmed send success:

1. Update `data/sent_log.json`:
   - Set `last_sent_date` to today (YYYY-MM-DD)
   - Set `last_sent_time` to current time (ISO 8601)
   - Append to `history` array: `{"date": "today", "time": "now", "preview": "first 50 chars"}`

2. Update `data/seen_tweets.json`:
   - Add all briefing items with: `{"tweet_id": "id", "username": "handle", "summary": "summary", "date": "today", "seen_at": "now"}`
   - Clean up entries older than 7 days
   - Update `last_cleanup` to today

## Important Rules

- Only execute Step 6 after Step 5 send success
- If any step fails, do not mark as sent; next run will retry
- Maximum one send per day; subsequent runs exit early
- When Scweet succeeds, use only Scweet data (no WebSearch mixing)
- VPN/proxy connection status is indicated by the VPN emoji in the title

## Adding New Bloggers

Users can add new bloggers by saying in conversation: "Add {category} blogger {handle}"

The AI then automatically:
1. Adds the blogger to `config/sources.yaml` under the appropriate category
2. Adds the handle to `scripts/fetch_tweets.py` in the `ACCOUNTS` dictionary
3. Updates the automation prompt's account list

See `references/add-blogger.md` for detailed instructions.

## Key Dependencies

- **Scweet 5.3+**: Python package for Twitter/X data fetching via auth_token
- **Twitter/X auth_token**: Obtain from browser cookies (requires periodic renewal)
- **Feishu/Lark connector**: Enabled in WorkBuddy connector management, bot identity sending
- **VPN/Proxy**: Required for Scweet to access x.com from restricted regions
- **WorkBuddy Automation**: For scheduled execution
