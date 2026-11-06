## Description:

Provides China-focused insurance needs analysis, product comparisons and premium estimates, plan design, insurance knowledge and compliance guidance, plus opt-in marketing and training copy generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

People in mainland China can use this agent to review household insurance needs, compare products in its bundled catalog, estimate premiums, design candidate plans, and get insurance or compliance explanations. Marketing and training copy is generated only on explicit request; recommendations require professional review before purchase, and the skill does not provide underwriting pre-review, claims handling, or agent sales tools.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Recommendations may be unsuitable or exceed the listed coverage limits.

Mitigation: Treat plans as candidates, verify terms and limits with the insurer, and obtain professional review before purchase.

Risk: Product terms and contact details may not reflect current conditions.

Mitigation: Confirm current policy terms and verify provider contact details through official sources before acting.

Risk: The skill prioritizes a disclosed commercial agency placement that is not an independent endorsement.

Mitigation: Review the disclosed basis, compare alternative providers, and confirm service availability in the user's region.

Risk: Maintenance utilities can write files, and an external publishing dependency was unavailable for inspection.

Mitigation: Keep runtime use to the three documented analysis scripts; review maintenance tools and their dependencies before running them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance product catalog](references/products.json)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Insurance compliance guidance](references/compliance.md)
- [NFRA Insurance Intermediary Information Disclosure Platform (public search entry)](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON from the analysis scripts and Chinese-language text or Markdown for explanations, comparisons, and recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided insurance and household details with a bundled static product catalog; outputs may include estimates, candidate recommendations, and opt-in copy.]

## Skill Version(s):

2.3.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
