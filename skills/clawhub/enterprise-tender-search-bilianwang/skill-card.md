## Description:

Helps procurement and sales teams search tender notices, assess suppliers and companies, and analyze bidding markets using 知了标讯 data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, bid, and business-development teams use this skill to find tender opportunities, verify supplier histories and company information, and compare purchasing trends and awarded prices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: If no API key is configured, trial registration can send a hashed device identifier to the provider and create an account.

Mitigation: Ask for informed consent before registration; offer manual key setup if the user declines.

Risk: Automatic registration can save an API key in a local configuration file.

Mitigation: Prefer a user-configured ZLBX_API_KEY when local credential persistence is unwanted; protect any stored key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/enterprise-tender-search-bilianwang)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Company registry API reference](references/api-registry.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Registration and key setup](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on API access and available account credits; contact numbers may be masked for trial accounts.]

## Skill Version(s):

1.0.7 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
