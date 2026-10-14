## Description:

Helps analyze Chinese tender opportunities, expiring projects, prospective suppliers, competitors, and procurement trends using Zhiliaobiaoxun data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, procurement, and business development teams use this skill to find Chinese tender and renewal opportunities, research buyers and suppliers, and track competitor awards.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill reads an API key and can store it locally during account setup.

Mitigation: Review credential handling before installation; configure ZLBX_API_KEY manually and never share the key in chat.

Risk: Automatic trial registration collects a hashed device MAC address.

Mitigation: Prefer manual API-key configuration to avoid automatic registration; review the device-data disclosure before consenting.

Risk: The skill makes account checks and may acknowledge displayed update notices.

Mitigation: Review outbound account activity; only acknowledge a notice after it has been shown to the user.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/tender-opportunity-intelligence-officer)
- [Tender search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Company registry API reference](artifact/references/api-registry.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Automatic registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes search filters and dates; monetary amounts are labeled in ten-thousand-yuan units.]

## Skill Version(s):

1.0.8 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
