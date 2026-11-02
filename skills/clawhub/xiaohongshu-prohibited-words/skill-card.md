## Description:

在小红书发布前，本地扫描标题、正文和标签中的违禁词，并帮助维护词库。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

小红书内容创作者在发布前扫描标题、正文和标签中的词语，并维护本地词库。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The platform's enforcement rules can change, and a clean local scan does not guarantee approval.

Mitigation: Keep the word list current and review the final draft before publishing. Use the separate preflight skill for checks beyond word matching.

## Reference(s):

- [违禁词库](references/prohibited-words.md)
- [词库段落配置](references/sections.json)
- [使用说明](README.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Guidance]

**Output Format:** [Plain-text scan report and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit status: 0 (no P0 match), 1 (P0 match), 2 (usage or runtime error), or 3 (required data unavailable). A passing result does not guarantee platform approval.]

## Skill Version(s):

1.0.5 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
