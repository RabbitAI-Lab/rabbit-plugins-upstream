## Description:

Guides agents in accessing SignUpGenius sign-ups, groups, and RSVPs with curl using account-based session authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve authorized SignUpGenius account, group, and sign-up data and manage RSVPs from a shell without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Passwords and session tokens could be exposed through logs, committed files, or temporary cookie and header files.

Mitigation: Store credentials securely, avoid logging or committing secrets, and delete temporary authentication files after use.

Risk: Group and sign-up queries may expose participant names, contact details, member IDs, and slot data.

Mitigation: Access only accounts and sign-ups you are authorized to use, and limit sharing or retention of personal data.

Risk: Write requests can change group membership or RSVPs.

Mitigation: Confirm the intended change with the user before sending write requests.

## Reference(s):

- [SignUpGenius session-mode endpoint examples](references/sug-endpoints.md)
- [SignUpGenius API skill release](https://clawhub.ai/chrischall/skills/signupgenius-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authorized SignUpGenius access for account-specific operations.]

## Skill Version(s):

2.1.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
