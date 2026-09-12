## Description:

多单品融合成一整套 Look。最多 8 张单品图 → 同一模特身上的完整搭配商拍图，每件单品保真。当用户说「多件搭配」「融图」「组一套 look」「搭配图」「几件衣服合成一张」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, creative operators, and agents use this skill to turn up to eight product images into a prompt and generation workflow for a unified modeled outfit image while preserving item appearance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper scripts can fetch arbitrary image URLs and may reach localhost, cloud metadata, or private network services.

Mitigation: Use local image files or trusted HTTPS image URLs, and avoid running the skill where localhost, cloud metadata, or private network services are reachable.

Risk: Prompts and uploaded images are sent to the selected cloud provider, and Ark credentials can be sent to an environment-selected endpoint.

Mitigation: Run only with trusted providers and endpoints, do not set ARK_BASE_URL unless the endpoint is fully trusted, and avoid sensitive prompts or images unless their disclosure is acceptable.

Risk: Security evidence marks the release suspicious pending review.

Mitigation: Review the skill before installing or running it in sensitive environments.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [Seedream 5.0 Model Flags](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with prompt templates and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides image generation workflows that may save generated image files through dLazy or another configured provider.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
