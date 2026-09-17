## Description:

Access SignUpGenius sign-ups, groups, and RSVPs from a shell with curl instead of running the signupgenius-mcp server, using email/password login to obtain session cookies and then calling the v3 API and legacy dispatcher directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to have an agent produce curl commands and request patterns for reading SignUpGenius profile, group, sign-up, slot, participant, and RSVP data without installing an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands may expose email/password credentials, JWTs, or cookies through shell history, logs, temporary files, or shared machines.

Mitigation: Use a password manager or prompt, avoid shell tracing and command logging, run only on a trusted single-user machine, store cookies in a private mktemp directory, and remove temporary files after use.

Risk: The skill documents unauthenticated endpoints that can reveal participant-level SignUpGenius data.

Mitigation: Use participant and slot data only when there is a legitimate authorization basis, and avoid retrieving or sharing personal information beyond the task need.

Risk: Some examples describe write-capable actions such as adding group members, RSVP submission, slot claims, or release flows.

Mitigation: Require explicit user confirmation before executing any write action and re-read the affected sign-up or slot after the request to verify the outcome.

## Reference(s):

- [SignUpGenius session-mode endpoints for curl](references/sug-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that handle credentials, session cookies, participant data, and write-capable SignUpGenius actions.]

## Skill Version(s):

1.8.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
