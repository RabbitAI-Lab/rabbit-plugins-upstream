## Description: <br>
Guides agents through OKX CEX spot, swap, futures, options, and event-contract order management, including placing, canceling, amending, monitoring, leverage, take-profit, stop-loss, trailing-stop, credential, and trading-mode checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[searchworld](https://clawhub.ai/user/searchworld) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to prepare or run OKX CEX trading workflows for spot, swap, futures, options, and event contracts. It is intended for order management and trading-mode guidance, not market-data, portfolio, or bot workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can let an agent manage OKX trades with account credentials, including live orders and leverage changes. <br>
Mitigation: Start in demo mode, require explicit user approval for live orders or leverage changes, and verify order details before execution. <br>
Risk: Trading actions such as cancellation, position closure, leverage updates, and remediation after API errors may affect real funds. <br>
Mitigation: Use read-only diagnostics first, present the findings, and wait for a separate confirmation before any cancellation, closure, transfer, bot stop, or other write remediation. <br>
Risk: The security summary flags bot-related troubleshooting as outside the skill's stated scope. <br>
Mitigation: Treat bot checks as out of scope unless the user explicitly authorizes the dedicated bot workflow. <br>
Risk: The skill requires OKX credentials. <br>
Mitigation: Do not accept credentials in chat; guide users to configure credentials through the OKX CLI setup flow. <br>


## Reference(s): <br>
- [OKX homepage](https://www.okx.com) <br>
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-trade) <br>
- [Event Contract Commands](artifact/references/event-commands.md) <br>
- [Event Contract Workflows](artifact/references/event-workflows.md) <br>
- [Futures / Delivery Command Reference](artifact/references/futures-commands.md) <br>
- [Options Command Reference](artifact/references/options-commands.md) <br>
- [Spot Command Reference](artifact/references/spot-commands.md) <br>
- [Swap / Perpetual Command Reference](artifact/references/swap-commands.md) <br>
- [MCP Tool Reference & Output Conventions](artifact/references/templates.md) <br>
- [Trade Workflows & Examples](artifact/references/workflows.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and CLI command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires configured OKX CLI credentials; authenticated command responses should identify live or demo mode.] <br>

## Skill Version(s): <br>
1.4.0 (source: evidence release and artifact frontmatter metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
