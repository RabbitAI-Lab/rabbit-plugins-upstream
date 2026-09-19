## Description:

This skill helps an agent work with SignUpGenius sign-up sheets, slots, reports, groups, and profile data, including limited account and sign-up changes when authorized by the user.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers use this skill to let an agent inspect SignUpGenius events, group membership, public slot availability, and owner-scoped reports. It is intended for accounts and sign-up sheets the user controls or is authorized to access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use sensitive SignUpGenius session cookies, passwords, or API keys.

Mitigation: Configure it only for accounts the user controls, prefer the narrowest authentication mode that works, and avoid exposing credentials in shared configuration.

Risk: The skill can change account or sign-up state, including RSVP, slot claim or release, and group-member changes.

Mitigation: Require explicit confirmation before any state-changing action and show the affected account, signup, slot, or group before proceeding.

Risk: The server security summary flags the release as suspicious because account/session access is sensitive and write actions may be undercounted.

Mitigation: Review the skill before installation and scan behavior against the release security guidance before enabling write-capable workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius)
- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration examples, command snippets, and tool-selection guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference MCP tool names and authentication modes; state-changing actions should require explicit user confirmation.]

## Skill Version(s):

2.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
