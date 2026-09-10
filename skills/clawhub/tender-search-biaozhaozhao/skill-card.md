## Description:

招投标快捷检索引擎-标找找 helps agents quickly search tender and award announcements by keyword, extract project names, amounts, and links, and return concise result lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business development teams use this skill to search tender opportunities, award announcements, company records, market summaries, and account usage data. It is intended for concise procurement intelligence workflows that need project titles, dates, amounts, purchasers, suppliers, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger device-based trial registration when no API key is configured.

Mitigation: Require explicit user consent before registration and prefer preconfiguring ZLBX_API_KEY through a trusted secret mechanism.

Risk: The skill may store a returned API key in a local configuration file.

Mitigation: Review local file permissions and avoid exposing the API key in conversation, logs, or generated output.

Risk: The skill may surface account, recharge, login, referral, and contact-data flows.

Mitigation: Review these flows before deployment, verify links before use, and preserve contact masking instead of attempting to reconstruct hidden contact details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/tender-search-biaozhaozhao)
- [Publisher profile](https://clawhub.ai/user/liu-jiapeng)
- [API account reference](references/api-account.md)
- [API company reference](references/api-company.md)
- [API market reference](references/api-market.md)
- [API search reference](references/api-search.md)
- [Auto-registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration guidance]

**Output Format:** [Markdown summaries with tables, links, and occasional JSON, HTTP, or shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved trial registration before authenticated data calls.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
