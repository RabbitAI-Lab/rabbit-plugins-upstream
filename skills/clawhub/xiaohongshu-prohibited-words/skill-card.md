## Description:

小红书违禁词离线检测（单一真相源）。纯本地词库 + 扫描脚本，不依赖付费 API，覆盖免费课程/证书等场景实测限流词 + 通用违禁词。发布前必跑，退出码 0 才可发布。词库带入库/出库维护机制，持续养护不过时。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Content creators and publishing workflow agents use this skill before posting Xiaohongshu notes to scan titles, body text, and tags for maintained prohibited-word patterns. Maintainers also use it to update the local word list when platform behavior changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local checker may miss rules documented in the maintained word list if the script and reference file drift out of sync.

Mitigation: Keep scripts/check_prohibited.py synchronized with references/prohibited-words.md and manually review platform names and repeated sensitive terms before publishing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/xiaohongshu-prohibited-words)
- [Prohibited Words Reference](references/prohibited-words.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Analysis]

**Output Format:** [Markdown guidance with inline shell commands and local scanner output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scanner exits 0 for pass, 1 when P0 terms are found, and 2 on runtime errors.]

## Skill Version(s):

1.0.0 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
