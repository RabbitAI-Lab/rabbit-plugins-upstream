## Description:

Operate Felt maps and projects through the OOMOL-connected oo CLI, including reading, creating, updating, moving, duplicating, and deleting Felt data with schema-driven JSON payloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Felt through their OOMOL-connected account. It helps agents inspect live action schemas, run Felt connector actions with JSON payloads, and require confirmation before write or destructive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the oo CLI that security evidence flags for review before installation.

Mitigation: Do not let an agent run the installer automatically; install the CLI through a verifiable manual method and use the skill only if OOMOL and the oo CLI distribution path are trusted.

Risk: Felt write and destructive actions can create, update, move, duplicate, or delete maps and projects.

Mitigation: Confirm exact target IDs, payloads, and intended effects with the user before running write or destructive Felt actions.

## Reference(s):

- [ClawHub Felt Skill](https://clawhub.ai/oomol/skills/oo-felt)
- [Felt homepage](https://felt.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Guidance, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
