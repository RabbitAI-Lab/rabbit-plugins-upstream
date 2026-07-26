## Description: <br>
Oh My OpenCode helps agents install, configure, and operate the oh-my-opencode OpenCode plugin for multi-agent orchestration, autonomous work modes, task delegation, routing, tmux integration, and troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mcoso](https://clawhub.ai/user/mcoso) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to set up and operate oh-my-opencode workflows, including autonomous coding modes, specialized agents, background research tasks, category-based model routing, tmux integration, configuration, and troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill documents powerful autonomous coding workflows and install commands that can modify projects or local configuration. <br>
Mitigation: Install only from trusted oh-my-opencode, OpenCode, and upstream package sources, prefer package-manager or verified installs over curl-to-bash, and run work on a clean git branch or worktree. <br>
Risk: Delegated agents, background tasks, and continuation workflows can continue making changes or consuming model/API budget longer than intended. <br>
Mitigation: Keep command and file permissions on ask or deny for risky actions, monitor model/API cost, review plans and diffs, and stop background or continuation workflows when finished. <br>


## Reference(s): <br>
- [Oh My OpenCode ClawHub Page](https://clawhub.ai/mcoso/skills/oh-my-opencode) <br>
- [Oh My OpenCode Repository](https://github.com/code-yeongyu/oh-my-opencode) <br>
- [Oh My OpenCode Configuration Reference](references/configuration.md) <br>
- [Oh My OpenCode Troubleshooting Guide](references/troubleshooting.md) <br>
- [Oh My OpenCode Schema](https://raw.githubusercontent.com/code-yeongyu/oh-my-opencode/master/assets/oh-my-opencode.schema.json) <br>
- [OpenCode Documentation](https://opencode.ai/docs/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown prose with inline shell and JSON/JSONC code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include OpenCode, bunx, tmux, provider, and permission configuration guidance; users should review commands and settings before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
