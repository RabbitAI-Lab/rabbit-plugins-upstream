## Description:

Read Microsoft Teams chats, teams, channels, Activity feed entries, and the currently open chat or channel from a signed-in browser tab using the fpx CLI instead of the microsoft-teams-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and authorized Microsoft Teams users use this skill to configure fpx and run shell commands that extract read-only Teams data from an already signed-in browser tab for scripts or local inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Teams exports may include sensitive chat, channel, or Activity feed content.

Mitigation: Use the skill only with Teams accounts and conversations you are authorized to inspect, and handle exported output as confidential data.

Risk: If multiple teams.cloud.microsoft tabs are open, fpx may read from a tab or conversation the user did not intend.

Mitigation: Close other Teams tabs before running commands and use the openConversation selector to confirm the currently open chat or channel.

Risk: The skill depends on the fpx CLI and Transporter browser extension having access to a signed-in Teams tab.

Mitigation: Install only trusted fpx and Transporter components, approve pairing deliberately, and rerun health checks or pairing when the bridge is unavailable.

## Reference(s):

- [fpx dom-list recipes for Teams](references/dom-list-recipes.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/microsoft-teams-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Teams Web DOM-list guidance; command output may contain confidential Teams data.]

## Skill Version(s):

0.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
