## Description:

小红书违禁词离线检测（单一真相源）。纯本地词库 + 扫描脚本，不依赖付费 API，覆盖免费课程/证书等场景实测限流词 + 通用违禁词。发布前必跑，退出码 0 才可发布。词库带入库/出库维护机制，持续养护不过时。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External creators, operators, and agents use this skill before publishing Xiaohongshu content to detect hard prohibited terms, sensitive promotional language, diversion phrases, and account-specific risk terms using a local wordlist and scanner.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local wordlist can warn on platform-specific or account-specific terms and may over-block acceptable wording.

Mitigation: Review and maintain the bundled wordlist for the target account, region, and current platform rules before relying on the result.

Risk: Missing wordlist or section configuration could otherwise create a false pass.

Mitigation: The scanner is designed to fail closed with exit code 3 when required wordlist assets are missing or empty.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/xiaohongshu-prohibited-words)
- [README](README.md)
- [Prohibited words wordlist](references/prohibited-words.md)
- [Section and severity configuration](references/sections.json)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and plain-text scanner output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-only scan results use exit codes 0, 1, 2, and 3; P0 findings block publication, while P1 and P2 findings are advisory.]

## Skill Version(s):

1.0.3 (source: frontmatter and changelog, released 2026-09-19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
