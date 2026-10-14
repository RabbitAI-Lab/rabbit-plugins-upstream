## Description:

Guides agents in retrieving homes.com listings, property details, and signed-in saved homes or searches through a paired browser session using fpx.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search US real-estate listings, resolve addresses, inspect property details and history, and access a signed-in user's saved homes or searches without the homes-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Accessing saved homes or searches can expose private account-specific real-estate interests.

Mitigation: Confirm the user wants this access before running saved-data recipes, and avoid retaining or sharing fetched HTML or JSON unnecessarily.

Risk: Address resolution can return a nearby property rather than an exact match.

Mitigation: Check the resolved property's street address against the requested address before using its details.

## Reference(s):

- [homes-fpx release on ClawHub](https://clawhub.ai/chrischall/skills/homes-fpx)
- [homes.com request recipes](artifact/references/homes-requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell, JavaScript, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offers recipes for public listing data and signed-in saved homes or searches; results depend on the paired browser session.]

## Skill Version(s):

2.1.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
