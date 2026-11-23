## Description:

静态主图转主图视频。一张商品图 → 3–5 秒可上架的主图短视频。当用户说「主图视频」「图转视频」「让图动起来」「加个视频」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers and their agents use this skill to turn a product's static listing image into a short product video, with controlled camera motion and material effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, or reference material may be sent to an external generation service.

Mitigation: Before running generation, confirm the selected provider and its data handling terms, and submit only images and prompts that are approved for that service.

Risk: The security inspection was incomplete, so some component behavior was not fully reviewed.

Mitigation: Review the skill and its dependencies before use, especially before sending sensitive content or running generation at scale.

## Reference(s):

- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)
- [Product video ad skill for longer videos](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/product-video-ad/skill.md)
- [Platform compliance skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)

## Skill Output:

**Output Type(s):** [Video files, Shell commands, Configuration instructions, Prompt guidance]

**Output Format:** [Short video files with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically one 3–5 second clip from a single product image; platform specifications require manual review.]

## Skill Version(s):

1.0.31 (source: SKILL.md frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
