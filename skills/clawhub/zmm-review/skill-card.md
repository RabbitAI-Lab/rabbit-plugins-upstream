## Description:

詹明明·发布前审一遍 reviews talking-head scripts before publication with per-sentence density scoring, eleven audience-decision checks, red-line review, and separate machine-signal notes, defaulting to diagnosis rather than rewriting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content reviewers use this skill to evaluate Chinese/Douyin-oriented talking-head scripts before publishing, with checks for audience fit, retention, memorability, action intent, platform red lines, and machine-signal risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may save feedback or recurring issues for future use.

Mitigation: Require confirmation before memory write-back, or disable persistence when reviewing sensitive drafts.

Risk: The skill may read mutable local vault policy files and prioritize them over bundled criteria.

Mitigation: Use only trusted vault files and review active local policy files before execution.

Risk: The workflow includes homophone or coded-word substitutions for platform-facing language.

Mitigation: Do not rely on substitutions to bypass platform moderation; use them only where compliant and editorially appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-review)
- [规则卡.md](artifact/references/规则卡.md)
- [评分锚点.md](artifact/references/评分锚点.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown review report with scoring tables, red-line findings, and replacement guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include staged diagnostic sections, concise verdicts, and two alternative rewrites for red-line issues when rewriting is requested.]

## Skill Version(s):

0.2.10 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
