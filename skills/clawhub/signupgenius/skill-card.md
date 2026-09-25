## Description:

Read SignUpGenius sign-up sheets, slot reports, groups, and public slot availability, and help manage RSVP, slot, and group-member actions with explicit confirmation for writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and operate a SignUpGenius MCP server for reading their own sign-ups, groups, created events, and public slot availability. It can also assist with limited write actions such as RSVP, claiming or releasing a slot, and adding group members after user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use SignUpGenius session cookies, passwords, or API keys.

Mitigation: Use only accounts and sign-up links that are acceptable to expose to the MCP server, and avoid sharing credentials beyond the configured MCP environment.

Risk: The skill can change sign-up state through RSVP, slot claim or release, and group-member actions.

Mitigation: Run preview or dry-run steps first and require explicit user approval before any confirmed write action.

Risk: The skill can read participant names from public sign-up sheets.

Mitigation: Limit use to sign-up links where the user has a legitimate reason to view participant data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius)
- [Publisher profile](https://clawhub.ai/user/chrischall)
- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [signupgenius-mcp source reference](https://github.com/chrischall/signupgenius-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets, tool names, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes dry-run and explicit-confirmation guidance for write actions.]

## Skill Version(s):

2.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
