## Description:

健康管理器 helps an agent provide Chinese-language personal health tracking, medication management, symptom review, and wellness guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill through an agent to record health metrics, manage medication details and reminders, review symptoms at an informational level, and receive wellness guidance in Chinese.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive health data may be stored or sent outside the user's intended context.

Mitigation: Require clear user consent before recording health data or using any external service, and keep collected data limited to the explicit health-management task.

Risk: Broad read, write, command, and API capabilities can exceed the needs of routine health tracking.

Mitigation: Limit the skill to explicit health-management tasks and avoid command execution unless it is strictly necessary and reviewed by the user.

Risk: Symptom and medication guidance may be mistaken for professional medical advice.

Mitigation: Present health guidance as informational support, preserve red-flag escalation language, and direct users to qualified care for urgent or uncertain situations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/personal-health-manager)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown or JSON-style structured responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include health metrics, medication schedules, symptom notes, reminders, and wellness recommendations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
