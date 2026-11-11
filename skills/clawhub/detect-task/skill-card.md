## Description:

Reviews AI-generated product images before listing or advertising, reports risk levels and eight visual checks, and suggests prompt corrections for another pass.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams use the skill to review AI-generated product photos before advertising or listing them. It produces a risk assessment, checks eight visual issues, and gives prompt-ready suggestions for images that need another generation pass.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a mismatch between the stated image-review purpose and some behavior, and the analysis is incomplete.

Mitigation: Review the skill before use and begin with non-sensitive images until its behavior is understood.

Risk: The security evidence reports that images are uploaded to hosted AI services.

Mitigation: Only submit images approved for external processing; remove confidential or personal information when possible.

Risk: The security evidence notes possible overwriting of batch outputs.

Mitigation: Check the output paths before running batch examples and use a separate destination for each run.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/detect-task)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured text or Markdown report with risk level, eight visual checks, a recommendation, and prompt correction suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can review up to 10 images per call; the report is a decision aid and does not replace human review.]

## Skill Version(s):

1.0.32 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
