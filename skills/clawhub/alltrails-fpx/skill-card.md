## Description:

Guides agents in querying AllTrails trail information and signed-in account data through a browser session using the fpx CLI without the AllTrails MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search trails and retrieve trail details, reviews, photos, weather, and their own saved lists or activity through an AllTrails browser tab.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Third-party CLI and browser extension access an AllTrails browser session.

Mitigation: Confirm you trust the fpx CLI and ContextMint Bridge before installing or pairing them.

Risk: Saved lists, completed trails, and activity may expose personal account data in shell output or logs.

Mitigation: Run account-data examples only when intended, and avoid retaining or sharing sensitive output and logs.

## Reference(s):

- [AllTrails via fpx on ClawHub](https://clawhub.ai/chrischall/skills/alltrails-fpx)
- [AllTrails endpoint examples](references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only requests; signed-in account data requires an active browser session.]

## Skill Version(s):

3.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
