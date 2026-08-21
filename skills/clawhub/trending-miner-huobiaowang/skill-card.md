## Description:

Helps agents analyze procurement and tender market activity, including industry heat, top purchasers and suppliers, company bid history, brand trends, prices, contacts, and opportunity signals through Huobiaowang/Zhiliaobiaoxun APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market analysts use this skill to query Chinese tender and procurement data, summarize market concentration and recent bidding activity, compare suppliers and brands, and identify follow-up business opportunities. The skill requires a ZLBX_API_KEY or its documented account setup flow to call the service APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic account setup can collect a device fingerprint and write credentials to ~/.zlbx/config.json.

Mitigation: Prefer manually creating and setting ZLBX_API_KEY; if auto-registration is used, obtain user consent before collection and review the local credential file.

Risk: Contact lookup may return names and phone numbers, including full phone numbers for some account tiers.

Mitigation: Use contact lookup only for a legitimate business need, display returned contact data as-is, and avoid bulk exporting or attempting to reconstruct masked numbers.

Risk: Company searches may broaden from a named company to related headquarters, subsidiaries, or branches.

Mitigation: Tell users when related entities are included and let them narrow the company set when exact entity-level analysis is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/liu-jiapeng/skills/trending-miner-huobiaowang)
- [Skill API Overview](artifact/SKILL.md)
- [Bid Search API Reference](artifact/references/api-search.md)
- [Company Analysis API Reference](artifact/references/api-company.md)
- [Market Analysis API Reference](artifact/references/api-market.md)
- [Account API Reference](artifact/references/api-account.md)
- [Automatic Account Setup Reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with JSON request examples and shell/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include tender records, company profiles, ranking tables, contact fields returned by the API, and follow-up analysis suggestions.]

## Skill Version(s):

2.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
