## Description:

多商品批量生图流水线。商品清单 CSV -> 整批统一视觉的商拍图，带并发、重试、断点续跑、成本熔断与挑图联系表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, creative teams, and developers use this skill to turn a product manifest into a visually consistent batch of product photography prompts, commands, outputs, and review artifacts. It is intended for SKU-scale image generation workflows that need sampling, retries, cost controls, and post-generation quality checks before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product and reference images may be sent to a selected generation provider.

Mitigation: Confirm that the images are approved for the chosen provider and account before running generation commands.

Risk: Provider credentials may grant access to paid image-generation services.

Mitigation: Configure API keys deliberately, use provider-specific environment variables or CLI login, and rotate or revoke keys when access changes.

Risk: Large batches can incur unexpected cost or rate-limit failures.

Mitigation: Use dry-run mode, sample a small SKU set first, cap concurrency, and apply the documented maximum-credit controls before full-batch execution.

Risk: Generated product images may be inaccurate or fail marketplace listing requirements.

Mitigation: Run sample quality checks, use the listing checker where applicable, review contact sheets, and rerun or manually fix rejected SKUs before publishing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider CLI Reference](artifact/references/provider-cli.md)
- [Model Flags Reference](artifact/references/model-flags.md)
- [Platform Image Specifications](artifact/references/platform-specs.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [detect-task Reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/detect-task/skill.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell commands, CSV inputs, JSON manifests, and locally saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch scripts can save generated image files, status manifests, reports, and contact sheets when executed by the user.]

## Skill Version(s):

1.0.4 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
