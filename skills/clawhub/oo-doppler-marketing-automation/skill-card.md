## Description:

Doppler Marketing Automation helps agents read, create, update, and delete Doppler Marketing Automation lists and subscribers through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents assisting Doppler Marketing Automation users use this skill to inspect live connector schemas and run account actions for subscriber lists and subscribers. It supports read workflows as well as confirmed write and destructive list or membership changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change Doppler Marketing Automation lists or subscriber membership.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write.

Risk: Destructive actions can delete lists or remove subscribers from lists.

Mitigation: Confirm the specific target and require explicit user approval before running actions tagged as destructive.

Risk: Setup steps can install or authorize the OOMOL oo CLI connection.

Mitigation: Run installer, login, or connection steps only after a matching command failure and only when the user trusts OOMOL and needs the integration configured.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-doppler-marketing-automation)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Doppler Marketing Automation homepage](https://www.fromdoppler.com/en/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON containing data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
