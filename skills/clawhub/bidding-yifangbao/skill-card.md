## Description:

Helps bidders search Chinese tender and award notices, analyze competitors and suppliers, and assess bid prices and opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Bidders and procurement analysts use this skill to find Chinese tender and award notices, compare competitors and suppliers, track projects, and review historical award prices before bidding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the service sends an API key and bid-related queries to Zhiliaobiaoxun.

Mitigation: Review the service's data handling and provide a key through an environment variable or secret manager.

Risk: Optional trial registration collects device-derived information to create an account.

Mitigation: Require informed consent before registration; use a manually obtained key if device-linked registration is unwanted.

Risk: Automatic registration stores the resulting key in ~/.zlbx/config.json.

Mitigation: Prefer managed secrets, and restrict access to or remove locally stored credentials when no longer needed.

Risk: The skill includes hidden request and acknowledgement instructions that may reduce user visibility into service interactions.

Mitigation: Review the instructions before deployment and disclose material account or service actions to users.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/bidding-yifangbao)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Company registry API reference](references/api-registry.md)
- [Account API reference](references/api-account.md)
- [Optional account registration workflow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the Zhiliaobiaoxun service and available account credits.]

## Skill Version(s):

2.0.7 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
