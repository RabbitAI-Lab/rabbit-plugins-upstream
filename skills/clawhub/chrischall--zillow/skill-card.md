## Description:

Helps users find Zillow listings, review property details and market trends, calculate housing costs, and retrieve their saved Zillow activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, renters, and other Zillow users can explore listings, property records, market reports, and their own saved homes and searches through an assistant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external package and browser extension use a signed-in Zillow session.

Mitigation: Verify the package, source repository, and extension checksum before installing, and enable session access only when intended.

Risk: Saved homes and searches may disclose sensitive personal plans.

Mitigation: Avoid connecting saved Zillow activity when that information should remain private.

## Reference(s):

- [Zillow skill release](https://clawhub.ai/chrischall/skills/zillow)
- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language answers with listing details, market figures, or saved-activity summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Zillow lookups; saved activity requires a signed-in session.]

## Skill Version(s):

1.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
