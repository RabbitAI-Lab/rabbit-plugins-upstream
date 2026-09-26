## Description:

帮助中国大陆中小学高年级至高中学生将课堂笔记整理为康奈尔格式，并按学科和课题检索复习。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking students in upper primary, middle, and high school use it to turn photographed or typed class notes into reviewable Cornell notes, find earlier notes, and request a note-usage report when their archive is enabled. Upper-primary students receive a simplified format.

### Deployment Geography for Use:

Mainland China; other regions require localization of language, curriculum, consent rules, and crisis contacts.

## Known Risks and Mitigations:

Risk: A persistent archive of a minor's class notes may expose personal learning information if enabled without appropriate consent.

Mitigation: Require the appropriate student or guardian consent before storing notes; provide view, correction, export, pause, and deletion controls.

Risk: Cross-skill sharing and review reminders may disclose learning patterns or contact a student unexpectedly.

Mitigation: Keep sharing and reminders off unless expressly requested; share only aggregate note counts and recurring gaps, not note text.

Risk: Chinese-language curriculum and crisis guidance may not fit students outside mainland China.

Mitigation: Limit deployment to the intended population or localize language, curriculum, consent rules, and local crisis contacts before broader use.

## Reference(s):

- [Cornell note format and subject templates](references/cornell-format-guide.md)
- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-cornell-notes)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language Cornell note outlines, retrieval suggestions, and on-request usage summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [With consent, indexes notes for later retrieval; optional cross-skill sharing passes aggregate counts and recurring gaps, not full notes.]

## Skill Version(s):

2.6.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
