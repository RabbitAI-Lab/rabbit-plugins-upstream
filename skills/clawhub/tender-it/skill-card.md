## Description:

This skill helps agents search and analyze IT, information technology, and digitalization tender data, including bid notices, awards, project timelines, company profiles, market statistics, account balance, and related supplier or purchaser insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, business development teams, procurement analysts, and bidding teams use this skill to query Chinese tender and award data, inspect company bidding records, identify market opportunities, and summarize IT-related procurement trends through Zhiliaobiaoxun APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read or store a ZLBX API key and may persist a locally obtained key.

Mitigation: Prefer setting your own ZLBX_API_KEY and review local credential storage before installation or first use.

Risk: If no key is configured, the skill can request user-approved auto-registration using OS, CPU architecture, and a hashed MAC-derived identifier.

Mitigation: Proceed with auto-registration only after explicit user consent; otherwise use the manual registration link to obtain an API key.

Risk: The release security verdict is suspicious because the skill combines tender-data API access with credential persistence and device-based registration behavior.

Mitigation: Install only after reviewing the security summary and confirming the Zhiliaobiaoxun API access pattern is acceptable for the deployment environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bailianai/skills/tender-it)
- [Zhiliaobiaoxun homepage](https://ai.zhiliaobiaoxun.com/?ch=s153)
- [Tender search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Auto-registration flow reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON request examples, tables, links, and shell commands when registration or configuration is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or local credential configuration; may call Zhiliaobiaoxun APIs and may persist an API key after user-approved auto-registration.]

## Skill Version(s):

1.0.1 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
