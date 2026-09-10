## Description:

Reference material, not a runnable skill: a one-page outline of a workflow for scanning GitHub forks and ClawHub skills using bash pre-filtering, sub-agent fan-out, and scheduled reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this reference material to design their own fork and skill scanning workflow, including candidate triage, parallel review, scoring, and scheduled reporting. It should be read as a workflow outline, not as a scanner that can be run directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake the package for a runnable scanner or assume it performs scheduled fork and skill reviews.

Mitigation: Treat the package as reference documentation only; build and review a separate implementation before relying on scanning, cron scheduling, sub-agent fan-out, GitHub access, or registry access.

Risk: An implementation based on the outline may require authenticated GitHub API access or other external service access.

Mitigation: Design credential handling separately, use least-privilege tokens, and review network and storage behavior before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/fork-and-skill-scanner-ultimate)
- [Publisher profile](https://clawhub.ai/user/globalcaos)
- [TinkerClaw repository referenced by the artifact](https://github.com/globalcaos/tinkerclaw)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown prose]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference-only content; no executable entry point, generated files, or scanner output is produced by this package.]

## Skill Version(s):

1.1.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
