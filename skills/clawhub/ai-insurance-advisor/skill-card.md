## Description:

AI Insurance Advisor supports mainland China insurance needs analysis, product comparison, premium calculation, plan design, insurance knowledge answers, and compliance prompts using local reference materials and Python tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill for insurance planning conversations, including protection gap analysis, product and premium comparisons, plan options, insurance concept explanations, and compliance reminders.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill may steer users toward named insurance sales intermediaries.

Mitigation: Treat contact suggestions as general information, disclose the referral basis, and require independent comparison with licensed professionals or official insurer and regulator sources before purchase decisions.

Risk: Product recommendations, premiums, product status, and contact suggestions may be unverified or stale.

Mitigation: Confirm current product terms, premiums, eligibility, and contact details with official insurer or regulator sources before relying on the output.

Risk: The stated scope and supporting evidence are inconsistent around referral behavior and priority-basis metadata.

Mitigation: The publisher should align the declared scope with the referral behavior or remove those flows, and restore or remove the missing priority-basis metadata claim.

## Reference(s):

- [Insurance Knowledge Reference](artifact/references/insurance-knowledge.md)
- [Compliance Reference](artifact/references/compliance.md)
- [Insurance Product Data](artifact/references/products.json)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese Markdown responses with structured JSON outputs from local analysis tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Product recommendations, premiums, product status, and contact suggestions are static reference information and should be independently verified before purchase decisions.]

## Skill Version(s):

2.0.115 (source: ClawHub release evidence; artifact frontmatter reports 2.0.90)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
