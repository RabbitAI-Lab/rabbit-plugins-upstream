## Description:

多商品批量生图流水线。商品清单 CSV -> 整批统一视觉的商拍图，带并发、重试、断点续跑、成本熔断与挑图联系表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn a CSV product manifest into a batch image-generation workflow with consistent product-shot styling, retries, resume behavior, cost checks, and summary reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and reference images may be uploaded to the selected image provider.

Mitigation: Use approved providers and inputs, and avoid submitting sensitive or unauthorized product imagery.

Risk: Batch image generation may consume provider credits at scale.

Mitigation: Use dry-run, small SKU samples, and cost limits before running a full manifest.

Risk: Example brand demographics or visual defaults may not fit the intended catalog or audience.

Mitigation: Review and adapt brand.yaml and prompt specifications before reuse.

Risk: Generated product images may contain fidelity or listing-compliance issues.

Mitigation: Run sample quality checks and review output reports before publishing generated assets.

Risk: Unrelated image-editing tasks such as watermark removal may require clear rights and lawful justification.

Mitigation: Do not use those workflows unless the operator has verified the rights and purpose.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [seedream-5.0 Model Flags](references/model-flags.md)
- [Platform Image Specifications](references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with shell commands, CSV/configuration examples, and code-backed workflow commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When executed, the workflow may produce image files, JSON manifests, CSV reports, and contact sheets.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
