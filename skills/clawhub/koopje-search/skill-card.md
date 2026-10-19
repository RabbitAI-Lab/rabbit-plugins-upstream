## Description:

Search koopje.ai for Belgian second-hand deals and auctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antarcticaice](https://clawhub.ai/user/antarcticaice)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers and developers use this skill to find and compare Belgian second-hand listings and auction lots, including similar items and asking-price context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved-listing and own-listing endpoints can change account data or publish public ads.

Mitigation: Use these endpoints only after the user explicitly requests the specific save, publish, remove, or renew action.

Risk: Location searches can disclose precise user coordinates.

Mitigation: Avoid sending precise coordinates unless needed for the requested distance filter.

Risk: Comparable asking-price statistics may be mistaken for appraised market values.

Mitigation: Describe them as asking prices from similar ads, not valuations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/antarcticaice/skills/koopje-search)
- [Koopje API reference](artifact/references/api.md)
- [Koopje MCP setup](https://koopje.ai/api#mcp)
- [Koopje agent documentation](https://koopje.ai/llms.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown listing summaries with links and optional API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices and price-context statistics reflect asking prices, not appraised values.]

## Skill Version(s):

1.0.20 (source: frontmatter, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
