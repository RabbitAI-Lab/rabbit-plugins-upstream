## Description:

初中到高中必修起点的化学解题教练，按四步法（定物质、三重表征、写式列式、守恒检验）陪学生完成当前化学题，并在明确授权后才读取档案、归档错题或安排提醒。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and education agents use this skill to coach Chinese K12 students through one chemistry problem at a time, using a four-step method for substance identification, macro-micro-symbol translation, equation setup, and conservation checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaged handoff schema could route chemistry wrong-answer or reminder data to more recipient skills than the stated workflow needs.

Mitigation: Before use in a student environment, narrow or enforce allowed handoff recipients so student data is sent only to the intended skills.

Risk: The skill is intended for a Chinese K12 tutoring context and may not match other regions' localization, emergency-referral, or minor-consent requirements.

Mitigation: Use outside that context only after localizing safety channels, consent handling, and deployment rules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-problem-coach)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [chemistry-4step-guide.md](references/chemistry-4step-guide.md)
- [chemistry-error-dimension-table.md](shared/chemistry-error-dimension-table.md)
- [lab-safety.md](shared/lab-safety.md)
- [crisis-referral-protocol.md](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown-style tutoring guidance with structured hints, checks, handoff payload guidance, and safety/referral language]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Works by default within the current session; long-term profile reads, wrong-answer handoff, and reminders require explicit student and, when applicable, guardian consent.]

## Skill Version(s):

2.3.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
