## Description:

This skill helps agents query and analyze Chinese tender and bidding data for bid discovery, company analysis, market aggregation, pricing trends, and competitive research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search tender notices, inspect company bidding activity, rank purchasers, suppliers, and brands, aggregate market trends, and retrieve account usage information through the Zhiliaobiaoxun API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional onboarding can create a trial account using device-derived identifiers and persist a local API key.

Mitigation: Set ZLBX_API_KEY manually before use, or proceed with automatic registration only after reviewing and accepting the device-feature disclosure.

Risk: Tender project contact data may be exposed when requested by the user and permitted by the service account.

Mitigation: Limit contact lookups to legitimate business needs, preserve any service-side masking, and avoid bulk exporting contact details.

Risk: Local credential storage can leave an API key available to other local processes or users with file access.

Mitigation: Protect the local configuration file, rotate the key if it is exposed, and prefer environment-based secret management in shared environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/tender-bid-union-zhongzhaolianhe)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account query API reference](artifact/references/api-account.md)
- [Automatic registration flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured summaries, tables, JSON request examples, and occasional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-consented trial account registration before paid data tools can run.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
