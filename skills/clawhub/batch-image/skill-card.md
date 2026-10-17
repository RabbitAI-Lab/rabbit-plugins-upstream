## Description:

Generates visually consistent product images from a SKU list with retries, resumable batches, cost limits, and an optional contact sheet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and developers use this skill to create a consistent set of product photos from a SKU manifest, monitor batch results, and select images for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local or URL-sourced product images may be uploaded to a cloud image provider.

Mitigation: Review the chosen provider's data policy, restrict manifests to trusted hosts and approved local folders, and exclude confidential images unless approved.

Risk: Bulk image generation can incur unexpected provider charges.

Mitigation: Run a dry-run, check the estimated cost and batch size, and apply a cost limit before starting paid jobs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Model flags](artifact/references/model-flags.md)
- [Platform image specifications](artifact/references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Images, CSV reports, HTML contact sheet, Shell commands, Markdown guidance]

**Output Format:** [Image files, CSV status report, optional HTML contact sheet, and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images are saved by SKU; dry-run supports cost review before processing.]

## Skill Version(s):

1.0.22 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
