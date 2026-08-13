## Description:

Access SignUpGenius sign-ups, groups, RSVPs, public lookup, and slot workflows from a shell with curl by using documented session login and API call patterns instead of running the signupgenius-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to have an agent generate curl-based SignUpGenius login, profile, group, sign-up listing, RSVP, slot claim, release, and lookup workflows for accounts and sign-ups they are authorized to access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session credentials and temporary cookie jars can expose active SignUpGenius access.

Mitigation: Store passwords and tokens only in approved secret stores or short-lived environment variables, avoid logging them, and delete temporary cookie jars and login headers after use.

Risk: Unauthenticated endpoints may reveal participant names, comments, quantities, member IDs, or item-member IDs from public sign-ups.

Mitigation: Use read flows only for sign-ups the user is authorized to inspect, minimize collection of participant data, and avoid processing third-party participant details unless necessary.

Risk: Generated RSVP, claim, release, or group-member commands can change account or sign-up state.

Mitigation: Require explicit user confirmation before executing write commands and re-read the relevant sign-up or group state after execution to confirm the intended change.

## Reference(s):

- [SignUpGenius session-mode endpoints for curl](references/sug-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius-api)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, API calls, configuration]

**Output Format:** [Markdown with inline shell commands, JSON request examples, and jq recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only output; users should review generated commands before executing account-changing requests.]

## Skill Version(s):

1.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
