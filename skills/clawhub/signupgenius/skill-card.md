## Description:

Helps agents read SignUpGenius sign-ups, available slots, participants, groups and reports, and manage RSVPs, slot claims, releases and group membership.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and event organizers use this skill to check their SignUpGenius sign-ups and groups, inspect public slot availability, and, when authorized, add group members, RSVP, claim or release slots. Pro users can access full reports for their own sign-ups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RSVP, slot claim or release, and group-member addition change a real account; the security review notes that documentation understates these actions.

Mitigation: Get explicit user approval for each account-changing action and review the target event, slot and person before proceeding.

Risk: Public sign-up sheets can expose participant names even without signing in.

Mitigation: Query only sheets relevant to the user's request and avoid sharing participant details unnecessarily.

Risk: Installation and authentication may expose account credentials or session access to third-party software.

Mitigation: Prefer project-scoped configuration, verify the npm package and extension source, and avoid storing a direct password when possible.

## Reference(s):

- [ClawHub signupgenius release](https://clawhub.ai/chrischall/skills/signupgenius)
- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include participant names; full reports require a Pro key.]

## Skill Version(s):

2.1.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
