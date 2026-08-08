## Description:

Reads SignUpGenius sign-up sheets, slot reports, and groups, and can add members to groups or RSVP to public slots for the user's signed-in account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to their SignUpGenius account for reading sign-ups, groups, public slot availability, and owner-scoped reports. It also supports limited write actions for adding group members and RSVPing to public slots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use SignUpGenius account credentials, session cookies, or a Pro API key.

Mitigation: Install only when the agent should access the user's SignUpGenius account, prefer project-level MCP configuration, and avoid direct password storage when fetchproxy or an API key is safer for the setup.

Risk: The skill exposes write actions for RSVPing to public slots and adding members to groups.

Mitigation: Require explicit user confirmation before RSVP or add-member actions and review the target sign-up, slot, group, and person details before execution.

Risk: The artifact notes a SignUpGenius automation terms-of-service caveat.

Mitigation: Use the connector only at personal-account, personal-scale levels and review SignUpGenius terms before broader or automated use.

## Reference(s):

- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [signupgenius-mcp source link from artifact](https://github.com/chrischall/signupgenius-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, API Calls]

**Output Format:** [Markdown guidance with JSON configuration examples and SignUpGenius MCP tool recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require fetchproxy cookies, SignUpGenius email/password credentials, or a SignUpGenius Pro API key depending on the requested tool.]

## Skill Version(s):

1.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
