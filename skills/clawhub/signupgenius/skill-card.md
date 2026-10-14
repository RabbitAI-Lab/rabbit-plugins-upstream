## Description:

Helps signed-in SignUpGenius users view sign-ups, available slots, reports, and groups, and manage group members, RSVPs, and slots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

SignUpGenius account holders and event organizers use this skill to check volunteer sign-ups and availability, review their groups, and confirm requested sign-up or membership changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account access may expose SignUpGenius session credentials and sign-up details.

Mitigation: Review the MCP package and browser extension before use, prefer project-local configuration, and use the least-sensitive supported authentication mode.

Risk: RSVP, slot, and group-member actions change the user's account and may affect other people.

Mitigation: Review the proposed identity and action in the confirmation preview before approving any change.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/signupgenius)
- [SignUpGenius MCP package](https://www.npmjs.com/package/signupgenius-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sign-up availability, participant details, and confirmation previews.]

## Skill Version(s):

2.1.10 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
