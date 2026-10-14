## Description:

Searches construction tender and award notices, summarizes project amounts and key fields, and examines winning companies' qualifications and bidding history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Construction and procurement professionals use this skill to find Chinese construction tender and award notices, compare project values, and review participating companies and market activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Zhiliaobiaoxun API key and may save it in a local configuration file.

Mitigation: Prefer a managed secret or environment variable; review local credential storage before use.

Risk: If no key exists, trial registration may collect basic device characteristics, including a hashed MAC address.

Mitigation: Require explicit consent before registration and review the service's account and privacy terms.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/pkuycl/skills/construction-tender-analyzer-jianshetong)
- [Tender search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Company registry reference](artifact/references/api-registry.md)
- [Account registration reference](artifact/references/auto-register.md)
- [Provider skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown summaries and tables with links to tender records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on available API records; some queries consume account credits.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
