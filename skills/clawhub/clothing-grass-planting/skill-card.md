## Description:

同款穿搭换模特换场景做种草图。穿搭图 → 社交平台风格的种草图。当用户说「种草图」「小红书风格」「换场景发帖」「达人图」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, merchants, and marketing teams use this skill to turn outfit photos into social-commerce lifestyle images while preserving garments and changing the model, pose, scene, lighting, and camera style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images could be used to imitate a real person's identity in promotional fashion imagery.

Mitigation: Use only consented, licensed, or synthetic model references and reject requests to imply real-person endorsement or fabricated product experience.

Risk: Prompts and uploaded images may be processed by the selected external generation provider.

Mitigation: Avoid private, confidential, or sensitive inputs and review the selected provider's data handling before use.

Risk: Image URLs supplied to helper commands can expose private-network or sensitive resources.

Mitigation: Use local files or trusted public image URLs, and do not provide private-network or sensitive URLs as references.

Risk: A custom ARK_BASE_URL can route generation requests to an untrusted endpoint.

Mitigation: Use a custom ARK_BASE_URL only when the endpoint is fully controlled and approved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Parameter List](references/model-flags.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands, configuration examples, and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Common outputs are JPEG social-commerce images, dry-run request previews, and optional JSON command envelopes.]

## Skill Version(s):

1.0.9 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
