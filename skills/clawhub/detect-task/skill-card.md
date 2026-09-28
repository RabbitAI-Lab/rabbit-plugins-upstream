## Description:

Reviews AI-generated e-commerce product images for visual defects and potential listing issues, then suggests corrections before publication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams review candidate AI-generated product images before listing, using an eight-point risk report and suggested prompt fixes to decide whether to publish, edit, or regenerate them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Candidate product images are sent to cloud model providers for review.

Mitigation: Submit images only when cloud processing is acceptable for the content.

Risk: The bundled multi-provider wrapper may route inspection images to generation or editing services rather than an analysis model.

Mitigation: Prefer the direct dLazy claude-sonnet-5 inspection command; constrain any alternative provider to image analysis.

Risk: Image inspection can miss defects or incorrectly approve content for a platform.

Mitigation: Treat the report as advisory and require human review and current platform-rule checks before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/detect-task)
- [Example inspection report](https://github.com/dlazy-ai/ecommerce-skills/blob/main/docs/detect-task/example-report.md)
- [Model flags](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [Platform image specifications](references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown report with an eight-item assessment and prompt corrections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk level, listing recommendation, and up to three English correction sentences; optional JSON output.]

## Skill Version(s):

1.0.15 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
