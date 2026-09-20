## Description:

Gift Up (giftup.com). Use this skill for ANY Gift Up request - reading, creating, updating, and deleting data. Whenever a task involves Gift Up, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Gift Up company, gift card, item, order, location, promotion, and report transaction data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact Gift Up account actions, including redemptions, voids, top-ups, reactivations, and undo operations.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running any write or destructive Gift Up action.

Risk: The skill includes a remote oo CLI installer command.

Mitigation: Review the oo CLI installation step before installing or executing the installer.

Risk: Gift Up operations run through an OOMOL-connected account.

Mitigation: Use only a Gift Up account that the user intends OOMOL to operate.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-gift-up)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Gift Up Homepage](https://www.giftup.com/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Gift Up action payloads.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
