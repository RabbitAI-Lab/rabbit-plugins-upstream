## Description:

睡前故事精靈，用溫暖聲音為 2-6 歲孩童講床邊故事。20+ 故事模板、免 API、支援 TTS 朗讀、故事收藏、睡前引導。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT

## Use Case:

External parents and caregivers use this skill to ask an agent for Traditional Chinese bedtime stories for children ages 2-6, with optional TTS playback, story favorites/history, and bedtime-routine reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Favorites, story history, and routine settings are stored locally under ~/.qclaw/kids.

Mitigation: Review or delete the local files if household preferences or child-related story history should not be retained.

Risk: The bedtime reminder can be installed as a daily 20:00 crontab task.

Mitigation: Install the cron reminder only when recurring local reminders are desired, and review the user's crontab to remove it later if needed.

## Reference(s):

- [README.md](README.md)
- [SKILL.md](SKILL.md)
- [ClawHub skill page](https://clawhub.ai/xuan905/skills/bedtime-story-teller)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or terminal text with optional JSON story records and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local favorites, history, and routine settings under ~/.qclaw/kids; optional crontab setup is user-installed.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
