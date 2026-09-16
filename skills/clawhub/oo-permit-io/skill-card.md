## Description:

Permit.io (permit.io). Use this skill for ANY Permit.io request - reading, creating, updating, and deleting data. Whenever a task involves Permit.io, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Permit.io connector schemas and manage Permit.io users, tenants, and role assignments through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can manage high-impact Permit.io authorization data through OOMOL.

Mitigation: Use trusted OOMOL and Permit.io accounts, prefer least-privilege Permit.io credentials, and review target users, tenants, roles, and environments before execution.

Risk: Write and destructive actions can change or remove Permit.io users, tenants, and role assignments.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running any write, destructive, or role-unassignment action.

Risk: First-time setup includes pipe-to-shell installer commands.

Mitigation: Avoid running installer commands unless the installer source has been independently verified and the local execution risk is acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-permit-io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Permit.io Homepage](https://www.permit.io)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and may return JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
