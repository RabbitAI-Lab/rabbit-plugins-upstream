## Description:

Guides developers through running and troubleshooting headless coding agents with the acpx ACP CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to launch, manage, and troubleshoot Codex, Claude, and Antigravity coding agents through acpx outside interactive panes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auto-approved headless coding agents may change files without interactive review.

Mitigation: Use disposable worktrees or narrowly scoped working directories, and keep secrets out of accessible paths.

Risk: A clean exit may not mean the agent completed the requested work.

Mitigation: Inspect the run log and any requested result files before accepting completion.

Risk: Persistent sessions leave background processes running.

Mitigation: Prefer one-shot runs when possible and close persistent sessions after use.

## Reference(s):

- [acpx FAQ skill homepage](https://github.com/tenequm/skills/tree/main/skills/acpx-faq)
- [acpx documentation and source](https://github.com/openclaw/acpx)
- [Antigravity ACP registry entry](https://github.com/agentclientprotocol/registry/blob/main/antigravity-acp/agent.json)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Troubleshooting guidance]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for checking results and closing persistent sessions]

## Skill Version(s):

0.7.0 (source: frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
