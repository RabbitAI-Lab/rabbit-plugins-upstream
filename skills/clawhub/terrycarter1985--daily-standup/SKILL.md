---
name: daily-standup
description: Daily standup meeting assistant — collect updates, generate summary, and distribute to the team channel
metadata:
  clawdbot:
    emoji: "📋"
    tags:
      - standup
      - team
      - meeting
      - productivity
  author: terrycarter1985
  created: "2026-08-30"
  version: "1.0.0"
  license: MIT
---

# Daily Standup Skill

## Overview

This skill automates the daily standup workflow by collecting individual updates from team members, synthesizing them into a structured summary, and distributing the result to the designated team channel.

## Applicable Scenarios

- Distributed or remote teams that run asynchronous daily standups
- Teams that need a searchable archive of standup history
- Organizations that want to reduce meeting overhead while maintaining alignment

## Prerequisites

- OpenClaw gateway running with a messaging channel configured (Discord, Slack, Telegram, etc.)
- Team members have a way to submit updates (via channel thread, DM, or form)
- A designated channel or thread for standup output

## Usage Steps

### 1. Configure Standup Settings

```json
{
  "channel": "#team-standup",
  "time": "09:30",
  "timezone": "Asia/Shanghai",
  "members": ["@alice", "@bob", "@carol"],
  "template": "{name}: ✅ {done} → 🔄 {doing} ⚠️ {blockers}"
}
```

### 2. Collect Updates

Trigger the collection phase at the scheduled time. The skill:
- Posts a standup prompt in the designated channel
- Collects responses from team members (thread or DM)
- Normalizes each response into the template format

### 3. Generate Summary

The skill synthesizes:
- Per-member status (done / doing / blockers)
- Cross-team themes and dependencies
- Action items and owner assignments

### 4. Distribute and Archive

- Posts the summary back to the channel
- Saves a dated copy to `memory/standup/YYYY-MM-DD.md`
- Updates `MEMORY.md` with notable blockers or decisions

## Metadata

| Field | Value |
|-------|-------|
| name | daily-standup |
| description | Daily standup meeting assistant — collect updates, generate summary, and distribute |
| author | terrycarter1985 |
| created | 2026-08-30 |
| version | 1.0.0 |
| tags | standup, team, meeting, productivity |
| license | MIT |

## Version History

- 1.0.0 (2026-08-30): Initial release — basic collection, summary, and distribution
