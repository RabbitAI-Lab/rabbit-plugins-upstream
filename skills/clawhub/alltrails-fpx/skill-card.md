## Description:

Helps agents retrieve AllTrails trail details, reviews, photos, weather, and account-linked trail activity through a browser-backed shell workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other AllTrails users can use this skill to query trail information and, with a signed-in session, their saved lists, completed trails, and activity feed from a shell without the AllTrails MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser bridge has AllTrails site access and commands can use a signed-in session.

Mitigation: Install only if comfortable granting that access, and run session-backed commands only when intended.

Risk: Saved lists, completed trails, activity feeds, and profile IDs can disclose personal data.

Mitigation: Retrieve and share account-linked results only when you intend to handle that information.

## Reference(s):

- [AllTrails fpx endpoint examples](references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/alltrails-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text]

**Output Format:** [Markdown with shell examples and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only requests; account-linked results require a signed-in AllTrails session.]

## Skill Version(s):

3.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
