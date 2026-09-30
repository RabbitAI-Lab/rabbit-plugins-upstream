## Description:

Search koopje.ai for Belgian second-hand deals and auctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antarcticaice](https://clawhub.ai/user/antarcticaice)

### License/Terms of Use:

MIT-0

## Use Case:

People looking for used goods or auction lots in Belgium can find, compare and price listings from multiple marketplaces using a koopje.ai API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key grants access to saved items and the user's own listings, not just searches.

Mitigation: Keep the key private and require explicit confirmation before saving or removing items, or publishing, renewing or removing listings.

Risk: Uploading listing images or sharing precise coordinates can disclose personal information.

Mitigation: Confirm the intended images and exact location with the user before sending them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/antarcticaice/skills/koopje-search)
- [koopje.ai API reference](references/api.md)
- [koopje.ai agent documentation](https://koopje.ai/llms.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with listing links and optional API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results should include price, location and original source; auction prices are not fixed sale prices.]

## Skill Version(s):

1.0.14 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
