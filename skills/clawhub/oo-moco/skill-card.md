## Description:

MOCO (mocoapp.com). Use this skill for searching and reading MOCO data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve MOCO companies, contacts, and the current user's profile through the OOMOL oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review and verify the oo CLI installer independently before running it; prefer an official pinned, checksum- or signature-verified installation method.

Risk: The skill can access MOCO account data through an OOMOL-connected account.

Mitigation: Use it only for the documented read-only MOCO actions unless additional actions are clearly documented and approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-moco)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [MOCO homepage](https://www.mocoapp.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running read-oriented MOCO actions.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
