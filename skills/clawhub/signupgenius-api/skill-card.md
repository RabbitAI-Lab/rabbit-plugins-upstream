## Description:

Access SignUpGenius sign-ups, groups, and RSVPs from a shell with curl by using email/password session login, a JWT access token, ColdFusion cookies, and direct calls to the v3 API and legacy SUGboxAPI dispatcher.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to script SignUpGenius account, group, sign-up, slot, participant, RSVP, claim, and release workflows from a shell without running the signupgenius-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents unauthenticated endpoints that can collect public sign-up participant names, identifiers, and quantities.

Mitigation: Use only with SignUpGenius sheets and data you own or are authorized to access, and avoid collecting participant data from third-party sheets.

Risk: The login flow handles SignUpGenius passwords, JWT access tokens, refresh tokens, and session cookies.

Mitigation: Treat credentials, tokens, cookies, and temporary files as account secrets; do not log or commit them, and clean them up after use.

Risk: Some documented calls can add group members, RSVP, claim slots, or release sign-ups.

Mitigation: Require explicit user confirmation before running any add-member, RSVP, claim, or release command.

## Reference(s):

- [SignUpGenius session-mode endpoints for curl](references/sug-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands, curl examples, jq filters, JSON request bodies, and endpoint notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command-oriented guidance for direct SignUpGenius API usage; commands may read or modify SignUpGenius data when executed.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
