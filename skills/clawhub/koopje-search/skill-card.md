## Description:

Search koopje.ai for Belgian second-hand deals and auctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antarcticaice](https://clawhub.ai/user/antarcticaice)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers and agents use this skill to find and compare Belgian second-hand listings and auction lots, including prices, locations, and links to original listings.

### Deployment Geography for Use:

Global (Belgian listings)

## Known Risks and Mitigations:

Risk: A search request could lead to saving items or changing public listings through the same skill.

Mitigation: Get user confirmation before saving items or creating, publishing, renewing, or removing listings; confirm any images or listing data being sent.

Risk: Location-filtered searches can disclose precise coordinates.

Mitigation: Confirm before sending exact coordinates; prefer a postcode when it meets the user's needs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/antarcticaice/skills/koopje-search)
- [koopje.ai API documentation](https://koopje.ai/api)
- [Skill API reference](references/api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown listing summaries with prices, locations, sources, and links; optional API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results depend on a koopje.ai API key and live listings; auction lots may lack a fixed price.]

## Skill Version(s):

1.0.19 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
