## Description:

多商品批量生图流水线。商品清单 CSV → 整批统一视觉的商拍图，带并发、重试、断点续跑、成本熔断与挑图联系表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

面向电商运营者与开发者，按商品清单批量生成视觉统一的商品摄影图，并整理每个 SKU 的输出与运行状态。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch image generation can incur unexpected provider charges.

Mitigation: Estimate the run cost before scaling up, use a dry run where available, and start with one SKU.

Risk: Product images and descriptions may be sent to external generation providers.

Mitigation: Check the selected provider's data handling and avoid submitting sensitive source material.

Risk: The security analysis is partial, and command and tool scope need review.

Mitigation: Inspect the commands before running, test a small sample, and review generated images before a full batch.

## Reference(s):

- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Image-generation requests]

**Output Format:** [Markdown guidance with CSV examples and shell or Node.js command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Organizes generated product images by SKU and can produce run status summaries.]

## Skill Version(s):

1.0.31 (source: SKILL.md frontmatter; release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
