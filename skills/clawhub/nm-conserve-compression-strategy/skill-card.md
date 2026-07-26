## Description: <br>
Recommends context compression strategies for bloated or quota-heavy sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to analyze session context pressure, choose a compression or delegation strategy, and reduce log-related context bloat before it affects task work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may recommend saving session state or context archives that retain secrets, credentials, proprietary logs, or private conversation details. <br>
Mitigation: Before using those recommendations, review the planned files under .claude/session-state.md or .claude/context-archive/, remove sensitive material, and treat the files as retained local records until deleted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-compression-strategy) <br>
- [ClawHub metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>
- [Drain3](https://github.com/logpai/Drain3) <br>
- [logs-tokenizer](https://github.com/sergeivaskov/logs-tokenizer) <br>
- [LLMLingua](https://github.com/microsoft/LLMLingua) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with analysis summaries, option recommendations, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend local session-state or context-archive files when preserving context before clearing or compacting.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
