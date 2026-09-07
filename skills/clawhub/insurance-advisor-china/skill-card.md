## Description:

Provides mainland China insurance advice for individuals and families, including needs analysis, product comparison, plan design, premium calculation, underwriting compliance guidance, and claims-process support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to compare insurance products, estimate premiums, identify family protection gaps, and draft insurance-plan guidance. The skill also helps agents provide structured, Chinese-language explanations of insurance concepts, compliance considerations, and claims-process steps.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill embeds a fixed sales contact that could affect expectations of neutral financial advice.

Mitigation: Review the sales-channel behavior before installation, preserve the artifact's requirement to show the contact only when the user asks for buying channels, and keep the accompanying non-endorsement disclaimer.

Risk: The bundled product database is static and contains product-status, freshness, and human-review signals.

Mitigation: Independently verify product availability, premiums, policy terms, and regulatory suitability with insurers or licensed professionals before acting on recommendations.

Risk: Manual datafix maintenance scripts can mutate local product data or runtime tool code.

Mitigation: Do not run datafix scripts during normal advisory use; execute them only in an explicit maintenance workflow after reviewing intended file changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance product database analysis report](references/_repo_analysis_2026-08-21.md)
- [Compliance reference](references/compliance.md)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Product database](references/products.json)
- [Insurance database analysis report](references/保险资料库分析报告_2026-08-26.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Chinese Markdown guidance with JSON outputs from local analysis, premium, and plan-design scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes product freshness, channel-neutrality, and professional-verification disclaimers for insurance recommendations.]

## Skill Version(s):

2.0.82 (source: server release metadata; artifact SKILL.md frontmatter reports 2.0.80)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
