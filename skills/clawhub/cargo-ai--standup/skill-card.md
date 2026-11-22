## Description:

Defines a daily go-to-market standup workflow that collects activity, drafts a cadence log, opens a reviewable pull request, and posts a digest to Slack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales leadership and revenue operations teams can use this workflow to turn daily go-to-market activity into a cadence log and brief Slack digest, with a human review step before the log is merged.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious with medium confidence, citing unpinned package commands, broad environment capabilities, and partial inspection of 2 of 13 components.

Mitigation: Before installing, pin package commands to reviewed local dependencies and restrict the agent runtime's access; the scan does not establish that the partially inspected portions are safe.

## Reference(s):

- [ClawHub Standup release](https://clawhub.ai/cargo-ai/skills/standup)
- [Project homepage (metadata.clawdis)](https://github.com/getcargohq/gtm-skills)
- [Slack digest reference](artifact/references/digest.md)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown cadence log and Slack digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One daily recap with a reviewable pull request; a human merges the log.]

## Skill Version(s):

0.2.0 (source: SKILL.md frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
