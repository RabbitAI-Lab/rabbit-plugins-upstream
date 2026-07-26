## Description: <br>
HR 税费计算器 estimates Chinese payroll, service remuneration, author remuneration, royalty, severance-compensation tax, and after-tax to pre-tax calculations using local Python scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zzzzzmh](https://clawhub.ai/user/zzzzzmh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
HR staff, payroll operators, and agents use this skill to answer Chinese personal tax and take-home pay questions, including salary, labor/service remuneration, author remuneration, royalties, severance compensation, and reverse calculations from after-tax to pre-tax amounts. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax estimates may be wrong if policy, local social security, housing fund, or average salary inputs are outdated or missing. <br>
Mitigation: Treat outputs as estimates, verify tax constants and user-provided deduction inputs, and seek professional tax advice for decisions with financial consequences. <br>
Risk: The skill does not query real-time city social security or housing fund parameters. <br>
Mitigation: Ask users to provide values from payroll records or local official sources, and clearly state when zero or assumed values are used. <br>


## Reference(s): <br>
- [Tax Rules Reference](artifact/references/tax-rules.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/zzzzzmh/skills/51shebao-test) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON calculation results from the bundled CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local Python 3 standard-library execution; no network access, persistence, credential handling, or hidden high-impact behavior found in security evidence.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
