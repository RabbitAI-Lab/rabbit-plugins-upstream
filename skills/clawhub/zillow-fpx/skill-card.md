## Description:

Helps agents search U.S. Zillow listings, inspect properties and market data, and access saved searches or homes through a browser-connected command-line tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Zillow users can guide an agent to find U.S. property listings, retrieve property details and market reports, or view their own saved searches and homes without a Zillow MCP server.

### Deployment Geography for Use:

Global (U.S. real-estate data)

## Known Risks and Mitigations:

Risk: Browser-connected requests can access Zillow data available in the user's signed-in tab, including saved searches and homes.

Mitigation: Use a signed-in Zillow tab only when saved data is intentionally needed, and approve browser pairing deliberately.

Risk: Address autocomplete sends the entered address to Zillow.

Mitigation: Enter addresses only when sharing them with Zillow is acceptable.

Risk: A successful fetch can still return a sign-in redirect or bot-check page instead of property data.

Mitigation: Check the returned page before extracting or relying on its results.

## Reference(s):

- [Zillow page recipes](references/pages.md)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/zillow-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with shell and data-extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide retrieval of listing, property, market, and user-saved data from Zillow.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
