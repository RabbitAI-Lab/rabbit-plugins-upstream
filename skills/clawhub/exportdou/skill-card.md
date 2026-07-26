## Description: <br>
导出公开抖音视频的一级评论和可选回复到 CSV 或 Excel，查看视频信息与评论数量，预览评论用于用户反馈、舆情、选题或市场分析，并管理可恢复的异步导出任务。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kenny-shaw](https://clawhub.ai/user/kenny-shaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and operators use this skill to export, preview, and download public Douyin comment data through the ExportDou CLI for user feedback, public opinion, content, or market analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public comment exports can still contain personal information. <br>
Mitigation: Process only user-supplied public Douyin links and keep large exports out of model context unless the user explicitly requests analysis of selected data. <br>
Risk: Authentication and download flows can expose API keys or short-lived signed URLs if echoed into responses. <br>
Mitigation: Use browser-based ExportDou login or secure environment variables, and do not print API keys, signed download URLs, raw provider responses, or internal cursors. <br>
Risk: Exports may consume credits or reserve row counts before completion. <br>
Mitigation: Inspect counts for all-comment exports, ask for a count when needed, stop on insufficient credits, and avoid retry loops that could create duplicate paid tasks. <br>
Risk: Private, deleted, login-gated, region-restricted, or otherwise unavailable videos may not be exportable. <br>
Mitigation: Attempt only publicly accessible content supplied by the user and ask for another public link when availability errors occur. <br>
Risk: Local download files can overwrite prior outputs. <br>
Mitigation: Do not use --force unless the user explicitly approves overwriting the exact output path. <br>


## Reference(s): <br>
- [ExportDou CLI command reference](references/commands.md) <br>
- [ExportDou error handling](references/errors.md) <br>
- [ExportDou website](https://exportdou.cn) <br>
- [ExportDou API docs](https://exportdou.cn/developers) <br>
- [ExportDou CLI guide](https://exportdou.cn/agents) <br>
- [ExportDou pricing](https://exportdou.cn/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands, JSON command output, and CSV/XLSX downloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preview output is limited to at most 50 rows; full exports are downloaded as local files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
