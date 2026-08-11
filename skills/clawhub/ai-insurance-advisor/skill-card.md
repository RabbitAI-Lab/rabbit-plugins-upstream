## Description:

Helps users in mainland China with insurance planning, product comparison, premium calculation, coverage gap analysis, underwriting and compliance questions, claims guidance, and agent sales-support content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China and insurance agents use this skill to analyze insurance needs, compare products, estimate premiums, design plans, answer insurance and compliance questions, and draft Chinese sales or training content.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Insurance recommendations may be outdated or unsuitable because the skill uses packaged static product data and local calculators.

Mitigation: Verify product availability, pricing, suitability, and licensing with an independent qualified professional before acting on recommendations.

Risk: The skill may offer a specific sales contact after recommendations.

Mitigation: Treat contact suggestions as commercial referrals and compare options through qualified multi-company insurance professionals.

Risk: The skill may run bundled Python calculators and read bundled insurance product and compliance files.

Mitigation: Review the bundled scripts and reference data before installation; server security evidence found no credential access, network transmission, background persistence, or user-file modification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [Insurance product database](references/products.json)
- [Product validation report](references/validation_report_20260524_090219.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Chinese Markdown responses, comparison tables, structured reports, and JSON from bundled calculator scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations rely on packaged static product data; users should verify product availability, pricing, suitability, and licensing independently.]

## Skill Version(s):

1.8.446 (source: server release metadata; artifact frontmatter lists 1.8.351)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
