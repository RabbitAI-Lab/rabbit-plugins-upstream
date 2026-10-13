## Description:

Guides agents in using curl to access SignUpGenius sign-ups, groups, and RSVPs through a password-authenticated session without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read authorized SignUpGenius sign-ups and groups and, with user confirmation, manage members or RSVPs from a shell without installing an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Login credentials, session cookies, and access tokens grant account access if exposed.

Mitigation: Protect them as full account secrets, avoid logging token-bearing commands, and delete temporary cookie and header files after use.

Risk: Public sign-up lookups may expose participant information beyond the intended task.

Mitigation: Access only sign-ups and participant data the user is authorized to view, and limit disclosure to the task.

Risk: Member additions, RSVPs, claims, and releases can change sign-up records.

Mitigation: Require explicit user confirmation before each write action.

## Reference(s):

- [SignUpGenius session-mode endpoints](artifact/references/sug-endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/signupgenius-api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover authenticated and public SignUpGenius requests.]

## Skill Version(s):

2.1.10 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
