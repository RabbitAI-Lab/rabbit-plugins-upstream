## Description:

Helps users check SignUpGenius sign-ups, available slots, reports and groups, and make requested changes to their own account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

SignUpGenius account holders and organizers use this skill to find sign-ups and open slots, review groups and reports, and manage their own RSVPs, slots and group members.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account passwords, API keys or session cookies may be exposed when configuring access.

Mitigation: Prefer project-local configuration, avoid storing a password unless necessary, and protect credentials and browser sessions.

Risk: RSVP, claim-slot, release-slot and add-group-member actions can change account data.

Mitigation: Show the proposed change and obtain clear user confirmation before each account-changing action.

Risk: An external npm package and browser extension may handle account access.

Mitigation: Verify the package and extension independently before installing or connecting a real account.

## Reference(s):

- [ClawHub signupgenius release](https://clawhub.ai/chrischall/skills/signupgenius)
- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sign-up, slot and participant details; account changes require user confirmation.]

## Skill Version(s):

2.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
