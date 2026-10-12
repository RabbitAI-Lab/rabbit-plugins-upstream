## Description:

A Chinese-language assistant that helps turn personal workflows and materials into reusable agent skills, then checks them against recorded tests and coverage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fuetsui](https://clawhub.ai/user/fuetsui)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and developers use this skill to create or revise personal agent skills from their own workflows, examples, and requirements, then document what has and has not been validated.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated briefs and experiment records may reveal user materials or workflow details.

Mitigation: Review and redact generated files and reports before sharing.

Risk: A structural audit alone does not establish task success or automatic triggering.

Mitigation: Test real tasks and verify behavior in the target host before claiming validation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/fuetsui/skills/personal-skill-builder)
- [Interview guidance](references/interview.md)
- [Skill synthesis guidance](references/synthesis.md)
- [Evaluation method](references/evaluation.md)
- [Coverage design](references/coverage.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Skill files and Markdown guidance, with optional JSON audit and evaluation records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a requirements brief, test cases, and evidence-backed validation reports.]

## Skill Version(s):

1.0.0 (source: frontmatter, VERSION, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
