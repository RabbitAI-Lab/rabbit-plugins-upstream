## Description:

Helps agents query Zillow listings, property records, market reports, and signed-in saved data through the fpx CLI and a paired browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up US real-estate listings, property histories, photos, and market data from Zillow without an MCP server. With an authorized signed-in tab, they can also retrieve saved homes and searches.

### Deployment Geography for Use:

Global (US real-estate data)

## Known Risks and Mitigations:

Risk: A paired, signed-in Zillow tab can expose personal saved homes and searches to the agent.

Mitigation: Use saved-data commands only when intended, and remove or revoke the browser pairing when no longer needed.

Risk: A login redirect or bot-wall response can be mistaken for an empty Zillow result.

Mitigation: Check the returned page for sign-in and bot-wall markers before treating an empty result as definitive.

## Reference(s):

- [Zillow page recipes](references/pages.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/zillow-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with shell examples and structured Zillow data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saved homes and searches require an authorized signed-in Zillow tab.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
