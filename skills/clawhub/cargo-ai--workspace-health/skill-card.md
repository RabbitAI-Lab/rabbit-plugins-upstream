## Description:

Monitors a Cargo workspace for new failures, stopped plays, silent writes, spend spikes, and stuck batches, then posts findings to Slack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace owners and go-to-market engineering teams use the skill to spot operational problems in a Cargo workspace each morning and receive new findings in Slack. On Mondays it summarizes findings that remain open or have cleared.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious because it reports an unpinned command that can download and run a package; the scan is incomplete.

Mitigation: Review the package download and execution path before installing, and account for the partially inspected component during review.

Risk: ClawScan flags undeclared repository integration, and the GitHub integration's repository access is not established by the scan.

Mitigation: Understand the GitHub integration's repository access before installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/workspace-health)
- [Project homepage](https://github.com/getcargohq/gtm-skills)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Concise Slack findings and a weekly summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Posts only new findings; reports issues without changing the workspace.]

## Skill Version(s):

0.2.0 (source: skill frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
