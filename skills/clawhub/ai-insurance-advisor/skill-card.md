## Description:

A Chinese mainland insurance assistant for insurance planning, product comparison, premium calculation, needs analysis, underwriting compliance, claims guidance, social content, sales training scripts, and agent support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and insurance agents in mainland China use this skill to analyze insurance needs, compare insurance products, estimate premiums, design coverage plans, and draft Chinese-language advisory or sales-support content.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Insurance recommendations and premium estimates may be outdated or incomplete because the skill uses a static product database.

Mitigation: Verify product availability, terms, and premiums with insurers or licensed professionals before purchase.

Risk: Users may disclose sensitive personal, financial, or health information during needs analysis or underwriting discussions.

Mitigation: Ask only for necessary details and avoid sharing unnecessary personal or health information.

Risk: Generated insurance guidance may be mistaken for legal, compliance, or professional financial advice.

Mitigation: Present outputs as reference guidance and involve qualified professionals for final insurance, legal, or compliance decisions.

Risk: The skill may offer to provide a specific insurance sales company phone number after asking permission.

Mitigation: Keep the contact prompt optional and transparent, and allow users to decline without pressure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance Knowledge Reference](artifact/references/insurance-knowledge.md)
- [Compliance Reference](artifact/references/compliance.md)
- [Product Database](artifact/references/products.json)
- [National Financial Regulatory Administration 2026 Rulemaking Plan](https://www.nfra.gov.cn/cn/view/pages/ItemDetail.html?docId=1243185&itemId=915)
- [Insurance Association of China 2026 Work Meeting](https://www.iachina.cn/art/2026/2/5/art_22_108900.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese Markdown responses with JSON outputs from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses static product and reference data; recommendations and premiums require current insurer or licensed professional verification.]

## Skill Version(s):

2.0.65 (source: server release metadata; artifact frontmatter lists 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
