## Description:

Helps users search and analyze tender notices, contract awards, suppliers, competitors, and procurement trends using Zhiliaobiaoxun data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and business-development teams use this skill to find tender opportunities, review awards and supplier histories, compare competitors, and summarize market activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic trial registration collects a hashed MAC-derived device identifier and contacts Zhiliaobiaoxun services.

Mitigation: Require informed consent before registration; configure your own ZLBX_API_KEY to skip automatic registration.

Risk: The skill stores an API key locally and may present automatic-login recharge links.

Mitigation: Protect local credentials and review the account and payment destination before using recharge links.

## Reference(s):

- [ClawHub release](https://clawhub.ai/liu-jiapeng/skills/tender-search)
- [Zhiliaobiaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](references/api-search.md)
- [Account and registration guidance](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language summaries and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the user's API access and available tender data.]

## Skill Version(s):

2.1.7 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
