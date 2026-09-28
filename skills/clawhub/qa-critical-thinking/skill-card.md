## Description:

Challenges assumptions in requirements and test cases to identify overlooked failure scenarios and reassess testing risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this skill to question hidden assumptions in requirements and existing test cases, identify missing edge cases, and prioritize follow-up testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requirements and test cases may contain customer, payment, identity, or production data.

Mitigation: Redact or mask sensitive details before providing them to the skill.

Risk: Broad question-like trigger phrases may activate the skill when a QA review was not intended.

Mitigation: Confirm the user wants a requirements or test-case review before applying its framework.

## Reference(s):

- [qa-critical-thinking on ClawHub](https://clawhub.ai/kokxi/skills/qa-critical-thinking)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown test-case table and lists of assumption challenges, thinking gaps, alternative scenarios, and risk reassessments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Test cases use a nine-column table; coverage claims are scoped to the supplied requirements.]

## Skill Version(s):

1.7.7 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
