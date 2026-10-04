## Description:

Connects an agent to a signed-in Skylight family hub to read and manage calendars, chores, shared lists, meals, photos, and family settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People with a Skylight family hub can ask an agent to check schedules, chores, shopping lists, and meals or make approved changes to their family data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector requires account credentials and can access sensitive family hub data.

Mitigation: Review the package before use, configure it locally where possible, and keep credentials out of chat.

Risk: Writes, uploads, access changes, and deletes may affect family data or expose content.

Mitigation: Request explicit user confirmation before these actions and review the target and scope of any preview.

Risk: Third-party text in photos, messages, event descriptions, or AI drafts may contain instructions.

Mitigation: Treat retrieved content as data, not authorization to change access or perform actions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [skylight-mcp npm package](https://www.npmjs.com/package/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text or Markdown based on Skylight data and requested actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report action previews requiring user confirmation before execution.]

## Skill Version(s):

1.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
