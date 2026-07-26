## Description: <br>
Huabei is a consumer-credit guidance skill for understanding Ant Credit Pay repayment mechanics, credit-report considerations, and real annualized installment cost using a local zero-dependency IRR calculator. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhangifonly](https://clawhub.ai/user/zhangifonly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to evaluate Huabei installment decisions, explain interest-free and fee-bearing repayment paths, and answer credit-reporting questions with debt-risk cautions. The bundled script can calculate real annualized cost from amount, term, and fee inputs before making repayment recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat general Huabei guidance as personalized financial advice. <br>
Mitigation: Frame recommendations as educational support and direct users to verify account-specific terms, rates, limits, and repayment obligations in Alipay. <br>
Risk: Huabei terms, fees, and credit-reporting status can vary by account and change over time. <br>
Mitigation: Use current in-app disclosures as the authority before acting on repayment, installment, closure, or limit-management guidance. <br>
Risk: IRR calculator output can be misleading if amount, term, or fee inputs are wrong. <br>
Mitigation: Confirm the principal, number of periods, and all fees before comparing calculated annualized cost with other credit or savings options. <br>


## Reference(s): <br>
- [Huabei Skill Page](https://clawhub.ai/zhangifonly/skills/huabei) <br>
- [zhangifonly Publisher Profile](https://clawhub.ai/user/zhangifonly) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, shell commands] <br>
**Output Format:** [Markdown guidance with inline shell commands and local calculator output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a local standard-library Python IRR calculator; no account access, credentials, network access, persistence, or transaction authority.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
