## Description:

OpenCode ACP Control helps an AI agent start, drive, resume, and monitor OpenCode CLI sessions over ACP and JSON-RPC instead of through an interactive terminal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[berriosb](https://clawhub.ai/user/berriosb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill when an AI agent needs to operate OpenCode as an ACP client: starting sessions, sending prompts, streaming updates, handling permissions, resuming sessions, and checking updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The demo auto-approves OpenCode requestPermission tool requests, which can allow commands or file changes without explicit user confirmation.

Mitigation: Remove or gate the auto-approval behavior and require explicit user confirmation for every requestPermission response.

Risk: The update workflow includes process-control and installer steps that can affect running OpenCode processes or execute an unverified installer.

Mitigation: Avoid the update workflow unless needed, manually verify the target processes, and review the installer source before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/berriosb/skills/opencode-acp-control-3)
- [Agent Client Protocol reference](https://agentclientprotocol.com/llms.txt)
- [OpenCode](https://opencode.ai)
- [OpenCode releases](https://github.com/sst/opencode/releases/latest)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown instructions with JSON-RPC examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes ACP session lifecycle guidance, permission handling, polling strategy, update checks, and an optional Python demo.]

## Skill Version(s):

0.3.1 (source: ClawHub release metadata; artifact frontmatter and changelog are 0.3.0 with no code changes vs 0.3.0 per release changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
