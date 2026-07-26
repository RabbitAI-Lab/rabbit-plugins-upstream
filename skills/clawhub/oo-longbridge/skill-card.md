## Description: <br>
Operates Longbridge through an OOMOL-connected account for market data, account data, rankings, news, filings, valuation, analyst ratings, financial reports, and related Longbridge connector actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve Longbridge market data, account balances, positions, orders, executions, cash flow, watchlists, portfolio analytics, news, filings, corporate actions, valuation data, analyst ratings, and financial reports through an OOMOL-connected Longbridge account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Longbridge account balances, positions, orders, executions, cash flow, and portfolio analytics can contain private financial data. <br>
Mitigation: Retrieve only the specific records needed for the user's task and treat returned account data as private financial information. <br>
Risk: One-time CLI installation, sign-in, or Longbridge connection steps may affect the user's local environment or account session. <br>
Mitigation: Review the setup commands before allowing them and only run setup recovery after an auth, connection, scope, credential, or missing-command failure. <br>
Risk: Actions tagged as write or destructive may change Longbridge state if invoked with an incorrect payload. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and require explicit approval for destructive actions. <br>


## Reference(s): <br>
- [ClawHub Longbridge skill page](https://clawhub.ai/oomol/skills/oo-longbridge) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Longbridge homepage](https://longbridge.com) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before building action payloads and returns connector responses as JSON.] <br>

## Skill Version(s): <br>
1.0.2 (source: skill metadata and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
