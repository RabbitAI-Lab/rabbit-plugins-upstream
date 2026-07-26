## Description: <br>
Interactive Brokers (IBKR) trading automation via the Client Portal API for account access, session authentication, portfolio and position checks, and trading-bot workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flokiew](https://clawhub.ai/user/flokiew) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and traders use this skill to set up IBKR Client Portal access, authenticate sessions with IBeam and IBKR Key, inspect account and portfolio data, and build or run trading automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give automation live brokerage authority without enough safety guardrails. <br>
Mitigation: Use an IBKR paper account first, require explicit human approval for orders, and add maximum order sizes, account limits, symbol allowlists, and a kill switch before connecting to a live brokerage account. <br>
Risk: Plaintext credential configuration can expose IBKR account access. <br>
Mitigation: Avoid storing secrets in plaintext where possible; if a .env file is used, restrict access tightly and protect the host environment. <br>
Risk: Automatic order confirmation can bypass a review step for potentially risky trades. <br>
Mitigation: Remove automatic order confirmation or gate it behind explicit approval and bounded trading rules. <br>
Risk: Cron-based keepalive can preserve an authenticated trading session longer than intended. <br>
Mitigation: Enable keepalive only when needed, monitor session activity, and disable it when trading automation is not actively supervised. <br>
Risk: Gateway and Python dependency setup affects a sensitive financial workflow. <br>
Mitigation: Verify the IBKR gateway package and Python dependencies before installation or execution. <br>


## Reference(s): <br>
- [IBKR Client Portal API Reference](references/api-endpoints.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/flokiew/skills/ibkr-trader) <br>
- [IBKR Client Portal Gateway Download](https://download2.interactivebrokers.com/portal/clientportal.gw.zip) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, Python code, configuration snippets, and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local scripts and IBKR Client Portal API endpoints; trade execution requires running configured scripts against an authenticated IBKR account.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
