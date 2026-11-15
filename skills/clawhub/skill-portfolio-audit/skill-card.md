## Description:

Audits a portfolio of agent skills to identify duplicates, stale assets, reusable workflows, sharing risks, and prioritized follow-up actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Skill maintainers and portfolio owners use it to inventory their skills, assess overlap and sharing suitability, and prioritize consolidation or follow-up work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs authenticated discovery across all accessible repositories, including private repositories outside the audit scope.

Mitigation: Review the repository-discovery instructions before installation and limit authenticated access to repositories in the audit scope where possible.

Risk: The security scan was partial because two referenced local paths were missing, so unexamined material is not covered by its results.

Mitigation: Treat the scan as incomplete and review the missing paths and remaining skill materials before relying on the scan results.

## Reference(s):

- [Skill Portfolio Audit on ClawHub](https://clawhub.ai/haiyangchenbj/skills/skill-portfolio-audit)
- [Publisher profile: haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Task lists]

**Output Format:** [Markdown audit report with a persistent dependency-linked execution queue]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The audit is read-only against existing skills; the execution queue is stored separately.]

## Skill Version(s):

1.1.8 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
