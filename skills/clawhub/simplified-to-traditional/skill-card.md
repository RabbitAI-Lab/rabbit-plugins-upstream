## Description:

Converts a named Simplified-Chinese article into a synchronized Traditional-Chinese version with reciprocal cross-links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and developers maintaining Chinese articles use this skill to create or update a Traditional-Chinese counterpart of a specifically named Simplified-Chinese Markdown article and check that both versions remain synchronized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the conversion can replace an existing Traditional-Chinese article.

Mitigation: Confirm the exact source and destination paths and obtain permission before overwriting an existing file.

Risk: Automatic conversion can choose incorrect characters for ambiguous terms or alter quotations.

Mitigation: Review flagged forms and compare quotations with the cited edition; preserve approved corrections in conversion overrides and verify synchronization.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/j3ffyang/skills/simplified-to-traditional)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Linked Simplified- and Traditional-Chinese Markdown articles with plain-text verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Converts a named article on demand; the Simplified article remains the source of truth.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
