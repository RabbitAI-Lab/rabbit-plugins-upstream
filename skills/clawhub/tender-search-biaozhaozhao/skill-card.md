## Description:

Searches Chinese tender and award notices by keyword and returns concise lists of project names, amounts, and links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and procurement teams use this skill to find tender and award notices, check project details, and explore related company and market data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional automatic registration sends a hashed device identifier to the vendor.

Mitigation: Obtain informed consent before collecting device features; configure your own ZLBX_API_KEY to skip automatic registration.

Risk: Automatic registration stores an API key in ~/.zlbx/config.json.

Mitigation: Protect access to the local credential file and do not disclose the key in responses.

Risk: Queries can expose business contacts and consume paid account credits.

Mitigation: Limit lookups to the user's request, preserve masked contact details, and check credit costs before expanding searches.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/tender-search-biaozhaozhao)
- [Skill usage documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Automatic registration and consent flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Concise Markdown lists with project names, amounts, and source links; optional company and market summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include company and contact data; some lookups consume account credits.]

## Skill Version(s):

1.0.7 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
