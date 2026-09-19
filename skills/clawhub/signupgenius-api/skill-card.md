## Description:

Access SignUpGenius sign-ups, groups, and RSVPs from curl by logging in with email and password to obtain session tokens, then calling SignUpGenius v3 and legacy endpoints directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to compose curl commands for reading SignUpGenius profile, group, sign-up, participant, and RSVP data. It also documents carefully confirmed write actions such as adding group members, submitting RSVPs, claiming slots, and releasing slots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires handling SignUpGenius passwords, JWTs, cookies, cookie jars, and refresh tokens.

Mitigation: Treat those values as account-access secrets, avoid exposing them in logs or shared shells, and delete temporary login artifacts after use.

Risk: The skill documents account-changing write actions such as adding members, submitting RSVPs, claiming slots, and releasing slots.

Mitigation: Confirm every write action with the user immediately before running it, then verify the result with a read-back call.

Risk: The skill documents no-login access patterns that can expose participant names and IDs for public sign-ups.

Mitigation: Use the unauthenticated participant-enumeration examples only for sign-ups the user is authorized to manage or view.

## Reference(s):

- [SignUpGenius session-mode endpoints for curl](references/sug-endpoints.md)
- [ClawHub release page for signupgenius-api](https://clawhub.ai/chrischall/skills/signupgenius-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SignUpGenius credentials, JWT and cookie headers, and endpoint-specific JSON bodies; write actions require user confirmation.]

## Skill Version(s):

2.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
