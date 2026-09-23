## Description:

Organizes student class notes into Cornell-style cue questions, note content, and one-sentence summaries, with subject/topic filing and consent-based retrieval reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

Students in upper-primary, middle-school, and high-school learning contexts use this skill to convert class notes or note photos into reusable Cornell-style study notes, retrieve related notes during review, and view consent-gated note usage summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may store student notes and limited note-usage counters when a profile is enabled.

Mitigation: Confirm profile, sharing, deletion, export, and guardian-consent settings before use, especially in K12 contexts.

Risk: The bundled crisis and referral guidance is written for Chinese mainland K12 learning contexts.

Mitigation: Localize emergency contacts and referral language before using the skill outside mainland China.

Risk: Photo-based note intake may fail or misread handwritten content.

Mitigation: Ask the student to confirm recognized subject, topic, and note content, or provide typed note points when image recognition is unavailable.

## Reference(s):

- [康奈尔笔记格式详解与各科模板](references/cornell-format-guide.md)
- [学段适用性](shared/grade-bands.md)
- [平台约定与降级行为](shared/platform-conventions.md)
- [危机例外处理](shared/crisis-exception.md)
- [学习DNA档案结构](shared/dna-profile.schema.json)
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-cornell-notes)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured text with note fields, cue questions, summaries, retrieval prompts, and consent-gated report sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference profile-enabled note counts and recurring note gaps when consent and platform memory are available.]

## Skill Version(s):

2.2.0 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
