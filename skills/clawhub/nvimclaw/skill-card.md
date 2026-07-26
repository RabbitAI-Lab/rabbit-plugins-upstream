## Description: <br>
Bridge to live Neovim over OpenClaw's node plugin for reading or editing buffers, discovering open buffers, running Ex substitutions, inspecting cursor state, selections, diagnostics, and sending Neovim chat messages to an agent session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[utrumsit](https://clawhub.ai/user/utrumsit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use Nvimclaw to let an agent inspect and edit the user's active Neovim workspace through OpenClaw. It is useful for live buffer reads, targeted edits, diagnostics review, cursor or selection inspection, and Neovim-originated chat with the same agent session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can allow an agent to read and edit live Neovim buffers. <br>
Mitigation: Install it only for workflows where editor interaction is intended, review the gateway allowlist, and keep privileged mode disabled unless edits are required. <br>
Risk: Privileged Ex commands or buffer edits can affect unsaved work. <br>
Mitigation: Use explicit command allowlists, require confirmation for destructive Ex commands, and prefer targeted buffer operations with changedtick or line-hash preconditions. <br>
Risk: A buffer can change between inspection and mutation. <br>
Mitigation: Re-read the buffer after conflicts and avoid blind retries; use dry runs and optimistic-lock fields for substitutions and line replacements. <br>


## Reference(s): <br>
- [Nvimclaw ClawHub skill page](https://clawhub.ai/utrumsit/skills/nvimclaw) <br>
- [nvimclaw plugin repository](https://github.com/utrumsit/nvimclaw) <br>
- [vscode.openclaw reference implementation](https://github.com/xiaoyaner-home/openclaw-vscode/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with inline bash, Lua, Vim, and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes read-only and privileged Neovim workflows, capability checks, and optimistic-lock guidance for edits.] <br>

## Skill Version(s): <br>
0.1.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
