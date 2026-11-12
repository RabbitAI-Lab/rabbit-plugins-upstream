## Description:

使用已有模特图或人台图替换模特、背景或两者，同时保持商品本身不变。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce teams can use an existing model or mannequin product photo to create versions with a different model, background, or both for varied audiences and settings, while keeping the product as the focal point.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports external image-service data transfers, so source images may be sent to a selected provider.

Mitigation: Before running, review the permissions and provider route, confirm you are comfortable uploading the source images, and use only images approved for that transfer.

Risk: The security review marks the release suspicious and reports partial inspection with degraded checks; unreviewed behavior is not established as safe.

Mitigation: Review the permissions and remaining files before installation, and postpone use until you can confirm which external providers receive images and accept that transfer.

## Reference(s):

- [Model flags reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/one-shot)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Generated image files and Markdown guidance with inline shell commands and prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image variations use a source photo and may use optional reference images; generation is performed by an image provider.]

## Skill Version(s):

1.0.30 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
