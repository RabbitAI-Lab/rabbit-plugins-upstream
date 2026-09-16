## Description:

This skill lets an agent operate Seedance video generation through OOMOL's oo CLI, including reading tasks, submitting generation jobs, and canceling or deleting tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Seedance video generation through an OOMOL-connected account, including submitting tasks, listing tasks, retrieving results, and canceling or deleting generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer scripts for the oo CLI.

Mitigation: Review the installer path before installing, prefer a trusted versioned release or package manager with checksum or signature verification, and do not allow the agent to run the remote install script automatically.

Risk: The skill can submit Seedance generation tasks and cancel or delete existing tasks.

Mitigation: Confirm the exact write or delete payload, target task, and expected effect with the user before execution.

## Reference(s):

- [Seedance skill on ClawHub](https://clawhub.ai/oomol/skills/oo-seedance)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Seedance homepage](https://www.volcengine.com/product/ark)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; read actions can be run directly, while write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
