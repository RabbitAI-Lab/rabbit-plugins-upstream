## Description:

Helps agents source medical devices and consumables using Chinese procurement notices, awarded prices, and brand analyses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and sales teams use the skill to find Chinese medical-device tenders, compare awarded prices, and identify purchasing organizations and brands. Its underlying service also offers broader bidding, company, and market analysis.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Queries use an external bidding-data API and require an API key that may be read from or stored in a local file.

Mitigation: Use a personally supplied key through the platform secret mechanism; review external data sharing and avoid local credential persistence if unacceptable.

Risk: Optional trial registration uses a hashed device identifier and persists the issued key locally.

Mitigation: Require informed consent before registration; decline auto-registration if device fingerprinting or local key storage is unacceptable.

Risk: The skill includes hidden request instructions and company and market intelligence capabilities beyond medical-device sourcing.

Mitigation: Review the full skill before use, disclose relevant behavior, and limit queries to the user's requested scope.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thuanlynham-stack/skills/medical-device-sourcing-yiliaoqixiezhaobiaowang)
- [Bid search API reference](artifact/references/api-search.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and result tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the external data service, available credits, and returned records.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
