## Description:

3-7 岁幼儿识数与加减法体系课程，按 L1-L5 五级体系生成 A4 可打印数学练习页和答案 JSON，并支持能力诊断、练习批改与进阶建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liyumingben](https://clawhub.ai/user/liyumingben)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and educators use this skill to create kindergarten math worksheets, diagnostic exercises, answer files, grading feedback, and parent-facing practice guidance for children ages 3-7.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated worksheet HTML can embed unescaped title or child-name input as executable browser content.

Mitigation: Use only trusted title and child-name inputs, or patch HTML escaping before installation in environments where those values may come from untrusted people.

Risk: The skill creates persistent HTML, JSON, and optional progress-journal files in the workspace.

Mitigation: Review generated files before sharing and avoid storing sensitive child information in filenames, worksheet fields, or progress journals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liyumingben/skills/kindergarten-math-course)
- [SkillHub homepage](https://skillhub.cn/skills/user_89a2cacc/kindergarten-math-course)
- [Curriculum reference](artifact/references/curriculum.md)
- [Pedagogy reference](artifact/references/pedagogy.md)
- [Worksheet generation specification](artifact/references/worksheet-spec.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands plus generated HTML worksheet and JSON answer files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create persistent HTML, JSON, and optional progress-journal files in the workspace.]

## Skill Version(s):

1.3.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
