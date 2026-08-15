## Description:

Reviews AI-generated test cases across eight QA dimensions and downgrades to a six-dimension review when upstream scenario trees or risk lists are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, testers, and developers use this skill after AI generates test cases to score completeness, correctness, executability, risk coverage, formatting, consistency, traceability, and redundancy, then identify gaps and improvement suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad requests to check output rather than deliberate test-case review.

Mitigation: Use it when the user specifically wants AI-generated test cases reviewed, and confirm scope before applying the critique.

Risk: Merge, delete, or simplification recommendations could remove useful or critical test cases if applied blindly.

Mitigation: Treat cleanup recommendations as review suggestions requiring human confirmation and back up source test cases before bulk changes.

## Reference(s):

- [Review Dimensions](references/review-dimensions.md)
- [Report Templates](references/report-templates.md)
- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/qa-ai-output-critique)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown review report with scored tables, issue lists, coverage gaps, quality score, and improvement suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only review guidance; recommendations require human confirmation before acting on test cases.]

## Skill Version(s):

1.6.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
