## Description:

Helps users inspect SignUpGenius sign-ups, available slots, reports, and groups, and make approved changes to sign-ups or group membership.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

SignUpGenius users and organizers can check their events, group members, and open slots, review participant reports where authorized, and request RSVPs, slot changes, or group-member additions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to the SignUpGenius session, login credentials, or API key may expose sensitive account information.

Mitigation: Install only when comfortable granting this access; protect credentials and limit account access.

Risk: Public sign-up lookups and reports may expose participant names or other sensitive details.

Mitigation: Limit lookups to appropriate sheets and avoid sharing participant details unnecessarily.

Risk: RSVPs, slot claims or releases, and group-member additions change user or participant records.

Mitigation: Show the proposed change and require explicit user confirmation before submitting it.

## Reference(s):

- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp package](https://www.npmjs.com/package/signupgenius-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions]

**Output Format:** [Markdown responses and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain account or participant details.]

## Skill Version(s):

2.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
