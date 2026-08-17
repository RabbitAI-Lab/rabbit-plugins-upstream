## Description:

Review plugin quality with tiered checks and dependency scoping for PR and pre-release audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and plugin maintainers use this skill to scope affected and related plugins, run branch, PR, or release quality gates, and report pass, warning, or fail verdicts before merge or release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Release and PR tiers may execute repository Python scripts and make targets in the checkout under review.

Mitigation: Use the skill only in trusted checkouts and review the planned commands before allowing local execution.

Risk: Broad trigger words such as review, quality, validation, testing, and architecture can activate the workflow for generic review requests.

Mitigation: Use explicit plugin-review wording when requesting this workflow and avoid applying it to unrelated review tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-plugin-review)
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)
- [Branch tier checks](modules/tier-branch.md)
- [PR tier checks](modules/tier-pr.md)
- [Release tier checks](modules/tier-release.md)
- [Dependency detection](modules/dependency-detection.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with tables, verdicts, scorecards, shell command snippets, and YAML configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include quality-gate exit code guidance and tier-specific scorecards.]

## Skill Version(s):

1.9.18 (source: server release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
