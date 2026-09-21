## Description:

微信文件自动归类（无头版）——扫描微信接收文件目录，按类型/月份归类、去重、生成报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to run a local, headless WeChat received-file organizer that scans one or more WeChat file folders, reports storage usage, copies files into type or month based folders, and can deduplicate organized output. It is suited to local cleanup and scheduled automation workflows where a dry run should be reviewed before applying file changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read local WeChat received-file folders and report file names, paths, sizes, hashes, and account labels.

Mitigation: Run it only on intended local folders and avoid sharing generated reports when they may expose private file or account information.

Risk: Using --apply or --trash changes local file organization by copying files and, with trash enabled, moving originals to the platform trash.

Mitigation: Run the default dry run first, review the report and destination, use --apply only when ready, and use --trash only after confirming organized copies are correct.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oracis/skills/wechat-file-organizer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON report output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled organizer defaults to dry-run reporting; --apply copies files, --dedupe keeps one organized copy per content hash, and --trash moves originals to recoverable trash where supported.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
