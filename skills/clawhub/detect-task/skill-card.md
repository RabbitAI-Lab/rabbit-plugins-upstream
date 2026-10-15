## Description:

Reviews AI-generated e-commerce images before publication and provides an eight-point risk assessment, placement advice, and prompt corrections for reruns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce content teams and developers use this skill to review AI-generated product images before listing or advertising, identify visual defects, and decide whether to publish, retouch, or regenerate them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image review may send sensitive or proprietary images to a selected cloud provider.

Mitigation: Select the provider explicitly and avoid submitting images unless that provider is approved to receive them.

Risk: Bundled generation, automatic rerun, and --fix or --save options can create or change image files beyond a judgment-only review.

Mitigation: Use the inspection path for review; run regeneration or file-writing options only when intended, and check output paths first.

Risk: Automated inspection can miss defects or incorrectly flag acceptable images.

Mitigation: Review the report evidence and perform a human final check before publication.

## Reference(s):

- [Example inspection report](https://github.com/dlazy-ai/ecommerce-skills/blob/main/docs/detect-task/example-report.md)
- [Platform image specifications](references/platform-specs.md)
- [Provider and CLI reference](references/provider-cli.md)
- [Model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown inspection report; optional JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk level, evidence for eight checks, placement recommendation, and English prompt corrections when changes are needed.]

## Skill Version(s):

1.0.22 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
