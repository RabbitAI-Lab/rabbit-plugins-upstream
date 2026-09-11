## Description:

多商品批量生图流水线：商品清单 CSV 生成整批统一视觉的商拍图，支持并发、重试、断点续跑、成本熔断与挑图联系表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and developers use this skill to turn a CSV product manifest into a consistent set of product photos and batch-run reports for online listing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted CSV manifests or provider-returned URLs could write files outside the expected output folder or create unsafe generated reports.

Mitigation: Use trusted manifests, run the skill in a dedicated output workspace, and require SKU validation, output path containment, URL download limits, and HTML escaping before using untrusted data.

Risk: Product images and prompts are sent to the selected generation provider.

Mitigation: Use only approved providers and avoid submitting confidential product data unless the provider and account controls are acceptable for the release.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/batch-image)
- [Model flags](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, image files, JSON reports]

**Output Format:** [Markdown guidance with shell command examples, JSON manifests, HTML contact sheets, and generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch workflow supports CSV manifests, concurrency, retries, resume state, dry-run cost estimates, and optional platform compliance checks.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
