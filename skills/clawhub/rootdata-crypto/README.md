# RootData Crypto Intelligence Skill

Query crypto project data, Web3 investor info, funding rounds, trending projects, personnel job changes, and person profiles powered by [RootData](https://www.rootdata.com).

## Features
- 🔍 Search projects, investors, and people by keyword
- 📊 Get detailed project info including funding history, investors, team members, former members, and RD score
- 💰 Query batch funding round data with filters (past 365 days, max 3 investors per round)
- 🔥 View trending crypto projects (daily & weekly)
- 👥 Track personnel job changes (recent hires and departures, max 20 per category)
- 🧑 Get full person profiles including investments, education, and influence metrics

## Usage

Install via ClawHub:

```
npx clawhub@latest install rootdata-crypto
```

No registration required. An anonymous API key is automatically generated on first use.

## What's New in v1.0.5

### Updated: Project Detail (`get_item`)
- `team_members` now includes `start_employ` and `end_employ` fields
- New `former_team_members` array — departed members with same fields as `team_members`
- New `eval` field — RootData RD score for the project

## What's New in v1.0.4

### New: Person Detail (`get_people`)
- Full person profile: bio, investments, education experience, influence metrics

### Updated: Personnel Job Changes (`job_changes`)
- Each person entry now includes `X` (Twitter) and `linkedin` profile links

## What's New in v1.0.3

### Updated: Funding Rounds
- Now returns only **past 365 days** of funding data (previously from 2018)
- Each funding round shows **max 3 investors** (prioritized by lead investors)
- Removed `valuation` field from response

### New: Personnel Job Changes
- Track recent hires and departures in the crypto industry
- Get up to **20 recent entries** for each category
- Includes person info, company details, and position

## Rate Limit

200 requests / minute per key.

## Version

Current version: **v1.0.5** (2026-07-10)

