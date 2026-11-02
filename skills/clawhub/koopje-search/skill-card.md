## Description:

Search koopje.ai for Belgian second-hand deals and auctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antarcticaice](https://clawhub.ai/user/antarcticaice)

### License/Terms of Use:

MIT-0

## Use Case:

External users can find Belgian second-hand listings and auction lots, then review listing details such as price, location, and source.

### Deployment Geography for Use:

Belgium

## Known Risks and Mitigations:

Risk: The API key enables account features, including actions that change saved listings or publish and manage public ads.

Mitigation: Use account-changing actions only when deliberately requested, confirm sensitive listing actions, and review ad content before posting.

Risk: Search questions, follow-up messages, and location filters are sent to koopje.ai.

Mitigation: Share only relevant information and prefer a postcode over precise coordinates.

## Reference(s):

- [API reference](references/api.md)
- [koopje.ai API and MCP documentation](https://koopje.ai/api#mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language listing summaries with links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include listing price, location, and source when provided by the service.]

## Skill Version(s):

1.0.22 (source: frontmatter, confirmed by server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
