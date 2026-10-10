## Description:

Guides agents in accessing SignUpGenius sign-ups, groups, and RSVPs with shell commands using account-based authentication instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other SignUpGenius users use this skill to retrieve sign-ups and group information or manage RSVPs and slot claims from a shell without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account passwords, bearer tokens, and session cookies may be exposed through shell history, logs, or temporary files.

Mitigation: Use a private machine and secure secret handling; do not log or paste authorization headers or cookies, and delete cookie jars and temporary header files after use.

Risk: Public participant lookups can expose personal information.

Mitigation: Only retrieve participant details for an authorized purpose and limit sharing of personal data.

Risk: RSVP, slot-claim, release, and group-member actions can change account or participant records.

Mitigation: Confirm the intended action and account details with the user before making changes.

## Reference(s):

- [SignUpGenius API skill release](https://clawhub.ai/chrischall/skills/signupgenius-api)
- [SignUpGenius session-mode endpoint reference](references/sug-endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
