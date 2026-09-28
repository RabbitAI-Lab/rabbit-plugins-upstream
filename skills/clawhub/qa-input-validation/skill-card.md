## Description:

Checks whether a QA request includes clear, testable requirements and enough context before test design begins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA practitioners and developers use this skill to assess requirement clarity, context, and input accessibility before designing tests, and to request missing details when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests or documents may contain customer, payment, identity, or production information.

Mitigation: Mask sensitive information before providing text, files, screenshots, or URLs to the skill.

Risk: When requirements remain incomplete, the workflow may still generate minimal test cases with gaps.

Mitigation: Resolve clarification questions before relying on test cases; label untested areas and review assumptions.

## Reference(s):

- [QA Input Validation on ClawHub](https://clawhub.ai/kokxi/skills/qa-input-validation)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured validation result with optional Markdown test-case table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes pass, need_more_info, or fail status; quality score; missing information; clarification questions; and a recommendation. May produce minimal test cases if the user declines to supply details.]

## Skill Version(s):

1.7.7 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
