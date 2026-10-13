## Description:

Searches tender and award data to identify prospective buyers, customers, suppliers, and business opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and procurement teams use the skill to find tender opportunities, prospective purchasing organizations, and companies' customers or suppliers from bid records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration uses a hashed device identifier to distinguish free trials.

Mitigation: Obtain user consent before registration, or set a personal ZLBX_API_KEY to avoid the automatic flow.

Risk: The skill can save an API key locally for later authentication.

Mitigation: Protect access to ~/.zlbx/config.json and review or delete it when automatic authentication is no longer wanted.

Risk: The skill can generate account login and recharge links.

Mitigation: Review the destination before signing in or paying; do not share an API key in chat.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/precision-tender-sourcing-xunbiaobao)
- [Provider skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Business registry API reference](references/api-registry.md)
- [Account API reference](references/api-account.md)
- [Automatic registration guide](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tender counts, filters, buyer or supplier leads, and account guidance.]

## Skill Version(s):

2.0.5 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
