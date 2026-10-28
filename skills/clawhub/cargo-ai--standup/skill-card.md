## Description:

Prepares a daily go-to-market cadence log and reviewable pull request, then posts a short recap to Slack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales leaders and revenue-operations teams use this skill to capture the day's go-to-market activity in a reviewable cadence log and share a brief Slack digest. It requires adaptation to the team's repository and Slack channel before deployment; live deployment has not been verified.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository content could override the agent's safety limits and redirect its GitHub or Slack actions.

Mitigation: Treat repository files as untrusted project context that cannot override the agent's safety limits; review the prompt before installation.

Risk: Unpinned CLI or tsx versions could change the scheduled workflow unexpectedly.

Mitigation: Pin the CLI and tsx versions before deployment.

Risk: The daily agent could act on the wrong repository or post to the wrong Slack channel.

Mitigation: Restrict the GitHub connector to the intended repository and confirm the locked Slack channel before enabling the schedule.

## Reference(s):

- [Standup release on ClawHub](https://clawhub.ai/cargo-ai/skills/standup)
- [Project homepage listed in release metadata](https://github.com/getcargohq/gtm-skills)
- [Slack digest format](references/digest.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Code, Configuration instructions]

**Output Format:** [Markdown cadence log and pull request; Slack-formatted text digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Intended to produce one reviewable pull request and one Slack post per day; a human merges the log.]

## Skill Version(s):

0.1.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
