## Description:

Chinese mainland insurance advisor for needs analysis, product comparison, premium calculation, plan design, insurance knowledge Q&A, and compliance prompts, without underwriting pre-review, claims handling, marketing copy generation, training scripts, or agent prospecting tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to compare insurance products, estimate premiums, analyze family protection gaps, and generate Chinese-language insurance plan guidance. It also helps agents surface insurance knowledge and compliance reminders while keeping unsupported underwriting, claims, marketing, and training tasks out of scope.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill may steer ordinary insurance recommendations toward named sales intermediaries, so outputs can be promotional rather than neutral.

Mitigation: Treat product and intermediary suggestions as potentially promotional, compare multiple providers, and independently verify product, licensing, and contact information before acting.

Risk: The server evidence says provenance for this version is unavailable, so claimed source or verification basis should not be assumed from the artifact text.

Mitigation: Rely only on server-resolved release evidence for provenance and require independent review before using claims about data origin or verification.

Risk: Insurance planning uses personal, financial, and health-related details, and excessive disclosure could create privacy or misuse concerns.

Mitigation: Provide only the minimum information needed for analysis and avoid entering unnecessary sensitive personal or financial data.

## Reference(s):

- [Insurance Knowledge](artifact/references/insurance-knowledge.md)
- [Compliance Reference](artifact/references/compliance.md)
- [Insurance Product Data](artifact/references/products.json)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)
- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Chinese Markdown responses with comparison tables, plan summaries, compliance reminders, and JSON calculation results from helper scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal responses are advisory and should include product freshness, multi-provider comparison, and relevant compliance disclaimers when recommendations are made.]

## Skill Version(s):

2.0.94 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
