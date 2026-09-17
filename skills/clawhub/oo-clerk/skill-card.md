## Description:

Clerk (clerk.com). Use this skill for ANY Clerk request: reading, creating, updating, and deleting data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Clerk action schemas and manage Clerk users through an OOMOL-connected account. It supports reading, listing, counting, creating, updating, locking, banning, unbanning, unlocking, and deleting Clerk users with confirmation requirements for write and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify, lock, ban, or delete Clerk users.

Mitigation: Require explicit confirmation of the target, payload, and expected effect before any write, ban, lock, or delete action.

Risk: The security summary flags an unsafe remote installer pattern.

Mitigation: Inspect or verify the oo CLI installer before running it, and prefer an installation path trusted by the deployment environment.

Risk: The skill connects OOMOL to Clerk with authority to modify account data.

Mitigation: Install only when the publisher is trusted and the Clerk connection has scopes appropriate for the intended operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clerk)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Clerk homepage](https://clerk.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
