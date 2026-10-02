## Description:

Reviews AI-generated product images before publication, reporting eight visual and compliance checks with risk ratings and actionable prompt corrections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creative teams and merchants use this skill to screen AI-generated product images before listing or advertising, identify visual defects, and decide whether to publish, retouch, or regenerate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private product images, unreleased designs, or customer photos may be sent to third-party providers.

Mitigation: Review data-sharing requirements before installation and avoid sending sensitive or regulated images without authorization.

Risk: Bundled helpers can generate or edit images, beyond the skill's inspection-only description.

Mitigation: Review helper capabilities, choose the provider explicitly, and use a dry run where available before invoking them.

Risk: Image judgments may miss defects or misclassify compliance issues.

Mitigation: Review the itemized evidence and conduct a human final check before publication.

## Reference(s):

- [Example inspection report](https://github.com/dlazy-ai/ecommerce-skills/blob/main/docs/detect-task/example-report.md)
- [Platform image specifications](references/platform-specs.md)
- [Model flags](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown report or optional JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk level, eight itemized judgments with evidence, publication recommendation, and optional English prompt corrections.]

## Skill Version(s):

1.0.17 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
