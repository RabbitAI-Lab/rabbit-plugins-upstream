## Description:

多商品批量生图 Batch Image helps agents turn a product CSV into visually consistent ecommerce product images with concurrency, retries, resume support, cost checks, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators, content teams, and developers use this skill to batch-generate listing images from SKU manifests while keeping visual specifications consistent across a product set. It also supports dry-run cost estimates, retry and resume workflows, output reports, and contact sheets for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product photos, filenames, and batch metadata may be sent to the selected cloud image provider and generation may incur costs.

Mitigation: Use dry-run and small SKU samples first, keep API keys scoped and revocable, and avoid uploading embargoed or confidential catalog assets without approval.

Risk: Large batch runs can produce inconsistent visuals or unexpected spend if the visual specification, provider, model, or batch settings change mid-run.

Mitigation: Freeze the visual specification before full runs, use concurrency limits, retries, resume state, cost caps, reports, contact sheets, and sample quality checks before publishing outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/batch-image)
- [Backend invocation reference](references/provider-cli.md)
- [seedream-5.0 model flags](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Files]

**Output Format:** [Markdown guidance with bash and Node.js command examples; executions can create image files, JSON manifests, CSV reports, and HTML contact sheets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses cloud image providers selected by configuration, supports dry-run cost estimates, retries, concurrency limits, resume state, and local output paths.]

## Skill Version(s):

1.0.12 (source: server release metadata, target metadata, and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
