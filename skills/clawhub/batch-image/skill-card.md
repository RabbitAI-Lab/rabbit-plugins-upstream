## Description:

Turns a product CSV into a batch of visually consistent product images with retries, progress tracking, and a reviewable output manifest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and creative teams use this skill to generate coordinated product photography across a CSV list of SKUs and review results before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid cloud jobs may exceed the estimated budget or intended batch size; advertised safeguards are not guaranteed.

Mitigation: Review a dry run, set explicit --max-credits and --limit, start with a small batch, and monitor actual provider charges.

Risk: CSV image paths or URLs may send private local files or internal images to an external AI provider.

Mitigation: Inspect every image path and URL, select the provider deliberately, and use only assets approved for external processing.

Risk: The example brand profile contains placeholder visual and model settings that may be inappropriate for a real store.

Mitigation: Replace the sample brand profile with approved store-specific settings before generating a batch.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider configuration and data flow](artifact/references/provider-cli.md)
- [Model parameters](artifact/references/model-flags.md)
- [Platform image specifications](artifact/references/platform-specs.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Images, Files]

**Output Format:** [Markdown instructions, image files, JSON batch manifest, and optional HTML contact sheet]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [SKU-indexed images and a summary of completed, failed, and skipped jobs.]

## Skill Version(s):

1.0.21 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
