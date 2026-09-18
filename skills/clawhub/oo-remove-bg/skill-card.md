## Description:

Operate remove.bg through an OOMOL-connected account to inspect account status, remove image backgrounds, and submit improvement images via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run remove.bg account, background-removal, and improvement-submission actions through an OOMOL-connected account without handling raw remove.bg credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Prefer a verified official release or package-manager installation flow, and review installer contents before running them.

Risk: Background removal uploads images and improvement submission can send source images for future model-quality improvements.

Mitigation: Confirm the exact image, payload, and expected effect with the user before running upload, improvement-submission, or account-affecting actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-remove-bg)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [remove.bg homepage](https://www.remove.bg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with oo CLI commands, JSON connector responses, and generated image or ZIP file references when background removal runs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and a meta.executionId value.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
