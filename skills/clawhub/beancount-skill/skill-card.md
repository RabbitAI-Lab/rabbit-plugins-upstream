## Description: <br>
Professional personal finance advisor specializing in plain-text accounting with Beancount and Fava. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[y1feng200156](https://clawhub.ai/user/y1feng200156) <br>

### License/Terms of Use: <br>
GNU General Public License v3.0 <br>


## Use Case: <br>
Developers, finance-focused users, and AI assistant users use this skill to analyze Beancount ledgers, understand Fava reports, create Beancount syntax and queries, and receive budgeting, planning, and investment education from their own financial data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process sensitive personal financial ledgers. <br>
Mitigation: Use only ledger files suitable for the agent environment, prefer redacted snippets when possible, and avoid sharing unnecessary account, payee, or transaction details. <br>
Risk: Financial, tax, debt, or investment guidance may be incomplete or unsuitable for a user's specific situation. <br>
Mitigation: Treat recommendations as general education and analysis, and consult qualified professionals for major financial, tax, debt, or investment decisions. <br>
Risk: Fava dashboard examples may involve third-party scripts or configuration. <br>
Mitigation: Use only dashboard scripts from trusted sources and review them before adding them to a personal ledger workflow. <br>


## Reference(s): <br>
- [Beancount Syntax Reference](artifact/references/beancount_syntax.md) <br>
- [Beancount Query Language Reference](artifact/references/beancount_query.md) <br>
- [Fava Reference](artifact/references/fava_features.md) <br>
- [Fava Dashboards Plugin](artifact/references/fava_dashboards.md) <br>
- [Financial Analysis Guide](artifact/references/financial_analysis.md) <br>
- [Beancount Documentation](https://beancount.github.io/docs/index.html) <br>
- [Fava Documentation](https://beancount.github.io/fava/) <br>
- [Beancount Project](https://github.com/beancount/beancount) <br>
- [Fava Project](https://github.com/beancount/fava) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Beancount examples, BQL snippets, shell commands, and financial analysis guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use the bundled Python analysis script when a user provides a Beancount file and asks for ledger metrics.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
