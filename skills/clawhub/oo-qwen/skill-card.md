## Description:

Qwen helps agents operate Qwen through an OOMOL-connected account for document analysis, OCR extraction, translation, image generation or editing, and Qwen-Audio workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect live Qwen connector schemas and run Qwen actions through the OOMOL `oo` CLI. It supports read, write, and destructive Qwen workflows with confirmation requirements for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run remote installer scripts for the `oo` CLI.

Mitigation: Verify the installer through official OOMOL CLI documentation before running pipe-to-shell commands.

Risk: The allowed command scope covers `oo *`, which is broader than the individual Qwen actions listed by the skill.

Mitigation: Limit execution to the documented Qwen connector schema and run commands, and inspect live schemas before building payloads.

Risk: Qwen write and destructive actions can create, change, or delete account resources.

Mitigation: Require explicit user confirmation of the exact payload, target, and expected effect before state-changing or destructive actions.

## Reference(s):

- [ClawHub Qwen skill page](https://clawhub.ai/oomol/skills/oo-qwen)
- [Qwen homepage](https://qwen.ai/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Qwen action payloads.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
