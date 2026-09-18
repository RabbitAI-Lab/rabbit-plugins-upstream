## Description:

Operates Quaderno through the OOMOL oo CLI for reading, creating, updating, and deleting Quaderno data instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate Quaderno through OOMOL's oo CLI, including reading account, contact, and product data, calculating tax rates, and performing approved record changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that can execute shell code.

Mitigation: Use a safer oo CLI installation path if available, verify the installer source, and do not let an agent run pipe-to-shell installer commands automatically.

Risk: The skill can create, update, and delete Quaderno contacts and products.

Mitigation: Review the exact payload, target record, and expected effect, then require explicit user approval before write or destructive actions.

## Reference(s):

- [ClawHub Quaderno Skill](https://clawhub.ai/oomol/skills/oo-quaderno)
- [Quaderno Homepage](https://quaderno.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that read or mutate Quaderno records; write and destructive actions require explicit user approval.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
