## Description:

快樂刷牙俠，讓孩子愛上刷牙的歡樂計時器與打卡系統

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT

## Use Case:

External users and caregivers use this skill to guide 2-6 year old children through two-minute brushing sessions with positive encouragement, stories, music, reminders, local tracking, and virtual sticker rewards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores children's brushing routine data locally under ~/.bookshelf-plus/kids.

Mitigation: Enable it only when local routine tracking is acceptable, and delete the generated JSON files to reset or remove stored history.

Risk: Voice environments could speak reminders or run brushing flows without clear user intent.

Mitigation: Use explicit commands or confirmations before running timer, reminder, or TTS flows.

Risk: The reward and timer flow may shape a child's routine through encouragement and virtual stickers.

Mitigation: Keep caregiver oversight for rewards, reminders, and routine expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xuan905/skills/happy-brushing-hero)
- [Source repository](https://github.com/xuan905/happy-brushing-hero)
- [README](README.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Plain text and Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local JSON routine, sticker, reminder, and configuration records under ~/.bookshelf-plus/kids when scripts are run.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
