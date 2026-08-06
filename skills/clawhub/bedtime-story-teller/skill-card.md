## Description:

Bedtime Story Teller helps an agent generate warm Traditional Chinese bedtime stories for children ages 2-6, with optional read-aloud, saved favorites, playback history, and bedtime routine reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT

## Use Case:

Parents and caregivers can use this skill through an agent to request age-appropriate bedtime stories, choose themes and story length, replay or save favorites, and support a bedtime routine. The skill is also useful for agents that need local, no-API story generation and gentle text or optional TTS output in Traditional Chinese.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional daily cron reminder can add a recurring local reminder that may be unwanted later.

Mitigation: Decide before installation whether to enable the cron reminder, review the resulting crontab after setup, and keep removal steps available.

Risk: Broad trigger phrases about stories or bedtime could activate the skill during ordinary family conversation.

Mitigation: Use narrower trigger phrases when accidental activation would be disruptive.

Risk: The skill stores favorites, history, settings, and bedtime routine data locally.

Mitigation: Review local files under the configured child-story storage directory if retention or deletion matters for the household.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xuan905/skills/bedtime-story-teller)
- [Server-Resolved GitHub Source](https://github.com/xuan905/bedtime-story-teller)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Traditional Chinese story text, terminal text output, JSON-backed local library records, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces child-oriented story content from local templates; optional TTS is used when an agent provides a compatible tool, otherwise the skill falls back to text output.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
