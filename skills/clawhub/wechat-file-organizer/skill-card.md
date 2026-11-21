## Description:

微信文件自动归类（无头版）——扫描微信接收文件目录，按类型/月份归类、去重、生成报告。零依赖、默认只读（dry-run）、绝不永久删除源文件。扫描逻辑与 GUI 应用 wechat-file-organizer-gui（main.py）同步。

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT

## Use Case:

WeChat users use this skill to scan received files across detected accounts, organize copies by file type or month, identify duplicates, and review storage reports. It defaults to a read-only report; copying requires the explicit --apply option.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious, citing possible irreversible source-file deletion and incomplete analysis of part of the organizer script; the scan does not establish malicious intent.

Mitigation: Follow the scanner guidance: review cleanup behavior and resolve the incomplete analysis before installing; use the default dry-run until then.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/oracis/skills/wechat-file-organizer)
- [Related GUI application](https://github.com/oracis/wechat-file-organizer-gui)

## Skill Output:

**Output Type(s):** [Text reports, JSON, Organized files]

**Output Format:** [Text report or JSON report; copied files arranged in directories]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only report by default; --apply enables copying, with optional --trash cleanup.]

## Skill Version(s):

2.1.2 (source: server release evidence, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
