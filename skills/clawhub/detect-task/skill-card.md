## Description:

Reviews AI-generated e-commerce images for visual defects and platform concerns, then suggests a release decision and corrective prompt wording.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creative teams and merchants use this skill to assess AI-generated product imagery before publication. It reports eight checks, recommends release, retouching or regeneration, and provides prompt corrections for another pass.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts can be sent to cloud providers.

Mitigation: Avoid sensitive or private images; confirm the intended provider and use dry-run or doctor before submitting.

Risk: Bundled multi-provider tooling can generate or edit images and write local outputs, beyond the stated image-review purpose.

Mitigation: Prefer the documented dlazy claude-sonnet-5 inspection path; enable alternative providers or rerun loops only when image changes and local writes are intended.

Risk: Model judgments may miss defects or incorrectly flag acceptable images.

Mitigation: Review the itemized evidence and conduct human approval before publishing or acting on automated rerun recommendations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/detect-task)
- [Example inspection report](https://github.com/dlazy-ai/ecommerce-skills/blob/main/docs/detect-task/example-report.md)
- [Provider CLI guidance](artifact/references/provider-cli.md)
- [Model parameters](artifact/references/model-flags.md)
- [Platform image checks](artifact/references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Markdown report; optional JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk level, eight itemized findings, publication recommendation, and one to three English prompt corrections when needed.]

## Skill Version(s):

1.0.19 (source: SKILL.md frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
