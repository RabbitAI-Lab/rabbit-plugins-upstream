## Description:

Helps users review SignUpGenius sign-ups, available slots, reports, and groups, and manage sign-ups and group membership with confirmation before changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People managing volunteer events, group invitations, or RSVPs use this skill to check sign-up sheets and open slots, review their groups, and confirm requested changes to participation or membership.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SignUpGenius cookies, passwords, or API keys may expose account access if mishandled.

Mitigation: Use the least sensitive authentication mode that works and protect credentials and keys.

Risk: Approving a write with the wrong identity, group, slot, or RSVP may change the wrong participation record or invite someone unintentionally.

Mitigation: Check the preview and approve only when the identity, group, slot, and RSVP match the intended action.

Risk: Global installation makes account access available across projects.

Mitigation: Prefer project-scoped configuration unless access is needed everywhere.

## Reference(s):

- [SignUpGenius skill on ClawHub](https://clawhub.ai/chrischall/skills/signupgenius)
- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sign-up details, availability, group information, or a preview requiring approval before a change.]

## Skill Version(s):

2.1.9 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
