## Description:

Enables an agent to read, search, create, update, and delete mymind data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected mymind account from an agent, including reading objects, searching minds, organizing content, saving URLs, and performing confirmed write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes a remote installer script for the oo CLI.

Mitigation: Review the setup path first and prefer installing the oo CLI from an official, verifiable package or installation guide.

Risk: Write and destructive actions can modify, overwrite, or delete mymind data.

Mitigation: Check the exact target and payload, then get explicit user confirmation before running write or destructive actions.

Risk: A mismatched payload could cause an unintended connector action.

Mitigation: Fetch the live connector schema before constructing action data and send only JSON that matches that schema.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mymind)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [mymind homepage](https://mymind.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: artifact frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
