## Description:

Helps agents search homes.com listings, inspect property details, and access saved homes and searches through the user's browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to find US real-estate listings, look up property details and history, and retrieve a signed-in user's saved homes or searches without running the homes-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to saved homes and searches uses the user's signed-in homes.com session and may expose account-specific data.

Mitigation: Run saved-homes or saved-searches commands only when the user intends to access that data; handle results carefully.

Risk: The skill relies on an external CLI and browser extension paired with the user's browser session.

Mitigation: Review the fpx CLI and ContextMint Bridge extension before installing and pairing them.

Risk: Address lookup may return a nearby property rather than the requested one.

Mitigation: Verify each resolved address against the requested address before using property details.

## Reference(s):

- [homes-fpx ClawHub release](https://clawhub.ai/chrischall/skills/homes-fpx)
- [homes.com request recipes](references/homes-requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands and data-extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include listing data or account-specific saved homes and searches.]

## Skill Version(s):

2.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
