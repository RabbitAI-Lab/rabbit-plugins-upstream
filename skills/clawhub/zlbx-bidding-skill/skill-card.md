## Description:

Helps users search and analyze Chinese bidding notices, company procurement activity, suppliers, and market trends through Zhiliaobiaoxun data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and bidding teams use this skill to find Chinese tender and award notices, examine company bidding histories and suppliers, and summarize purchasing patterns and prices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and account checks contact the Zhiliaobiaoxun service using an API key.

Mitigation: Use a trusted secret mechanism for ZLBX_API_KEY and review what information is sent before making queries.

Risk: If no key is available, trial registration can transmit limited device-derived information and persist a returned key in ~/.zlbx/config.json.

Mitigation: Decline trial registration if this is unwanted; provide your own ZLBX_API_KEY instead and review local credential storage.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/zlbx-bidding-skill)
- [Bidding search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Company registry API reference](artifact/references/api-registry.md)
- [Account API reference](artifact/references/api-account.md)
- [Trial registration reference](artifact/references/auto-register.md)
- [Zhiliaobiaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with linked search results and concise analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an API key; data queries may consume account credits.]

## Skill Version(s):

1.4.8 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
