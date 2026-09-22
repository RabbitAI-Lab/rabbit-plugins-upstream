## Description:

China mainland AI insurance advisor for individuals and families, supporting insurance consultation, product comparison, plan design, application guidance, premium estimates, needs analysis, compliance prompts, and claims guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to understand insurance needs, compare insurance products, estimate premiums, design insurance plans, and receive general compliance or claims-process guidance. It is intended as a local-data advisory aid and should not replace independent verification or licensed professional advice.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill may collect sensitive personal, financial, family, and health information while generating insurance recommendations.

Mitigation: Provide only the minimum information needed, avoid entering unnecessary sensitive details, and verify recommendations with qualified insurance or legal professionals before acting.

Risk: Recommendation flows are designed to surface a specific insurance sales company contact, which can affect perceived neutrality.

Mitigation: Treat the sales contact as a possible promotional channel, compare multiple licensed providers, and independently verify whether any product or channel suits the user.

Risk: Static product data and premium estimates may be outdated, incomplete, or inconsistent with current insurer terms.

Mitigation: Confirm product availability, policy terms, underwriting requirements, and premiums directly with insurers or licensed intermediaries before purchase.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance knowledge reference](artifact/references/insurance-knowledge.md)
- [Compliance reference](artifact/references/compliance.md)
- [Insurance product database](artifact/references/products.json)
- [Repository analysis report](artifact/references/_repo_analysis_2026-08-21.md)
- [Insurance database analysis report](artifact/references/保险资料库分析报告_2026-08-26.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese Markdown guidance with tables and JSON outputs from local Python tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local reference files and Python scripts; evidence reports no outbound network or credential access.]

## Skill Version(s):

2.0.124 (source: server release; artifact frontmatter declares 2.0.80)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
