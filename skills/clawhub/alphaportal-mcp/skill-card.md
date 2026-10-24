## Description:

Access AlphaPortal school-transportation data from shell scripts using curl and a signed-in account's refresh token, without running the alphaportal-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

AlphaPortal account holders and developers use this skill to retrieve student, stop, bus-location, notification, and district data in shell scripts, or to update transportation settings when explicitly intended.

### Deployment Geography for Use:

Global, wherever AlphaPortal is available; users should follow their school district's data-handling requirements.

## Known Risks and Mitigations:

Risk: Examples can permanently change student transportation settings without confirmation.

Mitigation: Keep use read-only unless you explicitly approve a specific student's proposed settings change.

Risk: Reusable login tokens or student information could be exposed through shell history, logs, or shared transcripts; example IDs may not belong to the intended account.

Mitigation: Replace example IDs with verified account records. Enter secrets through a secret-entry method or credential store instead of shell commands, and keep tokens and student information out of logs and shared transcripts.

## Reference(s):

- [AlphaPortal MCP on ClawHub](https://clawhub.ai/chrischall/skills/alphaportal-mcp)
- [Publisher profile](https://clawhub.ai/user/chrischall)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Configuration, Guidance]

**Output Format:** [Inline shell commands with filtered API data, typically JSON or text via jq.]

**Output Parameters:** [Single-stream output; commands may use an account token, student ID, shift, API path, and request fields.]

**Other Properties Related to Output:** [Can retrieve sensitive student records and live location data. Write commands change real transportation settings and have no preview or confirmation in this skill.]

## Skill Version(s):

1.2.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
