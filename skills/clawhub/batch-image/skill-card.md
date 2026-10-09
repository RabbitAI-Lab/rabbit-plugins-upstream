## Description:

Creates visually consistent product photos from a SKU list using shared styling, with retries, resume support, spending limits, and a review contact sheet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and developers use this skill to turn a product CSV and reference photos into a consistent set of SKU-specific commercial images, then review results and rerun failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and brand or model reference files may be sent to the selected cloud image provider.

Mitigation: Confirm which provider account and key are active, and approve sharing the source materials before running the batch.

Risk: Large batches can consume credits unexpectedly.

Mitigation: Run a dry run, estimate the total cost, and set a credit limit before processing all SKUs.

Risk: Generated product details may not accurately match the source images.

Mitigation: Test a small sample and review generated images before listing them.

Risk: The bundled task list includes a remove-watermark helper available for manual use.

Mitigation: Review the shared task list before use and avoid that helper if it is not appropriate for your workflow.

## Reference(s):

- [ClawHub batch-image release](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider setup and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Shell commands, Image files, JSON reports, HTML contact sheet]

**Output Format:** [Markdown guidance with local image files, JSON batch manifest, and optional HTML contact sheet]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [SKU-based outputs; supports dry runs, retries, resume, and an estimated-credit limit.]

## Skill Version(s):

1.0.18 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
