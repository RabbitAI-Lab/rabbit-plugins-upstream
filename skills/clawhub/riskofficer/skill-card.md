## Description: <br>
Portfolio risk management and analytics for calculating VaR, running Monte Carlo and stress tests, optimizing portfolios with Risk Parity, Calmar, or Black-Litterman methods, checking sector concentration, syncing broker data, and comparing portfolios. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[mib424242](https://clawhub.ai/user/mib424242) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to analyze virtual portfolios, calculate risk metrics, run optimization workflows, perform pre-trade checks, and review broker-synced portfolio data. The skill supports analysis and research workflows only and does not place real broker orders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a RiskOfficer API token that can access portfolio and broker-synced financial data. <br>
Mitigation: Install only if the publisher and RiskOfficer service are trusted, prefer a session environment variable for RISK_OFFICER_TOKEN, and rotate or revoke the token when access is no longer needed. <br>
Risk: Portfolio deletion, optimization application, and broker disconnection can change or remove RiskOfficer portfolio records. <br>
Mitigation: Review the proposed change and require explicit user confirmation before deleting portfolios, applying optimizations, syncing live broker data, or disconnecting broker integrations. <br>
Risk: Users may confuse analytical portfolio operations with real trading activity. <br>
Mitigation: Treat skill outputs as virtual portfolio analysis and research guidance only; execute any real trades outside the assistant through the user's broker or RiskOfficer-controlled flows. <br>
Risk: Currency and data-source constraints can affect calculations and comparisons. <br>
Mitigation: Check ticker currency before portfolio changes, keep single portfolios within RUB or USD, and disclose that FX conversion uses CBR rates when showing aggregated results. <br>


## Reference(s): <br>
- [RiskOfficer homepage](https://riskofficer.tech) <br>
- [ClawHub RiskOfficer skill page](https://clawhub.ai/mib424242/skills/riskofficer) <br>
- [Academic and Technical References](references/academic-references.md) <br>
- [VaR and CVaR Methodology](references/methodology-var.md) <br>
- [Pre-Trade Check Methodology](references/methodology-pre-trade.md) <br>
- [Risk Parity Methodology](references/methodology-risk-parity.md) <br>
- [Black-Litterman Optimization Methodology](references/methodology-black-litterman.md) <br>
- [Cross-Portfolio PnL Correlation Methodology](references/methodology-correlation.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with API request examples, configuration snippets, and concise analytical guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses RISK_OFFICER_TOKEN to call RiskOfficer APIs for virtual portfolio analysis; no real broker orders are placed by the skill.] <br>

## Skill Version(s): <br>
4.3.0 (source: ClawHub release metadata and artifact/clawhub.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
