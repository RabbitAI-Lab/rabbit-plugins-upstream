## Description:

Search koopje.ai for Belgian second-hand deals and auctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antarcticaice](https://clawhub.ai/user/antarcticaice)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers and agents use this skill to find and compare Belgian second-hand listings and auction lots, check listing details, and report prices, locations, and sources.

### Deployment Geography for Use:

Global (searches focus on listings in Belgium)

## Known Risks and Mitigations:

Risk: Account actions can save or remove items and create, publish, renew, or remove public listings.

Mitigation: Prefer read-only search and require clear user confirmation before any listing or saved-item change.

Risk: Location-based searches can disclose precise user coordinates to koopje.ai.

Mitigation: Use a postcode or omit location when possible; send precise coordinates only with explicit user consent.

Risk: API access requires a private account key.

Mitigation: Keep the API key in the configured environment variable and do not include it in shared commands or responses.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/antarcticaice/skills/koopje-search)
- [koopje.ai API reference](references/api.md)
- [koopje.ai agent-readable documentation](https://koopje.ai/llms.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with listing links, prices, locations, and sources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a koopje.ai API key; auction lots may not have a fixed price.]

## Skill Version(s):

1.0.15 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
