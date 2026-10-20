## Description:

Converts a named Simplified-Chinese article into a Traditional-Chinese Markdown counterpart and keeps the pair linked and synchronized on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and developers maintaining Chinese-language articles use this skill to create or update a Traditional-Chinese version of an explicitly named Simplified-Chinese article and check that both versions remain in sync.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The conversion can change the source article's cross-link and replace an existing Traditional article.

Mitigation: Confirm the named source and destination paths before running; require explicit approval before replacing an existing Traditional article.

Risk: Automated conversion can choose incorrect Traditional forms, including within quotations.

Mitigation: Review flagged ambiguous forms and quotations against the cited edition, pin confirmed corrections, and run the synchronization check.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/j3ffyang/skills/simplified-to-traditional)

## Skill Output:

**Output Type(s):** [Markdown files, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Updates the Simplified article's cross-link and creates or refreshes its Traditional counterpart; check mode reports synchronization status.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
