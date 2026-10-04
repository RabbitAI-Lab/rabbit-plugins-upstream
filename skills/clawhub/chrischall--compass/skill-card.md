## Description:

Helps agents look up Compass real-estate listings, property details, photos, price history, and addresses, and compare properties or estimate housing costs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate professionals, and their agents can search and compare Compass listings, inspect property records and photos, review price history, and estimate mortgage payments or affordability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Listing lookups run through an external package and browser extension using a signed-in Compass session.

Mitigation: Review the package and extension source or release checksums before use, and limit access to the documented read-only listing workflows.

## Reference(s):

- [Compass skill on ClawHub](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp package](https://www.npmjs.com/package/compass-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Plain-text or Markdown summaries of structured property, listing, and calculation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listing lookups are read-only; saved homes and saved searches are not supported.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
