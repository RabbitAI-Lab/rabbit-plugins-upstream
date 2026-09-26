## Description:

Helps agents research homes.com listings, property details, price and tax history, market reports, saved homes, and photo galleries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate professionals, and their agents use this skill to research US property listings, compare homes, review price and tax histories, and calculate housing costs using homes.com data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separate server package and browser extension can access listing data through a signed-in homes.com tab, including saved homes and searches.

Mitigation: Review both external components before installing, limit use to read-only property research, and avoid using a sensitive browser session.

## Reference(s):

- [Homes skill listing](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp project](https://github.com/chrischall/homes-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown summaries of property data and housing calculations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Property photos may be returned as URLs; saved homes and searches require a signed-in homes.com tab.]

## Skill Version(s):

2.1.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
