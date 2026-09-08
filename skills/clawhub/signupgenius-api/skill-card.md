## Description:

Provides curl-based guidance for logging into SignUpGenius and calling its v3 and legacy APIs for profiles, groups, sign-ups, slots, participants, and RSVPs without running the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to access authorized SignUpGenius data from shell scripts, including account profile, groups, sign-up lists, public sign-up metadata, slot counts, participant details, and RSVP workflows. It is also used to prepare SignUpGenius write actions when the user has explicitly confirmed the intended change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent SignUpGenius session authority through passwords, cookies, JWTs, and refresh tokens.

Mitigation: Use it only with accounts and sign-ups the user is authorized to access, and treat exported credentials, cookies, tokens, and temporary files as sensitive secrets.

Risk: The skill can expose participant personal data such as names, emails, phone details, comments, slot participation, and RSVP information.

Mitigation: Limit requests and retained output to the user-authorized task, and avoid sharing or storing participant data beyond what is necessary.

Risk: Some documented calls can change sign-ups, RSVPs, group membership, or existing slot claims.

Mitigation: Require explicit user confirmation before any RSVP, claim, release, delete, or group-member change, then re-read the relevant sign-up or group to verify the result.

## Reference(s):

- [SignUpGenius session-mode endpoints for curl](references/sug-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with curl, jq, shell, and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes SignUpGenius session setup, endpoint examples, response-shape notes, expiry handling, and confirmation guidance for write actions.]

## Skill Version(s):

1.8.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
