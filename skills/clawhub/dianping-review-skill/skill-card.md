## Description:

帮助大众点评个人用户根据亲身经历和照片，写出不编造事实的评价或探店笔记，并按需整理手动发布素材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT-0

## Use Case:

面向想分享真实消费体验的大众点评个人用户；依据用户口述和照片整理评价或探店笔记，核对事实与评分，并在用户需要时制作供其自行发布的图文素材。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Manual packaging can remove an existing output folder without a confirmation step.

Mitigation: Back up any existing dist output before rerunning packaging; review the command before execution.

Risk: Untrusted package inputs or path-like shop names and output paths could affect files outside the intended release folder.

Mitigation: Use only trusted post.json files and avoid path separators or traversal in shop names and --out-dir values.

## Reference(s):

- [Skill homepage](https://huiyonghkw.github.io/dianping-review-skill/)
- [ClawHub skill listing](https://clawhub.ai/huiyonghkw/skills/dianping-review-skill)
- [Writing templates](references/templates.md)
- [Writing style](references/style.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Copy-ready review or note text, title and tags; optional image cover and manually publishable text and photo files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a user-confirmed fact card; does not publish on the user's behalf.]

## Skill Version(s):

1.1.0 (source: frontmatter, CHANGELOG, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
