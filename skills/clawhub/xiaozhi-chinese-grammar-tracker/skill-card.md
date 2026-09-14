## Description:

语病追踪档案帮助学生按中考六类病句识别、改写和练习，并在学生同意后记录语病类型与进步情况。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and tutoring agents use this skill to coach Chinese grammar-error diagnosis, guide revisions through prompts and practice items, and maintain a consent-based grammar-error profile for recurring issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent learning profiles can contain records about minors if platform consent, age-band handling, or profile controls are weak.

Mitigation: Install only where profile enrollment, guardian consent when required, pause/delete controls, and strict schema validation are enforced before writeback.

Risk: Profile sharing may expose grammar-error records across skills or to parents beyond the student's consent.

Mitigation: Require speaker verification in shared chats and check cross-skill and parent-sharing consent before sharing the minimum necessary fields.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-grammar-tracker)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [grammar-error-library.md](references/grammar-error-library.md)
- [chinese-error-dimension-table.md](shared/chinese-error-dimension-table.md)
- [dna-profile.schema.json](shared/dna-profile.schema.json)
- [handover-protocol.schema.json](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown dialogue with optional JSON-compatible profile writeback payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user consent before persistent profile updates; falls back to session-only counts when memory or cross-session analytics are unavailable.]

## Skill Version(s):

2.1.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
