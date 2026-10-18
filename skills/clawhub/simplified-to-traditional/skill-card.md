## Description:

Converts an explicitly selected Simplified-Chinese article into a synchronized Traditional-Chinese Markdown counterpart with cross-links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and editors use this skill to create or refresh the Traditional-Chinese version of a specifically approved article while keeping the Simplified article as the source of truth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The sync can overwrite an existing Traditional-Chinese article.

Mitigation: Confirm the named source, output path, and overwrite approval before writing; keep changes under version control for review or reversal.

Risk: Automated conversion may choose an incorrect Traditional form or alter a quoted passage.

Mitigation: Review flagged ambiguous forms and quotations against the cited edition before accepting the generated article.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/j3ffyang/skills/simplified-to-traditional)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Linked Simplified- and Traditional-Chinese Markdown article files with a brief status report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Traditional text uses OpenCC s2twp; the paired files include reciprocal cross-links.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
