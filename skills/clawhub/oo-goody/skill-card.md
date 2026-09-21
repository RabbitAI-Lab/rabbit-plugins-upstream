## Description:

Goody (ongoody.com) connector skill for searching and reading Goody account, order, product, payment method, and workspace data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent retrieve Goody account, order, product, payment method, and workspace information through an existing OOMOL-connected Goody account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include one-line remote installer commands executed directly in a shell.

Mitigation: Do not let an agent run the remote installer automatically; install the oo CLI manually from a trusted source and verify the installer or package path before use.

## Reference(s):

- [ClawHub Goody skill page](https://clawhub.ai/oomol/skills/oo-goody)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Goody homepage](https://www.ongoody.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before running Goody read actions.]

## Skill Version(s):

1.0.5 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
