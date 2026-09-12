## Description:

3-7 岁幼儿识字与诗歌课程：L1 看图认字 → L2 描红 → L3 组词 → L4 古诗填空，生成 A4 可打印练习页（含答案页）。Use when 用户提到 识字、描红、笔顺、组词、古诗、儿歌、默写、幼小衔接练字；or asks for Chinese tracing worksheets, hanzi, poem with pinyin.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liyumingben](https://clawhub.ai/user/liyumingben)

### License/Terms of Use:

MIT

## Use Case:

Parents, educators, and agents use this skill to create age-leveled Chinese literacy and poem worksheets for children ages 3-7, including recognition, tracing, word formation, poem reading, and fill-in exercises with parent guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated worksheet files and JSON metadata may include a child's name if one is provided.

Mitigation: Keep generated files in a normal workspace folder and omit the name when it is not needed.

Risk: The local preflight report is not a complete security audit.

Mitigation: Review and scan the skill before deployment, and ask the agent to clarify or skip the skill if it activates outside Chinese literacy worksheet generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liyumingben/skills/kindergarten-chinese-course)
- [ClawHub distribution homepage](https://skillhub.cn/skills/user_89a2cacc/kindergarten-chinese-course)
- [Activity specification](references/activity-spec.md)
- [Curriculum](references/curriculum.md)
- [Pedagogy](references/pedagogy.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and local HTML/JSON worksheet files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates A4 printable HTML worksheets and JSON metadata for regeneration; generated files may include a child name if provided.]

## Skill Version(s):

1.0.3 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
