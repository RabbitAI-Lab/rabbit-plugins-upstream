## Description: <br>
Claude Code integration for OpenClaw that provides documentation queries, best-practice guidance, troubleshooting help, and task-planning commands for AI-assisted development workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill inside OpenClaw to query Claude Code documentation, retrieve workflow guidance, and prepare subagent task descriptions for coding work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documentation examples mention installing Claude Code and configuring MCP servers, which may grant additional local or external access if followed separately. <br>
Mitigation: Review installer sources, MCP server permissions, and OpenClaw or Claude Code configuration before running those separate commands. <br>
Risk: AI-assisted coding guidance or generated task descriptions may be incomplete, incorrect, or unsuitable for a target codebase. <br>
Mitigation: Review suggested workflows, test code changes, and scan skill outputs before applying them to a project. <br>


## Reference(s): <br>
- [Claude Code documentation](https://code.claude.com/docs) <br>
- [ClawHub listing](https://clawhub.ai/paudyyin/claude-code) <br>
- [OpenClaw documentation](https://docs.openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown-style CLI text with inline shell commands and documentation excerpts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs local documentation and workflow guidance; the task command prints OpenClaw execution guidance rather than directly running subagents.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
