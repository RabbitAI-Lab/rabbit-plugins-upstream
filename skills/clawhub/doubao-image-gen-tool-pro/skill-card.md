## Description:

Guides agents through Doubao image generation automation, including batch image generation, multiple output ratios, style presets, prompt enhancement, API-key setup, and workflow scripting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, designers, and enterprise teams use this skill to configure and automate Doubao image-generation workflows for e-commerce product images, marketing assets, educational materials, game assets, and content review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to call external Doubao or prompt-enhancement services.

Mitigation: Use only intended service accounts, apply request limits, and review generated scripts before execution.

Risk: API keys are required for some workflows.

Mitigation: Provide keys through environment variables and avoid hard-coding credentials in scripts or configuration files.

Risk: The skill can guide file writes, command execution, and image/report output paths.

Mitigation: Restrict file access and output directories to project folders and inspect commands before running them.

Risk: Generated images may raise copyright, privacy, or inappropriate-content concerns.

Mitigation: Prefer original prompts and approved reference materials, review outputs before use, and apply content and privacy checks appropriate to the deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/doubao-image-gen-tool-pro)
- [Detailed reference](references/detail.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON/YAML examples and bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to call external services, run commands, and write generated image files or reports.]

## Skill Version(s):

1.0.0 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
