## Description:

Helps agents read SignUpGenius sign-ups, available slots, reports and groups, and manage group membership and sign-up responses with confirmation before changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

SignUpGenius account holders and event organizers use this skill to check sign-ups, groups and open volunteer slots, and to add members, RSVP, claim or release slots after confirmation. Full participant reports for owned sign-ups require a Pro API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local MCP server may access a SignUpGenius session, password or API key.

Mitigation: Install only if comfortable with that access; verify the package and browser extension source, and prefer project-level configuration.

Risk: Adding group members, RSVPing, claiming or releasing slots changes account data.

Mitigation: Keep write confirmations enabled and review each proposed change before approving it.

## Reference(s):

- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions]

**Output Format:** [Markdown with JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account-scoped results; full reports require a Pro API key.]

## Skill Version(s):

2.1.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
