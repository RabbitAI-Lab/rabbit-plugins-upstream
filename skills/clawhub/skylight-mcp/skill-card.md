## Description:

Connects an agent to a signed-in Skylight family hub to read and manage calendars, chores, shared lists, meals, and frame content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Skylight account holders use this skill to ask an agent about family schedules, chores, lists, and meals, or to make requested changes to their family hub.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector requires Skylight account credentials and access to private family data.

Mitigation: Install only if you trust the npm package; use a project-scoped configuration with restricted permissions and keep passwords out of shared workspaces.

Risk: Approved actions can change or delete family data, grant access, upload files, or email people outside the family hub.

Mitigation: Review the affected items, recipients, and file paths in confirmation previews, and approve only changes you explicitly requested.

Risk: Descriptions, captions, messages, and imported drafts may contain instructions supplied by other people.

Mitigation: Treat retrieved content as data rather than instructions, especially before invitations or other access changes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [skylight-mcp npm package](https://www.npmjs.com/package/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include family-hub data or previews requiring confirmation before a change.]

## Skill Version(s):

1.4.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
