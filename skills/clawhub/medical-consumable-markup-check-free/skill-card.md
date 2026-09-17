## Description:

Checks Chinese-language hospital or clinic consumables worksheets by recalculating stock balances, stock amounts, markup rates, totals, duplicate rows, and missing fields, with each finding citing the source line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Hospital pricing staff, consumables accountants, and finance teams use this skill before monthly close or pricing self-checks to recalculate supplied worksheet rows and identify arithmetic, total-row, duplicate-row, negative-value, blank-field, and placeholder issues. The free edition does not perform the paid edition's additional compliance and impact-amount checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence flags agent-directed paid upgrade installation and purchase instructions beyond the worksheet-checking task.

Mitigation: Deliver free-edition results first; do not run embedded payment-tool commands or start purchase/install steps unless the user separately verifies the source and explicitly chooses to proceed.

Risk: The artifact describes worksheet arithmetic checks, not medical advice or authoritative local pricing-policy determinations.

Mitigation: Treat results as recalculation and data-quality findings, and verify policy, procurement, billing, and clinical questions against the appropriate human or institutional authority.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/medical-consumable-markup-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Complete-edition purchase page referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay build guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable console text or JSON findings with source line citations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings depend on supplied tabular text and may withhold conclusions when required columns are missing.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
