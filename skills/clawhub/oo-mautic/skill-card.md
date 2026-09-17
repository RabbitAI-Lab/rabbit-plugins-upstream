## Description:

Mautic (mautic.org). Use this skill for Mautic requests involving reading, creating, updating, and deleting data through the OOMOL `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Mautic connector schemas and run contact and segment actions through an OOMOL-connected account. It supports read, write, and destructive Mautic workflows with confirmation guidance for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that execute downloaded code immediately.

Mitigation: Install the oo CLI from a trusted, versioned source and verify checksums or signatures before execution.

Risk: Write and destructive Mautic actions can change or delete contact and segment data.

Mitigation: Check the live action schema, exact target, and payload, then obtain explicit confirmation before running write or destructive actions.

## Reference(s):

- [ClawHub Mautic skill page](https://clawhub.ai/oomol/skills/oo-mautic)
- [Mautic homepage](https://mautic.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
