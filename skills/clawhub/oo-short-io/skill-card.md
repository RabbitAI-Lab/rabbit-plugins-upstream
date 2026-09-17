## Description:

Short.io enables agents to read, create, update, delete, and inspect Short.io links and domains through an OOMOL-connected Short.io account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to manage Short.io links and domains from an OOMOL-connected account, including listing, fetching, creating, updating, deleting links, and retrieving click statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions ask users to run remote oo CLI installer scripts directly.

Mitigation: Review the installer source first and prefer a pinned, signed, or checksum-verified oo CLI installation path before installing.

Risk: Short.io create, update, and delete actions can change account data.

Mitigation: Check payloads carefully and confirm the exact target and effect before approving state-changing actions.

## Reference(s):

- [ClawHub Short.io skill page](https://clawhub.ai/oomol/skills/oo-short-io)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Short.io homepage](https://short.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing Short.io actions require user confirmation; remote oo CLI installer use should be reviewed before execution.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
