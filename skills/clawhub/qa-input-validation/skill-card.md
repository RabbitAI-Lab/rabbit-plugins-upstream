## Description:

Checks whether a QA testing request includes a clear requirement, enough context, and usable inputs before test design begins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and test-design agents use this skill as the first step in a testing workflow to score requirement clarity, identify missing context, and ask targeted clarification questions before generating test cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-supplied requirement files or URLs may contain sensitive customer, identity, payment, or production data.

Mitigation: Sanitize or mask sensitive data before using the skill, and avoid providing real production data unless it has been approved for testing.

Risk: Minimal test cases produced after missing information is identified may be incomplete.

Mitigation: Treat placeholder or fallback test coverage as high risk and wait for clarified requirements before relying on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-input-validation)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Markdown with structured JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs validation status, input quality score, missing information, clarification questions, and recommendations.]

## Skill Version(s):

1.6.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
