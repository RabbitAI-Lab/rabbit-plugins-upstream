## Description:

Access SignUpGenius (sign-ups, groups, RSVPs) from a shell with curl instead of running the signupgenius-mcp server - server-side email/password login to a JWT + cfid/cftoken cookies, then curl the v3 API and legacy /SUGboxAPI.cfm dispatcher directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to have an agent produce curl-based SignUpGenius login, read, listing, RSVP, slot-claim, and release workflows without installing the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad access to SignUpGenius account, group, participant, and public sign-up details.

Mitigation: Use it only for accounts and sign-ups the user is authorized to access, and avoid collecting unauthenticated participant details from arbitrary public sign-ups.

Risk: The login flow handles email/password credentials, bearer tokens, and session cookies.

Mitigation: Keep secrets in a private shell or secret manager, use secure temporary files instead of fixed /tmp paths, and clean up cookie jars after use.

Risk: Some examples can add group members, submit RSVPs, claim slots, or release sign-up entries.

Mitigation: Require explicit user confirmation before any add, RSVP, claim, or release action and verify the target entry before changing it.

## Reference(s):

- [SignUpGenius session-mode endpoints for curl](references/sug-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that handle credentials, session cookies, and authenticated or unauthenticated SignUpGenius API calls.]

## Skill Version(s):

1.8.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
