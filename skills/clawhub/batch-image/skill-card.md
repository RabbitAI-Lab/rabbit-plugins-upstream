## Description:

多商品批量生图流水线。商品清单 CSV → 整批统一视觉的商拍图，带并发、重试、断点续跑、成本熔断与挑图联系表。当用户说「批量生图」「一批商品」「跑整个 SKU 表」「几百个商品出图」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators and developers use this skill to generate a consistent set of product images from a SKU manifest, then organize results and review batch status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports a mismatch between the stated image-generation purpose and some supplied code, and notes incomplete scan coverage.

Mitigation: Review the supplied scripts and confirm the workflow matches the intended use before installation or execution; treat the automated assessment as partial.

Risk: Batch cost controls may be unreliable.

Mitigation: Run a dry estimate, check the total for the full SKU list, and confirm an effective spending limit before submitting generation jobs.

Risk: Prompts and source images are sent to the selected external generation provider.

Mitigation: Confirm which provider will receive the inputs and avoid sending sensitive prompts or images.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider CLI and data flow](references/provider-cli.md)
- [Seedream model flags](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)
- [dLazy](https://dlazy.com)
- [detect-task visual quality check](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/detect-task/skill.md)

## Skill Output:

**Output Type(s):** [Images, Files, CSV reports, Shell commands, Guidance]

**Output Format:** [Generated image files (typically JPEG) with CSV manifests or status reports and shell-command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch results are organized by SKU; generated images and reports depend on the selected provider and requested settings.]

## Skill Version(s):

1.0.35 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
