## Description:

Snapback connects MCP-capable agents to Snapback diagnostics for failed-run analysis, live loop and budget guarding, and structured fix guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ra1labsworkx-wq](https://clawhub.ai/user/ra1labsworkx-wq)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to connect AI agents to Snapback for diagnosing failed runs, catching loops or budget overruns during execution, and receiving concrete fix guidance. It is intended for normal ClawHub use with explicit operator control over trace uploads, token-authenticated calls, and metered payment flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent traces, live session steps, or private business context may be sent to a remote service.

Mitigation: Require explicit user approval before uploads or live sessions, send the minimum diagnostic structure needed, and redact locally before relying on server-side redaction.

Risk: Token-authenticated diagnosis and x402 payment flows may create metered usage or wallet-signing exposure.

Mitigation: Confirm each metered diagnosis or payment step with the operator, verify network and cost details, and avoid granting unattended wallet authority.

Risk: Broad activation wording could cause agents to invoke the skill during ordinary failures without clear confirmation boundaries.

Mitigation: Gate trace uploads, live monitoring, authenticated calls, and payment-related actions behind explicit user intent.

Risk: The optional self-heal pip package is executable software outside the text-only skill review.

Mitigation: Review and validate the package separately before installation, and keep automatic remediation limited to high-confidence, reversible actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ra1labsworkx-wq/skills/snapback-selfheal)
- [Snapback homepage](https://snapback.sh)
- [Snapback for agents](https://snapback.sh/for-agents)
- [Snapback MCP endpoint](https://api.snapback.sh/mcp)
- [Snapback MCP discovery](https://snapback.sh/.well-known/mcp.json)
- [Snapback machine guide](https://snapback.sh/llms.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON-RPC examples, shell commands, and code snippets; MCP tool responses are JSON strings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some tools are unauthenticated; token-authenticated and metered diagnosis flows can send trace or live-session data to Snapback.]

## Skill Version(s):

1.7.0 (source: SKILL.md frontmatter, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
