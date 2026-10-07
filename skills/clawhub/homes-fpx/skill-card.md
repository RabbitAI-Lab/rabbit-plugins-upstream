## Description:

Guides agents in querying US homes.com listings, property details, and saved account data through the user's paired browser session without a dedicated MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents, developers, and home shoppers use this skill to search US listings, inspect property details and history, resolve addresses, and retrieve their own saved homes or searches using a paired homes.com browser tab.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pairing the browser bridge with a signed-in homes.com tab allows access to private saved homes and searches.

Mitigation: Pair only when comfortable with this access; request saved account data only when needed and do not store or share it without explicit consent.

Risk: Address search may suggest a nearby property rather than the requested address.

Mitigation: Verify the returned street address before using or reporting property details.

## Reference(s):

- [homes.com request recipes](references/homes-requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [homes-fpx ClawHub release](https://clawhub.ai/chrischall/skills/homes-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and extracted listing or property data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on an available paired browser tab and current homes.com page content.]

## Skill Version(s):

2.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
