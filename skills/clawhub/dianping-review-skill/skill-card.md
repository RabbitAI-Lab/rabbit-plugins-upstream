## Description:

帮助大众点评个人用户根据真实体验和照片撰写评价或探店笔记，并按需整理供用户手动发布的文案与照片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT-0

## Use Case:

大众点评个人用户可将自己的消费经历和照片整理为真实的评价或探店笔记；需要发布时，还可生成供其在点评 App 中手动使用的文案和排序照片。该免费版不代替用户发布，也不适用于商家运营或虚假评价。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaging script can erase an existing output folder without confirmation.

Mitigation: Choose a dedicated empty output directory before running the packaging script.

Risk: Skipping the content check can allow unsupported or unsuitable review claims into the package.

Mitigation: Keep the content check enabled; avoid --no-gate for normal use and verify claims against the user's account and photos.

Risk: The separately advertised Pro replacement package has not been reviewed with this release.

Mitigation: Inspect the Pro package separately before using it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/huiyonghkw/skills/dianping-review-skill)
- [Skill homepage](https://huiyonghkw.github.io/dianping-review-skill/)
- [Writing playbook](references/playbook.md)
- [Category-specific writing templates](references/templates.md)
- [Category content rules](references/category_rules.json)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Markdown drafts and optional plain-text publication package with numbered image copies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes suggested tags, photo order and user-provided ratings; publication remains manual.]

## Skill Version(s):

1.0.0 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
