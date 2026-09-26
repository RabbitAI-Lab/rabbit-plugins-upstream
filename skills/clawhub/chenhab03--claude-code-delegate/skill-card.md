## Description:

Delegate programming tasks to Claude Code CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenhab03](https://clawhub.ai/user/chenhab03)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this skill to route coding, debugging, testing, and file-editing work from an OpenClaw agent to a local Claude Code CLI process while the main agent remains responsive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can delegate broad coding and file-editing tasks to a local AI process with full file access.

Mitigation: Use an isolated project directory and avoid repositories or directories that contain secrets or sensitive configuration.

Risk: The delegated command uses a permission mode that auto-accepts file operations.

Mitigation: Set up and verify a write-guard or equivalent file protection before running delegated tasks, and do not treat the sample guard as a complete sandbox.

Risk: Delegated changes may introduce incorrect code, unsafe commands, or unwanted file modifications.

Mitigation: Review delegate output, run independent tests in a fresh session, and prefer explicit `/code` invocation or confirmation before delegation.

Risk: The skill depends on external CLI installation and package installation commands.

Mitigation: Pin or verify external package installs where possible and confirm Claude Code authentication before use.

## Reference(s):

- [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code)
- [OpenClaw project](https://github.com/openclaw/openclaw)
- [ClawHub skill page](https://clawhub.ai/chenhab03/skills/claude-code-delegate)
- [PERSONA.md](artifact/PERSONA.md)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Files, Markdown, Configuration instructions, Guidance]

**Output Format:** [Markdown and plain text with inline shell commands and code or file-change summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May launch asynchronous local Claude Code CLI sessions and relay summarized results to the user.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
