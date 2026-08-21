## Description:

Queries dated TikTok Shop video rankings from EchoTik by date, region, ranking type, and metric, returning ranked videos with engagement, sales, and estimated GMV metrics across 16 marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and agents use this skill to discover top-performing TikTok Shop videos for a selected date and marketplace. It supports ranking by views or estimated video sales for market scouting, campaign analysis, and paginated review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles API keys and may guide phone or SMS onboarding.

Mitigation: Prefer the official self-service account portal for credentials, configure keys through environment variables, and do not share verification codes unless the user initiated the onboarding action.

Risk: The skill includes billing and payment flows for a paid external service.

Mitigation: Confirm the user intends to spend credits or create an order before running paid actions, and only scan payment QR codes or open payment links that the user requested.

Risk: Full API responses may be retained in the local linkfox output directory.

Mitigation: Review saved JSON files for sensitive or unnecessary data and clean the local linkfox directory when retention is not needed.

Risk: Ranking data may lag by 1-2 days, metrics can be sparse outside the selected ranking field, and sales or GMV values are estimates.

Mitigation: Use dates at least two days in the past, present estimated metrics as approximations, and avoid treating zero values in non-selected metrics as complete performance data without verification.

## Reference(s):

- [EchoTik-TikTok视频排行 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-video-rank)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, shell commands, and saved JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under the workspace linkfox directory; large responses print a summary unless --inline is used; calls consume 5 credits and identical parameter combinations use a 24h local cache.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
