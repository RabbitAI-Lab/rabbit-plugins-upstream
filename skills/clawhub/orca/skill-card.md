## Description:

Launch and coordinate agent sessions inside the Orca IDE runtime, including sending prompts to running terminals, launching new agent worktrees, and installing Orca skill bundles into supported harnesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to coordinate Orca-managed coding agent sessions, route prompts to an intended running terminal, launch new worktrees, and install Orca skill bundles into Claude Code, OpenClaw, or Antigravity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control other Orca agent sessions and send work to running terminals.

Mitigation: Install only from a trusted publisher, require explicit target confirmation before sending, and review terminal state before delivery.

Risk: The install topic can add persistent agent capabilities to local harnesses.

Mitigation: Prefer project-scoped installation, verify the harness reports the plugin as enabled, and avoid symlinking mutable checkouts unless updates are intentionally shared.

Risk: Security evidence notes that shell-command interpolation examples can execute untrusted prompt text.

Mitigation: Treat task briefs and messages as unsafe input until the examples are fixed, and pin or copy a reviewed version rather than using a mutable source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/orca)
- [Orca send guide](send.md)
- [Orca launch guide](launch.md)
- [Orca install guide](install.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the Orca CLI and may propose persistent plugin installation steps depending on the selected topic.]

## Skill Version(s):

0.3.0 (source: server release metadata and CHANGELOG, released 2026-09-13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
