## Description:

思维梯度训练师 helps Chinese-speaking junior-high students locate their current math practice level across a five-level gradient, practice targeted progression problems, and record consent-based growth notes and reminder requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-speaking junior-high students and learning assistants use this skill to diagnose a student's current math practice layer, generate scaffolded progression exercises, summarize growth, and enqueue consent-based weekly review reminders.

### Deployment Geography for Use:

Mainland China by default; localize safety resources, curriculum assumptions, consent handling, and language before serving other regions.

## Known Risks and Mitigations:

Risk: Use outside Mainland China may present incorrect curriculum assumptions, language, consent expectations, or emergency/help resources.

Mitigation: Localize the safety resources, curriculum assumptions, consent handling, and language before serving users in other regions.

Risk: The skill can record learning-progress data and reminder requests for minors.

Mitigation: Use the documented consent controls and privacy actions; only write profile or reminder data when the relevant consent is present.

Risk: A student may disclose self-harm, abuse, severe distress, or another safety issue during tutoring.

Mitigation: Stop math coaching and follow the bundled crisis referral flow, including asking for location before giving local emergency resources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-gradient-trainer)
- [Initial math gradient levels reference](references/gradient-levels.md)
- [AI item generation self-check protocol](shared/ai-item-check.md)
- [Platform capability conventions](shared/platform-conventions.md)
- [Crisis exception protocol](shared/crisis-exception.md)
- [Handover protocol schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration instructions, Guidance]

**Output Format:** [Chinese-language coaching dialogue, Markdown summaries, and JSON handoff payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate consent-gated subject profile writebacks and reminder enqueue payloads; no shell commands.]

## Skill Version(s):

2.3.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
