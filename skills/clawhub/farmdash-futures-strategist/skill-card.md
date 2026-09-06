## Description:

Research, size, and route user-signed Hyperliquid perpetual futures with funding analysis, drawdown guards, EIP-712, and zero custody.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trading agents use this skill to research Hyperliquid perpetual futures, compare strategy candidates, size positions, and prepare user-signed orders or cancellations with explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet-linked trading state may be persisted without clear storage, retention, or deletion limits.

Mitigation: Configure the host agent to keep trading ledgers transient or user-deletable and avoid storing unnecessary wallet, account, position, or signed-order history.

Risk: Real futures executions and cancellations can change market exposure and may cause financial loss.

Mitigation: Require fresh analysis and immediate manual user confirmation before every execution or cancellation; disable autonomous calls to state-changing tools.

Risk: FarmDash and Hyperliquid receive wallet, account, position, and signed-order metadata needed for the workflow.

Mitigation: Disclose the data flow before use, keep private keys and seed phrases out of the agent, and send only public addresses or pre-signed EIP-712 payloads.

Risk: A bearer token could be mistaken for execution authority.

Mitigation: Treat FARMDASH_API_KEY only as a tier and rate-limit credential; require a fresh user-controlled EIP-712 signature for each execution or cancellation request.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/parmasanandgarlic/skills/farmdash-futures-strategist)
- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [Canonical FarmDash Futures Strategist Manual](https://www.farmdash.one/openclaw-skills/farmdash-futures-strategist/SKILL.md)
- [FarmDash API Schema](https://www.farmdash.one/agents/openapi.yaml)
- [Agent Integration Documentation](https://www.farmdash.one/docs)
- [MCP Discovery Manifest](https://www.farmdash.one/.well-known/mcp.json)
- [Fees and Commercial Terms](https://www.farmdash.one/fees)
- [Security and Authority Boundaries](https://www.farmdash.one/security)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with structured JSON strategy objects and optional shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory until the user gives explicit confirmation and a fresh EIP-712 signature for each execution or cancellation.]

## Skill Version(s):

1.0.22 (source: server release metadata; artifact frontmatter reports 3.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
