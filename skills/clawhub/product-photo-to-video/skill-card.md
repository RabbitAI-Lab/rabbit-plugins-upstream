## Description:

Creates product videos and listing clips from one to three product photos, with guidance for preserving product details through generation and compositing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and ecommerce teams use the skill to turn product photos into short ads, listing videos, and product demonstrations while checking that generated footage preserves the real product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos or product information shared with the external service may be sensitive.

Mitigation: Use only materials you are comfortable sharing with Varg and protect the VARG_API_KEY.

Risk: Generated footage may change product details, and each generation can incur variable charges.

Mitigation: Review the quoted cost before approving generation and check labels, colours, parts, and the final composite for accuracy.

## Reference(s):

- [Prompt templates](artifact/references/prompts.md)
- [Common failures and fixes](artifact/references/failures.md)
- [Varg product video guide](https://varg.ai/how-to/turn-a-product-photo-into-a-video)
- [Fal commercial prompt patterns](https://github.com/fal-ai-community/skills/blob/main/skills/commercial/references/prompt-patterns.md)
- [Masonry product ad test](https://masonry.so/blog/best-ai-video-model-for-product-ads)
- [OpenAI image prompting cookbook](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Skill Output:

**Output Type(s):** [Video files, Guidance, Shell commands]

**Output Format:** [MP4 video and Markdown workflow guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Vertical 9:16 at 1080x1920, or 1:1 / 16:9 for product pages; generation cost and output quality vary by model and route.]

## Skill Version(s):

1.0.0 (source: server-resolved release; frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
