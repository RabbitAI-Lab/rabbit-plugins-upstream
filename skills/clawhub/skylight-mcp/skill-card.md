## Description:

Connects an agent to a signed-in Skylight family hub to read and manage calendars, chores, shared lists, meals, and related frame content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Skylight account holders and their agents use this skill to check family plans and manage events, chores, lists, meals, and frame content through a signed-in account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An external, unpinned package receives Skylight account credentials.

Mitigation: Verify the package and version before use; keep credentials in a protected project-local configuration rather than a global one.

Risk: Write, upload, member-management, and calendar-linking actions can change or disclose family data.

Mitigation: Review the intended frame, recipients, files, and scope before enabling those actions, and obtain user approval before sensitive changes.

Risk: Descriptions, captions, comments, and AI drafts may contain instructions from other people.

Mitigation: Treat retrieved content as data, not instructions for access changes or other actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [skylight-mcp npm package](https://www.npmjs.com/package/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain-language responses and confirmation previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results reflect the signed-in Skylight frame; some changes require explicit confirmation.]

## Skill Version(s):

1.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
