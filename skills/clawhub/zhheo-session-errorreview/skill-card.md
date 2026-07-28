## Description: <br>
当用户说「报错回顾」时，整理当前 session 中工具调用的所有报错，分析根因并自动修复，含分类/去重/压缩/淘汰机制 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhheo](https://clawhub.ai/user/zhheo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users invoke this skill after tool-call failures to review the current session, classify root causes, and update personal skill documentation or TOOLS.md with deduplicated error records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically edit persistent agent documentation and personal skills based on session errors without an explicit confirmation step. <br>
Mitigation: Review proposed diffs before accepting changes, require confirmation before writes in sensitive workspaces, and limit edits to the documented personal OpenClaw paths. <br>
Risk: General shell or Python text replacement can change more content than intended when error signatures or file structure are ambiguous. <br>
Mitigation: Prefer scoped file-editing operations, keep backups or version control for personal skill files, and inspect the final modified file list after each run. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Chinese Markdown report with file modification summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update persistent OpenClaw skill files or TOOLS.md, including compact one-line error records with counters.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
