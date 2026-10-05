## Description:

Turns a product CSV into a coordinated set of commercial product images, with batch progress tracking, retries, cost controls, and a contact sheet for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and developers use this skill to generate consistent product photography across a catalog of SKUs and review the resulting images before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Large batches can incur substantial provider charges without an enforced budget or confirmation gate.

Mitigation: Run a dry run, set a positive maximum-credit limit, and test a small sample with a row limit before processing the full catalog.

Risk: Product photos and prompts may be sent to third-party image providers.

Mitigation: Do not submit sensitive images or confidential prompts unless provider access and data handling meet your account and organizational policies.

Risk: Generated product details or visual style can vary across a batch.

Mitigation: Keep the shared visual specification fixed, sample-check outputs, and review product fidelity before publishing.

## Reference(s):

- [Batch Image ClawHub release](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider and authentication guide](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)
- [Marketplace image specifications](artifact/references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Images, Reports]

**Output Format:** [Markdown guidance and commands; generated image files, JSON batch manifest, and optional HTML contact sheet]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images are organized by SKU; batch progress and failures are recorded for review and resumption.]

## Skill Version(s):

1.0.17 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
