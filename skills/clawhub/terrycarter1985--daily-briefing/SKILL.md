---
name: daily-briefing
description: Generate a concise daily briefing by pulling together weather, calendar, recent messages, and news into one readable summary. Use when the user asks for a "daily digest", "morning briefing", or wants a quick overview of what matters today.
metadata: { "openclaw": { "emoji": "📋", "category": "productivity" } }
---

# Daily Briefing

Produces a structured daily briefing using available tools.

## When to Use

- User asks for "what's going on today" or "daily briefing"
- Morning check-in or end-of-day summary
- Recurring cron-triggered digest

## Inputs

| Parameter | Required | Description |
|-----------|----------|-------------|
| `timezone` | No | IANA timezone string (default: user's configured TZ) |
| `include_news` | No | Whether to include web search news (default: true) |
| `locale` | No | Language for output (default: en) |

## Steps

1. **Check timezone** — Resolve from parameter, USER.md, or session config.
2. **Gather weather** — Use the `weather` skill or wttr.in for the configured location.
3. **Check calendar** — Look for events in next 24h (if calendar tool available).
4. **Scan recent messages** — Summarize unread/important messages from last 12h.
5. **Fetch news** — Run `web_search` for top headlines if `include_news` is true.
6. **Compose briefing** — Format as markdown with sections: 🕐 Time, 🌤 Weather, 📅 Calendar, 💬 Messages, 📰 News.

## Output Format

```markdown
# 📋 Daily Briefing — YYYY-MM-DD

## 🌤 Weather
<weather summary>

## 📅 Calendar
<upcoming events or "Nothing scheduled">

## 💬 Unread Messages
<message summary or "Inbox zero 🎉">

## 📰 Top News
<2-3 headline summaries>
```

## Example Invocation

```
Please generate my daily briefing for Asia/Shanghai, include tech news.
```

## Dependencies

- `weather` skill (or wttr.in fallback)
- `web_search` for news
- Access to calendar/message tools if available

## Notes

- Keep output concise — aim for under 400 words.
- Gracefully skip sections if tools are unavailable.
- Cache weather results for 2 hours to avoid rate limits.
