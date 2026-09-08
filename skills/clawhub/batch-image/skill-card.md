## Description:

多商品批量生图流水线。商品清单 CSV → 整批统一视觉的商拍图，带并发、重试、断点续跑、成本熔断与挑图联系表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn a CSV product manifest into a consistent batch of ecommerce product images. It guides prompting, provider selection, dry-run cost checks, concurrency, retries, output naming, and review reports for SKU-based image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and images may be sent to the selected cloud provider.

Mitigation: Use the skill only when that data sharing is acceptable for the product catalog and provider account in use.

Risk: Untrusted CSV manifests or remote image URLs can introduce unsafe inputs into the batch workflow.

Mitigation: Use trusted manifests, avoid untrusted remote image URLs, and review input paths before execution.

Risk: Output-path handling can write generated assets into unexpected locations.

Mitigation: Run in an isolated output directory and review save paths before starting a batch.

Risk: Runtime npx execution can fetch CLI code at execution time.

Mitigation: Prefer an already-installed or audited CLI version before running production batches.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/batch-image)
- [dLazy Ecommerce Skills](https://github.com/dlazy-ai/ecommerce-skills)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [Provider CLI Reference](references/provider-cli.md)
- [Platform Image Specifications](references/platform-specs.md)
- [seedream-5.0 Model Flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash and JavaScript command examples, plus generated image files, JSON status output, CSV manifests, and CSV reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are organized by SKU and may include dry-run cost estimates, saved image paths, asynchronous task IDs, and batch status summaries.]

## Skill Version(s):

1.0.7 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
