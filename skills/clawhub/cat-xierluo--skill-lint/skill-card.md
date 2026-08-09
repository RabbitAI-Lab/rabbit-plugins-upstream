## Description:

Skill Lint helps agents review agent skills for creation readiness, reliability evidence, format quality, instruction stability, harness contracts, candidate-bound verification, directory structure, business-flow depth, and disclosed security risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT

## Use Case:

Developers, skill maintainers, and reviewers use this skill before creating, substantially changing, publishing, or assessing agent skills. It produces quality and safety-oriented review guidance covering structure, metadata, trigger boundaries, workflow outputs, harness evidence, instruction stability, and disclosed security risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dynamic verification can execute candidate checkers or review workflows.

Mitigation: Use dynamic verification only on owned or reviewed candidate skills, or run third-party candidates in a disposable isolated environment.

Risk: Online dependency vulnerability checks can disclose private dependency lists to OSV.

Mitigation: Avoid the online mode for private dependency lists unless that disclosure is acceptable.

Risk: Evaluator signing keys can lose independence if stored in candidate workspaces or normal agent runs.

Mitigation: Keep evaluator private keys outside candidate workspaces and away from normal agent execution paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cat-xierluo/skills/skill-lint)
- [ClawHub publisher profile](https://clawhub.ai/user/cat-xierluo)
- [ClawHub homepage metadata](https://github.com/cat-xierluo/legal-skills)
- [Skill Standards](references/skill-standards.md)
- [Security Assessment Standards](references/security-assessment-standards.md)
- [Harness Reliability Standards](references/harness-reliability-standards.md)
- [Instruction Stability Standards](references/instruction-stability-standards.md)
- [Skill Quality Opinion Report Template](templates/skill-quality-opinion-report.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown review reports with JSON evidence, shell command snippets, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce formal review reports, evidence receipts, and archive guidance when the user requests validation; dynamic verification is reserved for user-confirmed trusted candidates or isolated environments.]

## Skill Version(s):

2.8.0 (source: frontmatter, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
