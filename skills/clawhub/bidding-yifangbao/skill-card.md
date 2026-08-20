## Description:

Helps users search tender and award notices, analyze winning results, and summarize company, competitor, supplier, buyer, brand, and price signals for pre-bid research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Business development, sales, procurement, and tender-response teams use this skill to find relevant bid opportunities, review award history, analyze company profiles, and compare competitors before deciding where to bid.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic account setup can collect a hashed device profile and write a service key to ~/.zlbx/config.json.

Mitigation: Review the skill before installing and configure ZLBX_API_KEY manually when device profiling or local key persistence is not acceptable.

Risk: Company contact lookups may expose sensitive business or personal data.

Mitigation: Use contact data only for authorized business workflows, avoid bulk extraction or unsolicited outreach, and protect any exported results.

Risk: Persisted API keys can remain available to later agent sessions or local users.

Mitigation: Protect ~/.zlbx/config.json, remove it when persistence is no longer desired, and avoid sharing API keys in chat output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/bidding-yifangbao)
- [API overview and tool list](artifact/SKILL.md)
- [Tender search API details](artifact/references/api-search.md)
- [Company analysis API details](artifact/references/api-company.md)
- [Market analysis API details](artifact/references/api-market.md)
- [Account API details](artifact/references/api-account.md)
- [Automatic registration flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured summaries, tables, JSON request examples, and shell commands when setup is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY. API responses use a success/data/error/meta envelope and paginated result sets.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
