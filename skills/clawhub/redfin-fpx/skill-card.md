## Description:

Guides agents in querying U.S. Redfin listings, property details, market trends, and saved items through a paired browser tab using fpx.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate researchers use this skill to retrieve U.S. listing and property information, market trends, and, when signed in, saved homes and searches without running an MCP server.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Pairing with a signed-in Redfin tab can expose saved homes and saved searches to the agent.

Mitigation: Use a dedicated browser profile or sign out of Redfin when only public listing data is needed.

## Reference(s):

- [Redfin fpx skill release](https://clawhub.ai/chrischall/skills/redfin-fpx)
- [Redfin endpoint reference](references/stingray-endpoints.md)
- [Redfin](https://www.redfin.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples extract Redfin responses as JSON; saved items require a signed-in tab.]

## Skill Version(s):

1.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
