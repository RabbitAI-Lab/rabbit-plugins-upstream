## Description:

Detects delivery packages in surveillance images or videos and returns structured package-detection results, counts, location details, reminders, and report links for station, entrance, and lobby monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and site operators use this skill to analyze package presence in camera images or videos for delivery-station inventory checks, residential entrance monitoring, office-lobby package counts, and unattended pickup reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance images, videos, or media URLs are sent to remote lifeemergence.com services for analysis.

Mitigation: Use the skill only with media approved for remote processing and avoid sensitive camera footage unless the publisher and remote service are trusted.

Risk: The skill silently resolves or creates an internal user identity and associates analysis and report history with that identity.

Mitigation: Run in an isolated workspace and review identity handling before use in shared or regulated environments.

Risk: Local token and identity persistence may reuse values from workspace data or the local skill database.

Mitigation: Remove unintended data/smyx-api-key.txt files and clear local skill data before installing or running under a different user context.

Risk: Historical report retrieval can expose previously associated analysis records and report links.

Mitigation: Limit access to workspaces where the skill is installed and review report-list output before sharing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-package-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Package detection API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON-like structured text with report links from remote API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can print historical report lists and can write analysis output to a user-selected file path when invoked with an output argument.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; SKILL.md frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
