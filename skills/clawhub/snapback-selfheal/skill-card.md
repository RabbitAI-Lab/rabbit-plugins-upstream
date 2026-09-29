## Description:

Diagnose failed AI-agent runs, catch loops or budget problems during execution, and return structured fixes through a Snapback MCP service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ra1labsworkx-wq](https://clawhub.ai/user/ra1labsworkx-wq)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to diagnose failed or looping agent runs, monitor runs for budget and context issues, and receive structured root-cause and fix guidance. Some diagnostic flows send trace or live-run details to the third-party Snapback service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent traces and live-run details may be sent to a third-party Snapback service.

Mitigation: Do not send secrets or regulated/proprietary traces unless Snapback handling and retention terms have been reviewed; keep SNAPBACK_TOKEN in environment configuration rather than prompts or committed files.

Risk: Optional autonomous repair and self-heal behavior can retry, refetch, or change configuration during tool execution.

Mitigation: Enable auto_apply only around tool calls where retry, refetch, or configuration changes are acceptable, and require human approval for wallet, payment, authentication, mutation, or destructive actions.

Risk: The skill describes package installation and wallet-based pay-per-call flows that may introduce operational and financial exposure.

Mitigation: Review the snapback-selfheal dependency before installation and require explicit human approval before wallet or payment flows are used.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ra1labsworkx-wq/skills/snapback-selfheal)
- [Snapback homepage](https://snapback.sh)
- [Snapback MCP endpoint](https://api.snapback.sh/mcp)
- [Snapback MCP discovery](https://snapback.sh/.well-known/mcp.json)
- [Snapback machine guide](https://snapback.sh/llms.txt)
- [Snapback agent guide](https://snapback.sh/for-agents)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, shell commands, configuration snippets, and MCP tool-call outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured diagnostic verdicts, loop or budget warnings, root-cause analysis, fix suggestions, and references to metered or token-authenticated Snapback flows.]

## Skill Version(s):

1.8.2 (source: frontmatter, claw.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
