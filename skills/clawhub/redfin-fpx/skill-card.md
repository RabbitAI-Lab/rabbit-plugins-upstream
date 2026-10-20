## Description:

Helps agents query US Redfin listings, property details, market trends, climate data, and optionally a signed-in user's saved homes and searches through a paired browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to research US real estate listings, property histories, local markets, rentals, and climate risks without a running MCP server. With explicit access to a signed-in Redfin tab, they can also retrieve saved homes and searches.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: A paired browser tab can expose private saved homes and saved searches when signed in to Redfin.

Mitigation: Pair fpx and ContextMint Bridge only when comfortable, and request saved account data only when you intend to share it in the current session.

## Reference(s):

- [Redfin fpx skill release](https://clawhub.ai/chrischall/skills/redfin-fpx)
- [Redfin endpoint reference](artifact/references/stingray-endpoints.md)
- [ContextMint Bridge](https://github.com/nullnet-app/contextmint-bridge)
- [Fetchproxy extension information](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with shell examples and summarized Redfin data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saved homes and searches can contain private account data.]

## Skill Version(s):

1.2.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
