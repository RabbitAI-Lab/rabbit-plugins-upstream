## Description:

Privora gives AI agents a Bearer-token gateway to Privora investment workflows for market data, Python backtesting, paper trading, portfolio attribution, cloud alerts, and process orchestration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guangfuwu](https://clawhub.ai/user/guangfuwu)

### License/Terms of Use:

MIT-0

## Use Case:

External investors, quant developers, and AI-agent operators use this skill to connect agents to Privora workflows for market-data retrieval, strategy backtesting, simulated trading, alerts, and portfolio analysis. Operators should grant tokens only for the scopes needed by the agent's task.

### Deployment Geography for Use:

Global, subject to user access to Privora and relevant market-data permissions.

## Known Risks and Mitigations:

Risk: A Bearer token can grant agents broad access to account data, workflow execution, scheduling, alerts, deletion paths, and Python execution.

Mitigation: Install only for trusted agents, start with a read-only token, and grant the narrowest Privora scopes needed for the task.

Risk: Some high-impact actions can be self-confirmed through the approvalId flow, so the flow should not be treated as independent human approval.

Mitigation: Add an operator review step before state-changing, destructive, scheduling, or account-reset actions, even when the platform returns a confirmRequired challenge.

Risk: Workflow Python and pip requirements can introduce unsafe code or unexpected network and package behavior.

Mitigation: Review Python workflow code and pipRequirements before execution and avoid running untrusted strategies under privileged tokens.

Risk: Alert and webhook workflows can send data or actions to external endpoints outside Privora.

Mitigation: Verify webhook destinations, payload templates, and alert rules before enabling or replacing plugin bindings.

Risk: Self-hosted or custom LG_AGENT_BASE_URL destinations can receive the token and request body if explicitly allowlisted.

Mitigation: Use only trusted hosts in LG_AGENT_ALLOWED_HOSTS, avoid wildcards, and keep the default official-domain and loopback allowlist unless self-hosting is required.

Risk: Request bodies may be sensitive on shared Windows/MSYS2 hosts.

Mitigation: Avoid shared Windows/MSYS2 environments for sensitive request bodies and prefer hosts with user-isolated temporary storage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guangfuwu/skills/privora-cn-quant)
- [Privora homepage](https://privora.cn)
- [Privora market-data coverage](https://privora.cn/features/realtime-minute-data-coverage)
- [Privora token management](https://privora.cn/profile/tokens)
- [Privora agent skills catalog](https://privora.cn/agent/skills)
- [Privora agent skill execution endpoint](https://privora.cn/agent/skills/execute)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LG_AGENT_TOKEN and optionally LG_AGENT_BASE_URL; API results and side effects depend on the token scopes granted by the operator.]

## Skill Version(s):

1.0.55 (source: frontmatter and server release evidence, released 2026-09-15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
