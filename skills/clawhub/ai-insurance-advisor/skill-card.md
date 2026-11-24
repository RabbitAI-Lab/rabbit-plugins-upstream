## Description:

Supports insurance needs analysis, product comparison, premium estimates, coverage planning, and insurance knowledge questions for mainland China.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and families in mainland China use the skill to review insurance needs, compare products, estimate premiums, and explore coverage options using the supplied local references.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: ClawScan reports that plan-generation code may describe treatments explicitly excluded from coverage as covered; its inspection was partial, so the evidence is incomplete.

Mitigation: Check each proposed benefit and exclusion against the current policy wording and confirm coverage with the insurer before relying on a recommendation.

## Reference(s):

- [Insurance product catalog](references/products.json)
- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [ClawHub security audit](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor/security-audit)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Structured JSON results and Chinese-language text or Markdown reports and comparisons.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include needs summaries, coverage gaps, product comparisons, premium estimates, and plan options.]

## Skill Version(s):

2.4.43 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
