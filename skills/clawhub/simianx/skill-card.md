## Description:

Give an agent access to SimianX AI for stock and crypto research, live analysis, news and catalyst monitoring, and scheduled autopilots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simianxai](https://clawhub.ai/user/simianxai)

### License/Terms of Use:

MIT

## Use Case:

Agents use SimianX AI to research US stocks and crypto, summarize market news and sector catalysts, and follow symbols through live sessions or scheduled monitoring. The service can return trade proposals and PDF research reports; review findings before acting and require approval for real orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research can include trade proposals that may be incorrect or misleading.

Mitigation: Review conclusions and stated risks before acting, and require explicit approval before any real order.

Risk: Credit spending and recurring work may not be visible enough to the user.

Mitigation: Review spending estimates, use a narrowly scoped key with spending caps and expiry, and set a stopping point before recurring work.

Risk: Instructions may be replaced by updates fetched from the internet without clear approval.

Mitigation: Review instruction changes and approve them before following the updated instructions.

Risk: Some referenced helper scripts are missing from the release.

Mitigation: Review any separately obtained helper code before running it.

## Reference(s):

- [SimianX agent documentation](https://www.simianx.ai/agents)
- [SimianX API OpenAPI specification](https://service.simianx.ai/v1/openapi.json)
- [SimianX ClawHub release](https://clawhub.ai/simianxai/skills/simianx)
- [Authentication and API keys](artifact/references/auth.md)
- [Deep research](artifact/references/deep.md)
- [Live analysis sessions](artifact/references/live.md)
- [Autopilots](artifact/references/autopilots.md)
- [News and news watches](artifact/references/news.md)
- [API integration guidance](artifact/references/developers.md)
- [Billing and usage](artifact/references/billing.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, PDF reports, Guidance]

**Output Format:** [Agent-facing research summaries and updates, with optional PDF reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live or scheduled updates across multiple analysis steps.]

## Skill Version(s):

1.0.7 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
