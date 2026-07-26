## Description: <br>
Loan Calculator helps calculate equal-installment or equal-principal repayments, compare loan plans, analyze prepayment, assess affordability, generate repayment schedules, and evaluate refinancing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ckchzh](https://clawhub.ai/user/ckchzh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to estimate mortgage or loan repayment scenarios, compare financing options, and produce repayment guidance or shell-command calculations from supplied loan terms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release includes an unrelated utility script that can store user input locally without clear disclosure. <br>
Mitigation: Use only the loan-specific calculator script for calculations, avoid entering sensitive personal or financial information into generic utility commands, and inspect the local loan-calculator data directory after testing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ckchzh/loan-calculator) <br>
- [BytesAgain homepage](https://bytesagain.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or terminal text with loan calculations, comparisons, schedules, and guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include currency amounts, monthly payments, interest totals, affordability estimates, and repayment schedule rows based on user-provided loan terms.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
