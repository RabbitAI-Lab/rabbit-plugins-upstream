## Description:

Helps agents diagnose failed runs and infrastructure errors, detect loops and budget overruns during execution, and suggest fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ra1labsworkx-wq](https://clawhub.ai/user/ra1labsworkx-wq)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Snapback to investigate failed runs, receive suggested fixes, and monitor live runs for repeated actions or budget overruns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent traces, tool inputs and outputs, live steps, and feedback may contain sensitive workspace data sent to Snapback.

Mitigation: Confirm data sharing is permitted; omit secrets and regulated data from traces and use a scoped token.

Risk: The separately installed self-heal package may apply fixes automatically and has not been reviewed with this skill.

Mitigation: Review the package separately before enabling auto_apply, and require human approval for consequential changes.

Risk: The optional x402 payment path could expose funds to unwanted charges.

Mitigation: Use a low-value, purpose-specific wallet if trying payment-based diagnosis.

## Reference(s):

- [Snapback ClawHub release](https://clawhub.ai/ra1labsworkx-wq/skills/snapback-selfheal)
- [Snapback tool schemas](https://snapback.sh/.well-known/mcp.json)
- [Snapback machine guide](https://snapback.sh/llms.txt)
- [Snapback MCP endpoint](https://api.snapback.sh/mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions, Code]

**Output Format:** [Markdown guidance and structured JSON verdicts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Suggested fixes, root causes, confidence estimates, and live-run warnings; some diagnosis is metered.]

## Skill Version(s):

1.8.3 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
