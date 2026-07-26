## Description: <br>
Provides read-only OKX market data commands for prices, order books, candles, derivatives metrics, instrument discovery, market screening, and technical indicators. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[searchworld](https://clawhub.ai/user/searchworld) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and market analysts use this skill to retrieve public OKX market data, discover instruments, and inspect technical indicators. It is intended for informational market-data workflows, not account access, order placement, or trading bots. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing this skill adds the broader OKX CLI globally, including helper binaries under ~/.okx/bin. <br>
Mitigation: Review the installed OKX CLI and helper binaries before installation, and install only in environments where a global OKX CLI is acceptable. <br>
Risk: The broader OKX CLI may include account or trading capabilities outside this market-data skill. <br>
Mitigation: Use this skill only for documented read-only market commands, and keep account or trading credentials separate unless intentionally using other OKX skills or commands. <br>
Risk: Indicator and market-data outputs can be mistaken for trading recommendations. <br>
Mitigation: Treat outputs as informational data only; users remain responsible for interpretation and trading decisions. <br>
Risk: Large historical candle requests can consume excessive context or time. <br>
Mitigation: Estimate requested candle counts before paginated historical fetches and ask for confirmation when the estimate exceeds 500 candles. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-market) <br>
- [OKX homepage](https://www.okx.com) <br>
- [Price and market data commands](references/price-data-commands.md) <br>
- [Derivatives and contract data commands](references/derivatives-commands.md) <br>
- [Instrument discovery commands](references/instrument-commands.md) <br>
- [Technical indicator command reference](references/indicator-commands.md) <br>
- [Cross-skill workflows and MCP tool reference](references/workflows.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands are documented as read-only market-data calls that require no API credentials; users can request raw OKX API responses with --json.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
