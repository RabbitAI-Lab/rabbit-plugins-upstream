## Description:

帮助学生记录学习时间、启动番茄钟、分析黄金时段和分心规律，并在明确同意后维护专注力档案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

Students in Chinese-language K-12 learning contexts use this skill to understand how study time is spent, run focus sessions, review distraction patterns, and decide when to study. Guardians, teachers, or platform operators can use its consent and handoff rules to keep focus records, reminders, and cross-skill sharing bounded.

### Deployment Geography for Use:

China mainland by default; use elsewhere requires localizing emergency contacts, curriculum assumptions, and minor-consent rules before student-facing deployment.

## Known Risks and Mitigations:

Risk: Minor students may create sensitive focus records or cross-skill handoffs without fully understanding data retention.

Mitigation: Keep long-term memory, reminders, and cross-skill sharing off until the student, and a guardian where required, intentionally consents; provide view, correct, export, pause, and delete controls.

Risk: Crisis or safety disclosures can appear during focus coaching or distraction review.

Mitigation: Stop the focus workflow, avoid diagnosis and detailed recording, direct the student to a trusted adult, and provide emergency channels only after confirming the relevant region.

Risk: Focus patterns can be overstated when there is too little data.

Mitigation: Mark low-sample observations as insufficient, avoid formal golden-time reports when fewer than five days of data are available, and keep unsupported conclusions out of long-term records.

Risk: Deploying the skill outside its intended Chinese K-12 context can produce mismatched safety contacts, curriculum assumptions, or consent handling.

Mitigation: Localize emergency resources, school-stage assumptions, and minor-consent requirements before use in other regions or languages.

Risk: Persistent attention difficulties may need support beyond study-time coaching.

Mitigation: Frame the skill as study support, not clinical assessment, and suggest professional evaluation when attention problems are severe, persistent, or affect everyday life and social functioning.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach)
- [focus-archives-template.md](artifact/references/focus-archives-template.md)
- [pomodoro-statemachine.md](artifact/references/pomodoro-statemachine.md)
- [grade-bands.md](artifact/shared/grade-bands.md)
- [crisis-exception.md](artifact/shared/crisis-exception.md)
- [platform-conventions.md](artifact/shared/platform-conventions.md)
- [handover-protocol.schema.json](artifact/shared/handover-protocol.schema.json)
- [dna-profile.schema.json](artifact/shared/dna-profile.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance]

**Output Format:** [Chinese Markdown-style conversational guidance, focus summaries, and JSON-compatible profile or reminder handoff records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long-term memory, reminders, and cross-skill sharing are consent-gated and default off.]

## Skill Version(s):

2.3.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
