## Description:

Sage Sales Management (forcemanager.com). Use this skill for Sage Sales Management requests involving reading, creating, updating, and deleting data through the OOMOL `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage Sage Sales Management accounts, contacts, and opportunities through an OOMOL-connected account. It supports schema discovery plus read, create, update, list, and delete workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path includes one-line remote installer commands for the `oo` CLI.

Mitigation: Prefer a separately reviewed, version-pinned, checksum- or signature-verified installation path before using the skill.

Risk: Create, update, and delete actions can change Sage Sales Management CRM data.

Mitigation: Review the live schema and confirm the exact payload, target, and effect with the user before approving write or destructive actions.

Risk: The security verdict is suspicious because setup can ask an agent or user to run an unverified remote installer directly in a shell.

Mitigation: Install only when the publisher is trusted and the `oo` CLI installation path has been independently reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sage-sales-management)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Sage Sales Management homepage](https://www.forcemanager.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses `oo connector schema` to inspect action schemas and `oo connector run --json` to execute actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
