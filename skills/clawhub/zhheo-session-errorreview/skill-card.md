## Description: <br>
当用户说「报错回顾」时，整理当前 session 中工具调用的所有报错，分析根因并自动修复，含分类/去重/压缩/淘汰机制 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhheo](https://clawhub.ai/user/zhheo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to review recent tool-call failures, classify root causes, and repair skill documentation or workspace guidance when the error pattern supports a concrete fix. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read recent tool-error context and automatically make persistent changes to skill files or workspace guidance. <br>
Mitigation: Review generated changes before relying on them, and prefer a confirmation step before persistent writes in sensitive workspaces. <br>
Risk: Incorrect error classification could add misleading guidance or modify the wrong skill documentation. <br>
Mitigation: Check the reported classification, affected files, and deduped error signature before keeping the change. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhheo/skills/zhheo-session-errorreview) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown report with file-change summaries and inline commands or edits when applicable] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update SKILL.md or TOOLS.md when the analyzed error category calls for a persistent fix.] <br>

## Skill Version(s): <br>
2.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
