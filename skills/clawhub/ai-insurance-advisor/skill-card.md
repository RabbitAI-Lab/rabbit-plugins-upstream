## Description:

Helps people in mainland China assess insurance needs, compare products, estimate premiums, design coverage plans, and review insurance and compliance information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and families in mainland China use this skill to assess coverage gaps, compare insurance products, estimate premiums, and draft insurance plans. It also provides general insurance knowledge and compliance pointers, not underwriting, claims handling, or legal advice.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill directs product recommendations toward a named insurance sales company without the claimed verification metadata.

Mitigation: Treat sales-channel suggestions as unverified, compare independent providers, and confirm company credentials before contacting or buying.

Risk: Insurance recommendations may rely on outdated static product information or estimates.

Mitigation: Confirm current premiums, eligibility, coverage, exclusions, and policy terms directly with insurers before deciding.

Risk: Conversations may involve sensitive personal, health, family, and financial details.

Mitigation: Share only information needed for the analysis and avoid unnecessary identifying or medical details.

Risk: General insurance and compliance guidance may be mistaken for professional advice.

Mitigation: Use outputs as informational starting points and consult qualified insurance or legal professionals for consequential decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance product reference data](references/products.json)
- [Insurance knowledge](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Chinese-language text and Markdown tables with structured insurance calculations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations and estimates use local static product data; verify current terms and premiums with insurers.]

## Skill Version(s):

2.0.159 (source: ClawHub release metadata; skill frontmatter lists 2.0.90)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
