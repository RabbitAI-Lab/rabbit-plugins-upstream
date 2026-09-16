## Description:

Use this skill for Slab (slab.com) requests including reading, creating, updating, and deleting data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Slab connector schemas, search and read Slab content, and perform approved write or delete actions on Slab posts and topics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of a remote oo CLI installer.

Mitigation: Review installer instructions before use and prefer a verifiable package or installer with checksum or signature verification.

Risk: The skill can modify or delete Slab posts and topics.

Mitigation: Confirm exact targets, payloads, and intended effects before allowing write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-slab)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Slab homepage](https://slab.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
