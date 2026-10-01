## Description:

Helps agents query Zillow listings, property details, market reports, and signed-in saved items through a browser-connected command-line workflow without the Zillow MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate researchers, and developers can ask an agent to search US Zillow listings, inspect property and market information, or retrieve their saved homes and searches when explicitly requested.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Zillow requests pass through fpx and the ContextMint Bridge browser extension.

Mitigation: Install only if comfortable routing Zillow requests through that browser connection.

Risk: Fetching saved homes or searches can reveal personal account information.

Mitigation: Request signed-in saved data only when you intend to share it with the agent for the current task.

## Reference(s):

- [Zillow via fpx release](https://clawhub.ai/chrischall/skills/zillow-fpx)
- [Zillow page recipes](references/pages.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and Zillow data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saved homes and searches may contain personal Zillow account data.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
