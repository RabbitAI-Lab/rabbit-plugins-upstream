## Description:

Transforms an existing model or mannequin product photo into alternate model, background, or combined model-and-background variants while keeping the garment unchanged.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and e-commerce teams use this skill to generate localized apparel catalog variants from existing worn-product photos without changing the garment. It supports replacing the model, background, or both, and provides prompt templates and command examples for image-editing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and referenced images may be sent to dLazy or another configured external provider.

Mitigation: Use only assets you are authorized to process, confirm the selected provider and credentials, and run dry-run checks before paid execution.

Risk: URL-based image inputs can expose private network resources or unauthorized third-party content.

Mitigation: Avoid localhost, private network, cloud metadata, internal dashboard, and unauthorized third-party URLs; prefer local files or trusted public URLs.

Risk: Generated model or background variants can be misused to imply endorsement or identity use that the skill does not support.

Mitigation: Do not use the skill for face-swapping to a specific real person or for fabricated product endorsements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/one-shot)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [Provider CLI Reference](references/provider-cli.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with prompt templates, CLI commands, and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or save generated image files when the user runs the referenced provider commands.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
