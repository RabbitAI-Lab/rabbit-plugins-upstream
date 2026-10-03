## Description:

Guides agents in querying U.S. homes.com listings, property details, and optionally a signed-in user's saved homes through a paired browser tab using fpx.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to prepare shell commands for searching U.S. homes.com listings, resolving addresses, inspecting property details, and accessing saved homes or searches when explicitly requested.

### Deployment Geography for Use:

Global (U.S. real-estate listings)

## Known Risks and Mitigations:

Risk: Saved homes and searches may reveal private account information.

Mitigation: Request saved-account recipes only when needed, and avoid logging or sharing their results.

Risk: Pairing fpx with a browser tab grants access through that session.

Mitigation: Verify the npm package and browser extension source before setup, and pair only if comfortable with this access.

Risk: Address resolution may return a nearby property rather than an exact match.

Mitigation: Confirm the candidate's street address before using property details.

## Reference(s):

- [homes-fpx on ClawHub](https://clawhub.ai/chrischall/skills/homes-fpx)
- [homes.com request recipes](references/homes-requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require a paired homes.com browser tab; saved-account queries require sign-in.]

## Skill Version(s):

2.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
