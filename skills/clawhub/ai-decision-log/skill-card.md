## Description:

AI Decision Log records AI-assisted decisions, model names, evidence hashes, human reviewers, and timestamps to JSONL, and reports model usage and unreviewed decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, governance teams, and agent operators use this skill to create local audit records for AI-assisted decisions and to identify decisions that lack human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented one-command global install uses an unpinned remote package command.

Mitigation: Review the installer and prefer a pinned or manually verified source checkout before global installation.

Risk: Decision logs can include sensitive decision content, evidence descriptions, or regulated data.

Mitigation: Keep secrets and regulated data out of log entries, control the log path, and apply an appropriate retention process.

Risk: The logger records review status but does not replace professional or compliance review.

Mitigation: Require human review for critical, regulated, legal, medical, or high-impact decisions before relying on the logged outcome.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-decision-log)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Files, JSON, Text, Shell commands, Guidance]

**Output Format:** [JSONL decision-log records, JSON reports, and terminal text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local file output; zero third-party runtime dependencies; documented exit codes 0, 1, and 2.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and changelog report 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
