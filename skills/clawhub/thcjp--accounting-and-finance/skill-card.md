## Description: <br>
Accounting And Finance helps agents produce finance-analysis guidance for valuation modeling, financial statement analysis, and risk assessment workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Analysts, developers, and finance teams use this skill to structure financial analysis tasks such as DCF valuation, ratio and DuPont analysis, cash-flow review, and fraud or liquidity risk checks. It is best suited for report-style outputs based on user-supplied financial statements and assumptions, not real-time market data, tax planning, or quantitative trading. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence marks this skill as suspicious because it requests broad read, write, and command authority that is not well scoped. <br>
Mitigation: Install only in a controlled workspace and require explicit approval before file writes, external requests, or command execution. <br>
Risk: The skill may process confidential financial data and includes callback and API-oriented behavior in its artifact text. <br>
Mitigation: Avoid confidential inputs unless data handling is understood, and review any callback URL, API use, or outbound request before execution. <br>
Risk: Finance outputs can be sensitive to incomplete data, stale statements, and subjective valuation assumptions. <br>
Mitigation: Validate source data, document assumptions, and have a qualified reviewer check conclusions before relying on them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/accounting-and-finance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured reports with optional code or command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on user-supplied financial data and assumptions; results should be reviewed before business or investment use.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
