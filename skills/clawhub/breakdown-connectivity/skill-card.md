## Description:

Diagnose Internet, DNS, Wi-Fi, packet loss, latency, endpoint reachability, browser navigation, API, upload, download, MCP, and cloud-tool failures with Breakdown on macOS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[breakdown](https://clawhub.ai/user/breakdown)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to investigate failed or flaky network-dependent tasks, install or connect Breakdown's local MCP server on macOS, and produce evidence-backed connectivity reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can install the Breakdown macOS app and persist MCP configuration for Codex or Claude Code.

Mitigation: Review the requested setup command before execution and use status or print-config when inspection or manual configuration is enough.

Risk: Breakdown tools can expose local network evidence, and cloud-backed analysis may be used during troubleshooting.

Mitigation: Confirm the user wants Breakdown evidence or analysis used for the task, and prefer focused time windows, result limits, and relevant context identifiers.

## Reference(s):

- [Breakdown MCP tools](references/mcp-tools.md)
- [Breakdown for Agents](https://breakdown.live/for-agents/)
- [Breakdown macOS download](https://breakdown.live/download/mac)
- [ClawHub skill page](https://clawhub.ai/breakdown/skills/breakdown-connectivity)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request or summarize local Breakdown MCP evidence and Evidence Report exports when available.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
