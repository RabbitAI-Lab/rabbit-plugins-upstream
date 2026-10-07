## Description:

Connects an agent to a signed-in Skylight family hub to read and manage calendars, chores, shared lists, meals, and frame information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and families use this skill to ask an agent about their Skylight hub and manage events, chores, shopping lists, meals, and other shared household information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to a real Skylight family hub permits changes to shared household information.

Mitigation: Install only if account access is intended, and review proposed changes before approval.

Risk: Credentials or sensitive photos could be exposed through broad configuration or unintended uploads.

Mitigation: Use project-scoped configuration, keep credentials private, and limit sensitive files in upload directories.

Risk: Access changes, uploads, bulk deletes, and recurrence-wide edits can have broad effects.

Mitigation: Review confirmation previews carefully before allowing these actions.

## Reference(s):

- [Skylight MCP on npm](https://www.npmjs.com/package/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions]

**Output Format:** [Markdown with JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can read and change data in the signed-in Skylight account; high-impact actions require confirmation.]

## Skill Version(s):

1.4.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
