## Description:

查询并分析 Google Trends 在指定时间范围和国家/地区的实时热门话题与热搜，帮助用户发现近期热门搜索、趋势主题和区域热点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to query recent Google Trends topics by time window and supported region, then summarize trend terms, relative search volume, and interest changes. It is suited to near-real-time market and content research, not long-term historical search-volume analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trend queries and account recovery flows may send LinkFox search queries, phone numbers, SMS codes, account tokens, API keys, and payment or order details.

Mitigation: Install and use the skill only when that data sharing is acceptable; prefer the LinkFox self-service website for account setup and review the configured endpoints before use.

Risk: Feedback reporting can include user intent, results, or conversation details.

Mitigation: Avoid sending sensitive conversation text through the feedback flow and review feedback content before submission.

Risk: Full API responses and cache files may remain in local LinkFox output directories.

Mitigation: Clean the local LinkFox session and cache directories when stored trend responses should not remain on disk.

Risk: Repeated or high-frequency calls consume LinkFox credits.

Mitigation: Use the built-in cache where appropriate and confirm with the user before making additional chargeable calls.

## Reference(s):

- [Google Trends API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Listing](https://clawhub.ai/linkfox-ai/skills/linkfox-google-trend-get-trend-by-time)
- [LinkFox Self-Service Account Setup](https://agent.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries and tables, with JSON API responses saved to local files and optionally printed inline.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses use a 24-hour parameter cache; small responses can print fully, while large responses print a concise summary with the full JSON saved in a LinkFox session directory.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
