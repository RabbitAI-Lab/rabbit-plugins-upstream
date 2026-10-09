# Rumoro skill for OpenClaw

Social listening from plain language. Once installed, OpenClaw can track keywords, search and triage scored mentions, set up Slack, Telegram, email and webhook alerts, read analytics and find the people behind the mentions, through the [Rumoro API](https://docs.rumoro.dev).

## Install

```bash
openclaw skills install @markolo10/rumoro --global
echo 'RUMORO_API_KEY=ref_...' >> ~/.openclaw/.env
openclaw gateway restart
```

Create the key on the API keys page at [app.rumoro.dev](https://app.rumoro.dev). New accounts start with $5.80 of free credit. The guide is at [docs.rumoro.dev/integrations/openclaw](https://docs.rumoro.dev/integrations/openclaw).

## Then ask

- "Start tracking `acme` as our brand and `globex` as a competitor."
- "What did people say about us on Hacker News this week? Which ones should I reply to?"
- "Any complaints or questions about acme in the last 24 hours? Mark the ones I already answered as done."
- "Send negative mentions to our Slack channel as they come in, and email me a digest every morning at 9."
- "How did mentions split across platforms over the last 30 days, and how do we compare with globex?"
- "Who are the ten people with the most reach who mentioned us?"
- "The classifier keeps flagging posts that aren't about us. Update our company profile so it knows what we sell."

## What is inside

`SKILL.md` has the setup, the rules of the API and which calls answer which request. `rules/` has one file per area: authentication, keywords, mentions, people and segments, alerts and channels, analytics, account, errors, and the CLI and SDKs. The reference parts are generated from the API's OpenAPI document, so the skill follows the API.

## Platforms

Reddit, X, Hacker News, GitHub, Bluesky, LinkedIn, Stack Overflow, DEV, YouTube, TikTok, Instagram and news.

## Links

- Website: [rumoro.dev](https://rumoro.dev)
- Docs: [docs.rumoro.dev](https://docs.rumoro.dev)
- Dashboard: [app.rumoro.dev](https://app.rumoro.dev)
- Source: [github.com/rumoro-dev/openclaw-skill](https://github.com/rumoro-dev/openclaw-skill)

MIT.
