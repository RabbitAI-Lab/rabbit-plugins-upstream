## Description: <br>
Manage background coding agents in tmux sessions. Spawn Claude Code or other agents, check progress, get results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cuba6112](https://clawhub.ai/user/cuba6112) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to start, monitor, attach to, and stop persistent tmux sessions that run coding agents on background software tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent tmux-managed agents may keep running unattended and can edit files or run commands in the workspace. <br>
Mitigation: Use the skill in a disposable branch or sandbox, monitor sessions with status.sh or tmux, and kill sessions when finished. <br>
Risk: Cloud agent modes may send task context to external agent services. <br>
Mitigation: Avoid secrets and sensitive repositories, and prefer local Ollama-backed agents for private work. <br>
Risk: The spawn script accepts user-provided session, task, and agent values and the security evidence notes weak input validation. <br>
Mitigation: Use trusted inputs, inspect commands before spawning sessions, and restrict use to expected agent names when operating in shared or sensitive workspaces. <br>
Risk: Some launched agent commands use permissive or auto-approval modes. <br>
Mitigation: Review generated changes and command output before merging, deploying, or using results in production work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cuba6112/skills/tmux-agents) <br>
- [Publisher profile](https://clawhub.ai/user/cuba6112) <br>
- [Artifact README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and terminal status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires tmux; optional local-agent setup uses Ollama.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
