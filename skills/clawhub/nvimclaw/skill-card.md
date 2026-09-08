## Description:

nvimclaw bridges an agent to a live Neovim instance over OpenClaw so it can read or edit buffers, inspect editor state and diagnostics, run targeted Ex substitutions, and route chat through Neovim.

This skill is ready for commercial/non-commercial use.

## Publisher:

[utrumsit](https://clawhub.ai/user/utrumsit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use nvimclaw to let an agent inspect and update files open in a live Neovim workspace, including unnamed buffers, selections, diagnostics, and cursor state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects an agent to a live Neovim session where it can read buffer content and editor state.

Mitigation: Install it only for trusted agent sessions and keep the read-only safe tier unless editor changes are required.

Risk: Privileged nvim.* commands can edit buffers or execute powerful Ex commands when the gateway and plugin are configured to allow them.

Mitigation: Use explicit command allowlists on shared gateways and enable broad privileged access only in trusted private setups.

Risk: Chat sends from Neovim may include current-buffer context.

Mitigation: Disable or limit attached buffer context when working with sensitive files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/utrumsit/skills/nvimclaw)
- [Plugin repo](https://github.com/utrumsit/nvimclaw)
- [vscode.openclaw extension](https://github.com/xiaoyaner-home/openclaw-vscode/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell, Lua, Vimscript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include OpenClaw command invocations and Neovim configuration snippets.]

## Skill Version(s):

0.1.10 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
