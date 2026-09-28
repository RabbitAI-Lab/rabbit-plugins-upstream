## Description:

Reviews AI-generated test cases for coverage, correctness, executability, risk, consistency, traceability, formatting, and redundancy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this skill to critique AI-generated test cases, identify coverage gaps and unclear steps, and prioritize revisions before using the cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may prompt a review outside the intended test-case context.

Mitigation: Invoke it explicitly for AI-generated test cases and confirm that the cases and requirements are in scope.

Risk: Merge or deletion suggestions could remove valuable test coverage if followed automatically.

Mitigation: Treat these suggestions as review proposals; back up existing cases and confirm coverage before making changes.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/kokxi/skills/qa-ai-output-critique)
- [Review dimensions and scoring](references/review-dimensions.md)
- [Review report templates](references/report-templates.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown review report with scores, issue list, and improvement suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Eight-dimension review with scenario and risk inputs; a reduced review is available without them.]

## Skill Version(s):

1.7.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
