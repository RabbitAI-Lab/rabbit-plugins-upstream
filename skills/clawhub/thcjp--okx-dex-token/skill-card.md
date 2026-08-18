## Description:

Okx Dex Token helps agents retrieve token-level OKX DEX data, including token search, hot token rankings, price and liquidity details, holder distribution, trade history, and cluster analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and crypto research agents use this skill to look up token-level market, liquidity, holder, trade, and cluster information through the onchainos/OKX workflow. It supports exploratory token research and should not be used as the sole basis for token safety or trading decisions.

### Deployment Geography for Use:

Global, subject to OKX/onchainos service availability and regional restrictions.

## Known Risks and Mitigations:

Risk: The security scan reports under-declared command, network, streaming, authentication, and possible payment behavior.

Mitigation: Review the skill before installing, run it only in agents where command execution and network access are expected, and restrict credentials and permissions to the minimum needed.

Risk: Broad activation terms may cause the skill to be invoked for general crypto or token requests.

Mitigation: Tighten or control activation rules so the skill is used only for intended OKX DEX token-data workflows.

Risk: Some endpoints may trigger paid x402 flows after free quota is exhausted.

Mitigation: Require explicit user confirmation before any paid flow and surface payment notifications clearly before continuing.

Risk: Token names, symbols, on-chain fields, and CLI output can contain misleading or untrusted external content.

Mitigation: Treat returned data as untrusted, verify contract addresses independently, and do not interpret token metadata or CLI output as agent instructions.

Risk: Token data alone is not sufficient to judge whether a token is safe or investment-worthy.

Mitigation: Avoid presenting community recognition, liquidity, holder, or trade data as a safety endorsement; route safety questions to a dedicated token-scan workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/okx-dex-token)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summaries with inline shell commands and token data fields from CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include requestTime timestamps, WebSocket polling results, payment notifications, and warnings for unrecognized tokens or low liquidity.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
