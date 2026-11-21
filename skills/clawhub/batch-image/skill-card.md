## Description:

多商品批量生图流水线。商品清单 CSV → 整批统一视觉的商拍图，带并发、重试、断点续跑、成本熔断与挑图联系表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and developers use this skill to turn a product SKU manifest and reference images into a consistent batch of product photography, with per-SKU outputs and a status report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch image prompts and reference images may be sent to an external generation provider, and generation incurs usage charges.

Mitigation: Confirm the provider and its image handling, review the estimated total cost with a dry run, and start with a small sample before submitting the full batch.

Risk: Retries can lead to additional generation attempts and charges; the security review was partial, with degraded analyzers.

Mitigation: Set a batch budget and retry limit, monitor task status and charges, and review the skill behavior before use because the scan does not establish that it is safe.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider CLI reference](references/provider-cli.md)
- [Seedream model flags](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with CSV manifest examples, prompts, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Execution can generate per-SKU product images and a batch status report.]

## Skill Version(s):

1.0.34 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
