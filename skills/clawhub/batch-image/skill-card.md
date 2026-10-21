## Description:

Guides batch generation of visually consistent e-commerce product images from a SKU manifest, with retries, resumable runs, cost estimates, and review sheets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and developers use this skill to turn a product SKU list and reference images into a consistently styled catalog, track batch progress, and review results before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Catalog images, unreleased products, and prompts may be sent to paid external image services.

Mitigation: Review sensitive inputs and provider data-sharing terms before running; explicitly choose the provider.

Risk: Large batches can consume provider credits without an enforced spending cap or confirmation.

Mitigation: Start with --dry-run, use --limit for a small sample, and set a positive --max-credits for every paid batch; review the estimated cost.

Risk: A custom DLAZY_BIN value can change which executable handles image requests.

Mitigation: Do not set DLAZY_BIN unless it points to a trusted binary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider CLI reference](references/provider-cli.md)
- [Model options](references/model-flags.md)
- [Platform specifications](references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands; execution can produce product images and CSV/HTML review artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch settings include concurrency, retry, resume, dry-run, item limit, and optional spending threshold.]

## Skill Version(s):

1.0.24 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
