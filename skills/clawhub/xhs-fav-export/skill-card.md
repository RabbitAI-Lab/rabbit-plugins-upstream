## Description:

把小红书 Web 端当前登录用户「收藏」tab 的收藏笔记批量导出为本地 Markdown（每篇含标题、原文链接、正文、图片/视频 URL），支持 offset/count 分批断点续导。当用户需要导出/备份/检索自己的小红书收藏内容时唤起。

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External users who keep Xiaohongshu favorites use this skill to export their own logged-in favorites into local Markdown files for backup, search, and reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The exporter uses the current logged-in Xiaohongshu browser session and can access private favorite content.

Mitigation: Run it only in a browser profile and account you intend to export, and review the exported files before sharing them.

Risk: Favorites are saved to a local output directory, which may contain personal notes and signed media URLs.

Mitigation: Choose a private output directory you control and avoid committing or syncing the export unless you have reviewed the contents.

Risk: Server security evidence flags an obfuscated, undocumented LLM helper that does not match the stated export purpose.

Mitigation: Review the package before installation and prefer a release that removes wc3-code.mjs or replaces it with clear, documented, purpose-aligned code.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fatmind/skills/xhs-fav-export)

## Skill Output:

**Output Type(s):** [markdown, json, text]

**Output Format:** [Local Markdown files, a summary JSON file, and a single-line JSON status message.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exports one Markdown file per favorite note, saves media URLs rather than downloading media, and supports offset/count batch continuation.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
