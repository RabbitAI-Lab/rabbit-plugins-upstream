## Description:

Science-based running coach via Telegram that logs training, syncs Garmin data, sends visual training-plan images, and coaches with evidence-driven discipline without asking for data it already has.

This skill is ready for commercial/non-commercial use.

## Publisher:

[enawareness](https://clawhub.ai/user/enawareness)

### License/Terms of Use:

MIT-0

## Use Case:

External runners and agent users use this skill to maintain a Telegram running coach that logs training, consults optional Garmin sync data, maintains runner memory, and generates weekly training plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Telegram credentials, optional Garmin credentials, Garmin cached session tokens, runner memory, and synced fitness data are sensitive local data.

Mitigation: Store credentials only in chmod-600 dotfiles, protect the configured data directory, and delete .credentials, garmin/.credentials, garmin/.garth, MEMORY.md, summary.json, and activity JSON files when no longer needed.

Risk: The skill can send running plans and coaching content to Telegram and can sync Garmin fitness data when those integrations are enabled.

Mitigation: Enable only the integrations you intend to use, review generated plans before sending when accuracy matters, and keep account tokens and local data private.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/enawareness/skills/run-coach)
- [Publisher profile](https://clawhub.ai/user/enawareness)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown coaching replies, shell commands, JSON summaries, local files, and Telegram messages or photo albums when configured]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local runner memory, Garmin JSON snapshots, activity JSON files, and PNG training-plan images.]

## Skill Version(s):

1.1.2 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
