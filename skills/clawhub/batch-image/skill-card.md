## Description:

多商品批量生图流水线。商品清单 CSV → 整批统一视觉的商拍图，带并发、重试、断点续跑、成本熔断与挑图联系表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and e-commerce operators use this skill to generate visually consistent product images in batches from SKU manifests, organize results by SKU, and review batch progress.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented batch example may execute commands embedded in imported product lists.

Mitigation: Have the batch command fixed before processing imported lists, and use only approved product data.

Risk: The advertised spending limit does not cover all additional paid requests.

Mitigation: Set and enforce spending limits at the selected image-generation provider before running a batch.

Risk: Product images and descriptions may be sent to an unintended provider.

Mitigation: Select the intended provider explicitly and upload only approved images and descriptions.

Risk: A successful exit code may conceal an unreadable image or an incomplete result.

Mitigation: Inspect validation reports and generated images manually before using the results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/batch-image)
- [Model flags reference](references/model-flags.md)
- [Platform specifications](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)
- [Linked image quality-check skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/detect-task/skill.md)

## Skill Output:

**Output Type(s):** [Images, Files, Shell commands, CSV reports, Guidance]

**Output Format:** [Generated product-image files, CSV progress summaries, and shell-command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are organized by SKU; generated images and reports require review.]

## Skill Version(s):

1.0.25 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
