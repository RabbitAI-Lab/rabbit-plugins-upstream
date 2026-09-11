## Description:

面向 3-7 岁幼儿的 L1-L4 思维启蒙体系，生成 A4 可打印训练页与答案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liyumingben](https://clawhub.ai/user/liyumingben)

### License/Terms of Use:

MIT

## Use Case:

Parents, teachers, and agents serving early-childhood education use this skill to generate printable thinking and logic worksheets for children ages 3-7, including diagnostics, answer keys, correction support, and parent-facing guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch roster summary CSV has a bounded spreadsheet-safety issue when opened in spreadsheet software.

Mitigation: Use trusted roster files, prefer the JSON summary and generated worksheets for review, and open _summary.csv cautiously until CSV serialization is hardened.

Risk: Generated worksheets and answer files may contain child names supplied by the user.

Mitigation: Use only the minimum identifying information needed, or use the default blank name field when printing for groups.

Risk: Worksheet difficulty may not match a child's current development level.

Mitigation: Start with the diagnostic preset when level is uncertain and use the documented progression rules before advancing levels.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/liyumingben/skills/kindergarten-thinking-course)
- [ClawHub Publisher Profile](https://clawhub.ai/user/liyumingben)
- [SkillHub Homepage](https://skillhub.cn/skills/user_89a2cacc/kindergarten-thinking-course)
- [Activity Specification](references/activity-spec.md)
- [Curriculum](references/curriculum.md)
- [Pedagogy](references/pedagogy.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands, plus generated HTML worksheets and JSON answer data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated worksheet JSON includes seeds for reproducible regeneration; batch mode can produce multiple worksheet files and a summary CSV.]

## Skill Version(s):

1.2.1 (source: SKILL.md frontmatter, CHANGELOG, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
