## Description:

Reviews plugin quality with tiered checks and dependency-aware scoping for PR and pre-release audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review plugin changes with branch, PR, and release-level quality gates, including dependency scoping, test/lint/type checks, scorecards, and remediation summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic activation triggers may bring the skill into unrelated review, quality, validation, testing, or architecture discussions.

Mitigation: Use it deliberately for plugin review workflows and confirm the intended tier and repository scope before acting on its recommendations.

Risk: The workflow proposes local git, make, and repository-specific script commands for branch, PR, and release checks.

Mitigation: Review commands before running them, confirm required scripts and dependency maps exist, and prefer dry-run or scoped execution where available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-plugin-review)
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown review reports with command snippets and optional YAML configuration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tiered branch, PR, and release review modes with quality-gate exit code guidance.]

## Skill Version(s):

1.9.19 (source: ClawHub release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
