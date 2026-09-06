## Description:

写一个新 SKILL 时用的编写工具：四层结构（角色/规则/记忆/输出）、安全与隐私边界、五步落地流程、常见问题诊断。面向 SKILL 开发者与有编程/写提示词基础的高中生，在"我要新写一个学习类 SKILL""帮我把这个 SKILL 的规则写清楚""我的 SKILL 行为不稳定怎么排查""这个 SKILL 该记哪些字段"时使用。它不替你写具体学科内容、不做学习辅导、不生成练习题；本仓库的词表与阈值一律以 shared/vocab.md 为准。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, and advanced high school students use this skill to draft or revise learning-oriented SKILL files with clear roles, rules, memory boundaries, safety constraints, and output behavior. It provides authoring guidance and templates rather than subject tutoring, exercises, or platform runtime capabilities.

### Deployment Geography for Use:

China Mainland by default; other regions require localization of crisis channels, curriculum assumptions, and minor-data consent rules before student-facing use.

## Known Risks and Mitigations:

Risk: A copyable template may cause downstream education skills to archive student records after user silence.

Mitigation: Replace any 'two rounds without response, archive' rule with ending the interaction without archiving unless the user explicitly confirms and required consent checks pass.

Risk: The artifact is designed around China Mainland Chinese K12 assumptions, including crisis channels, curriculum alignment, and minor-data consent defaults.

Mitigation: Localize emergency contacts, curriculum assumptions, and consent rules before using generated skills in other regions.

## Reference(s):

- [Skill Templates Library](artifact/references/skill-templates-library.md)
- [Platform Conventions](artifact/shared/platform-conventions.md)
- [Vocabulary and Thresholds](artifact/shared/vocab.md)
- [Crisis Exception](artifact/shared/crisis-exception.md)
- [AI Item Check](artifact/shared/ai-item-check.md)
- [DNA Profile Schema](artifact/shared/dna-profile.schema.json)
- [Handover Protocol Schema](artifact/shared/handover-protocol.schema.json)
- [JSON Schema 2020-12](https://json-schema.org/draft/2020-12/schema)
- [DNA Profile Schema URL](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown guidance with copyable skill-template text and schema-oriented references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces authoring guidance only; generated downstream skills should be reviewed and scanned before deployment.]

## Skill Version(s):

2.1.10 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
