## Description:

Searches Chinese procurement notices and related company, supplier, brand, and medical-device award-price data through Zhiliaobiaoxun.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams and market researchers can find Chinese tender notices, review company and supplier activity, and compare historical award prices for medical devices and consumables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic account registration may use device features, and procurement terms and filters are sent to an external service; requests may consume credits.

Mitigation: Prefer a manually obtained API key to skip hardware identification. Before automatic registration, disclose the requested device features and obtain user consent; check the credit cost before querying.

Risk: Saved API keys and login links could expose account access.

Mitigation: Protect stored keys and login links, and avoid sharing them in output.

Risk: The review could not verify server-side behavior or data retention.

Mitigation: Avoid sending sensitive procurement details unless the user approves sharing them with the service.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/pkuycl/skills/medical-device-sourcing-yiliaoqixiezhaobiaowang)
- [Tender search API guide](artifact/references/api-search.md)
- [Company data API guide](artifact/references/api-company.md)
- [Market analysis API guide](artifact/references/api-market.md)
- [Account API guide](artifact/references/api-account.md)
- [Business registry API guide](artifact/references/api-registry.md)
- [Credential setup and automatic registration guidance](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Concise summaries and Markdown tables of search results, company information, market statistics, and historical prices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected filters and available service data.]

## Skill Version(s):

1.0.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
