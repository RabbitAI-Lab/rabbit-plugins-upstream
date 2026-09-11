## Description:

同款穿搭换模特换场景做种草图。穿搭图 -> 社交平台风格的种草图。当用户说「种草图」「小红书风格」「换场景发帖」「达人图」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, merchants, and marketing operators use this skill to turn a source outfit image into lifestyle social-commerce images with changed model, pose, scene, lighting, and camera framing while preserving outfit details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload local or remote images and prompts to dLazy or another configured cloud provider.

Mitigation: Use only images you have rights to upload, prefer dry-run before paid execution, and configure only trusted providers.

Risk: Reference-image prompts may copy a person's identity, pose, and scene into new clothing images.

Mitigation: Avoid real-person likeness transfer unless rights and consent are clear, and do not use outputs to imply unauthorized endorsement or real product use.

Risk: Custom provider settings and remote image URLs can expand data exposure beyond the default workflow.

Mitigation: Do not set custom provider base URLs unless trusted, and avoid untrusted remote image URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [One-shot comparison skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/one-shot/skill.md)
- [Remove-watermark companion skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/remove-watermark/skill.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, image files]

**Output Format:** [Markdown guidance with inline bash commands and saved JPEG image outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses image inputs, prompt text, optional brand configuration, provider credentials, dry-run estimation, and batch generation.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
