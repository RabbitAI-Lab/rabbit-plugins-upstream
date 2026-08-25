## Description:

Science-based running coach via Telegram that logs training, sends visual training plans as HD photo albums, coaches with evidence-driven discipline, and optionally syncs Garmin health metrics while storing credentials and session tokens locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[enawareness](https://clawhub.ai/user/enawareness)

### License/Terms of Use:

MIT-0

## Use Case:

External runners and coaching agents use this skill to maintain a runner profile, log training, generate Telegram-delivered training plans, and optionally incorporate locally synced Garmin activity and health metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Telegram bot credentials and optional Garmin credentials, health metrics, and session tokens are stored locally.

Mitigation: Install only if local storage of these files is acceptable; use chmod 600 for credential files and chmod 700 for the Garmin directory.

Risk: Optional Garmin sync collects health and training data that persists locally until deleted.

Mitigation: Do not enable Garmin sync unless needed; delete garmin/activities, garmin/summary.json, and garmin/.garth to remove stored Garmin data and tokens.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/enawareness/skills/run-coach)
- [Publisher profile](https://clawhub.ai/user/enawareness)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and locally rendered Telegram image artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May send generated PNG training plans to the configured Telegram chat; optional Garmin sync writes local JSON summaries and activity snapshots.]

## Skill Version(s):

1.1.6 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
