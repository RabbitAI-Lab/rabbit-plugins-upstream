## Description:

Helps independent teachers draft low-anxiety, specific, and actionable parent communications while recording only channel, scenario, facts, and send status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External educators use this skill to draft Chinese parent messages for lesson feedback, progress concerns, renewal conversations, scheduling confirmations, and group announcements without sending messages automatically. It also helps record communication metadata in parentCommunicationLogs while keeping student-card changes and formal stage reports outside this skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive student emotional observations could be drafted for parents without clear proof of student consent.

Mitigation: Before drafting parent-visible emotional or classroom-state content, require explicit parentCommunicationAllowed and emotionSharingWithParent consent; treat missing, guardian-only, or ambiguous consent provenance as denial and fall back to learning facts only.

Risk: Crisis-resource guidance may be inappropriate outside mainland China.

Mitigation: Ask for the user's country or region before giving crisis resources, use local emergency contacts when outside mainland China, and keep the general instruction to contact a trusted adult and local emergency services.

Risk: Requested parent actions may not be preserved consistently because artifact behavior refers to actionSuggestion while the distributed schema excerpt omits that field.

Mitigation: Patch the schema to include actionSuggestion before relying on structured action logging, or keep the requested action in reviewed draft text until the schema is updated.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-parent-communication)
- [Typical scenario scripts](references/typical-scenario-scripts.md)
- [Communication principles examples](references/communication-principles-examples.md)
- [Weekly group announcement template](references/weekly-group-announcement-template.md)
- [Crisis exception protocol](shared/crisis-exception.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Chinese message drafts, Markdown checklists, and structured communication-log field guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts are not sent automatically; the teacher sends them and confirms whether the log status is draft, sent, or not_sent.]

## Skill Version(s):

2.1.10 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
