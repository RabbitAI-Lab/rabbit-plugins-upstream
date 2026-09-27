## Description:

Query real-time and historical financial data across equities and crypto for market analysis, alerts, reporting, watchlists, and portfolio workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bibaofeng](https://clawhub.ai/user/bibaofeng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and autonomous agents use this skill to retrieve AIsa stock and crypto market data for research, monitoring, alerts, reports, and portfolio workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AIsa API key exposure or misuse.

Mitigation: Install only in trusted environments and provide AISA_API_KEY through environment variables rather than embedding it in prompts or files.

Risk: Market queries may reveal ticker lists, portfolio interests, or investment research topics to AIsa.

Mitigation: Avoid sending sensitive portfolio details unless the user is comfortable sharing them with the API provider.

Risk: Requests may consume AIsa credits.

Mitigation: Review planned API calls, especially broad screenings or repeated portfolio queries, before running them.

## Reference(s):

- [ClawHub Market skill page](https://clawhub.ai/bibaofeng/skills/market)
- [bibaofeng ClawHub publisher profile](https://clawhub.ai/user/bibaofeng)
- [AIsa API Reference](https://docs.aisa.one/reference/)
- [AIsa](https://aisa.one)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON API responses and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires AISA_API_KEY; requests may consume AIsa credits.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
