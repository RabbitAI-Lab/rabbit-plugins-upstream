## Description:

Guides agents in searching U.S. Zillow listings and retrieving property details, history, photos, market reports, and signed-in saved items through a user-approved browser connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve U.S. real-estate listings and property information from Zillow without the Zillow MCP server. With a signed-in browser tab, they can also access the user's saved searches and homes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a browser extension and CLI to access Zillow through the user's browser session.

Mitigation: Install only if you trust @fetchproxy/cli and the ContextMint Bridge extension; approve browser pairing yourself.

Risk: Saved searches and saved homes can reveal private Zillow account activity to the agent session.

Mitigation: Use saved-item commands only when you intend to share that account data with the agent.

Risk: A sign-in redirect or bot challenge may be mistaken for valid property data.

Mitigation: Check the fetched page for sign-in or challenge markers before treating results as complete.

## Reference(s):

- [Zillow page and extraction guide](references/pages.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/zillow-fpx)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance and shell snippets; extracted Zillow data as JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saved searches and homes require a signed-in Zillow tab.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
