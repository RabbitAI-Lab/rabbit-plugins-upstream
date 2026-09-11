## Description:

PipRail gives OpenClaw agents a self-custodial, budget-capped crypto wallet for discovering, quoting, planning, and paying x402-gated resources across supported chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[piprail](https://clawhub.ai/user/piprail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use PipRail to let agents discover, quote, plan, and pay for x402-gated APIs under explicit spend caps. The skill also supports read-only discovery and quoting workflows when no wallet signing key is configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server may receive a wallet signing key when payments are enabled.

Mitigation: Use read-only mode unless payments are required, and use a dedicated low-value wallet when enabling payments.

Risk: The configured npm MCP package is not pinned in the artifact configuration.

Mitigation: Pin and review the MCP package version where possible before deployment.

Risk: Budget controls inside the MCP server may be the only limit on agent-initiated payments.

Mitigation: Keep wallet balances no higher than acceptable loss and prefer externally enforced wallet or smart-contract limits.

## Reference(s):

- [PipRail homepage](https://piprail.com)
- [PipRail OpenClaw integration docs](https://docs.piprail.com/integrations/openclaw/)
- [PipRail MCP configuration](https://docs.piprail.com/mcp/configuration/)
- [PipRail MCP tools](https://docs.piprail.com/mcp/tools/)
- [PipRail spend controls](https://docs.piprail.com/spend-controls/payment-policy/)
- [@piprail/mcp npm package](https://www.npmjs.com/package/@piprail/mcp)
- [PipRail source repository](https://github.com/piprail/piprail)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline JSON and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Configures an MCP server that exposes PipRail payment and wallet tools to an OpenClaw agent.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
