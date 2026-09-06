## Description:

康奈尔笔记 helps Chinese K12 students turn classroom notes into reusable Cornell-style notes with cue questions, concise summaries, subject/topic indexing, and consent-controlled retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in upper primary, middle school, and high school use this skill to organize photographed or typed classroom notes into Cornell-style study material, retrieve relevant notes during review, and generate a limited note-usage report when profile storage is enabled. Operators should treat it as a student-support workflow that depends on platform memory, OCR, and reminder-consent controls.

### Deployment Geography for Use:

China mainland by default; localize emergency contacts, curriculum assumptions, and minor-data consent rules before deployment elsewhere.

## Known Risks and Mitigations:

Risk: A referenced template suggests retaining self-test results and scheduling a one-day IM reminder, which conflicts with the skill's stated session-only recall state and reminder-consent rules.

Mitigation: Before student deployment, clarify that SKILL.md and shared consent rules override reference templates, remove or label the self-test record as session-only, and queue reminders only after explicit reminder consent.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-cornell-notes)
- [康奈尔笔记格式详解与各科模板](references/cornell-format-guide.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [学段参数表](shared/grade-bands.md)
- [LearningDNAProfile schema](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)
- [Xiaozhi multi-agent handover protocol schema](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or structured text responses with optional JSON handover/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May rely on platform OCR, cross-session memory, and reminder queue capabilities; degrades to current-session text-only note organization when those capabilities are unavailable.]

## Skill Version(s):

2.1.10 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
