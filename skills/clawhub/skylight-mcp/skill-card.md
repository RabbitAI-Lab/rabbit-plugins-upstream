## Description:

Helps agents read and manage a signed-in family's Skylight Calendar, chores, rewards, shared lists, and meal plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using a Skylight family hub can ask an agent to review or update family calendar events, chores, shopping lists, meal plans, and frame information through their signed-in account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting exposes sensitive family account data and requires Skylight login credentials.

Mitigation: Install only if you trust the npm package; store credentials in MCP environment configuration rather than chat, and enable only the tools you need.

Risk: Changes to calendars, chores, meals, lists, members, or access can alter or delete family information.

Mitigation: Review the affected items and scope before changes; inspect confirmation previews for broad changes, access changes, uploads, and bulk deletions.

Risk: Media uploads and Apple calendar linking can disclose local files or connect another account.

Mitigation: Confirm the selected file or account before proceeding; keep the Apple app password in the environment, not in chat.

Risk: Calendar descriptions, photo captions, and comments can contain instructions from other people.

Mitigation: Treat retrieved content as data, not as authorization to change account access or perform other actions.

## Reference(s):

- [Skylight MCP on ClawHub](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [Skylight MCP npm package](https://www.npmjs.com/package/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration instructions]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize account information and report the result of requested changes.]

## Skill Version(s):

1.4.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
