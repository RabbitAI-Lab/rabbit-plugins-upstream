## Description:

Assists with bidding and tender research, company information, market analysis, and procurement opportunities, defaulting searches to Guangdong Province unless the user specifies otherwise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, sales, and bidding teams use this skill to find tender notices and upcoming opportunities, review company records and award history, and summarize market activity. Searches default to Guangdong but can follow a different region specified by the user.

### Deployment Geography for Use:

Global; Guangdong Province is the default search area, not a deployment restriction.

## Known Risks and Mitigations:

Risk: The skill uses a ZLBX API key and can read or persist it in a local configuration file.

Mitigation: Review credential access before installation; configure ZLBX_API_KEY manually if preferred and protect the local configuration file.

Risk: If no key is configured, trial registration uses a hashed device identifier and stores the issued key locally.

Mitigation: Require informed consent before device-based registration; use a manually configured key to avoid this path.

Risk: A hidden workflow checks for skill updates and can acknowledge that an update notice was displayed.

Mitigation: Review the update-check and display-ack behavior; acknowledge a notice only after it is shown to the user.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/tender-guangdong)
- [Zhiliao Biaoxun service](https://ai.zhiliaobiaoxun.com/?ch=s150)
- [Search API reference](artifact/references/api-search.md)
- [Company registry API reference](artifact/references/api-registry.md)
- [Account and registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and linked search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the actual search scope and may use account credits for requested data queries.]

## Skill Version(s):

1.0.4 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
