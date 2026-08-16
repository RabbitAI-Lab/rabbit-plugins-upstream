## Description:

Reads SignUpGenius sign-up sheets, slot reports, and groups, and supports user-directed group-member, RSVP, slot-claim, and slot-release actions for a signed-in account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this MCP skill to check their SignUpGenius sign-ups, group membership, public slot availability, and owner-scoped reports, and to perform user-directed updates on their own account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server may handle SignUpGenius session cookies, passwords, or Pro API keys.

Mitigation: Install only when the user accepts that account-access tradeoff, keep credentials scoped to the user's own account, and remove or rotate credentials if exposure is suspected.

Risk: The skill can expose participant names and sign-up details from public or account-linked sheets.

Mitigation: Reveal participant names only when the user clearly asks for that information and the request is appropriate for the sheet being accessed.

Risk: Write-capable tools can add group members, RSVP, claim slots, or release slots.

Mitigation: Require explicit user confirmation before executing any RSVP, group-member, claim, or release action.

Risk: Automated access may be inappropriate for accounts the user does not own or for high-scale scraping.

Mitigation: Use the skill only for personal-scale, user-directed tasks on the user's own account or authorized public sign-up sheets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius)
- [SignUpGenius](https://www.signupgenius.com)
- [npm package](https://www.npmjs.com/package/signupgenius-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce MCP configuration snippets and user-facing summaries of SignUpGenius data.]

## Skill Version(s):

1.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
