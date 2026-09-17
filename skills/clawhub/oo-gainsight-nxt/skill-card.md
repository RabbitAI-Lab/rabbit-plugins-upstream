## Description:

Operate Gainsight NXT Company data through the OOMOL gainsight_nxt connector and oo CLI for reading, creating, updating, and deleting records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query and manage Gainsight NXT Company records from an OOMOL-connected account. It supports read operations and controlled write or delete actions after schema inspection and user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents mutable remote installer scripts executed directly in a shell.

Mitigation: Review OOMOL's installer path before running it, and prefer signed, pinned, package-manager, or checksum-verified installation methods when available.

Risk: Write and destructive Gainsight NXT actions can change or delete Company records.

Mitigation: Inspect the live action schema first, then confirm the exact payload, target records, and intended effect with the user before running write or delete commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-gainsight-nxt)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Gainsight NXT Homepage](https://www.gainsight.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before constructing action payloads; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
