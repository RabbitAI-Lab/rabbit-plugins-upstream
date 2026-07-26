## Description: <br>
Delegate coding tasks to external agents such as Claude Code and Codex via ACP for code changes, analysis, review, and multi-agent collaboration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haidiantoutou](https://clawhub.ai/user/haidiantoutou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to route code analysis, bug fixing, implementation, testing, and review tasks to external coding agents. It supports simple single-agent delegation and multi-stage workflows such as analysis, implementation, and review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent OpenClaw configuration changes can broaden agent permissions beyond a single task. <br>
Mitigation: Review the installer before running it, keep a backup of the OpenClaw configuration, and confirm each persistent setting is intended. <br>
Risk: Broad agent delegation and cross-session visibility can expose code or context to external coding agents. <br>
Mitigation: Limit allowed agents to trusted tools, scope use to appropriate workspaces, and avoid routing sensitive repositories unless the agent access model is approved. <br>
Risk: Reduced approval prompts may allow delegated agents to act with less interactive consent. <br>
Mitigation: Prefer explicit opt-in configuration and restore stricter approval settings when autonomous delegation is not required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haidiantoutou/skills/acp-coder) <br>
- [Publisher profile](https://clawhub.ai/user/haidiantoutou) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with inline commands, configuration snippets, and delegated agent results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger external coding agents and persistent OpenClaw configuration changes when installed and used.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
