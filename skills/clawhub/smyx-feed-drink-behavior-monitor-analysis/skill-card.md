## Description:

Analyzes fixed-camera feeder and waterer videos to quantify livestock feeding duration, feeding bouts, drinking frequency, and behavior anomaly alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agricultural operations use this skill to analyze livestock feeder or waterer images and videos, compare behavior against baselines, and review historical monitoring reports. It supports feeding and drinking behavior statistics and anomaly alerts, but not disease diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends feeder or waterer images and videos to the publisher's remote service for analysis.

Mitigation: Use only footage that is acceptable for external processing, and confirm the publisher's retention and handling practices before using sensitive facility media.

Risk: The skill can automatically create or reuse an identity and cache tokens in a local workspace SQLite database.

Mitigation: Run the skill in an isolated workspace, avoid shared machines for sensitive use, and clear the workspace data store when the identity should not persist.

Risk: History-list mode retrieves cloud report history for the current resolved identity.

Mitigation: Verify the workspace and identity context before listing reports, and avoid mixing unrelated operators or facilities in the same workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-feed-drink-behavior-monitor-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local media paths or media URLs; history-list mode returns structured report records.]

## Skill Version(s):

1.0.7 (source: server release evidence; artifact frontmatter is 1.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
