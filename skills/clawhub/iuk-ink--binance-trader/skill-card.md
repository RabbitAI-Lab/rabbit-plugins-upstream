## Description:

Binance Trader guides agents in using the @iuk-ink/binance-mcp-server MCP server for Binance USDT-M futures market analysis, technical indicators, risk checks, and guarded futures order workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iuk-ink](https://clawhub.ai/user/iuk-ink)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to a Binance MCP server, choose market-analysis and trading tools, configure local or HTTP MCP access, and follow safer futures-trading workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mainnet Binance API keys can authorize real futures orders, position changes, leverage changes, and stop or limit management.

Mitigation: Keep testnet enabled until the full workflow is verified, add API credentials only when trading is intended, and treat mainnet credentials as real trading authority.

Risk: Missing or unavailable MCP tools can lead to failed calls or unsupported market and trading responses.

Mitigation: Confirm the Binance MCP server is available before use, such as with a lightweight market ping or tool-list check, and avoid inventing market or order data when tools are absent.

Risk: A repeated order after an exchange timeout can unintentionally increase exposure.

Mitigation: Wait for the server result or verify order state before retrying, and use dry-run checks before placing new parameters or symbols.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iuk-ink/skills/binance-trader)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and command or tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No files are produced by the skill itself; agents may provide MCP client configuration snippets and trading workflow guidance.]

## Skill Version(s):

3.1.0 (source: metadata.version and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
