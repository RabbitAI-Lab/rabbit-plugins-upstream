## Description:

Clerk enables agents to inspect and run Clerk account actions through the OOMOL-connected oo CLI for reading, creating, updating, and deleting Clerk data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Clerk users through an OOMOL-connected account, including read actions, user creation, profile updates, locks, bans, and deletion with confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands for the oo CLI can execute code on the user's machine.

Mitigation: Review the install path, prefer a verified package or documented release with integrity checks, and avoid running installer commands without user approval.

Risk: The skill can perform write or destructive Clerk user-management actions.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before banning, locking, updating, or deleting users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clerk)
- [Clerk homepage](https://clerk.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Clerk action payloads.]

## Skill Version(s):

1.0.5 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
