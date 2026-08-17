## Description:

AI Insurance Advisor helps users in mainland China with insurance planning, product comparisons, premium estimates, coverage-gap analysis, compliance prompts, claims questions, social copy, and agent training scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to assess insurance needs, compare products, estimate premiums, draft insurance plans, and review insurance knowledge or compliance prompts. Insurance agents may also use it to draft client-facing social copy and training scripts.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill may request sensitive financial, family, and health-related insurance information.

Mitigation: Share only information needed for the insurance task and handle user-provided details according to applicable privacy and compliance requirements.

Risk: Insurance product availability, pricing, and compliance notes come from static bundled data and may be outdated.

Mitigation: Verify product details, premiums, and regulatory requirements with the insurer or a licensed professional before buying or recommending coverage.

Risk: Insurance guidance may be mistaken for a final legal, financial, underwriting, or purchasing decision.

Mitigation: Treat outputs as advisory reference material and confirm decisions against official policy documents and licensed professional advice.

Risk: A named sales-contact referral may be mistaken for a complete or endorsed channel list.

Mitigation: Present any named contact as a reference option and encourage comparison across licensed multi-company insurance channels.

## Reference(s):

- [Skill definition](artifact/SKILL.md)
- [Insurance knowledge base](artifact/references/insurance-knowledge.md)
- [Compliance reference](artifact/references/compliance.md)
- [Insurance product database](artifact/references/products.json)
- [Product data validation report](artifact/references/validation_report_20260524_090219.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese natural-language guidance, Markdown tables, and JSON from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses static bundled product data; product availability, pricing, compliance notes, and sales-contact referrals require external verification.]

## Skill Version(s):

1.8.466 (source: server release metadata; artifact frontmatter says 1.8.351)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
