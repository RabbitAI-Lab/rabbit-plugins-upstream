## Description:

Provides curl-based guidance for logging into SignUpGenius with an email/password session and calling SignUpGenius endpoints for profiles, groups, sign-up listings, public slot lookup, and RSVP workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when they want shell-based SignUpGenius access without installing or running the SignUpGenius MCP server. It helps an agent produce authenticated curl requests, request bodies, and operational guidance for reading SignUpGenius account data and performing supported RSVP or group-member actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause an agent to handle SignUpGenius passwords, JWTs, and session cookies.

Mitigation: Use a secret manager or a dedicated low-privilege account, avoid storing credentials in shell profiles or logs, and delete temporary cookie or header files after use.

Risk: Some generated commands can perform write actions such as adding group members or submitting RSVP responses.

Mitigation: Require explicit user confirmation before every write action and verify the target sign-up, group, and payload before executing the command.

Risk: Commands may expose account, group, RSVP, or public sign-up data.

Mitigation: Query only SignUpGenius resources the user is authorized to view and avoid sharing command output that contains personal or event data.

## Reference(s):

- [SignUpGenius endpoint reference](artifact/references/sug-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius-api)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command snippets and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-supplied SignUpGenius credentials or session values; generated commands may read account data or perform write actions when executed.]

## Skill Version(s):

1.3.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
