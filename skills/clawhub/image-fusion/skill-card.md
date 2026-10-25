## Description:

Combines up to eight product images into a complete outfit image on one model while preserving the individual items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion sellers, creative teams, and agents use this skill to combine several product photos into a single styled look image for product presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input images are sent to the selected cloud provider for generation.

Mitigation: Choose the provider explicitly, upload only images you have permission to share, and review that provider’s retention terms.

Risk: Documented credit costs differ, and the Replicate option is unsuitable for multi-image fusion.

Mitigation: Preview with --dry-run, confirm current charges with the selected provider, and avoid Replicate for this multi-image task.

## Reference(s):

- [Model flags](references/model-flags.md)
- [Provider and CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Image files]

**Output Format:** [Generated outfit image file (typically JPEG)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One composite outfit image using up to eight product images; aspect ratio and resolution are configurable.]

## Skill Version(s):

1.0.25 (source: server-resolved release evidence, changelog dated 2026-10-22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
