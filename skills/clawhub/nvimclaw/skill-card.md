## Description: <br>
Bridge to live Neovim over OpenClaw's node plugin. Use for reading or editing named and unnamed buffers, discovering open buffers, running surgical Ex substitutions, inspecting cursor/selection/diagnostics, and Neovim chat-to-session messaging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[utrumsit](https://clawhub.ai/user/utrumsit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to let an agent inspect, read, and edit a live Neovim session through OpenClaw while preserving awareness of buffers, cursor state, selections, diagnostics, and available command tiers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes a privileged arbitrary Ex-command path that can affect files and shell state beyond scoped buffer editing. <br>
Mitigation: Keep privileged mode disabled unless needed, prefer structured buffer tools, and require confirmation for Ex commands that write, delete, quit, source files, or run shell commands. <br>
Risk: Broad gateway command allowlists can expose newly added privileged Neovim tools without per-command review. <br>
Mitigation: Use explicit nvim.* command allowlists on shared gateways and review new privileged commands before allowing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/utrumsit/skills/nvimclaw) <br>
- [Plugin repo](https://github.com/utrumsit/nvimclaw) <br>
- [vscode.openclaw extension](https://github.com/xiaoyaner-home/openclaw-vscode/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown with inline shell, Lua, Vim, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance distinguishes safe read-only commands from privileged mutating commands and uses structured JSON parameters for OpenClaw node invocations.] <br>

## Skill Version(s): <br>
0.1.9 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
