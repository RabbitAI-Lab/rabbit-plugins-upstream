## Description: <br>
This skill helps users in mainland China analyze insurance needs, compare insurance products, estimate premiums, design coverage plans, and answer underwriting, compliance, and claims questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users in mainland China use the skill to plan personal or family insurance coverage, compare local products, calculate estimated premiums, and receive general compliance or claims guidance. It is a planning aid and should not replace licensed insurance, legal, or product-channel verification. <br>

### Deployment Geography for Use: <br>
Mainland China <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask for personal, family, income, mortgage, existing coverage, budget, and health-related insurance information. <br>
Mitigation: Share only the minimum information needed for planning and avoid unnecessary sensitive detail. <br>
Risk: Insurance product terms, availability, and premiums may change after the local product data was prepared. <br>
Mitigation: Verify current terms and premiums through licensed insurance channels before making purchase decisions. <br>
Risk: The skill provides insurance planning guidance that can affect financial, health, underwriting, or claims decisions. <br>
Mitigation: Treat outputs as planning support and confirm important decisions with licensed professionals, insurers, or applicable legal guidance. <br>


## Reference(s): <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Insurance knowledge reference](artifact/references/insurance-knowledge.md) <br>
- [Compliance reference](artifact/references/compliance.md) <br>
- [Product data reference](artifact/references/products.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Chinese-language Markdown responses, with JSON emitted by local helper scripts when calculators or plan designers are invoked.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local static product and reference data; current product terms, availability, and premiums require licensed-channel verification.] <br>

## Skill Version(s): <br>
1.8.414 (source: server release metadata; artifact frontmatter says 1.8.347) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
