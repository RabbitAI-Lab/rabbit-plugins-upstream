## Description:

同款穿搭换模特换场景做种草图。穿搭图 -> 社交平台风格的种草图。当用户说「种草图」「小红书风格」「换场景发帖」「达人图」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and marketing teams use this skill to turn outfit images into social-commerce lifestyle images while preserving garment details and changing model, pose, scene, lighting, and camera style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can upload unrestricted local files or fetched URLs to cloud image-generation providers.

Mitigation: Use only trusted local image files, avoid arbitrary URLs, and run the skill from a workspace that does not expose sensitive files.

Risk: A custom Ark endpoint can receive the Ark API key if ARK_BASE_URL is set.

Mitigation: Leave ARK_BASE_URL unset unless the endpoint is fully trusted and scoped for this workflow.

Risk: Broad API keys in the environment can be used by configured providers.

Mitigation: Use provider credentials with the minimum required scope and avoid installing the skill in environments with unrelated sensitive keys.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Model Flags](references/model-flags.md)
- [Provider CLI Reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash command examples and image-generation parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to call image-generation providers and save generated image files.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
