## Description: <br>
Loan Qualification Check helps loan brokers pre-screen applicant qualifications, estimate possible loan amounts, match loan products, identify rejection risks, and generate follow-up guidance through a paid SaaS backend. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g620710](https://clawhub.ai/user/g620710) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External loan brokers and lending service teams use this skill to run initial customer qualification checks, compare applicants against a listed loan product catalog, and prepare screening reports before formal lender review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends sensitive applicant data and a user key to a hardcoded plain-HTTP backend with limited privacy disclosure. <br>
Mitigation: Do not use real applicant data unless the operator is trusted, consent and privacy terms are in place, and a secure HTTPS endpoint can be enforced. <br>
Risk: The published script currently appears broken due to a Python syntax error. <br>
Mitigation: Inspect and test the script in a disposable environment before installation, and require a corrected release before production use. <br>
Risk: Loan qualification results are pre-screening guidance and may not match final lender approval. <br>
Mitigation: Present reports as non-binding estimates and verify outcomes against bank or lending institution review before making commitments. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/g620710/skills/loan-qualification-check) <br>
- [Loan product list](references/product_list.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [JSON by default, with artifact documentation describing text and Markdown report options.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and LOAN_CHECK_USER_KEY; calls a paid backend service for account, product, and loan-check operations.] <br>

## Skill Version(s): <br>
2.2.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
