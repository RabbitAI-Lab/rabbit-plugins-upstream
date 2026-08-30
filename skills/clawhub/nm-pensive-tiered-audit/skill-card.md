## Description:

Runs a three-tier codebase audit that starts with git-history analysis, escalates to targeted scans when evidence warrants it, and gates full-codebase review on explicit user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering reviewers use this skill to audit codebase quality, branch changes, instability, churn, and pre-PR risk. It guides agents through evidence-backed review tiers and records local findings before escalating scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Git-history analysis may inspect repository metadata, branch diffs, churn, blame, and commit messages.

Mitigation: Run the skill only in repositories where local audit of that development history is authorized.

Risk: The workflow may write local findings files under .coordination/agents.

Mitigation: Review generated findings before committing, publishing, or sharing them outside the repository context.

Risk: Full-codebase review can consume substantial compute and token budget.

Mitigation: Use the built-in Tier 3 gate and proceed only after explicit user approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-tiered-audit)
- [metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown reports with evidence-tagged findings and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local findings files under .coordination/agents when run by an agent; Tier 3 requires explicit user approval.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
