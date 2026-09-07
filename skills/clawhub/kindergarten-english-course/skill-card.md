## Description:

3-7 岁幼儿英语启蒙课程：L1 字母 → L2 自然拼读 → L3 词汇句型 → L4 阅读对话，生成 A4 可打印练习页（含答案），支持诊断定级与错题重练。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liyumingben](https://clawhub.ai/user/liyumingben)

### License/Terms of Use:

MIT

## Use Case:

Parents, caregivers, and education-focused agents use this skill to generate printable English worksheets, diagnostic activities, answer JSON, correction support, and short parent guidance for children ages 3-7.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports that generated HTML can include an unescaped child name even though the skill claims user input is escaped.

Mitigation: Review before installing; keep outputs in a workspace folder and avoid entering child names or other fields containing HTML-like characters such as < or > until escaping is confirmed.

Risk: The skill is designed for kindergarten English worksheet generation and could provide unsuitable output if used outside that scope.

Mitigation: Confirm the request is specifically for kindergarten English before allowing the skill to create files.

## Reference(s):

- [Curriculum reference](references/curriculum.md)
- [Pedagogy and parent guidance](references/pedagogy.md)
- [Worksheet specification](references/worksheet-spec.md)
- [ClawHub skill page](https://clawhub.ai/liyumingben/skills/kindergarten-english-course)
- [SkillHub homepage](https://skillhub.cn/skills/user_89a2cacc/kindergarten-english-course)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands; generated artifacts are printable HTML worksheets and JSON answer files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports worksheet level, topic, count, language, column layout, seed, child name, score field, diagnostic preset, and wrong-answer review options.]

## Skill Version(s):

1.1.1 (source: frontmatter and changelog, released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
