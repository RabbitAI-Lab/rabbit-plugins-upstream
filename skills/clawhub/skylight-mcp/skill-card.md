## Description:

Read and manage your Skylight Calendar family hub: calendar events, chores and reward stars, shared lists, and meal plans through a signed-in Skylight account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to their own Skylight family hub for calendar, chore, reward, shared-list, meal, media, and device tasks. It is intended for account-scoped household management where write, upload, and device-related actions may affect family hub data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Skylight email and password and can access household data.

Mitigation: Install only when comfortable granting account access, keep credentials in the MCP environment configuration, and remove access when no longer needed.

Risk: Write, upload, or device-related actions can change family calendars, lists, meals, chores, photos, or settings.

Mitigation: Confirm ambiguous or sensitive write and upload requests before allowing the agent to execute them.

Risk: The security verdict is suspicious because the integration exposes broader household, media, and device capabilities than the main description and triggers make clear.

Mitigation: Review the full tool surface and security guidance before installing or enabling broad agent autonomy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)
- [npm package: skylight-mcp](https://www.npmjs.com/package/skylight-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration snippets and tool-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or perform account-scoped Skylight MCP actions when configured with user credentials.]

## Skill Version(s):

0.7.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
